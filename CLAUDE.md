# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project overview

`django-dsfr` is a Django app that integrates the French government's design
system (DSFR — Système de Design de l'État) into Django projects: template
tags/inclusion templates for DSFR components (buttons, cards, alerts, forms,
header/footer, etc.), a `DsfrConfig` admin model for site-wide settings, and
vendored DSFR static assets. Published on PyPI. Supports Python 3.10–3.14 and
Django >4.2.27 (tested on 4.2, 5.0, 5.1, 5.2, 6.0).

Note: the DSFR design system itself may only be used by official French
government websites — this is a legal constraint on the underlying design
system, not on this Python package (MIT licensed, excluding the "Marianne"
font).

## Tooling: use `just` and `uv`, not `make`

- Package manager: **uv**. Never hand-edit `uv.lock`; use `uv add [--dev] <pkg>`.
- Task runner: **just** (see `justfile`). A `Makefile` also exists but is
  deprecated — every target in it just prints a warning to use `just` instead.

Key recipes (`just <recipe>`, or `just` alone to list them):

| Recipe | What it does |
| --- | --- |
| `init` | `uv sync --dev --all-extras`, install pre-commit hooks, migrate, collectstatic, load sample data |
| `runserver` (alias `rs`) | Run the demo/example Django site (`config` project) |
| `test [app]` | Run tests for the whole project or one app |
| `coverage [app]` | Run tests with coverage, build HTML report, open in Firefox |
| `quality` | Run all pre-commit hooks against the whole repo |
| `export_static` | Build the static documentation site via django-distill |
| `static_server` | Serve the exported static docs locally |
| `makemessages` / `compilemessages` | i18n (French locale) |
| `update_dsfr` | Pull latest upstream DSFR release, trim assets, refresh checksums |
| `prepare_release {major\|minor\|patch}` | Bump version, create `release/<version>` branch |

## Testing

- Tests run through Django's own test runner: `just test` or
  `uv run python manage.py test [app]` — **not** pytest, even though `pytest`
  is listed as a dev dependency (unused leftover; don't assume pytest
  conventions/fixtures apply).
- CI runs the test suite against multiple Django majors
  (supported versions are listed in the README.md) — avoid
  code that depends on a single Django version's behavior.
- CI also runs `manage.py makemigrations --check --dry-run --noinput` on every
  push — always generate and commit migrations when models change, or CI
  fails.
- Run a single test: `uv run python manage.py test dsfr.test.test_templatetags.ClassName.test_method`.

## Linting & formatting

Run everything with `just quality` (= `pre-commit run --all-files`). Configured
hooks:

- **ruff** — general linting.
- **black** — formatting, line-length 88.
- **djlint** — lints/reformats Django templates (`[tool.djlint]` in
  `pyproject.toml`: 2-space indent, ignores `H030,H031,H006`; a few templates
  have per-file ignores).
- **bandit** — security linting (excludes `/tests/`).
- **markdownlint** — Markdown style.

Always run `just quality` before considering a change done; CI does not
currently re-run these hooks separately from the test workflow, but
pre-commit is the source of truth for style.

## Repository structure

| Path | Purpose |
| --- | --- |
| `dsfr/` | The actual published package: models, templatetags, templates, static DSFR assets, forms/widgets, management commands, tests. This is what matters for most feature work. |
| `example_app/` | Demo Django app showcasing every component; also the source that gets exported into the documentation site. |
| `config/` | Django project (settings/urls) used to run `example_app` locally. |
| `doc/*.md` | Source Markdown content rendered into documentation pages. |
| `docs/` | **Generated output** (static export via django-distill), deployed to GitHub Pages. Never hand-edit — edit `doc/*.md` or `example_app/` and run `just export_static` instead. |
| `static/`, `media/`, `dist/`, `htmlcov/`, `db.sqlite3` | Build/dev artifacts, not source. |
| `scripts/download_latest.sh` | Used by `just update_dsfr` to pull upstream DSFR releases. |

Inside `dsfr/`:

- `templatetags/dsfr_tags.py` — all public `{% dsfr_* %}` template tags
(the main Python API surface of the package).
- `templates/dsfr/<component>.html` — one template per DSFR component,
  rendered by the matching inclusion tag.
- `models.py` — `DsfrConfig`/`DsfrSocialMedia`, admin-configurable site
  settings, exposed to templates via `dsfr.context_processors.site_config`.
- `forms.py` / `widgets.py` / `fields.py` — `DsfrDjangoTemplates` renderer and
  `DsfrBoundField` for DSFR-styled Django form rendering.
- `utils.py` — shared helpers, including `parse_tag_args` used by most
  inclusion tags to normalize arguments.
- `checksums.py` / `constants.py` — vendored asset integrity hashes and DSFR
  asset path enums.
- `static/dsfr/` — vendored upstream DSFR CSS/JS/fonts/icons.
- `test/` — Django `TestCase`-based test suite, one file per concern
  (`test_templatetags.py`, `test_forms.py`, etc.).

## Adding or changing a DSFR component

Follow the existing pattern (see any entry in `dsfr/templatetags/dsfr_tags.py`
for reference):

1. Template: `dsfr/templates/dsfr/<name>.html`.
2. Tag: `@register.inclusion_tag("dsfr/<name>.html")` function named
   `dsfr_<name>` in `dsfr/templatetags/dsfr_tags.py`; use `parse_tag_args` from
   `dsfr/utils.py` to normalize `*args, **kwargs` into the template context.
   Use `takes_context=True` only if the tag needs `request`/context (e.g. for
   active-state detection, as in `dsfr_breadcrumb`).
3. Deprecating a parameter: gate the warning behind
   `settings.DSFR_CHECK_DEPRECATED_PARAMS` unless it should always warn.
4. Add/update a demo entry in `example_app/dsfr_components.py`'s
   `IMPLEMENTED_COMPONENTS` dict so the component shows up in the docs site.
5. Add tests under `dsfr/test/` and run `just test`.

## Language conventions

- **Code, code comments, and git branch names: English.**
- **Documentation, component examples, and PR titles: French.**
- Issues may be opened in either language.
- In practice, commit messages end up mixed French/English (squash-merge
  titles inherit the PR title, which is French; dependabot/chore commits are
  English) — don't assume one language when reading git history.

## Consumer-facing settings & known gotchas

- Django < 5.0 requires `django.forms` in `INSTALLED_APPS` *after* `dsfr`,
  plus `FORM_RENDERER = "django.forms.renderers.TemplatesSetting"` in
  settings — otherwise `FormSet`s render incorrectly. Relevant whenever
  touching `dsfr/forms.py`, `widgets.py`, or `fields.py`.
- `dsfr.context_processors.site_config` must be added to
  `TEMPLATES[].OPTIONS.context_processors` for `DsfrConfig` to be available in
  templates — it isn't wired up automatically by installing the app.
- Optional settings consumers can define (see `INSTALL.md`):
  `DSFR_CHECK_DEPRECATED_PARAMS`, `DSFR_USE_INTEGRITY_CHECKSUMS`,
  `DSFR_MARK_OPTIONAL_FIELDS`, `DSFR_MESSAGE_TAGS_CSS_CLASSES`.

## Release process (for context, not routine work)

`just prepare_release {major|minor|patch}` bumps the version and creates a
`release/<version>` branch; after merge, a GitHub Release with tag
`v<version>` triggers `publish-package.yml` (`uv build` + `uv publish` via
PyPI trusted publishing). Documentation redeploys automatically on push to
`main` via `deploy-doc.yml`. Don't trigger releases unless explicitly asked.
