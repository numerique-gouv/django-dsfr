import { test as base, expect, type Locator } from '@playwright/test'

export const test = base.extend<{ sandbox: void }>({
  sandbox: [
    async ({ context, page, baseURL }, use) => {
      const origin = new URL(baseURL!).origin
      await context.route('**/*', (route) =>
        new URL(route.request().url()).origin === origin ? route.fallback() : route.abort('blockedbyclient'),
      )
      const errors: Error[] = []
      page.on('pageerror', (error) => errors.push(error))
      await use()
      expect(errors, 'uncaught JavaScript errors').toEqual([])
    },
    { auto: true },
  ],
})

/** Ids referenced by aria-describedby / aria-labelledby inside `root` that match no element of the page. */
export const danglingIdRefs = (root: Locator): Promise<string[]> =>
  root.evaluate((el) =>
    [...el.querySelectorAll('[aria-describedby], [aria-labelledby]')]
      .flatMap((node) => `${node.getAttribute('aria-describedby') ?? ''} ${node.getAttribute('aria-labelledby') ?? ''}`.split(/\s+/))
      .filter((id) => id && !document.getElementById(id)),
  )

export { expect }
