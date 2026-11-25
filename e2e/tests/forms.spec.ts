import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '../fixtures'

const FORM = 'form[action$="/form/example/"]'

test.beforeEach(async ({ page }) => {
  await page.goto('/django-dsfr/form/example/')
})

test('le libellé d’un champ requis est stylisé DSFR, et son astérisque reste caché aux lecteurs d’écran', async ({ page }) => {
  const label = page.locator('label[for="id_user_name"]')
  await expect(label).toHaveClass('fr-label')
  await expect(label).toHaveText('Nom d’utilisateur *')
  await expect(label.locator('.fr-required-marker')).toHaveAttribute('aria-hidden', 'true')
  await expect(page.getByRole('textbox', { name: 'Nom d’utilisateur', exact: true })).toBeVisible()
})

test('un champ facultatif n’affiche pas d’astérisque', async ({ page }) => {
  await expect(page.locator('label[for="id_password"]')).toHaveText('Mot de passe')
})

test('le texte d’aide reste dans le libellé, garde son HTML et décrit bien le champ', async ({ page }) => {
  const help = page.locator('label[for="id_user_email"] > .fr-hint-text')
  await expect(help).toHaveId('id_user_email_helptext')
  await expect(help.locator('code')).toHaveText('prenom.nom@domaine.fr')
  await expect(page.locator('#id_user_email')).toHaveAccessibleDescription('Format attendu : prenom.nom@domaine.fr')
})

test('une case à cocher requise est bien reliée à son libellé', async ({ page }) => {
  await expect(page.locator('label[for="id_sample_boolean"]')).toHaveClass('fr-label')
  await expect(page.getByRole('checkbox', { name: 'Cochez la case', exact: true })).toBeVisible()
})

test('boutons radio et cases à cocher partagent une légende de groupe, avec son texte d’aide', async ({ page }) => {
  for (const [name, help] of [
    ['radio', 'Boutons radio'],
    ['checkbox', 'Cases à cocher'],
  ]) {
    const legend = page.locator(`#id_sample_${name}-legend`)
    await expect(legend).toHaveClass('fr-fieldset__legend fr-fieldset__legend--regular')
    await expect(legend.locator('.fr-hint-text')).toHaveId(`id_sample_${name}_helptext`)
    await expect(
      page.getByRole('group', { name: `${help} Le troisième choix renvoie une erreur s’il est sélectionné`, exact: true }),
    ).toBeVisible()
  }
})

test('le texte d’aide du curseur de plage mentionne bien l’intervalle autorisé', async ({ page }) => {
  await expect(page.locator('#id_sample_integer_range_small_helptext')).toHaveText(
    'Déplacez les curseurs pour choisir un intervalle de prix, valeur comprise entre 10 et 70.',
  )
})

test('le contrôle segmenté affiche sa légende, en ligne quand on le demande', async ({ page }) => {
  const inline = page.locator('legend', { hasText: 'Choix de vue segmenté avec légende inline' })
  await expect(inline).toContainClass('fr-segmented__legend fr-segmented__legend--inline')
  const regular = page.locator('legend', { hasText: /^\s*Choix de vue segmenté\s*$/ })
  await expect(regular).toContainClass('fr-segmented__legend')
  await expect(regular).not.toContainClass('fr-segmented__legend--inline')
})

test('l’interrupteur est bien relié à son libellé', async ({ page }) => {
  await expect(page.locator('label[for="id_example_toggle"]')).toHaveClass('fr-toggle__label')
  await expect(page.getByRole('checkbox', { name: /Example toogle/ })).toBeAttached()
})

test('toutes les références d’identifiants du formulaire pointent vers un élément existant (axe)', async ({ page }) => {
  const { violations } = await new AxeBuilder({ page })
    .include(FORM)
    .exclude('[id^="id_sample_integer_range"]')
    .withRules(['label', 'aria-valid-attr-value', 'duplicate-id-aria', 'aria-input-field-name'])
    .analyze()
  expect(violations).toEqual([])
})
