"""
Models Package

Contains data model classes for plot configuration.

DESIGN STRUCTURE:
-----------------
PlotConfig = Global settings (applies to whole plot)
  - Text sizing
  - Grid, legend
  - Axis scales
  - Figure dimensions

SeriesConfig = Individual series settings (applies to one line/scatter)
  - Line style, width, color
  - Marker style, size
  - Data (x, y arrays)

This separation makes it clear what applies globally vs. per-series!
"""

# Global configuration
from .plot_config import (
    PlotConfig,
    get_preset_config,
    PRESET_CONFIGS
)

# Series configuration
from .series_config import (
    SeriesConfig,
    create_line_series,
    create_scatter_series,
    create_line_scatter_series
)

__all__ = [
    # Global configuration
    'PlotConfig',
    'get_preset_config',
    'PRESET_CONFIGS',
    
    # Series configuration
    'SeriesConfig',
    'create_line_series',
    'create_scatter_series',
    'create_line_scatter_series',
]
