const { test, expect } = require('@playwright/test');

function numeric(text) {
  const cleaned = text.replace(/[^0-9,.-]/g, '').replace(/\.(?=\d{3}(?:\D|$))/g, '').replace(',', '.');
  return Number(cleaned);
}

test('homepage exposes the three published actuarial lessons', async ({ page }) => {
  await page.goto('/');
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
  await page.goto('/bibliotheque/');
  await expect(page.locator('#count')).toContainText('320 / 320');
  await page.locator('#status').selectOption('available');
  await expect(page.locator('#catalogue .card')).toHaveCount(10);
  await expect(page.locator('#catalogue')).toContainText('S1.01');
  await page.locator('#search').fill('S1.01');
  await expect(page.locator('#catalogue .card')).toHaveCount(1);
  await expect(page.locator('#catalogue a')).toHaveAttribute('href', '../lessons/S1-01/');
});

test('A1.01 calculator recalculates future and present values', async ({ page }) => {
  await page.goto('/lessons/A1-01/');
  await expect(page.locator('#present')).toContainText('231');
  await page.locator('#capital').fill('10000');
  await page.locator('#taux').fill('4');
  await page.locator('#duree').fill('10');
  await expect.poll(async () => numeric(await page.locator('#present').innerText())).toBeCloseTo(6755.64, 1);
  await expect.poll(async () => numeric(await page.locator('#future').innerText())).toBeCloseTo(14802.44, 1);
});

test('A2.01 risk-pooling simulator returns the validated binomial examples', async ({ page }) => {
  await page.goto('/lessons/A2-01/');
  await expect(page.locator('#expected')).toHaveText('200');
  await expect.poll(async () => numeric(await page.locator('#loss').innerText())).toBeCloseTo(7.32, 1);
  await page.locator('#n').fill('100');
  await expect(page.locator('#expected')).toHaveText('2');
  await expect.poll(async () => numeric(await page.locator('#sdmean').innerText())).toBeCloseTo(7, 1);
  await expect.poll(async () => numeric(await page.locator('#loss').innerText())).toBeCloseTo(32.33, 1);
});

test('M0.01 percentage calculator updates from a fraction', async ({ page }) => {
  await page.goto('/lessons/M0-01/');
  await expect(page.locator('#pct')).toContainText('25');
  await page.locator('#num').fill('6');
  await page.locator('#den').fill('40');
  await expect(page.locator('#pct')).toContainText('15');
});

test('S1.01 exercise gives immediate corrective feedback', async ({ page }) => {
  await page.goto('/lessons/S1-01/');
  await page.locator('.answer[data-correct="yes"]').click();
  await expect(page.locator('.feedback')).toContainText('Exact');
});

test('S1.05 transcript reveals source-script corrections', async ({ page }) => {
  await page.goto('/lessons/S1-05/');
  const reveal = page.locator('.reveal').first();
  await expect(reveal).toBeVisible();
  await reveal.click();
  await expect(page.locator('.correction').first()).toHaveClass(/show/);
});

test('M0.02 and S1.04 transcript lessons render source material', async ({ page }) => {
  await page.goto('/lessons/M0-02/');
  await expect(page.locator('h1')).toContainText('Un milliard de secondes');
  await page.goto('/lessons/S1-04/');
  await expect(page.locator('h1')).toContainText('Combien de chômeurs');
  await page.goto('/en/lessons/M0-02/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('How long is a billion seconds');
});

test('English routes open the English edition', async ({ page }) => {
  await page.goto('/en/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toContainText('Numbers tell stories');
});

test('lesson pages remain within the mobile viewport', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  for (const route of ['/lessons/A0-01/', '/lessons/A1-01/', '/lessons/A2-01/', '/lessons/M0-01/', '/lessons/M0-02/', '/lessons/M0-03/', '/lessons/S1-01/', '/lessons/S1-02/', '/lessons/S1-03/', '/lessons/S1-04/', '/lessons/S1-05/', '/lessons/S1-06/', '/lessons/S1-07/', '/bibliotheque/']) {
    await page.goto(route);
    await expect(page.locator('h1, .hero h1').first()).toBeVisible();
    const width = await page.evaluate(() => document.documentElement.scrollWidth);
    expect(width, 'horizontal overflow on ' + route).toBeLessThanOrEqual(375);
  }
});
