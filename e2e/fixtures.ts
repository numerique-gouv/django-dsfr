import { test as base, expect } from '@playwright/test'

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

export { expect }
