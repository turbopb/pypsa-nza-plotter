"""
Contour Plot Plotter - PlotLib v2.8.0

Creates contour plots for 2D function visualization with comprehensive customization.

DESIGN PHILOSOPHY:
------------------
- Uses same PlotConfig for global settings
- Supports filled contours, line contours, or both
- Custom levels and colormaps
- Contour labels
- Returns (fig, ax) for consistency

USAGE:
------
Basic filled contour:
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig, ax = create_contour_plot(X, Y, Z, config, filled=True)

Line contours with labels:
    fig, ax = create_contour_plot(X, Y, Z, config, 
                                   filled=False, labels=True)

Both filled and lines:
    fig, ax = create_contour_plot(X, Y, Z, config,
                                   filled=True, lines=True)
"""

import matplotlib
##matplotlib.use('Agg')  # Commented for interactive  # Commented for interactive
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
from typing import Tuple, Optional, List, Union
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.plot_config import PlotConfig


def create_contour_plot(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    config: Optional[PlotConfig] = None,
    filled: bool = True,
    lines: bool = False,
    levels: Union[int, List[float], None] = None,
    cmap: str = 'viridis',
    labels: bool = False,
    label_fontsize: int = 9,
    label_format: str = '%1.1f',
    cbar: bool = True,
    cbar_label: Optional[str] = None,
    line_colors: str = 'black',
    line_widths: float = 1.0,
    line_styles: str = 'solid',
    alpha: float = 1.0,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create contour plot for 2D function visualization.
    
    Args:
        X: 2D array of x-coordinates (from meshgrid)
        Y: 2D array of y-coordinates (from meshgrid)
        Z: 2D array of function values
        config: PlotConfig for global settings (optional)
        filled: Show filled contours (default True)
        lines: Show contour lines (default False)
        levels: Number of levels or list of level values (optional)
        cmap: Colormap name (default 'viridis')
        labels: Show contour labels (default False)
        label_fontsize: Font size for labels (default 9)
        label_format: Format string for labels (default '%1.1f')
        cbar: Show color bar (default True)
        cbar_label: Label for color bar (optional)
        line_colors: Color for contour lines (default 'black')
        line_widths: Width of contour lines (default 1.0)
        line_styles: Style of contour lines (default 'solid')
        alpha: Transparency for filled contours (default 1.0)
        vmin: Minimum value for colormap (optional)
        vmax: Maximum value for colormap (optional)
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Examples:
        >>> # Basic filled contour
        >>> X, Y = np.meshgrid(x, y)
        >>> Z = np.sin(X) * np.cos(Y)
        >>> fig, ax = create_contour_plot(X, Y, Z, config)
        
        >>> # Line contours with labels
        >>> fig, ax = create_contour_plot(X, Y, Z, config,
        ...                               filled=False, lines=True, labels=True)
        
        >>> # Both filled and lines
        >>> fig, ax = create_contour_plot(X, Y, Z, config,
        ...                               filled=True, lines=True)
        
        >>> # Custom levels
        >>> levels = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
        >>> fig, ax = create_contour_plot(X, Y, Z, config, levels=levels)
    """
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Validate data
    if X.shape != Y.shape or X.shape != Z.shape:
        raise ValueError("X, Y, and Z must have the same shape")
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, facecolor=config.axes_facecolor)
    
    # Determine levels if not provided
    if levels is None:
        levels = 10  # Default number of levels
    
    # Create filled contours
    contour_set = None
    if filled:
        contour_set = ax.contourf(
            X, Y, Z,
            levels=levels,
            cmap=cmap,
            alpha=alpha,
            vmin=vmin,
            vmax=vmax
        )
    
    # Create line contours
    line_set = None
    if lines:
        line_set = ax.contour(
            X, Y, Z,
            levels=levels,
            colors=line_colors,
            linewidths=line_widths,
            linestyles=line_styles,
            vmin=vmin,
            vmax=vmax
        )
        
        # Add contour labels if requested
        if labels and line_set is not None:
            ax.clabel(line_set, inline=True, fontsize=label_fontsize, fmt=label_format)
    
    # Add color bar (for filled contours)
    if cbar and filled and contour_set is not None:
        cbar_obj = fig.colorbar(contour_set, ax=ax)
        if cbar_label:
            cbar_obj.set_label(cbar_label, fontsize=config.axis_label_size)
    
    # Apply global formatting
    _apply_global_formatting(ax, config)
    
    return fig, ax


def create_contour_from_function(
    func,
    x_range: Tuple[float, float],
    y_range: Tuple[float, float],
    config: Optional[PlotConfig] = None,
    resolution: int = 100,
    **kwargs
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Convenience function to create contour plot from a 2D function.
    
    Args:
        func: Function that takes (x, y) and returns z
        x_range: (x_min, x_max) tuple
        y_range: (y_min, y_max) tuple
        config: PlotConfig (optional)
        resolution: Number of points in each direction (default 100)
        **kwargs: Additional arguments passed to create_contour_plot
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Example:
        >>> def my_function(x, y):
        ...     return np.sin(x) * np.cos(y)
        >>> fig, ax = create_contour_from_function(
        ...     my_function, (-5, 5), (-5, 5), config
        ... )
    """
    # Create meshgrid
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    
    # Evaluate function
    Z = func(X, Y)
    
    # Create contour plot
    return create_contour_plot(X, Y, Z, config, **kwargs)


def _apply_global_formatting(ax: plt.Axes, config: PlotConfig) -> None:
    """
    Apply PlotConfig settings to axes.
    """
    # Labels
    if config.x_label:
        ax.set_xlabel(
            config.x_label,
            fontsize=config.x_axis_label_size or config.axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            fontstyle=config.axis_label_style,
            color=config.axis_label_color
        )
    
    if config.y_label:
        ax.set_ylabel(
            config.y_label,
            fontsize=config.y_axis_label_size or config.axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            fontstyle=config.axis_label_style,
            color=config.axis_label_color
        )
    
    # Title
    if config.title:
        title_kwargs = {
            'fontsize': config.title_size,
            'fontfamily': config.title_family,
            'fontweight': config.title_weight,
            'fontstyle': config.title_style,
            'color': config.title_color
        }
        if config.title_pad is not None:
            title_kwargs['pad'] = config.title_pad
        ax.set_title(config.title, **title_kwargs)
    
    # Tick labels
    x_tick_size = config.x_tick_label_size or config.tick_label_size
    y_tick_size = config.y_tick_label_size or config.tick_label_size
    
    ax.tick_params(axis='x', labelsize=x_tick_size)
    ax.tick_params(axis='y', labelsize=y_tick_size)
    
    for label in ax.get_xticklabels():
        label.set_fontfamily(config.tick_label_family)
        label.set_fontweight(config.tick_label_weight)
        label.set_color(config.tick_label_color)
    
    for label in ax.get_yticklabels():
        label.set_fontfamily(config.tick_label_family)
        label.set_fontweight(config.tick_label_weight)
        label.set_color(config.tick_label_color)
    
    # Grid
    if config.show_grid:
        ax.grid(
            True,
            alpha=config.grid_alpha,
            linestyle=config.grid_style,
            linewidth=config.grid_linewidth,
            color=config.grid_color
        )
        ax.set_axisbelow(True)
    
    # Spines
    if not config.show_top_spine:
        ax.spines['top'].set_visible(False)
    if not config.show_right_spine:
        ax.spines['right'].set_visible(False)
    if not config.show_left_spine:
        ax.spines['left'].set_visible(False)
    if not config.show_bottom_spine:
        ax.spines['bottom'].set_visible(False)
    
    # Equal aspect ratio (often desired for contour plots)
    # ax.set_aspect('equal')
    
    # Tight layout
    if config.tight_layout:
        plt.tight_layout()


def save_plot(fig: plt.Figure, filename: str, dpi: int = 300) -> None:
    """
    Save figure to file.
    
    Args:
        fig: Matplotlib figure
        filename: Output filename
        dpi: Resolution (default: 300)
    """
    fig.savefig(filename, dpi=dpi, bbox_inches='tight')
    plt.close(fig)
