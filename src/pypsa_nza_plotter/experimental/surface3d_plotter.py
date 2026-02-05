"""
3D Surface Plot Plotter - PlotLib v2.9.0

Creates 3D surface plots for 3D function visualization with comprehensive customization.

DESIGN PHILOSOPHY:
------------------
- Uses same PlotConfig for global settings
- Supports surface plots, wireframe, contour3d
- Custom colormaps and viewing angles
- Returns (fig, ax) for consistency

USAGE:
------
Basic surface plot:
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig, ax = create_surface_plot(X, Y, Z, config)

Wireframe:
    fig, ax = create_surface_plot(X, Y, Z, config, plot_type='wireframe')

From function:
    fig, ax = create_surface_from_function(func, x_range, y_range, config)
"""

import matplotlib
##matplotlib.use('Agg')  # Commented for interactive  # Commented for interactive
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from typing import Tuple, Optional, List, Union
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.plot_config import PlotConfig


def create_surface_plot(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    config: Optional[PlotConfig] = None,
    plot_type: str = 'surface',
    cmap: str = 'viridis',
    alpha: float = 1.0,
    edgecolor: str = 'none',
    linewidth: float = 0.0,
    cbar: bool = True,
    cbar_label: Optional[str] = None,
    elev: float = 30,
    azim: float = -60,
    stride: int = 1,
    antialiased: bool = True,
    shade: bool = True,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create 3D surface plot for 3D function visualization.
    
    Args:
        X: 2D array of x-coordinates (from meshgrid)
        Y: 2D array of y-coordinates (from meshgrid)
        Z: 2D array of function values
        config: PlotConfig for global settings (optional)
        plot_type: 'surface', 'wireframe', or 'contour3d' (default 'surface')
        cmap: Colormap name (default 'viridis')
        alpha: Transparency (default 1.0)
        edgecolor: Color of edges (default 'none')
        linewidth: Width of edges (default 0.0)
        cbar: Show color bar (default True)
        cbar_label: Label for color bar (optional)
        elev: Elevation viewing angle in degrees (default 30)
        azim: Azimuth viewing angle in degrees (default -60)
        stride: Stride for surface sampling (default 1)
        antialiased: Use antialiasing (default True)
        shade: Use shading (default True)
        vmin: Minimum value for colormap (optional)
        vmax: Maximum value for colormap (optional)
    
    Returns:
        (fig, ax): Matplotlib figure and 3D axes
    
    Examples:
        >>> # Basic surface plot
        >>> X, Y = np.meshgrid(x, y)
        >>> Z = np.sin(np.sqrt(X**2 + Y**2))
        >>> fig, ax = create_surface_plot(X, Y, Z, config)
        
        >>> # Wireframe plot
        >>> fig, ax = create_surface_plot(X, Y, Z, config, 
        ...                               plot_type='wireframe')
        
        >>> # Custom viewing angle
        >>> fig, ax = create_surface_plot(X, Y, Z, config,
        ...                               elev=20, azim=-45)
    """
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Validate data
    if X.shape != Y.shape or X.shape != Z.shape:
        raise ValueError("X, Y, and Z must have the same shape")
    
    # Validate plot type
    valid_types = ['surface', 'wireframe', 'contour3d']
    if plot_type not in valid_types:
        raise ValueError(f"plot_type must be one of {valid_types}")
    
    # Create figure with 3D projection
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, projection='3d', facecolor=config.axes_facecolor)
    
    # Create plot based on type
    surf = None
    if plot_type == 'surface':
        surf = ax.plot_surface(
            X, Y, Z,
            cmap=cmap,
            alpha=alpha,
            edgecolor=edgecolor,
            linewidth=linewidth,
            rstride=stride,
            cstride=stride,
            antialiased=antialiased,
            shade=shade,
            vmin=vmin,
            vmax=vmax
        )
    elif plot_type == 'wireframe':
        surf = ax.plot_wireframe(
            X, Y, Z,
            rstride=stride,
            cstride=stride,
            linewidth=linewidth if linewidth > 0 else 1.0,
            alpha=alpha
        )
    elif plot_type == 'contour3d':
        surf = ax.contour3D(
            X, Y, Z,
            levels=20,
            cmap=cmap,
            linewidth=linewidth if linewidth > 0 else 1.0,
            alpha=alpha
        )
    
    # Set viewing angle
    ax.view_init(elev=elev, azim=azim)
    
    # Add color bar (for surface and contour3d)
    if cbar and surf is not None and plot_type in ['surface', 'contour3d']:
        cbar_obj = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        if cbar_label:
            cbar_obj.set_label(cbar_label, fontsize=config.axis_label_size)
    
    # Apply global formatting
    _apply_global_formatting(ax, config)
    
    return fig, ax


def create_surface_from_function(
    func,
    x_range: Tuple[float, float],
    y_range: Tuple[float, float],
    config: Optional[PlotConfig] = None,
    resolution: int = 50,
    **kwargs
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Convenience function to create 3D surface plot from a function.
    
    Args:
        func: Function that takes (x, y) and returns z
        x_range: (x_min, x_max) tuple
        y_range: (y_min, y_max) tuple
        config: PlotConfig (optional)
        resolution: Number of points in each direction (default 50)
        **kwargs: Additional arguments passed to create_surface_plot
    
    Returns:
        (fig, ax): Matplotlib figure and 3D axes
    
    Example:
        >>> def my_function(x, y):
        ...     return np.sin(np.sqrt(x**2 + y**2))
        >>> fig, ax = create_surface_from_function(
        ...     my_function, (-5, 5), (-5, 5), config
        ... )
    """
    # Create meshgrid
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    
    # Evaluate function
    Z = func(X, Y)
    
    # Create surface plot
    return create_surface_plot(X, Y, Z, config, **kwargs)


def _apply_global_formatting(ax: Axes3D, config: PlotConfig) -> None:
    """
    Apply PlotConfig settings to 3D axes.
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
    
    # Z label (3D specific)
    z_label = getattr(config, 'z_label', 'Z')
    if z_label:
        ax.set_zlabel(
            z_label,
            fontsize=config.axis_label_size,
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
    z_tick_size = config.tick_label_size
    
    ax.tick_params(axis='x', labelsize=x_tick_size)
    ax.tick_params(axis='y', labelsize=y_tick_size)
    ax.tick_params(axis='z', labelsize=z_tick_size)
    
    # Grid
    if config.show_grid:
        ax.grid(
            True,
            alpha=config.grid_alpha,
            linestyle=config.grid_style,
            linewidth=config.grid_linewidth,
            color=config.grid_color
        )
    
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
