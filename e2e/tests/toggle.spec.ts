import { danglingIdRefs, expect, test } from '../fixtures'

test('chaque interrupteur, même avec un id personnalisé, pointe vers un texte d’aide existant', async ({ page }) => {
  await page.goto('/django-dsfr/components/toggle/')
  await expect(page.locator('#toggle-full')).toHaveAttribute('aria-describedby')
  expect(await danglingIdRefs(page.locator('main'))).toEqual([])
})
