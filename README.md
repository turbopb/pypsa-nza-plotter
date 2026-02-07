# pypsa-nza-plotter

** A configuration-driven, reproducible plotting for publication-quality scientific figures**

# pypsa-nza-plotter

**pypsa-nza-plotter** is a configuration-driven plotting system for producing reproducible, publication-quality scientific figures using matplotlib.

Rather than embedding plot structure, styling, and parameters directly in Python scripts, figures are specified declaratively via configuration files. These configurations are then rendered programmatically, enabling deterministic regeneration of figures across machines, experiments, and analysis pipelines with minimal code duplication.

The package is designed for research workflows where figures are generated repeatedly (e.g. across scenarios, sensitivity analyses, or model runs) and where reproducibility, consistency, and clarity are more important than interactive plotting.



## Scope

### What this package is
- A configuration-driven interface to matplotlib
- A tool for reproducible, publication-quality figure generation
- Designed for batch plotting, automation, and research pipelines

### What this package is not
- Not a replacement for matplotlib
- Not an interactive plotting environment
- Not a grammar-of-graphics framework

---

## Design philosophy

The core design principles are:

- **Declarative configuration**  
  Plot appearance is defined via a `PlotConfig` object (or YAML file), not ad-hoc Matplotlib calls.

- **Separation of configuration and data**  
  - `PlotConfig` controls global figure and axes styling  
  - `SeriesConfig` controls per-series intent (data, colour, label, etc.)

- **Reproducibility first**  
  Figures can be regenerated exactly by reusing the same configuration.

- **Matplotlib compatibility**  
  All plotting functions return standard `(fig, ax)` objects for downstream customisation.

- **Small, stable public API**  
  A minimal set of core plotters is provided; advanced usage builds on these primitives.

---

## Installation

### From source (development / review)

```bash
git clone https://github.com/turbopb/pypsa-nza-plotter.git
cd pypsa-nza-plotter
pip install -e .
```

---

## Minimal runable demo

The following command generates two example figures (a line plot and a histogram)
using the public API and saves them to disk.

```bash
python -m pypsa_nza_plotter.demo --outdir demo_output
```

### Expected output

```
Demo figures created:
  - demo_output/demo_line.png
  - demo_output/demo_histogram.png
```

This demo is **headless-safe** (uses `matplotlib.use("Agg")`) and runs in CI environments.

---

## Minimal usage example

```python
import numpy as np
from pypsa_nza_plotter import PlotConfig, SeriesConfig, create_line_plot

x = np.linspace(0, 1, 200)
y = np.sin(2 * np.pi * x)

config = PlotConfig(
    title="Example line plot",
    x_label="x",
    y_label="sin(2πx)"
)

series = SeriesConfig(
    x=x,
    y=y,
    label="signal",
    color="#0066CC"
)

fig, ax = create_line_plot([[series]], config)
fig.show()
```

---

## Configuration-driven workflow

A typical workflow is:

1. Start with a simple plot
2. Move all styling into `PlotConfig`
3. Refine appearance (ticks, fonts, grids, figure size) without touching plotting code
4. Optionally serialize the configuration to YAML for reuse

```python
config.to_yaml("publication_style.yaml")
config = PlotConfig.from_yaml("publication_style.yaml")
```

---

## Tests

A minimal smoke-test suite verifies that figures are generated correctly.

Run tests with:

```bash
pytest
```

### Expected output

```
3 passed in <1s
```

---

## Advanced examples

More complex, publication-style examples (including subplots and multi-panel figures)
are provided in the `examples/` directory. These are not required for review, but
demonstrate how the same API scales to real research figures.

---

## License

MIT License

```

---
