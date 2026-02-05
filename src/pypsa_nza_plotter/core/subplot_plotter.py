"""
Subplot/Faceting Module - PlotLib v2.7.0

Creates multi-panel figures with subplots for publication-ready layouts.

DESIGN PHILOSOPHY:
------------------
- Simple grid creation (rows × cols)
- Shared axes support
- Individual subplot titles
- Uniform styling across subplots
- Works with all plot types
- Returns figure and axes array

USAGE:
------
Simple 2×2 grid:
    fig, axes = create_subplots(2, 2, config)
    # axes[0,0], axes[0,1], axes[1,0], axes[1,1]

Shared x-axis (vertical stack):
    fig, axes = create_subplots(3, 1, config, sharex=True)

Mixed plot types:
    fig, axes = create_subplots(2, 2, config)
    # Create different plots in each subplot
    # using the existing plot functions
"""

import matplotlib
##matplotlib.use('Agg')  # Commented for interactive  # Commented for interactive
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
from typing import Tuple, Optional, List
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.plot_config import PlotConfig


def create_subplots(
    nrows: int = 1,
    ncols: int = 1,
    config: Optional[PlotConfig] = None,
    sharex: bool = False,
    sharey: bool = False,
    subplot_titles: Optional[List[str]] = None,
    figure_title: Optional[str] = None,
    width_ratios: Optional[List[float]] = None,
    height_ratios: Optional[List[float]] = None,
    hspace: Optional[float] = None,
    wspace: Optional[float] = None
) -> Tuple[plt.Figure, np.ndarray]:
    """
    Create a figure with multiple subplots in a grid layout.
    
    Args:
        nrows: Number of rows (default 1)
        ncols: Number of columns (default 1)
        config: PlotConfig for global settings (optional)
        sharex: Share x-axis across subplots (default False)
        sharey: Share y-axis across subplots (default False)
        subplot_titles: List of titles for each subplot (optional)
        figure_title: Overall figure title (optional)
        width_ratios: Relative widths of columns (optional)
        height_ratios: Relative heights of rows (optional)
        hspace: Height spacing between subplots (optional)
        wspace: Width spacing between subplots (optional)
    
    Returns:
        (fig, axes): Figure and axes array
            - For single subplot: axes is single Axes object
            - For 1D grid: axes is 1D array
            - For 2D grid: axes is 2D array
    
    Examples:
        >>> # Simple 2×2 grid
        >>> fig, axes = create_subplots(2, 2, config)
        >>> # axes[0,0], axes[0,1], axes[1,0], axes[1,1]
        
        >>> # Vertical stack with shared x-axis
        >>> fig, axes = create_subplots(3, 1, config, sharex=True)
        >>> # axes[0], axes[1], axes[2]
        
        >>> # Horizontal with titles
        >>> titles = ['Plot A', 'Plot B', 'Plot C']
        >>> fig, axes = create_subplots(1, 3, config, subplot_titles=titles)
        
        >>> # Custom spacing
        >>> fig, axes = create_subplots(2, 2, config, hspace=0.3, wspace=0.3)
    """
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Validate dimensions
    if nrows < 1 or ncols < 1:
        raise ValueError("nrows and ncols must be >= 1")
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    # Create subplots with gridspec
    if width_ratios or height_ratios:
        from matplotlib.gridspec import GridSpec
        gs = GridSpec(
            nrows, ncols,
            figure=fig,
            width_ratios=width_ratios,
            height_ratios=height_ratios,
            hspace=hspace,
            wspace=wspace
        )
        
        # Create axes manually
        axes = []
        for i in range(nrows):
            row = []
            for j in range(ncols):
                ax = fig.add_subplot(gs[i, j])
                ax.set_facecolor(config.axes_facecolor)
                row.append(ax)
            axes.append(row)
        axes = np.array(axes)
        
        # Handle axis sharing manually if needed
        if sharex:
            for i in range(1, nrows):
                for j in range(ncols):
                    axes[i, j].sharex(axes[0, j])
        if sharey:
            for i in range(nrows):
                for j in range(1, ncols):
                    axes[i, j].sharey(axes[i, 0])
    else:
        # Use standard subplots
        fig, axes = plt.subplots(
            nrows, ncols,
            sharex=sharex,
            sharey=sharey,
            figsize=(config.figure_width, config.figure_height),
            dpi=config.dpi,
            facecolor=config.figure_facecolor
        )
        
        # Set axes facecolor
        if nrows == 1 and ncols == 1:
            axes.set_facecolor(config.axes_facecolor)
        else:
            axes_flat = axes.flatten() if hasattr(axes, 'flatten') else [axes]
            for ax in axes_flat:
                ax.set_facecolor(config.axes_facecolor)
    
    # Apply subplot spacing
    if hspace is not None or wspace is not None:
        plt.subplots_adjust(hspace=hspace, wspace=wspace)
    
    # Add subplot titles
    if subplot_titles:
        axes_flat = axes.flatten() if hasattr(axes, 'flatten') else [axes]
        for i, (ax, title) in enumerate(zip(axes_flat, subplot_titles)):
            ax.set_title(
                title,
                fontsize=config.axis_label_size,
                fontweight=config.title_weight,
                fontfamily=config.title_family
            )
    
    # Add figure title
    if figure_title or config.title:
        title_text = figure_title or config.title
        fig.suptitle(
            title_text,
            fontsize=config.title_size,
            fontweight=config.title_weight,
            fontfamily=config.title_family,
            fontstyle=config.title_style,
            color=config.title_color
        )
    
    # Apply tight layout if requested
    if config.tight_layout:
        plt.tight_layout()
    
    return fig, axes


