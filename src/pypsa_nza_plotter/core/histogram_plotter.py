"""
Histogram Plotter - PlotLib v2.0

Creates histograms (frequency distributions, single and overlapping).

DESIGN PHILOSOPHY:
------------------
- Uses same SeriesConfig/PlotConfig as other plotters
- Returns (fig, ax) for consistency
- One function handles all histogram types
- Simple, clear API

USAGE:
------
Single histogram:
    series = SeriesConfig(y=data, label='Distribution')
    fig, ax = create_histogram(series, config, bins=20)

Multiple overlapping:
    series1 = SeriesConfig(y=data1, label='Group A')
    series2 = SeriesConfig(y=data2, label='Group B')
    fig, ax = create_histogram([series1, series2], config, bins=20)

Stacked:
    fig, ax = create_histogram([series1, series2], config, bins=20, stacked=True)

Custom bin edges:
    fig, ax = create_histogram(series, config, bins=[0, 10, 20, 30, 40, 50])
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
from models.series_config import SeriesConfig


def create_histogram(
    series: Union[SeriesConfig, List[SeriesConfig]],
    config: PlotConfig,
    bins: Union[int, List[float]] = 10,
    density: bool = False,
    stacked: bool = False,
    cumulative: bool = False,
    orientation: str = 'vertical',
    bin_range: Optional[Tuple[float, float]] = None,
    alpha: float = 0.7
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create histogram (frequency distribution).
    
    Args:
        series: SeriesConfig or list of SeriesConfig objects
                Note: For histograms, use .y for the data values
        config: PlotConfig for global settings
        bins: Number of bins (int) or explicit bin edges (list)
        density: If True, normalize to probability density
        stacked: If True and multiple series, histograms are stacked
        cumulative: If True, compute cumulative histogram
        orientation: 'vertical' or 'horizontal'
        bin_range: (min, max) tuple to limit histogram range
        alpha: Transparency (0-1, default 0.7 for overlapping)
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Examples:
        >>> # Single histogram
        >>> series = SeriesConfig(y=np.random.randn(1000), label='Normal')
        >>> fig, ax = create_histogram(series, config, bins=30)
        
        >>> # Compare two distributions
        >>> series1 = SeriesConfig(y=data1, label='Group A', color='#0066CC')
        >>> series2 = SeriesConfig(y=data2, label='Group B', color='#CC6666')
        >>> fig, ax = create_histogram([series1, series2], config, bins=20)
        
        >>> # Stacked histogram
        >>> fig, ax = create_histogram([series1, series2], config, bins=20, stacked=True)
        
        >>> # Density (normalized)
        >>> fig, ax = create_histogram(series, config, bins=20, density=True)
    """
    # Normalize to list
    if not isinstance(series, list):
        series = [series]
    
    # Validate
    if not series:
        raise ValueError("Must provide at least one series")
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, facecolor=config.axes_facecolor)
    
    # Extract data from series
    data = [s.y for s in series]
    colors = [s.color if s.color else None for s in series]
    labels = [s.label if s.label else None for s in series]
    edgecolors = [s.marker_edgecolor if s.marker_edgecolor else 'black' for s in series]
    linewidths = [s.marker_edgewidth if s.marker_edgewidth else 0 for s in series]
    hatches = [s.hatch if hasattr(s, 'hatch') and s.hatch else None for s in series]
    
    # Create histogram
    if orientation == 'vertical':
        n, bins_out, patches = ax.hist(
            data,
            bins=bins,
            range=bin_range,
            density=density,
            cumulative=cumulative,
            histtype='bar' if not stacked else 'barstacked',
            color=colors,
            label=labels,
            alpha=alpha,
            edgecolor=edgecolors[0] if len(edgecolors) == 1 else 'black',
            linewidth=linewidths[0] if len(linewidths) == 1 else 0.5,
            stacked=stacked
        )
    else:  # horizontal
        n, bins_out, patches = ax.hist(
            data,
            bins=bins,
            range=bin_range,
            density=density,
            cumulative=cumulative,
            histtype='bar' if not stacked else 'barstacked',
            color=colors,
            label=labels,
            alpha=alpha,
            edgecolor=edgecolors[0] if len(edgecolors) == 1 else 'black',
            linewidth=linewidths[0] if len(linewidths) == 1 else 0.5,
            stacked=stacked,
            orientation='horizontal'
        )
    
    # Apply hatch patterns if specified
    # Note: matplotlib's hist doesn't support per-series hatching directly,
    # so we apply it to the patch collections after creation
    if hatches and any(hatches):
        if stacked or len(series) == 1:
            # For stacked or single histogram, patches is a list of BarContainer
            for i, (hatch, patch_container) in enumerate(zip(hatches, patches if isinstance(patches, list) else [patches])):
                if hatch:
                    for patch in patch_container:
                        patch.set_hatch(hatch)
        else:
            # For overlapping histograms
            for i, (hatch, patch_container) in enumerate(zip(hatches, patches)):
                if hatch:
                    for patch in patch_container:
                        patch.set_hatch(hatch)
    
    # Apply global formatting
    _apply_global_formatting(ax, config)
    
    return fig, ax


def _apply_global_formatting(ax: plt.Axes, config: PlotConfig) -> None:
    """
    Apply PlotConfig settings to axes (same as bar plotter).
    
    This keeps formatting consistent across all plot types.
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
    
    # Legend
    if config.show_legend:
        # Check if there are any labeled artists before creating legend
        handles, labels = ax.get_legend_handles_labels()
        if handles and labels:
            legend = ax.legend(
                loc=config.legend_location,
                frameon=config.legend_frameon,
                framealpha=config.legend_framealpha,
                fontsize=config.legend_font_size
            )
            # Apply legend font weight if available
            if hasattr(config, 'legend_font_weight'):
                for text in legend.get_texts():
                    text.set_fontweight(config.legend_font_weight)
    
    # Spines
    if not config.show_top_spine:
        ax.spines['top'].set_visible(False)
    if not config.show_right_spine:
        ax.spines['right'].set_visible(False)
    if not config.show_left_spine:
        ax.spines['left'].set_visible(False)
    if not config.show_bottom_spine:
        ax.spines['bottom'].set_visible(False)
    
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
