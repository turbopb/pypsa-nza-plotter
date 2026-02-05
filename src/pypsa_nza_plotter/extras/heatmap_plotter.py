"""
Heatmap Plotter - PlotLib v2.6.0

Creates heatmaps for 2D data visualization with comprehensive customization.

DESIGN PHILOSOPHY:
------------------
- Uses same PlotConfig for global settings
- Heatmap-specific parameters for data visualization
- Comprehensive customization (colormaps, annotations, color bars)
- Returns (fig, ax) for consistency

USAGE:
------
Basic heatmap:
    data = np.random.randn(10, 10)
    fig, ax = create_heatmap(data, config)

With row/column labels:
    data = correlation_matrix
    labels = ['Feature 1', 'Feature 2', 'Feature 3']
    fig, ax = create_heatmap(data, config, row_labels=labels, col_labels=labels)

With annotations:
    fig, ax = create_heatmap(data, config, annot=True, fmt='.2f')

Custom colormap:
    fig, ax = create_heatmap(data, config, cmap='RdBu_r', center=0)
"""

import matplotlib
##matplotlib.use('Agg')  # Commented for interactive  # Commented for interactive
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
from typing import List, Union, Tuple, Optional
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.plot_config import PlotConfig


def create_heatmap(
    data: np.ndarray,
    config: Optional[PlotConfig] = None,
    row_labels: Optional[List[str]] = None,
    col_labels: Optional[List[str]] = None,
    cmap: str = 'viridis',
    annot: bool = False,
    fmt: str = '.2f',
    annot_size: int = 10,
    annot_color_threshold: Optional[float] = None,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    center: Optional[float] = None,
    cbar: bool = True,
    cbar_label: Optional[str] = None,
    square: bool = False,
    linewidths: float = 0,
    linecolor: str = 'white'
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create heatmap for 2D data visualization.
    
    Args:
        data: 2D numpy array
        config: PlotConfig for global settings (optional)
        row_labels: Labels for rows (optional)
        col_labels: Labels for columns (optional)
        cmap: Colormap name (default 'viridis')
        annot: Show data values in cells (default False)
        fmt: Format string for annotations (default '.2f')
        annot_size: Font size for annotations (default 10)
        annot_color_threshold: Value threshold for switching text color (optional)
        vmin: Minimum value for colormap (optional)
        vmax: Maximum value for colormap (optional)
        center: Center value for diverging colormap (optional)
        cbar: Show color bar (default True)
        cbar_label: Label for color bar (optional)
        square: Use square cells (default False)
        linewidths: Width of lines between cells (default 0)
        linecolor: Color of lines between cells (default 'white')
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Examples:
        >>> # Basic heatmap
        >>> data = np.random.randn(10, 10)
        >>> fig, ax = create_heatmap(data, config)
        
        >>> # Correlation matrix with annotations
        >>> corr_matrix = np.corrcoef(data.T)
        >>> labels = ['Var1', 'Var2', 'Var3']
        >>> fig, ax = create_heatmap(corr_matrix, config, 
        ...                          row_labels=labels, col_labels=labels,
        ...                          annot=True, cmap='RdBu_r', center=0)
        
        >>> # Custom colormap with grid
        >>> fig, ax = create_heatmap(data, config, cmap='coolwarm',
        ...                          linewidths=0.5, linecolor='black')
    """
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Validate data
    if not isinstance(data, np.ndarray) or data.ndim != 2:
        raise ValueError("data must be a 2D numpy array")
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, facecolor=config.axes_facecolor)
    
    # Handle diverging colormap with center
    if center is not None:
        # Calculate symmetric vmin/vmax around center
        vrange = max(abs(data.max() - center), abs(data.min() - center))
        if vmin is None:
            vmin = center - vrange
        if vmax is None:
            vmax = center + vrange
    
    # Create heatmap using imshow
    im = ax.imshow(
        data,
        cmap=cmap,
        aspect='auto' if not square else 'equal',
        vmin=vmin,
        vmax=vmax,
        interpolation='nearest'
    )
    
    # Add grid lines between cells
    if linewidths > 0:
        for i in range(data.shape[0] + 1):
            ax.axhline(i - 0.5, color=linecolor, linewidth=linewidths)
        for j in range(data.shape[1] + 1):
            ax.axvline(j - 0.5, color=linecolor, linewidth=linewidths)
    
    # Set tick positions and labels
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    
    if col_labels is not None:
        ax.set_xticklabels(col_labels)
    else:
        ax.set_xticklabels(np.arange(data.shape[1]))
    
    if row_labels is not None:
        ax.set_yticklabels(row_labels)
    else:
        ax.set_yticklabels(np.arange(data.shape[0]))
    
    # Rotate x-axis labels if they're long
    if col_labels and any(len(str(label)) > 3 for label in col_labels):
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
    
    # Add annotations if requested
    if annot:
        _add_annotations(ax, data, fmt, annot_size, annot_color_threshold, vmin, vmax)
    
    # Add color bar
    if cbar:
        cbar_obj = fig.colorbar(im, ax=ax)
        if cbar_label:
            cbar_obj.set_label(cbar_label, fontsize=config.axis_label_size)
    
    # Apply global formatting
    _apply_global_formatting(ax, config)
    
    return fig, ax


def _add_annotations(ax, data, fmt, annot_size, threshold, vmin, vmax):
    """Add text annotations to heatmap cells"""
    # Determine threshold for text color switching
    if threshold is None:
        if vmin is not None and vmax is not None:
            threshold = (vmax + vmin) / 2
        else:
            threshold = (data.max() + data.min()) / 2
    
    # Add text annotations
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            value = data[i, j]
            
            # Choose text color based on cell value
            if value > threshold:
                text_color = 'white'
            else:
                text_color = 'black'
            
            # Format value
            text = format(value, fmt)
            
            ax.text(j, i, text,
                   ha='center', va='center',
                   color=text_color,
                   fontsize=annot_size)


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
    
    # Move x-axis to top if desired (common for heatmaps)
    # ax.xaxis.tick_top()
    # ax.xaxis.set_label_position('top')
    
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


# Utility function for creating correlation matrices
def create_correlation_heatmap(
    data: np.ndarray,
    labels: Optional[List[str]] = None,
    config: Optional[PlotConfig] = None,
    **kwargs
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Convenience function for creating correlation matrix heatmaps.
    
    Args:
        data: 2D array where each column is a variable
        labels: Variable names (optional)
        config: PlotConfig (optional)
        **kwargs: Additional arguments passed to create_heatmap
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Example:
        >>> # Data with 5 variables
        >>> data = np.random.randn(100, 5)
        >>> labels = ['Var1', 'Var2', 'Var3', 'Var4', 'Var5']
        >>> fig, ax = create_correlation_heatmap(data, labels, config)
    """
    # Calculate correlation matrix
    corr_matrix = np.corrcoef(data.T)
    
    # Default settings for correlation matrices
    defaults = {
        'cmap': 'RdBu_r',
        'center': 0,
        'vmin': -1,
        'vmax': 1,
        'annot': True,
        'fmt': '.2f',
        'square': True,
        'cbar_label': 'Correlation'
    }
    
    # Override defaults with user kwargs
    for key, value in kwargs.items():
        defaults[key] = value
    
    # Create heatmap
    return create_heatmap(
        corr_matrix,
        config=config,
        row_labels=labels,
        col_labels=labels,
        **defaults
    )
