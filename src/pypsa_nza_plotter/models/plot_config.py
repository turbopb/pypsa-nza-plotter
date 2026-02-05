"""
Plot Configuration Model (Refactored)

This module defines PlotConfig which contains GLOBAL plot settings that
apply to the entire figure/axes, NOT individual series.

DESIGN CHANGE:
--------------
OLD: PlotConfig contained both global settings AND series-specific settings
     (line color, marker style, etc.)
     
NEW: PlotConfig contains ONLY global settings (tick sizes, grid, etc.)
     Series-specific settings moved to SeriesConfig class

This separation makes it clearer what applies globally vs. per-series.

WHAT BELONGS HERE:
------------------
✓ Text sizing (tick labels, axis labels, title)
✓ Figure dimensions
✓ Grid settings
✓ Legend settings  
✓ Axis scales and limits
✓ Spine visibility
✓ Background colors

WHAT DOES NOT BELONG HERE:
---------------------------
✗ Line colors, styles, widths (→ SeriesConfig)
✗ Marker styles, sizes (→ SeriesConfig)
✗ Individual series labels (→ SeriesConfig)
"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any, Tuple
import yaml
from datetime import datetime


@dataclass
class PlotConfig:
    """
    Global configuration for a plot (applies to entire figure/axes).
    
    This contains settings that affect the whole plot, not individual
    data series. For series-specific settings, use SeriesConfig.
    
    Philosophy:
    -----------
    - One PlotConfig per figure
    - Multiple SeriesConfig per figure
    - PlotConfig = the "canvas" settings
    - SeriesConfig = what you draw on the canvas
    
    Example:
    --------
    >>> config = PlotConfig(
    ...     tick_label_size=12,
    ...     axis_label_size=14,
    ...     figure_width=8.0,
    ...     show_grid=True
    ... )
    >>> # This config applies to the whole plot
    >>> # Individual series have their own SeriesConfig
    """
    
    # ========== Metadata ==========
    version: str = "2.0"  # Version 2.0 - refactored design!
    description: str = ""
    created: Optional[str] = None
    
    # ========== Figure Dimensions ==========
    # Control overall figure size
    figure_width: float = 8.0       # inches
    figure_height: float = 6.0      # inches
    dpi: int = 100                  # dots per inch (screen display)
    aspect_ratio: Optional[float] = None  # If set, overrides figure_height
    
    # ========== Figure Background ==========
    figure_facecolor: str = '#FFFFFF'  # Outside the axes
    axes_facecolor: str = '#FFFFFF'    # Inside the axes (plot area)
    
    # ========== Text Sizing (PRIORITY FEATURE) ==========
    # These are GLOBAL - apply to all text on the plot
    
    # Tick labels (the numbers on axes) (EXTENDED)
    tick_label_size: float = 10.0
    x_tick_label_size: Optional[float] = None  # None = use tick_label_size
    y_tick_label_size: Optional[float] = None  # None = use tick_label_size
    tick_label_family: str = 'sans-serif'
    tick_label_weight: str = 'normal'  # 'normal', 'bold'
    tick_label_color: str = '#000000'  # Color for tick labels
    
    # Axis labels (e.g., "Time (s)", "Temperature (°C)") (EXTENDED)
    axis_label_size: float = 12.0
    x_axis_label_size: Optional[float] = None  # None = use axis_label_size
    y_axis_label_size: Optional[float] = None  # None = use axis_label_size
    axis_label_family: str = 'sans-serif'
    axis_label_weight: str = 'normal'
    axis_label_color: str = '#000000'  # Color for axis labels
    axis_label_style: str = 'normal'   # 'normal', 'italic', 'oblique'
    
    # Title (EXTENDED)
    title_size: float = 14.0
    title_family: str = 'sans-serif'
    title_weight: str = 'normal'  # Changed from 'bold' to 'normal' (per user request)
    title_style: str = 'normal'   # 'normal', 'italic', 'oblique'
    title_color: str = '#000000'
    title_pad: Optional[float] = None  # Space between title and plot (None = auto)
    
    # Legend text (EXTENDED)
    legend_font_size: float = 10.0
    legend_font_family: str = 'sans-serif'
    legend_font_weight: str = 'normal'  # 'normal', 'bold'
    legend_title_weight: str = 'bold'   # For legend title if present
    
    # ========== Labels ==========
    # These are the actual text strings
    title: str = ""
    x_label: str = ""
    y_label: str = ""
    
    # ========== Axes Configuration ==========
    # Scale
    x_scale: str = 'linear'  # 'linear', 'log', 'symlog'
    y_scale: str = 'linear'
    
    # Limits (None = auto)
    x_limits: Optional[Tuple[float, float]] = None  # (min, max)
    y_limits: Optional[Tuple[float, float]] = None
    
    # Ticks
    x_ticks: Optional[List[float]] = None  # Custom tick locations
    y_ticks: Optional[List[float]] = None
    x_tick_labels: Optional[List[str]] = None  # Custom tick labels
    y_tick_labels: Optional[List[str]] = None
    
    # Minor ticks
    show_minor_ticks: bool = False
    
    # Spine visibility (the box around the plot)
    show_top_spine: bool = True
    show_right_spine: bool = True
    show_bottom_spine: bool = True
    show_left_spine: bool = True
    
    # ========== Legend ==========
    # Legend is GLOBAL (applies to all series)
    show_legend: bool = True
    legend_location: str = 'best'  # 'best', 'upper right', 'lower left', etc.
    legend_frameon: bool = True    # Draw box around legend
    legend_framealpha: float = 0.8
    legend_shadow: bool = False
    
    # ========== Grid ==========
    # Grid is GLOBAL (applies to whole axes)
    show_grid: bool = True
    grid_which: str = 'major'  # 'major', 'minor', 'both'
    grid_axis: str = 'both'    # 'both', 'x', 'y'
    grid_alpha: float = 0.3
    grid_style: str = '--'
    grid_linewidth: float = 0.5
    grid_color: str = '#888888'
    
    # ========== Layout ==========
    tight_layout: bool = True
    subplot_adjust: Optional[Dict[str, float]] = None  # left, right, top, bottom
    
    def __post_init__(self):
        """Set defaults and validate"""
        if self.created is None:
            self.created = datetime.now().isoformat()
        
        # Apply aspect ratio if specified
        if self.aspect_ratio is not None:
            self.figure_height = self.figure_width / self.aspect_ratio
        
        # Set per-axis sizes if not specified
        if self.x_tick_label_size is None:
            self.x_tick_label_size = self.tick_label_size
        if self.y_tick_label_size is None:
            self.y_tick_label_size = self.tick_label_size
        if self.x_axis_label_size is None:
            self.x_axis_label_size = self.axis_label_size
        if self.y_axis_label_size is None:
            self.y_axis_label_size = self.axis_label_size
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        data = asdict(self)
        # Convert tuples to lists for YAML serialization
        if data['x_limits'] is not None:
            data['x_limits'] = list(data['x_limits'])
        if data['y_limits'] is not None:
            data['y_limits'] = list(data['y_limits'])
        return data
    
    def to_yaml(self, filepath: str):
        """Save configuration to YAML file"""
        with open(filepath, 'w') as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False, sort_keys=False)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PlotConfig':
        """Create PlotConfig from dictionary"""
        # Convert lists back to tuples where needed
        if data.get('x_limits') is not None:
            data['x_limits'] = tuple(data['x_limits'])
        if data.get('y_limits') is not None:
            data['y_limits'] = tuple(data['y_limits'])
        
        # Filter out keys that aren't in PlotConfig
        import inspect
        sig = inspect.signature(cls)
        valid_keys = set(sig.parameters.keys())
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        
        return cls(**filtered_data)
    
    @classmethod
    def from_yaml(cls, filepath: str) -> 'PlotConfig':
        """Load configuration from YAML file"""
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        return cls.from_dict(data)
    
    def copy(self) -> 'PlotConfig':
        """Create a copy of this configuration"""
        return PlotConfig.from_dict(self.to_dict())
    
    def update(self, **kwargs):
        """Update configuration parameters"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


