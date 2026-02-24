import { test, expect } from '@playwright/test';

// await page.screenshot({ path: 'screenshot.png' });
// https://shop.sprouts.com/store/sprouts/products/17859053-sprouts-whey-protein-chocolate-32-oz
test('has price', async ({ page }) => {
  await page.goto('https://shop.sprouts.com/store/sprouts/products/17859053-sprouts-whey-protein-chocolate-32-oz');
  await page.locator('#id-39').getByRole('button', { name: 'In-Store · open 7am - 10pm' }).click();
  await page.getByRole('button', { name: 'REJECT COOKIES' }).click();
  await expect(page.locator('#item_details')).toMatchAriaSnapshot(`
    - text: "/Current price: \\\\$\\\\d+\\\\.\\\\d+ Quantity/"
    - combobox "Quantity 1"
    - button "Add to List"
    `);
});

test('is on sale', async ({ page }) => {
  await page.goto('https://shop.sprouts.com/store/sprouts/products/17859053-sprouts-whey-protein-chocolate-32-oz');
  await page.locator('#id-39').getByRole('button', { name: 'In-Store · open 7am - 10pm' }).click();
  await page.getByRole('button', { name: 'REJECT COOKIES' }).click();
  await expect(page.locator('#item_details')).toMatchAriaSnapshot(`
    - text: "/Original price:|% off/"
    - combobox "Quantity 1"
    - button "Add to List"
    `);
});