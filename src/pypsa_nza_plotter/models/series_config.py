"""
Series Configuration Model

This module defines the SeriesConfig class which represents configuration
for a SINGLE data series (one line or scatter plot).

DESIGN PHILOSOPHY:
------------------
In matplotlib, line plots and scatter plots are the same thing - they both
use ax.plot(). The only difference is styling:
  - Line plot: line_style='-', marker=''
  - Scatter plot: line_style='', marker='o'
  - Combined: line_style='-', marker='o'

Therefore, we use ONE configuration class for both!

A plot can contain multiple series, each with its own SeriesConfig.
"""

from dataclasses import dataclass, asdict
from typing import Optional, List, Union
import numpy as np


@dataclass
class SeriesConfig:
    """
    Configuration for a single data series (line or scatter).
    
    This represents ONE line/scatter plot that will be drawn on axes.
    A plot can contain multiple SeriesConfig objects.
    
    Philosophy:
    -----------
    - Line and scatter are the same (just different styling)
    - Each series is independent (own color, style, markers, etc.)
    - Corresponds to one call to ax.plot() in matplotlib
    
    Examples:
    ---------
    Pure line (no markers):
        >>> series = SeriesConfig(
        ...     x=x_data, y=y_data,
        ...     line_style='-',
        ...     marker='',
        ...     color='#0066CC',
        ...     label='Fitted curve'
        ... )
    
    Pure scatter (no line):
        >>> series = SeriesConfig(
        ...     x=x_data, y=y_data,
        ...     line_style='',
        ...     marker='o',
        ...     color='#CC0000',
        ...     label='Data points'
        ... )
    
    Combined (line with markers):
        >>> series = SeriesConfig(
        ...     x=x_data, y=y_data,
        ...     line_style='-',
        ...     marker='o',
        ...     color='#9933FF',
        ...     label='Measurements'
        ... )
    """
    
    # ========== Data ==========
    # y is always required (the data values)
    # x is optional - not needed for histograms, auto-generated if None
    y: Union[List[float], np.ndarray]
    x: Optional[Union[List[float], np.ndarray]] = None
    
    # ========== Series Identification ==========
    label: str = ''  # Legend label for this series
    
    # ========== Line Properties ==========
    # Line style: '-' (solid), '--' (dashed), '-.' (dash-dot), ':' (dotted), '' (no line)
    line_style: str = '-'
    line_width: float = 1.5
    line_alpha: float = 1.0  # 0.0 (transparent) to 1.0 (opaque)
    
    # ========== Marker Properties ==========
    # Marker style: '' (none), 'o' (circle), 's' (square), '^' (triangle up),
    #               'v' (triangle down), 'd' (diamond), '*' (star), 'x' (x), etc.
    marker: str = ''
    marker_size: float = 6.0
    marker_facecolor: Optional[str] = None  # None = use series color
    marker_edgecolor: Optional[str] = None  # None = use series color
    marker_edgewidth: float = 0.5
    
    # ========== Bar/Fill Properties ==========
    # Hatch pattern for bars or filled areas
    # Patterns: '/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
    # Can combine: '//', '\\\\', '||', '--', '++', 'xx', '/o', etc.
    # None = no hatch (solid fill)
    hatch: Optional[str] = None
    
    # ========== Color ==========
    # Color for both line and markers (can be overridden by marker colors)
    # Format: '#RRGGBB' (hex) or named colors ('red', 'blue', etc.)
    color: str = '#0066CC'
    
    # ========== Error Bars (Future) ==========
    # TODO: Add support for error bars
    # x_error: Optional[np.ndarray] = None
    # y_error: Optional[np.ndarray] = None
    # error_bar_style: str = 'bars'  # 'bars', 'band', 'boxes'
    
    # ========== Fill Between (Future) ==========
    # TODO: Add support for filling under/between curves
    # fill_to: Optional[float] = None  # y-value to fill to
    # fill_alpha: float = 0.3
    
    # ========== Area Fill ==========
    fill_below: bool = False  # Fill area between curve and bottom
    fill_color: Optional[str] = None  # None = use series color
    fill_alpha: float = 0.3  # Transparency for fill (0.0-1.0)
    fill_hatch: Optional[str] = None  # Hatch pattern: '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
    hatch_color: Optional[str] = None  # Hatch line color. None = use fill_color
    
    # ========== Plot Order (Z-Order) ==========
    z_order: Optional[int] = None  # Plotting order (higher = on top). None = auto
    
    def __post_init__(self):
        """Validate and convert data to numpy arrays"""
        # Convert y to numpy array (always required)
        self.y = np.array(self.y)
        
        # Convert x to numpy array only if provided (optional for histograms)
        if self.x is not None:
            self.x = np.array(self.x)
            
            # Validate data lengths match (only if x is provided)
            if len(self.x) != len(self.y):
                raise ValueError(
                    f"x and y data must have same length. "
                    f"Got x: {len(self.x)}, y: {len(self.y)}"
                )
        
        # Set default marker colors if not specified
        if self.marker_facecolor is None:
            self.marker_facecolor = self.color
        if self.marker_edgecolor is None:
            self.marker_edgecolor = self.color
        
        # Set default fill color if not specified
        if self.fill_color is None:
            self.fill_color = self.color
        
        # Set default hatch color if not specified
        if self.hatch_color is None:
            self.hatch_color = self.fill_color
    
    def to_dict(self) -> dict:
        """
        Convert to dictionary (excluding data arrays for YAML).
        
        Note: Data (x, y) is NOT included in dict - only styling.
        This is intentional for YAML configs which reference data separately.
        """
        d = asdict(self)
        # Remove data arrays (too large for YAML, reference data files instead)
        d.pop('x')
        d.pop('y')
        return d
    
    def is_line_plot(self) -> bool:
        """Check if this series has a line component"""
        return self.line_style != ''
    
    def is_scatter_plot(self) -> bool:
        """Check if this series has markers"""
        return self.marker != ''
    
    def get_plot_type(self) -> str:
        """
        Return human-readable plot type.
        
        Returns:
            'line' - has line, no markers
            'scatter' - has markers, no line  
            'line+scatter' - has both
            'none' - neither (invalid)
        """
        has_line = self.is_line_plot()
        has_marker = self.is_scatter_plot()
        
        if has_line and has_marker:
            return 'line+scatter'
        elif has_line:
            return 'line'
        elif has_marker:
            return 'scatter'
        else:
            return 'none'  # Invalid - should have at least one!
    
    def copy(self) -> 'SeriesConfig':
        """Create a copy of this series configuration"""
        return SeriesConfig(
            x=self.x.copy(),
            y=self.y.copy(),
            label=self.label,
            line_style=self.line_style,
            line_width=self.line_width,
            line_alpha=self.line_alpha,
            marker=self.marker,
            marker_size=self.marker_size,
            marker_facecolor=self.marker_facecolor,
            marker_edgecolor=self.marker_edgecolor,
            marker_edgewidth=self.marker_edgewidth,
            color=self.color,
            fill_below=self.fill_below,
            fill_color=self.fill_color,
            fill_alpha=self.fill_alpha,
            fill_hatch=self.fill_hatch,
            hatch_color=self.hatch_color,
            z_order=self.z_order
        )


