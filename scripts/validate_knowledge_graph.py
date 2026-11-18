#!/usr/bin/env python3
"""Validate the ACTU-BASICS knowledge graph against the source catalogue."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "data/knowledge-graph/statistics-core-v1.json"
CATALOGUE_PATH = ROOT / "data/catalogue.json"
ALLOWED_NODE_TYPES = {"concept", "skill", "learning_unit", "tool_practice", "assessment", "project"}
ALLOWED_EDGE_TYPES = {"requires", "recommends", "supports", "applies", "assessed_by", "continues_to"}
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def main() -> int:
    if not GRAPH_PATH.exists():
        fail(f"Missing graph file: {GRAPH_PATH.relative_to(ROOT)}")
    if not CATALOGUE_PATH.exists():
        fail(f"Missing catalogue file: {CATALOGUE_PATH.relative_to(ROOT)}")
    if errors:
        return report()

    try:
        graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        catalogue = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Could not parse graph or catalogue JSON: {exc}")
        return report()

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = [node.get("id") for node in nodes]

    if not nodes:
        fail("Knowledge graph contains no nodes")
    if len(node_ids) != len(set(node_ids)):
        fail("Duplicate node identifiers")
    if not isinstance(edges, list):
        fail("Graph edges must be an array")
        edges = []

    known_ids = set(node_ids)
    catalogue_ids = {entry.get("id") for entry in catalogue.get("entries", [])}
    edge_keys: set[tuple[str, str, str]] = set()
    prerequisite_adjacency = {node_id: [] for node_id in known_ids}

    for node in nodes:
        node_id = node.get("id", "<missing>")
        if node.get("type") not in ALLOWED_NODE_TYPES:
            fail(f"{node_id}: invalid node type {node.get('type')!r}")
        for field in ("title_fr", "title_en"):
            if not node.get(field):
                fail(f"{node_id}: missing {field}")
        if node.get("stage") not in {1, 2, 3, 4, 5}:
            fail(f"{node_id}: stage must be an integer from 1 to 5")
        for catalogue_id in node.get("catalogue_refs", []):
            if catalogue_id not in catalogue_ids:
                fail(f"{node_id}: unknown catalogue reference {catalogue_id}")

    for edge in edges:
        source, target, edge_type = edge.get("from"), edge.get("to"), edge.get("type")
        if source not in known_ids:
            fail(f"Edge references unknown source node: {source}")
        if target not in known_ids:
            fail(f"Edge references unknown target node: {target}")
        if edge_type not in ALLOWED_EDGE_TYPES:
            fail(f"Invalid edge type: {edge_type}")
        key = (source, target, edge_type)
        if key in edge_keys:
            fail(f"Duplicate edge: {source} -> {target} ({edge_type})")
        edge_keys.add(key)
        if edge_type == "requires" and source in known_ids and target in known_ids:
            prerequisite_adjacency[source].append(target)

    # A strict-prerequisite graph must be acyclic.
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node_id: str) -> None:
        if node_id in visiting:
            fail(f"Cycle detected in strict prerequisites at {node_id}")
            return
        if node_id in visited:
            return
        visiting.add(node_id)
        for target in prerequisite_adjacency[node_id]:
            visit(target)
        visiting.remove(node_id)
        visited.add(node_id)

    for node_id in known_ids:
        visit(node_id)

    if graph.get("schema_version") != "1.0":
        fail("Unexpected or missing schema_version")
    if graph.get("status") not in {"design", "reviewed", "approved"}:
        fail("Graph status must explicitly distinguish design from approval")

    if errors:
        return report()

    print(
        f"Knowledge graph valid: {len(nodes)} nodes, {len(edges)} edges, "
        f"{sum(bool(node.get('catalogue_refs')) for node in nodes)} nodes mapped to catalogue units."
    )
    return 0


def report() -> int:
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Knowledge graph validation failed with {len(errors)} error(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
