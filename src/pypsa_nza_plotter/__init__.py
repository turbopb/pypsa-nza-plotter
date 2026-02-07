"""
pypsa-nza-plotter

A configuration-driven plotting toolkit for reproducible, publication-quality
matplotlib figures, originally developed for PyPSA-NZ energy systems workflows.

Design principles:
- Separate global figure/axes configuration (PlotConfig) from per-series intent (SeriesConfig)
- Generate figures programmatically from declarative specifications to improve reproducibility
- Return standard matplotlib (fig, ax) objects to allow downstream customization
- Keep a small, stable public API; provide additional plotters as extras/experimental modules
"""

from __future__ import annotations

# Version is intentionally defined here so tools can introspect it.
# You can automate this later (e.g., via setuptools-scm), but keep it simple for v0.1.
__version__ = "0.1.1"

# ---------------------------------------------------------------------------
# Core public API: models (stable)
# ---------------------------------------------------------------------------
from .models.plot_config import PlotConfig
from .models.series_config import SeriesConfig

# Optional: expose preset helpers if you have them in PlotConfig.
# If these do not exist in your PlotConfig implementation, delete these imports.
try:
    from .models.plot_config import get_preset_config  # type: ignore
except Exception:  # pragma: no cover
    get_preset_config = None  # type: ignore


# ---------------------------------------------------------------------------
# Core public API: renderers (stable)
# ---------------------------------------------------------------------------
from .core.line_plotter import create_line_plot
from .core.histogram_plotter import create_histogram
from .core.subplot_plotter import create_subplots

# Optional: expose save_plot if it exists somewhere in your codebase.
# If you place it in src/pypsa_nza_plotter/utils.py, change the import accordingly.
try:
    from .utils import save_plot  # type: ignore
except Exception:  # pragma: no cover
    save_plot = None  # type: ignore


# ---------------------------------------------------------------------------
# Public symbols
# ---------------------------------------------------------------------------
__all__ = [
    "__version__",
    "PlotConfig",
    "SeriesConfig",
    "get_preset_config",
    "create_line_plot",
    "create_histogram",
    "create_subplots",
    "save_plot",
]
