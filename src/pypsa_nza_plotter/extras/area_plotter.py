"""
Area Plot Plotter - PlotLib v2.0

Creates area plots (filled line plots, stacked areas, fill-between).

DESIGN PHILOSOPHY:
------------------
- Uses same SeriesConfig/PlotConfig as other plotters
- Returns (fig, ax) for consistency
- One function handles all area plot types
- Comprehensive customization (hatching, lines, edges, colors)

USAGE:
------
Single area (fill under curve):
    series = SeriesConfig(x=x, y=y, color='#0066CC', label='Area')
    fig, ax = create_area_plot(series, config)

Stacked areas:
    series1 = SeriesConfig(x=x, y=y1, color='#0066CC', label='Layer 1')
    series2 = SeriesConfig(x=x, y=y2, color='#CC6666', label='Layer 2')
    fig, ax = create_area_plot([series1, series2], config, stacked=True)

Fill between two curves:
    series1 = SeriesConfig(x=x, y=y_upper, label='Upper')
    series2 = SeriesConfig(x=x, y=y_lower, label='Lower')
    fig, ax = create_area_plot([series1, series2], config, fill_between=True)
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


def create_area_plot(
    series: Union[SeriesConfig, List[SeriesConfig]],
    config: PlotConfig,
    stacked: bool = False,
    fill_between: bool = False,
    baseline: float = 0.0,
    alpha: float = 0.7,
    show_line: bool = True
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create area plot (filled line plot, stacked areas, or fill-between).
    
    Args:
        series: SeriesConfig or list of SeriesConfig objects
        config: PlotConfig for global settings
        stacked: If True, stack areas on top of each other
        fill_between: If True, fill between first and second series
        baseline: Y-value for baseline (default 0.0)
        alpha: Transparency for fill (0.0-1.0, default 0.7)
        show_line: If True, draw line on top of fill (default True)
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Examples:
        >>> # Single area under curve
        >>> series = SeriesConfig(x=x, y=y, color='#0066CC')
        >>> fig, ax = create_area_plot(series, config)
        
        >>> # Stacked areas
        >>> series1 = SeriesConfig(x=x, y=y1, color='#0066CC', label='Layer 1')
        >>> series2 = SeriesConfig(x=x, y=y2, color='#CC6666', label='Layer 2')
        >>> fig, ax = create_area_plot([series1, series2], config, stacked=True)
        
        >>> # Fill between two curves
        >>> series_upper = SeriesConfig(x=x, y=y_upper, label='Upper')
        >>> series_lower = SeriesConfig(x=x, y=y_lower, label='Lower')
        >>> fig, ax = create_area_plot([series_upper, series_lower], config, 
        ...                            fill_between=True)
        
        >>> # With hatching and custom lines
        >>> series = SeriesConfig(
        ...     x=x, y=y,
        ...     color='#0066CC',
        ...     hatch='///',
        ...     line_style='-',
        ...     line_width=2.0,
        ...     marker_edgecolor='black',
        ...     marker_edgewidth=0.5
        ... )
        >>> fig, ax = create_area_plot(series, config, alpha=0.6)
    """
    # Normalize to list
    if not isinstance(series, list):
        series = [series]
    
    # Validate
    if not series:
        raise ValueError("Must provide at least one series")
    
    if fill_between and len(series) != 2:
        raise ValueError("fill_between requires exactly 2 series")
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, facecolor=config.axes_facecolor)
    
    # Create area plots
    if fill_between:
        # Fill between two curves
        _create_fill_between(ax, series, alpha, show_line)
    elif stacked:
        # Stacked areas
        _create_stacked_areas(ax, series, alpha, show_line)
    else:
        # Single or overlapping areas
        _create_single_areas(ax, series, baseline, alpha, show_line)
    
    # Apply global formatting
    _apply_global_formatting(ax, config)
    
    return fig, ax


