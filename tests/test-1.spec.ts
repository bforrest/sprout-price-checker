import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://shop.sprouts.com/store/sprouts/products/47831-tera-s-whey-whey-protein-organic-grass-fed-unsweetened-12-oz');
  await page.getByRole('button', { name: 'REJECT COOKIES' }).click();
  
  await expect(page.locator('#item_details')).toMatchAriaSnapshot(`
    - text: "/Original price:|% off/"
    - combobox "Quantity 1"
    - button "Add to List"
    `);
});