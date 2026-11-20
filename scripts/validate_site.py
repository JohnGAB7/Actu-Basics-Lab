#!/usr/bin/env python3
"""Dependency-free quality checks for the ACTU-BASICS static site."""
from __future__ import annotations
import json
import math
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids: set[str] = set()
        self.duplicates: set[str] = set()
        self.links: list[str] = []
        self.lang = None
        self.title = False
        self.viewport = False
        self.images_without_alt: list[str] = []
        self._in_title = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "title":
            self._in_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.viewport = True
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.duplicates.add(attrs["id"])
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "img" and "alt" not in attrs:
            self.images_without_alt.append(attrs.get("src", "(image without src)"))
    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
    def handle_data(self, data):
        if self._in_title and data.strip():
            self.title = True

def fail(message: str):
    ERRORS.append(message)

pages = sorted(ROOT.rglob("*.html"))
if len(pages) < 10:
    fail(f"Expected at least 10 HTML pages; found {len(pages)}")

for page in pages:
    rel = page.relative_to(ROOT)
    parser = PageParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{rel}: HTML parser error: {exc}")
        continue
    if not parser.lang:
        fail(f"{rel}: missing html lang attribute")
    if not parser.title:
        fail(f"{rel}: missing non-empty title")
    if not parser.viewport:
        fail(f"{rel}: missing responsive viewport meta")
    if parser.duplicates:
        fail(f"{rel}: duplicate id(s): {', '.join(sorted(parser.duplicates))}")
    if parser.images_without_alt:
        fail(f"{rel}: image(s) missing alt: {', '.join(parser.images_without_alt)}")
    for href in parser.links:
        if href.startswith(("data:", "mailto:", "tel:", "javascript:")):
            continue
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            continue
        raw_path = unquote(parsed.path)
        if raw_path.startswith("/"):
            target = ROOT / raw_path.lstrip("/")
        elif raw_path:
            target = (page.parent / raw_path).resolve()
        else:
            target = page
        if target.is_dir():
            target = target / "index.html"
        elif not target.exists() and not target.suffix:
            target = target / "index.html"
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(f"{rel}: local link escapes site root: {href}")
            continue
        if not target.exists():
            fail(f"{rel}: broken local link: {href} -> {target.relative_to(ROOT)}")
        if parsed.fragment and target.exists() and target.suffix == ".html":
            try:
                target_parser = PageParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                if parsed.fragment not in target_parser.ids:
                    fail(f"{rel}: missing fragment #{parsed.fragment} in {target.relative_to(ROOT)}")
            except Exception as exc:
                fail(f"{rel}: could not inspect fragment target {href}: {exc}")

catalog_path = ROOT / "data/catalogue.json"
if not catalog_path.exists():
    fail("Missing data/catalogue.json")
else:
    try:
        catalogue = json.loads(catalog_path.read_text(encoding="utf-8"))
        entries = catalogue["entries"]
        ids = [entry["id"] for entry in entries]
        if catalogue.get("count") != len(entries):
            fail("Catalogue count does not match entries length")
        if len(entries) != 320:
            fail(f"Expected 320 source curriculum units; found {len(entries)}")
        if len(ids) != len(set(ids)):
            fail("Duplicate curriculum identifiers")
        for entry in entries:
            for field in ("id", "title", "titleEn", "status", "sourceCatalogue"):
                if not entry.get(field):
                    fail(f"Catalogue entry {entry.get('id', '?')} missing {field}")
            if entry.get("status") not in {"available", "script", "planned"}:
                fail(f"Invalid status on {entry.get('id')}: {entry.get('status')}")
            if entry.get("status") == "available" and not entry.get("pagePath"):
                fail(f"Available catalogue entry {entry.get('id')} has no pagePath")
            if entry.get("pagePath"):
                page_target = ROOT / entry["pagePath"] / "index.html"
                if not page_target.exists():
                    fail(f"Catalogue pagePath for {entry.get('id')} does not exist: {entry['pagePath']}")
        if sum(bool(e.get("scriptPath")) for e in entries) != 30:
            fail("Expected 30 source-script references in the curriculum catalogue")
        if sum(e["status"] == "available" for e in entries) != 10:
            fail("Expected ten published curriculum lessons in the catalogue")
        statistics = [e for e in entries if e["id"].startswith("S") and "." in e["id"]]
        if len(statistics) != 177:
            fail(f"Expected 177 statistics curriculum topics; found {len(statistics)}")
        if len({e["module"] for e in statistics}) != 19:
            fail("Expected 19 statistics modules")
    except Exception as exc:
        fail(f"Catalogue JSON validation failed: {exc}")