def _create_single_areas(ax, series, baseline, alpha, show_line):
    """Create single or overlapping area fills"""
    for s in series:
        # Get customization from SeriesConfig
        fill_color = s.color if s.color else '#0066CC'
        line_color = s.line_color if hasattr(s, 'line_color') and s.line_color else fill_color
        line_style = s.line_style if s.line_style else '-'
        line_width = s.line_width if s.line_width else 1.5
        edge_color = s.marker_edgecolor if s.marker_edgecolor else None
        edge_width = s.marker_edgewidth if s.marker_edgewidth else 0
        hatch = s.hatch if hasattr(s, 'hatch') and s.hatch else None
        label = s.label if s.label else None
        
        # Fill area
        fill = ax.fill_between(
            s.x, baseline, s.y,
            color=fill_color,
            alpha=alpha,
            edgecolor=edge_color,
            linewidth=edge_width,
            hatch=hatch,
            label=label if not show_line else None  # Label on line or fill, not both
        )
        
        # Draw line on top if requested
        if show_line and line_style != '':
            ax.plot(
                s.x, s.y,
                color=line_color,
                linestyle=line_style,
                linewidth=line_width,
                label=label if show_line else None
            )


def _create_stacked_areas(ax, series, alpha, show_line):
    """Create stacked area plot"""
    # Extract data
    x = series[0].x
    y_data = [s.y for s in series]
    colors = [s.color if s.color else None for s in series]
    labels = [s.label if s.label else None for s in series]
    
    # Get hatch patterns (if any)
    hatches = [s.hatch if hasattr(s, 'hatch') and s.hatch else None for s in series]
    
    # Create stacked plot
    polys = ax.stackplot(
        x, *y_data,
        colors=colors,
        labels=labels,
        alpha=alpha
    )
    
    # Apply hatch patterns to the polygon collections
    for i, (poly, hatch) in enumerate(zip(polys, hatches)):
        if hatch:
            poly.set_hatch(hatch)
        
        # Apply edge styling if specified
        s = series[i]
        if s.marker_edgecolor:
            poly.set_edgecolor(s.marker_edgecolor)
        if s.marker_edgewidth:
            poly.set_linewidth(s.marker_edgewidth)
    
    # Draw lines on top if requested
    if show_line:
        # Calculate cumulative sums for stacked areas
        cumsum = np.zeros_like(y_data[0])
        for i, s in enumerate(series):
            cumsum = cumsum + s.y
            
            line_color = s.line_color if hasattr(s, 'line_color') and s.line_color else s.color
            line_style = s.line_style if s.line_style else '-'
            line_width = s.line_width if s.line_width else 1.0
            
            if line_style != '':
                ax.plot(
                    s.x, cumsum,
                    color=line_color,
                    linestyle=line_style,
                    linewidth=line_width
                )


def _create_fill_between(ax, series, alpha, show_line):
    """Fill between two curves"""
    if len(series) != 2:
        raise ValueError("fill_between requires exactly 2 series")
    
    s1, s2 = series[0], series[1]
    
    # Use first series for styling
    fill_color = s1.color if s1.color else '#0066CC'
    edge_color = s1.marker_edgecolor if s1.marker_edgecolor else None
    edge_width = s1.marker_edgewidth if s1.marker_edgewidth else 0
    hatch = s1.hatch if hasattr(s1, 'hatch') and s1.hatch else None
    label = s1.label if s1.label else None
    
    # Fill between curves
    ax.fill_between(
        s1.x, s1.y, s2.y,
        color=fill_color,
        alpha=alpha,
        edgecolor=edge_color,
        linewidth=edge_width,
        hatch=hatch,
        label=label if not show_line else None
    )
    
    # Draw boundary lines if requested
    if show_line:
        for s in [s1, s2]:
            line_color = s.line_color if hasattr(s, 'line_color') and s.line_color else s.color
            line_style = s.line_style if s.line_style else '-'
            line_width = s.line_width if s.line_width else 1.5
            
            if line_style != '':
                ax.plot(
                    s.x, s.y,
                    color=line_color,
                    linestyle=line_style,
                    linewidth=line_width,
                    label=s.label
                )


def _apply_global_formatting(ax: plt.Axes, config: PlotConfig) -> None:
    """
    Apply PlotConfig settings to axes (same as other plotters).
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
        handles, labels = ax.get_legend_handles_labels()
        if handles and labels:
            legend = ax.legend(
                loc=config.legend_location,
                frameon=config.legend_frameon,
                framealpha=config.legend_framealpha,
                fontsize=config.legend_font_size
            )
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
