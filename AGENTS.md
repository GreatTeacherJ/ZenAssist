# AGENTS.md

Projet d'exploration data-science / IA (comparaison d'algorithmes ML vs LLM sur les données de plaintes consommateurs CFPB). Première version du scaffold : pas encore de tests, lint, ni CI.

## Toolchain

- Gestionnaire de paquets : **uv** (pas pip/venv). Environnement virtuel actif : `.venv/`. Utiliser `uv add`, `uv run`, `uv sync`.
- Python 3.13 (`.python-version`, `requires-python = ">=3.13"`).
- `pyproject.toml` utilise le backend `uv_build` avec une **structure src** : le package importable est `app`, situé dans `src/app/`. Le script console est `mission-1 = "app:main"` (dans `src/app/__init__.py`).
- Les données se trouvent dans `src/data/dataset.csv` (plaintes consommateurs CFPB).

## Notebooks

- Le travail se fait dans `src/app/exploration.ipynb`, évalué avec le kernel **`zenassist`** (affichage « Python (ZenAssist) »). Il n'est pas encore installé dans `.venv` ; si le kernel manque, l'enregistrer contre le venv :
  `uv run python -m ipykernel install --name zenassist --display-name "Python (ZenAssist)"`
- Le notebook est rédigé en **français** ; conserver les annotations/markdown en français. Il référence un style visuel spécifique (titres bleu foncé `#1A5276` / `#2980B9`).
- Les dépendances de données sont installées dans `[project]` : `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `sentence-transformers`. Les dépendances dev (`[dependency-groups].dev`) contiennent `ipykernel`, `nbclient`, `nbconvert`, `nbformat` et `pandas`. Toujours utiliser `uv add` pour toute nouvelle dépendance.
- `.venv` et les artefacts de build sont gitignorés ; ne pas les committer.

## Mission_1

L'entreprise propose une plateforme de suivi des réclamations du support client qui centralise et optimise la gestion des plaintes pour plus de 200 entreprises.
Son objectif est d'automatiser le taggage de ces plaintes afin de réduire la charge de travail manuel nécessaire au routage des plaintes vers l'équipe de support appropriée.
Vous êtes chargé de concevoir cette solution de taggage automatisé en comparant une approche basée sur un Large Language Model (LLM) avec diverses méthodes de machine learning. Vous devrez fournir une recommandation à votre client, en tenant compte de toutes ces contraintes.