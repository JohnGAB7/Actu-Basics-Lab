const { test, expect } = require('@playwright/test');

function numeric(text) {
  const cleaned = text.replace(/[^0-9,.-]/g, '').replace(/\.(?=\d{3}(?:\D|$))/g, '').replace(',', '.');
  return Number(cleaned);
}

test('homepage exposes the three published actuarial lessons', async ({ page }) => {
  await page.goto('');
  await expect(page.locator('h1')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/A0-01/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/A1-01/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/A2-01/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-01/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-02/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-03/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/M0-01/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/M0-02/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/M0-03/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-04/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-05/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-06/"]')).toBeVisible();
  await expect(page.locator('a.lesson[href="lessons/S1-07/"]')).toBeVisible();
});

test('library loads the 320-unit source curriculum and filters it', async ({ page }) => {
  await page.goto('bibliotheque/');
  await expect(page.locator('#count')).toContainText('320 / 320');
  await page.locator('#status').selectOption('available');
  await expect(page.locator('#catalogue .card')).toHaveCount(10);
  await expect(page.locator('#catalogue')).toContainText('S1.01');
  await page.locator('#search').fill('S1.01');
  await expect(page.locator('#catalogue .card')).toHaveCount(1);
  await expect(page.locator('#catalogue a')).toHaveAttribute('href', '../lessons/S1-01/');
});

test('A1.01 calculator recalculates future and present values', async ({ page }) => {
  await page.goto('lessons/A1-01/');
  await expect(page.locator('#present')).toContainText('231');
  await page.locator('#capital').fill('10000');
  await page.locator('#taux').fill('4');
  await page.locator('#duree').fill('10');
  await expect.poll(async () => numeric(await page.locator('#present').innerText())).toBeCloseTo(6755.64, 1);
  await expect.poll(async () => numeric(await page.locator('#future').innerText())).toBeCloseTo(14802.44, 1);
});

test('A2.01 risk-pooling simulator returns the validated binomial examples', async ({ page }) => {
  await page.goto('lessons/A2-01/');
  await expect(page.locator('#expected')).toHaveText('200');
  await expect.poll(async () => numeric(await page.locator('#loss').innerText())).toBeCloseTo(7.32, 1);
  await page.locator('#n').fill('100');
  await expect(page.locator('#expected')).toHaveText('2');
  await expect.poll(async () => numeric(await page.locator('#sdmean').innerText())).toBeCloseTo(7, 1);
  await expect.poll(async () => numeric(await page.locator('#loss').innerText())).toBeCloseTo(32.33, 1);
});

test('M0.01 percentage calculator updates from a fraction', async ({ page }) => {
  await page.goto('lessons/M0-01/');
  await expect(page.locator('#pct')).toContainText('25');
  await page.locator('#num').fill('6');
  await page.locator('#den').fill('40');
  await expect(page.locator('#pct')).toContainText('15');
});

test('S1.01 is a complete bilingual data-foundations lesson', async ({ page }) => {
  await page.goto('lessons/S1-01/');
  await expect(page.locator('h1')).toContainText('Qu\'est-ce qu\'une donnée');
  await expect(page.locator('#vocabulaire')).toContainText('Population cible');
  await expect(page.locator('#paris')).toContainText('13 320 752');
  await expect(page.locator('#structure')).toContainText('xᵢⱼ');
  await expect(page.locator('#qualite')).toContainText('Non-réponse');
  await expect(page.locator('.exercise')).toHaveCount(4);
  await page.locator('.exercise summary').first().click();
  await expect(page.locator('.exercise details[open]')).toHaveCount(1);
  await expect(page.locator('pre code').first()).toContainText('data.frame');
  await expect(page.locator('pre code').nth(1)).toContainText('pandas');
  await page.goto('en/lessons/S1-01/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('What counts as data');
  await expect(page.locator('#vocabulaire')).toContainText('Target population');
  await expect(page.locator('#paris')).toContainText('13,320,752');
  await expect(page.locator('#lab')).toContainText('Mini-lab');
});

test('S1.05 transcript reveals source-script corrections', async ({ page }) => {
  await page.goto('lessons/S1-05/');
  const reveal = page.locator('.reveal').first();
  await expect(reveal).toBeVisible();
  await reveal.click();
  await expect(page.locator('.correction').first()).toHaveClass(/show/);
});

test('M0.02 and S1.04 transcript lessons render source material', async ({ page }) => {
  await page.goto('lessons/M0-02/');
  await expect(page.locator('h1')).toContainText('Un milliard de secondes');
  await page.goto('lessons/S1-04/');
  await expect(page.locator('h1')).toContainText('Combien de chômeurs');
  await page.goto('en/lessons/M0-02/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('How long is a billion seconds');
});

test('English routes open the English edition', async ({ page }) => {
  await page.goto('en/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('Numbers tell stories');
  await expect(page.locator('a.lesson[href="en/lessons/S1-01/"]')).toBeVisible();
  await page.goto('en/library/');
  await page.locator('#status').selectOption('available');
  await page.locator('#search').fill('S1.01');
  const englishLesson = page.locator('#catalogue a').first();
  await expect(englishLesson).toHaveAttribute('href', '../lessons/S1-01/');
  await englishLesson.click();
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
});

test('lesson pages remain within the mobile viewport', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  for (const route of ['lessons/A0-01/', 'lessons/A1-01/', 'lessons/A2-01/', 'lessons/M0-01/', 'lessons/M0-02/', 'lessons/M0-03/', 'lessons/S1-01/', 'lessons/S1-02/', 'lessons/S1-03/', 'lessons/S1-04/', 'lessons/S1-05/', 'lessons/S1-06/', 'lessons/S1-07/', 'bibliotheque/']) {
    await page.goto(route);
    await expect(page.locator('h1, .hero h1').first()).toBeVisible();
    const width = await page.evaluate(() => document.documentElement.scrollWidth);
    expect(width, 'horizontal overflow on ' + route).toBeLessThanOrEqual(375);
  }
});


test('learning paths provide keyboard skip navigation and an operable mobile menu', async ({ page }) => {
  for (const route of ['parcours/', 'en/paths/']) {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(route);
    const english = route.startsWith('en/');
    const skip = page.locator('.skip-link');
    await expect(skip).toBeAttached();
    await page.keyboard.press('Tab');
    await expect(skip).toBeFocused();
    await expect(skip).toHaveAttribute('href', '#contenu');
    await page.locator('.mobile-menu summary').click();
    const panel = page.locator('.mobile-menu-panel');
    await expect(panel).toBeVisible();
    await expect(panel.locator('a[aria-current="page"]')).toBeVisible();
    await skip.focus();
    await skip.press('Enter');
    await expect(page.locator('#contenu')).toBeFocused();
    await expect(page.locator('html')).toHaveAttribute('lang', english ? 'en' : 'fr');
    const width = await page.evaluate(() => document.documentElement.scrollWidth);
    expect(width, 'horizontal overflow on ' + route).toBeLessThanOrEqual(390);
  }
});

test('learning path navigation and focus indicators work at desktop width', async ({ page }) => {
  await page.setViewportSize({ width: 1365, height: 900 });
  await page.goto('parcours/');
  await expect(page.locator('nav[aria-label="Navigation principale"] a[aria-current="page"]')).toContainText('Parcours');
  await expect(page.locator('.mobile-menu')).toBeHidden();
  await page.keyboard.press('Tab');
  await page.keyboard.press('Tab');
  await page.keyboard.press('Tab');
  const firstLink = page.locator('nav[aria-label="Navigation principale"] a').first();
  await expect(firstLink).toBeFocused();
  const outline = await firstLink.evaluate(el => getComputedStyle(el).outlineStyle);
  expect(outline).not.toBe('none');
});


test('French knowledge map loads concepts, filters relationships and links published lessons', async ({ page }) => {
  await page.goto('connaissances/');
  await expect(page.locator('h1')).toContainText('La carte des connaissances');
  await expect(page.locator('#nodes .node-btn')).toHaveCount(26);
  const allEdges = await page.locator('#graph .edge').count();
  expect(allEdges).toBeGreaterThan(0);
  await page.locator('#relation').selectOption('requires');
  const prerequisiteEdges = await page.locator('#graph .edge').count();
  expect(prerequisiteEdges).toBeGreaterThan(0);
  expect(prerequisiteEdges).toBeLessThan(allEdges);
  await page.locator('#nodes .node-btn').filter({ hasText: 'Fractions et proportions' }).click();
  await expect(page.locator('#detail')).toContainText('M0.01');
  await expect(page.locator('#detail a[href="../lessons/M0-01/"]')).toBeVisible();
});

test('English knowledge map links to English published lessons', async ({ page }) => {
  await page.goto('en/knowledge-map/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('#nodes .node-btn')).toHaveCount(26);
  await page.locator('#nodes .node-btn').filter({ hasText: 'Fractions and proportions' }).click();
  await expect(page.locator('#detail a[href="../../en/lessons/M0-01/"]')).toBeVisible();
});

test('French and English software workshops expose four practical tools and shared data', async ({ page }) => {
  for (const route of ['ateliers/', 'en/workshops/']) {
    await page.goto(route);
    await expect(page.locator('h1')).toBeVisible();
    await expect(page.locator('#excel')).toBeVisible();
    await expect(page.locator('#vba')).toBeVisible();
    await expect(page.locator('#python')).toBeVisible();
    await expect(page.locator('#r')).toBeVisible();
    await expect(page.locator('a[download]')).toHaveAttribute('href', route.startsWith('en/') ? '../../data/atelier-sinistres-synthetiques.csv' : '../data/atelier-sinistres-synthetiques.csv');
    await expect(page.locator('pre#python-code')).toContainText('csv.DictReader');
    await expect(page.locator('pre#r-code')).toContainText('read.csv');
    await expect(page.locator('pre#vba-code')).toContainText('BuildPortfolioSummary');
    await expect(page.locator('body')).toContainText(route.startsWith('en/') ? '87.06%' : '87,06 %');
  }
});

test('homepage exposes bilingual knowledge map and workshop destinations', async ({ page }) => {
  await page.goto('');
  await expect(page.locator('#nav a[data-fr-href="connaissances/"]')).toBeVisible();
  await expect(page.locator('#nav a[data-fr-href="ateliers/"]')).toBeVisible();
  await page.locator('#lang').click();
  await expect(page.locator('#nav a[data-fr-href="connaissances/"]')).toHaveAttribute('href', 'en/knowledge-map/');
  await expect(page.locator('#nav a[data-fr-href="ateliers/"]')).toHaveAttribute('href', 'en/workshops/');
});

test('knowledge map and workshops remain usable on narrow mobile screens', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  for (const route of ['connaissances/', 'ateliers/', 'en/knowledge-map/', 'en/workshops/']) {
    await page.goto(route);
    await expect(page.locator('h1')).toBeVisible();
    const width = await page.evaluate(() => document.documentElement.scrollWidth);
    expect(width, 'horizontal overflow on ' + route).toBeLessThanOrEqual(375);
  }
});


test('foundation curriculum distinguishes published M0 lessons from planned M1 and M2 units', async ({ page }) => {
  for (const route of ['parcours/', 'en/paths/']) {
    await page.goto(route);
    await expect(page.locator('#fondations, #foundations')).toBeVisible();
    const section = page.locator(route.startsWith('en/') ? '#foundations' : '#fondations');
    await expect(section.locator('a[href="../lessons/M0-01/"]')).toBeVisible();
    await expect(section.locator('a[href="../lessons/M0-02/"]')).toBeVisible();
    await expect(section.locator('a[href="../lessons/M0-03/"]')).toBeVisible();
    await expect(section).toContainText(route.startsWith('en/') ? '5 curriculum units' : '5 unités au programme');
    await expect(section).toContainText(route.startsWith('en/') ? '3 curriculum units' : '3 unités au programme');
  }
});

test('VBA automation is represented in the knowledge graph', async ({ page }) => {
  await page.goto('connaissances/');
  await page.locator('#nodes .node-btn').filter({ hasText: 'Automatiser une analyse dans Excel VBA' }).click();
  await expect(page.locator('#detail')).toContainText('tool_practice');
});


test('statistics curriculum exposes all 177 topics across 19 modules in French', async ({ page }) => {
  await page.goto('statistiques/');
  await expect(page.locator('h1')).toContainText('De la première donnée');
  await expect(page.locator('#topicCount')).toHaveText('177');
  await expect(page.locator('#results .module')).toHaveCount(19);
  await expect(page.locator('#results')).toContainText('S19.08');
  await expect(page.locator('#results')).toContainText('S1.01');
  await expect(page.locator('#results .topic a[href="../lessons/S1-01/"]')).toBeVisible();
  await page.locator('#search').fill('maximum de vraisemblance');
  await expect(page.locator('#results .topic')).toHaveCount(1);
  await expect(page.locator('#results')).toContainText('S7.05');
  await page.locator('#search').fill('');
  await page.locator('#levelFilter').selectOption('5');
  await expect(page.locator('#results .module')).toHaveCount(7);
  await page.locator('#levelFilter').selectOption('');
  await page.locator('#statusFilter').selectOption('available');
  await expect(page.locator('#results .topic')).toHaveCount(7);
});

test('statistics curriculum is bilingual and keeps publication statuses honest', async ({ page }) => {
  await page.goto('en/statistics/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('From the first data point');
  await expect(page.locator('#topicCount')).toHaveText('177');
  await expect(page.locator('#results')).toContainText('S18.06');
  await expect(page.locator('#results')).toContainText('To develop');
  await page.locator('#statusFilter').selectOption('available');
  await expect(page.locator('#results .topic')).toHaveCount(7);
  await page.locator('#lang').click();
  await expect(page).toHaveURL(/statistiques\/$/);
  await expect(page.locator('html')).toHaveAttribute('lang', 'fr');
});

test('statistics course navigation is available from the homepage in both languages', async ({ page }) => {
  await page.goto('');
  await expect(page.locator('#nav a[data-fr-href="statistiques/"]')).toBeVisible();
  await page.locator('#nav a[data-fr-href="statistiques/"]').click();
  await expect(page).toHaveURL(/statistiques\/$/);
  await page.goto('');
  await page.locator('#lang').click();
  await expect(page.locator('#nav a[data-fr-href="statistiques/"]')).toHaveAttribute('href', 'en/statistics/');
});


test('statistics Level 1 curriculum lists all 31 topics and links published lessons', async ({ page }) => {
  await page.goto('statistiques/niveau-1/');
  await expect(page.locator('h1')).toContainText('Apprendre à lire');
  await expect(page.locator('#topics .topic')).toHaveCount(31);
  await expect(page.locator('#topics')).toContainText('S1.01');
  await expect(page.locator('#topics')).toContainText('S3.09');
  await expect(page.locator('#topics a[href$="/lessons/S1-01/"]')).toBeVisible();
  await page.locator('#module').selectOption('S2');
  await expect(page.locator('#topics .topic')).toHaveCount(10);
  await page.locator('#status').selectOption('available');
  await expect(page.locator('#topics .topic')).toHaveCount(0);
  await page.locator('#module').selectOption('S1');
  await expect(page.locator('#topics .topic')).toHaveCount(7);
});

test('statistics Level 1 curriculum is available in English', async ({ page }) => {
  await page.goto('en/statistics/level-1/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('Learn to read');
  await expect(page.locator('#topics .topic')).toHaveCount(31);
  await expect(page.locator('#topics')).toContainText('To develop');
  await page.locator('#lang').click();
  await expect(page).toHaveURL(/statistiques\/niveau-1\/$/);
});
