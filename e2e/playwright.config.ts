import { defineConfig, devices } from '@playwright/test'

const isCI = !!process.env.CI
const port = Number(process.env.E2E_PORT ?? 8765)

export default defineConfig({
  testDir: './tests',
  outputDir: './.cache/test-results',
  forbidOnly: isCI,
  retries: isCI ? 2 : 0,
  reporter: isCI ? [['github'], ['html', { open: 'never', outputFolder: '.cache/report' }]] : [['list']],
  use: {
    baseURL: `http://localhost:${port}`,
    locale: 'fr-FR',
    timezoneId: 'Europe/Paris',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'], contextOptions: { reducedMotion: 'reduce' } },
    },
  ],
  webServer: {
    command: `uv run python manage.py migrate --noinput > /dev/null && uv run python manage.py runserver ${port} --noreload`,
    cwd: '..',
    url: `http://localhost:${port}/`,
    reuseExistingServer: !isCI,
    timeout: 120_000,
  },
})
