# IBM Bob Premium Package for Z 3.x: Features, Modes, Workflows, Skills and Labs

A bilingual (English default, French on a discreet `FR` / `EN` switch in the page header)
reference page for IBM Bob Premium Package for Z (COBOL, PL/I, JCL, HLASM): features,
modes, workflows, slash commands, skills, latest releases and the CBSA labs matrix.

- **Read it online:** https://bmarolleau.github.io/bob-ppz-prompt-guide/ (French: `/fr/`)
- **Sources:** [`src/GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs.md`](src/GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs.md) (EN) and [`src/GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs-FR.md`](src/GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs-FR.md) (FR)

## Layout

| Path | Purpose |
|---|---|
| `src/GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs.md` | English guide (edit this) |
| `src/GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs-FR.md` | French guide (edit this) |
| `src/redbook-template.html` | Pandoc template (Redbook-style look, language switch) |
| `src/build.py` | Generates `content/index.html` (EN) and `content/fr/index.html` (FR) |
| `content/` | Generated pages, published as the site |
| `mkdocs.yml`, `requirements.txt` | MkDocs project used to publish to GitHub Pages |

## Edit and rebuild

Requires Python 3 and [pandoc](https://pandoc.org/).

```sh
python3 src/build.py
```

## Preview and publish

MkDocs 1.6 needs Python 3.8 or newer. If your default `python3` is older, use a newer
interpreter to create the virtual environment.

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m mkdocs serve                  # local preview
.venv/bin/python -m mkdocs gh-deploy --strict     # publish to the gh-pages branch
```

In the repository settings, set **Pages** to deploy from the `gh-pages` branch, root (`/`).
Pushing to `main` alone does not publish.