required = [
    "index.html", "en/index.html", "bibliotheque/index.html", "en/library/index.html",
    "parcours/index.html", "en/paths/index.html", "statistiques/index.html", "en/statistics/index.html", "statistiques/niveau-1/index.html", "en/statistics/level-1/index.html", "a-propos/index.html",
    "en/about/index.html", "lessons/A0-01/index.html", "en/lessons/A0-01/index.html",
    "lessons/A1-01/index.html", "en/lessons/A1-01/index.html",
    "lessons/A2-01/index.html", "en/lessons/A2-01/index.html",
    "lessons/M0-01/index.html", "en/lessons/M0-01/index.html",
    "lessons/S1-01/index.html", "en/lessons/S1-01/index.html",
    "lessons/S1-02/index.html", "en/lessons/S1-02/index.html",
    "lessons/S1-03/index.html", "en/lessons/S1-03/index.html",
    "lessons/M0-02/index.html", "en/lessons/M0-02/index.html",
    "lessons/M0-03/index.html", "en/lessons/M0-03/index.html",
    "lessons/S1-04/index.html", "en/lessons/S1-04/index.html",
    "lessons/S1-05/index.html", "en/lessons/S1-05/index.html",
    "lessons/S1-06/index.html", "en/lessons/S1-06/index.html",
    "lessons/S1-07/index.html", "en/lessons/S1-07/index.html",
]
for item in required:
    if not (ROOT / item).exists():
        fail(f"Missing required product page: {item}")

# The English root is a deliberate route into the translated homepage.
en_root = ROOT / "en/index.html"
if en_root.exists() and "location.replace('../index.html?lang=en" not in en_root.read_text(encoding="utf-8"):
    fail("English homepage route must open the translated homepage")

for lesson in ("lessons/A1-01/index.html", "en/lessons/A1-01/index.html"):
    source = (ROOT / lesson).read_text(encoding="utf-8")
    if 'id="present"' not in source or "Math.pow(1+r,n)" not in source:
        fail(f"{lesson}: missing interactive present-value calculation")
for lesson in ("lessons/A2-01/index.html", "en/lessons/A2-01/index.html"):
    source = (ROOT / lesson).read_text(encoding="utf-8")
    if "function tail(n,p,k)" not in source or "Math.sqrt(n*p*(1-p))" not in source:
        fail(f"{lesson}: missing binomial risk-pooling calculations")

# Recalculate the key examples from the source pilot scripts.
checks = {
    "A0.01 pure premium": abs((1000 * .02 * 500) / 1000 - 10) < 1e-9,
    "A1.01 compound value": abs(1000 * 1.05**30 - 4321.94237515067) < 1e-6,
    "A1.01 present value": abs(1000 / 1.05**30 - 231.377448) < 1e-5,
    "A1.01 worked discounting": abs(10000 / 1.04**10 - 6755.641) < .01,
    "A2.01 expected cost": abs(.02 * 500 - 10) < 1e-9,
    "A2.01 standard deviation": abs(500 * math.sqrt(.02 * .98) - 70) < 1e-9,
    "A2.01 pooled mean uncertainty": abs(70 / math.sqrt(2500) - 1.4) < 1e-9,
}
for name, ok in checks.items():
    if not ok:
        fail(f"Mathematical check failed: {name}")

def binomial_tail(n: int, p: float, k: int) -> float:
    term = (1-p)**n
    cdf = term
    for i in range(1, k):
        term *= ((n-i+1)/i) * (p/(1-p))
        cdf += term
    return 1-cdf

if abs(binomial_tail(100, .02, 3) - .32) > .01:
    fail("A2.01 binomial tail check for 100 policies is outside expected tolerance")
if abs(binomial_tail(10000, .02, 221) - .073) > .002:
    fail("A2.01 binomial tail check for 10,000 policies is outside expected tolerance")

if ERRORS:
    print("ACTU-BASICS quality checks FAILED:")
    for error in ERRORS:
        print(" - " + error)
    raise SystemExit(1)

print(f"ACTU-BASICS quality checks passed: {len(pages)} HTML pages, 320 curriculum units, bilingual A0/A1/A2 pages, local links and mathematical examples.")
