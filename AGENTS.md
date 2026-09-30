# AGENTS.md

Data-science / AI exploration project (compare ML vs LLM algorithms on CFPB consumer-complaints data). Early scaffold: no tests, lint, or CI yet.

## Toolchain

- Package manager is **uv** (not pip/venv). Active venv already at `.venv/`. Use `uv add`, `uv run`, `uv sync`.
- Python 3.13 (`.python-version`, `requires-python = ">=3.13"`).
- `pyproject.toml` uses the `uv_build` backend with a **src layout**: the importable package is `app`, living at `src/app/`. Console script is `mission-1 = "app:main"` (in `src/app/__init__.py`).
- Data lives at `src/data/dataset.csv` (CFPB consumer complaints).

## Notebooks

- Work happens in `src/app/exploration.ipynb`, scored with a kernel named **`zenassist`** (display "Python (ZenAssist)"). It is NOT installed in `.venv` yet; if the kernel is missing, register it against the venv:
  `uv run python -m ipykernel install --name zenassist  --display-name "Python (ZenAssist)"`
- The notebook is authored in **French**; keep markdown/annotations in French. It references a specific visual style (dark-blue headings `#1A5276`/`#2980B9`).
- Dev deps (`[dependency-groups].dev`) currently only include `ipykernel`; data libraries (pandas, matplotlib, scikit-learn) are not added yet — use `uv add` before importing them.
- `.venv` and build artifacts are gitignored; do not commit them.

## Mission_1

The company offers a customer support complaint tracking platform that centralizes and optimizes complaint management for over 200 businesses.
Its goal is to automate the tagging of these complaints to reduce the manual workload required to route complaints to the appropriate support team.
You have been tasked with designing this automated tagging solution by comparing a Large Language Model (LLM)-based approach with various machine learning methods. You will need to provide a recommendation to your client, taking all these constraints into account.