def apply_subplot_formatting(
    ax: plt.Axes,
    config: PlotConfig,
    hide_xlabel: bool = False,
    hide_ylabel: bool = False
) -> None:
    """
    Apply PlotConfig formatting to a single subplot axes.
    
    Useful for formatting individual subplots after creation.
    
    Args:
        ax: Matplotlib axes object
        config: PlotConfig with formatting settings
        hide_xlabel: Don't show x-axis label (for shared axes)
        hide_ylabel: Don't show y-axis label (for shared axes)
    
    Example:
        >>> fig, axes = create_subplots(2, 2)
        >>> apply_subplot_formatting(axes[0,0], config)
        >>> apply_subplot_formatting(axes[0,1], config, hide_ylabel=True)
    """
    # Labels
    if not hide_xlabel and config.x_label:
        ax.set_xlabel(
            config.x_label,
            fontsize=config.x_axis_label_size or config.axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            fontstyle=config.axis_label_style,
            color=config.axis_label_color
        )
    
    if not hide_ylabel and config.y_label:
        ax.set_ylabel(
            config.y_label,
            fontsize=config.y_axis_label_size or config.axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            fontstyle=config.axis_label_style,
            color=config.axis_label_color
        )
    
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
    
    # Legend
    if config.show_legend:
        ax.legend(
            loc=config.legend_location,
            fontsize=config.legend_fontsize,
            frameon=config.legend_frameon,
            framealpha=config.legend_framealpha,
            edgecolor=config.legend_edgecolor
        )


def add_subplot_labels(
    fig: plt.Figure,
    axes: np.ndarray,
    labels: Optional[List[str]] = None,
    loc: str = 'upper left',
    fontsize: int = 12,
    fontweight: str = 'bold',
    offset: Tuple[float, float] = (-0.1, 1.05)
) -> None:
    """
    Add labels (a, b, c, ...) to subplots for publication figures.
    
    Args:
        fig: Figure object
        axes: Axes array from create_subplots
        labels: Custom labels (default: a, b, c, ...)
        loc: Label location (default 'upper left')
        fontsize: Label font size (default 12)
        fontweight: Label font weight (default 'bold')
        offset: Position offset as (x, y) in axes coordinates
    
    Example:
        >>> fig, axes = create_subplots(2, 2)
        >>> add_subplot_labels(fig, axes)  # Adds (a), (b), (c), (d)
        >>> # Or custom labels:
        >>> add_subplot_labels(fig, axes, labels=['A', 'B', 'C', 'D'])
    """
    # Generate default labels if not provided
    if labels is None:
        axes_flat = axes.flatten() if hasattr(axes, 'flatten') else [axes]
        n_subplots = len(axes_flat)
        labels = [f'({chr(97 + i)})' for i in range(n_subplots)]  # (a), (b), (c), ...
    
    # Add labels to each subplot
    axes_flat = axes.flatten() if hasattr(axes, 'flatten') else [axes]
    for ax, label in zip(axes_flat, labels):
        ax.text(
            offset[0], offset[1],
            label,
            transform=ax.transAxes,
            fontsize=fontsize,
            fontweight=fontweight,
            va='top',
            ha='right'
        )


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