# ========== Preset Configurations ==========

PRESET_CONFIGS = {
    'default': PlotConfig(),
    
    'publication': PlotConfig(
        figure_width=6.0,
        figure_height=4.5,
        dpi=300,
        tick_label_size=10,
        axis_label_size=12,
        title_size=14,
        grid_alpha=0.2
    ),
    
    'presentation': PlotConfig(
        figure_width=10.0,
        figure_height=7.5,
        dpi=150,
        tick_label_size=14,
        axis_label_size=16,
        title_size=18
    ),
    
    'nature_style': PlotConfig(
        figure_width=3.5,  # Nature single column
        figure_height=2.625,
        dpi=300,
        tick_label_size=7,
        axis_label_size=8,
        title_size=8,
        legend_font_size=7,
        show_grid=False,
        show_top_spine=False,
        show_right_spine=False
    ),
    
    'science_style': PlotConfig(
        figure_width=3.3,  # Science single column
        figure_height=2.5,
        dpi=300,
        tick_label_size=6,
        axis_label_size=7,
        title_size=8,
        legend_font_size=6,
        show_grid=False,
        show_top_spine=False,
        show_right_spine=False
    )
}


def get_preset_config(preset_name: str) -> PlotConfig:
    """
    Get a predefined configuration.
    
    Args:
        preset_name: One of 'default', 'publication', 'presentation', 
                    'nature_style', 'science_style'
    
    Returns:
        PlotConfig object
    
    Example:
        >>> config = get_preset_config('nature_style')
        >>> config.title = 'My Title'  # Customize as needed
    """
    if preset_name not in PRESET_CONFIGS:
        raise ValueError(f"Unknown preset: {preset_name}. "
                        f"Available: {list(PRESET_CONFIGS.keys())}")
    
    return PRESET_CONFIGS[preset_name].copy()
