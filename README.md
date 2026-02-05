# pypsa-nza-plotter

Configuration-driven, reproducible plotting for publication-quality scientific figures using Matplotlib.

> **Goal:** Define figure structure + styling declaratively (via config), generate consistent figures programmatically, and avoid rewriting bespoke plotting code across studies/runs.

## Status

- ✅ Installable Python package (`pyproject.toml`)
- ✅ Basic tests passing (`pytest`)
- ✅ Examples included (see `examples/`)
- 🚧 Documentation being consolidated (see `docs/`)

## Why this exists

In research workflows (including energy systems modelling), the bottleneck is rarely “can I plot this?” — it’s:

- **reproducibility:** consistent styling across papers, chapters, and reruns
- **speed:** avoiding repetitive Matplotlib boilerplate
- **maintenance:** reducing plot code duplication as analysis evolves
- **batch generation:** automated figure production across scenarios/experiments

`pypsa-nza-plotter` provides a small set of plotting functions driven by a configuration model so you can standardize and reuse “figure intent” across projects.

## What it is (and isn’t)

**It is:**
- a configuration-driven plotting workflow on top of Matplotlib
- designed for reproducible, publication-grade figures
- practical for batch/automated figure generation

**It is not:**
- a new plotting library replacing Matplotlib
- a GUI plotting program
- an attempt to cover every possible chart type or domain

## Installation

From source (recommended during development):

```bash
pip install -e .