# ========== Helper Functions ==========

def create_line_series(
    x: Union[List[float], np.ndarray],
    y: Union[List[float], np.ndarray],
    label: str = '',
    color: str = '#0066CC',
    line_style: str = '-',
    line_width: float = 1.5
) -> SeriesConfig:
    """
    Helper to create a pure line series (no markers).
    
    This is a convenience function for the common case of a simple line.
    
    Example:
        >>> series = create_line_series(x, y, 'My Line', '#FF0000')
    """
    return SeriesConfig(
        x=x, y=y,
        label=label,
        color=color,
        line_style=line_style,
        line_width=line_width,
        marker=''  # No markers
    )


def create_scatter_series(
    x: Union[List[float], np.ndarray],
    y: Union[List[float], np.ndarray],
    label: str = '',
    color: str = '#0066CC',
    marker: str = 'o',
    marker_size: float = 6.0
) -> SeriesConfig:
    """
    Helper to create a pure scatter series (no line).
    
    This is a convenience function for the common case of scatter points.
    
    Example:
        >>> series = create_scatter_series(x, y, 'Data', '#CC0000', marker='s')
    """
    return SeriesConfig(
        x=x, y=y,
        label=label,
        color=color,
        line_style='',  # No line
        marker=marker,
        marker_size=marker_size
    )


def create_line_scatter_series(
    x: Union[List[float], np.ndarray],
    y: Union[List[float], np.ndarray],
    label: str = '',
    color: str = '#0066CC',
    line_style: str = '-',
    line_width: float = 1.5,
    marker: str = 'o',
    marker_size: float = 6.0
) -> SeriesConfig:
    """
    Helper to create a combined line+scatter series.
    
    Example:
        >>> series = create_line_scatter_series(x, y, 'Measurements', '#9933FF')
    """
    return SeriesConfig(
        x=x, y=y,
        label=label,
        color=color,
        line_style=line_style,
        line_width=line_width,
        marker=marker,
        marker_size=marker_size
    )
