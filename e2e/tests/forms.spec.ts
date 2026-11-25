import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '../fixtures'

const FORM = 'form[action$="/form/example/"]'

test.beforeEach(async ({ page }) => {
  await page.goto('/django-dsfr/form/example/')
})

test('un champ texte requis a un label DSFR, avec l’astérisque masqué aux lecteurs d’écran', async ({ page }) => {
  const label = page.locator('label[for="id_user_name"]')
  await expect(label).toHaveClass('fr-label')
  await expect(label).toHaveText('Nom d’utilisateur *')
  await expect(label.locator('.fr-required-marker')).toHaveAttribute('aria-hidden', 'true')
  await expect(page.getByRole('textbox', { name: 'Nom d’utilisateur', exact: true })).toBeVisible()
})

test('un champ facultatif n’a pas de marqueur', async ({ page }) => {
  await expect(page.locator('label[for="id_password"]')).toHaveText('Mot de passe')
})

test('le texte d’aide est dans le label, garde son HTML et décrit le champ', async ({ page }) => {
  const help = page.locator('label[for="id_user_email"] > .fr-hint-text')
  await expect(help).toHaveId('id_user_email_helptext')
  await expect(help.locator('code')).toHaveText('prenom.nom@domaine.fr')
  await expect(page.locator('#id_user_email')).toHaveAccessibleDescription('Format attendu : prenom.nom@domaine.fr')
})

test('une case à cocher requise est nommée par son label', async ({ page }) => {
  await expect(page.locator('label[for="id_sample_boolean"]')).toHaveClass('fr-label')
  await expect(page.getByRole('checkbox', { name: 'Cochez la case', exact: true })).toBeVisible()
})

test('les boutons radio et cases à cocher sont groupés sous leur légende', async ({ page }) => {
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

test('le curseur ajoute l’intervalle autorisé à son texte d’aide', async ({ page }) => {
  await expect(page.locator('#id_sample_integer_range_small_helptext')).toHaveText(
    'Déplacez les curseurs pour choisir un intervalle de prix, valeur comprise entre 10 et 70.',
  )
})

test('le contrôle segmenté garde sa légende, en ligne si demandé', async ({ page }) => {
  const inline = page.locator('legend', { hasText: 'Choix de vue segmenté avec légende inline' })
  await expect(inline).toContainClass('fr-segmented__legend fr-segmented__legend--inline')
  const regular = page.locator('legend', { hasText: /^\s*Choix de vue segmenté\s*$/ })
  await expect(regular).toContainClass('fr-segmented__legend')
  await expect(regular).not.toContainClass('fr-segmented__legend--inline')
})

test('l’interrupteur est nommé par son label', async ({ page }) => {
  await expect(page.locator('label[for="id_example_toggle"]')).toHaveClass('fr-toggle__label')
  await expect(page.getByRole('checkbox', { name: /Example toogle/ })).toBeAttached()
})

test('le formulaire ne référence que des identifiants existants (axe)', async ({ page }) => {
  const { violations } = await new AxeBuilder({ page })
    .include(FORM)
    .exclude('[id^="id_sample_integer_range"]')
    .withRules(['label', 'aria-valid-attr-value', 'duplicate-id-aria', 'aria-input-field-name'])
    .analyze()
  expect(violations).toEqual([])
})
