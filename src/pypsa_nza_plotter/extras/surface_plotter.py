"""
3D Surface Plot Plotter - PlotLib v2.9.0

Creates 3D surface plots for visualizing 3D data and functions.

DESIGN PHILOSOPHY:
------------------
- Uses same PlotConfig for global settings
- Supports surface, wireframe, and combined plots
- Custom colormaps and viewing angles
- Contour projections
- Returns (fig, ax) for consistency

USAGE:
------
Basic surface plot:
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig, ax = create_surface_plot(X, Y, Z, config)

Wireframe:
    fig, ax = create_surface_plot(X, Y, Z, config, plot_type='wireframe')

With contour projections:
    fig, ax = create_surface_plot(X, Y, Z, config, contour_proj=True)
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
    alpha: float = 0.9,
    edgecolor: str = 'none',
    linewidth: float = 0,
    antialiased: bool = True,
    cbar: bool = True,
    cbar_label: Optional[str] = None,
    elev: float = 30,
    azim: float = -60,
    contour_proj: bool = False,
    contour_offset: Optional[float] = None,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    rstride: int = 1,
    cstride: int = 1
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create 3D surface plot.
    
    Args:
        X: 2D array of x-coordinates (from meshgrid)
        Y: 2D array of y-coordinates (from meshgrid)
        Z: 2D array of z-values
        config: PlotConfig for global settings (optional)
        plot_type: 'surface', 'wireframe', or 'both' (default 'surface')
        cmap: Colormap name (default 'viridis')
        alpha: Transparency (default 0.9)
        edgecolor: Edge color (default 'none')
        linewidth: Line width for edges (default 0)
        antialiased: Smooth shading (default True)
        cbar: Show color bar (default True)
        cbar_label: Label for color bar (optional)
        elev: Elevation viewing angle in degrees (default 30)
        azim: Azimuthal viewing angle in degrees (default -60)
        contour_proj: Project contours on bottom plane (default False)
        contour_offset: Z-offset for contour projection (optional)
        vmin: Minimum value for colormap (optional)
        vmax: Maximum value for colormap (optional)
        rstride: Row stride for surface (default 1)
        cstride: Column stride for surface (default 1)
    
    Returns:
        (fig, ax): Matplotlib figure and 3D axes
    
    Examples:
        >>> # Basic surface
        >>> X, Y = np.meshgrid(x, y)
        >>> Z = np.sin(np.sqrt(X**2 + Y**2))
        >>> fig, ax = create_surface_plot(X, Y, Z, config)
        
        >>> # Wireframe
        >>> fig, ax = create_surface_plot(X, Y, Z, config, plot_type='wireframe')
        
        >>> # With contour projections
        >>> fig, ax = create_surface_plot(X, Y, Z, config, contour_proj=True)
        
        >>> # Custom viewing angle
        >>> fig, ax = create_surface_plot(X, Y, Z, config, elev=45, azim=-30)
    """
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Validate data
    if X.shape != Y.shape or X.shape != Z.shape:
        raise ValueError("X, Y, and Z must have the same shape")
    
    # Validate plot type
    if plot_type not in ['surface', 'wireframe', 'both']:
        raise ValueError("plot_type must be 'surface', 'wireframe', or 'both'")
    
    # Create figure with 3D axes
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, projection='3d', facecolor=config.axes_facecolor)
    
    # Set viewing angle
    ax.view_init(elev=elev, azim=azim)
    
    # Create surface or wireframe
    surf = None
    if plot_type == 'surface' or plot_type == 'both':
        surf = ax.plot_surface(
            X, Y, Z,
            cmap=cmap,
            alpha=alpha,
            edgecolor=edgecolor,
            linewidth=linewidth,
            antialiased=antialiased,
            vmin=vmin,
            vmax=vmax,
            rstride=rstride,
            cstride=cstride
        )
    
    if plot_type == 'wireframe' or plot_type == 'both':
        wire_color = 'black' if plot_type == 'both' else None
        wire_alpha = 0.3 if plot_type == 'both' else 1.0
        ax.plot_wireframe(
            X, Y, Z,
            color=wire_color,
            alpha=wire_alpha,
            linewidth=0.5,
            rstride=rstride*2,
            cstride=cstride*2
        )
    
    # Add contour projections on bottom plane
    if contour_proj:
        if contour_offset is None:
            contour_offset = Z.min()
        ax.contour(X, Y, Z, zdir='z', offset=contour_offset, cmap=cmap, alpha=0.6)
    
    # Add color bar
    if cbar and surf is not None:
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


def _apply_global_formatting(ax: plt.Axes, config: PlotConfig) -> None:
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
            color=config.axis_label_color
        )
    
    if config.y_label:
        ax.set_ylabel(
            config.y_label,
            fontsize=config.y_axis_label_size or config.axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            color=config.axis_label_color
        )
    
    # Z-axis label (3D specific)
    ax.set_zlabel(
        'Z',
        fontsize=config.axis_label_size,
        fontfamily=config.axis_label_family,
        fontweight=config.axis_label_weight,
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
    ax.tick_params(axis='z', labelsize=config.tick_label_size)
    
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
