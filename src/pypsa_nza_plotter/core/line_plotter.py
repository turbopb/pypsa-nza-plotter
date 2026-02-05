"""
Unified Line/Scatter Plotter

This is the CORE plotting function implementing the unified philosophy:
  - All plots are subplots (1x1 is just a special case)
  - Line and scatter are the same (just different styling)
  - Multi-series is fundamental (not an add-on)

DESIGN PHILOSOPHY:
------------------
In matplotlib, ax.plot() handles both lines and scatter plots.
The difference is only in styling:
  - ax.plot(x, y, '-')   → line plot
  - ax.plot(x, y, 'o')   → scatter plot  
  - ax.plot(x, y, '-o')  → both!

Therefore, we have ONE plotter that handles all line/scatter combinations.

SUBPLOT PHILOSOPHY:
-------------------
Every matplotlib plot is actually a subplot! Even a simple plot is
really a 1×1 grid of subplots. By treating everything as subplots
from the start, we get:
  - Consistent API
  - Easy to extend to multi-plot layouts
  - Natural support for shared axes
  - Follows matplotlib's actual design

USAGE PATTERN:
--------------
1. Create SeriesConfig objects for each data series
2. Create PlotConfig for global settings
3. Call create_line_plot() with list of series
4. Get back (fig, ax) or (fig, axes) depending on layout
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from typing import List, Union, Tuple, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.plot_config import PlotConfig
from models.series_config import SeriesConfig


def create_line_plot(
    series_list: Union[SeriesConfig, List[SeriesConfig]],
    config: PlotConfig,
    subplot_layout: Tuple[int, int] = (1, 1),
    sharex: bool = False,
    sharey: bool = False,
    subplot_titles: Optional[List[str]] = None
) -> Tuple[Figure, Union[plt.Axes, np.ndarray]]:
    """
    Create line/scatter plot(s) with full subplot support.
    
    This is the UNIFIED plotting function that handles:
    - Single series or multiple series
    - Line plots, scatter plots, or combined
    - Single plot (1×1) or multi-plot layouts (n×m)
    - All with consistent API
    
    Philosophy:
    -----------
    Everything is a subplot! A simple plot is just a 1×1 grid.
    This makes the API consistent and easy to extend.
    
    Args:
        series_list: Single SeriesConfig or list of SeriesConfig objects
                    For single plot: list of series to plot together
                    For subplots: list of lists, one per subplot
        config: PlotConfig with global settings (text sizes, grid, etc.)
        subplot_layout: (rows, cols) for subplot grid. Default (1, 1) = single plot
        sharex: Share x-axis across subplots
        sharey: Share y-axis across subplots  
        subplot_titles: Optional list of titles for each subplot
    
    Returns:
        (fig, ax) if subplot_layout is (1, 1)
        (fig, axes) if subplot_layout is (n, m) where n*m > 1
        
        axes is a numpy array of Axes objects
    
    Examples:
    ---------
    Simple single series:
        >>> series = SeriesConfig(x=x, y=y, color='#0066CC')
        >>> config = PlotConfig(tick_label_size=12)
        >>> fig, ax = create_line_plot(series, config)
    
    Multiple series on same plot:
        >>> series1 = SeriesConfig(x=x, y=y1, label='Data 1')
        >>> series2 = SeriesConfig(x=x, y=y2, label='Data 2')  
        >>> fig, ax = create_line_plot([series1, series2], config)
    
    2×2 subplot layout:
        >>> # Four separate plots
        >>> series_list = [series1, series2, series3, series4]
        >>> fig, axes = create_line_plot(series_list, config, 
        ...                              subplot_layout=(2, 2))
        >>> # axes is a 2×2 array of Axes objects
    
    2×2 with multiple series per subplot:
        >>> # Each subplot has multiple series
        >>> subplot1_series = [s1a, s1b]  # Two series on subplot 1
        >>> subplot2_series = [s2a, s2b]  # Two series on subplot 2
        >>> # etc...
        >>> series_list = [subplot1_series, subplot2_series, 
        ...               subplot3_series, subplot4_series]
        >>> fig, axes = create_line_plot(series_list, config,
        ...                              subplot_layout=(2, 2))
    """
    
    # ========== Input Handling ==========
    # Normalize input to list of lists
    # - Single series → [[series]]
    # - List of series → [[series1, series2, ...]]  (one subplot)
    # - List of lists → [[subplot1_series], [subplot2_series], ...]

    if not isinstance(series_list, list):
        # single series-like object
        series_list = [[series_list]]
    else:
        if len(series_list) == 0:
            raise ValueError("series_list cannot be empty")

        # If it's a flat list (not a list of lists), wrap it.
        if not isinstance(series_list[0], list):
            series_list = [series_list]
    
    # ========== Validate ==========
    rows, cols = subplot_layout
    n_subplots = rows * cols
    n_series_groups = len(series_list)
    
    if n_series_groups != n_subplots:
        raise ValueError(
            f"Number of series groups ({n_series_groups}) must match "
            f"number of subplots ({n_subplots} = {rows}×{cols})"
        )
    
    # ========== Create Figure and Subplots ==========
    fig, axes = plt.subplots(
        rows, cols,
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        sharex=sharex,
        sharey=sharey
    )
    
    # Normalize axes to always be array (even for single subplot)
    if rows == 1 and cols == 1:
        axes = np.array([axes])
        return_single_ax = True
    else:
        axes = np.array(axes).flatten()  # Flatten to 1D for easy iteration
        return_single_ax = False
    
    # Set figure background
    fig.patch.set_facecolor(config.figure_facecolor)
    
    # ========== Plot on Each Subplot ==========
    for idx, (ax, series_group) in enumerate(zip(axes, series_list)):
        # Set axes background
        ax.set_facecolor(config.axes_facecolor)
        
        # Plot each series in this subplot
        for series in series_group:
            _plot_series_on_axes(ax, series)
        
        # Apply global formatting to this subplot
        _apply_global_formatting(ax, config)
        
        # Apply subplot-specific title if provided
        if subplot_titles and idx < len(subplot_titles):
            title_kwargs = {
                'fontsize': config.title_size,
                'fontfamily': config.title_family,
                'fontweight': config.title_weight,
                'fontstyle': config.title_style,
                'color': config.title_color
            }
            if config.title_pad is not None:
                title_kwargs['pad'] = config.title_pad
            ax.set_title(subplot_titles[idx], **title_kwargs)
    
    # ========== Final Layout ==========
    if config.tight_layout:
        fig.tight_layout()
    
    if config.subplot_adjust:
        fig.subplots_adjust(**config.subplot_adjust)
    
    # ========== Return ==========
    if return_single_ax:
        return fig, axes[0]  # Return single ax for (1, 1) layout
    else:
        return fig, axes.reshape((rows, cols))  # Return array for multi-plot


def _plot_series_on_axes(ax: plt.Axes, series: SeriesConfig):
    """
    Plot a single series on the given axes.
    
    This is where the actual plotting happens. It's separated into
    its own function for clarity.
    
    This function implements the core insight:
    - Line and scatter are the same, just different styling
    - Use ax.plot() for both
    - Matplotlib handles the rest!
    """
    
    # Determine what to plot (line, marker, or both)
    has_line = series.line_style != ''
    has_marker = series.marker != ''
    
    if not has_line and not has_marker:
        raise ValueError(
            f"Series '{series.label}' has no line and no marker! "
            f"Must specify at least one."
        )
    
    # Prepare plot arguments
    plot_kwargs = {
        'color': series.color,
        'label': series.label if series.label else None,
        'alpha': series.line_alpha
    }
    
    # Line properties
    if has_line:
        plot_kwargs['linestyle'] = series.line_style
        plot_kwargs['linewidth'] = series.line_width
    else:
        plot_kwargs['linestyle'] = ''  # No line
    
    # Marker properties
    if has_marker:
        plot_kwargs['marker'] = series.marker
        plot_kwargs['markersize'] = series.marker_size
        plot_kwargs['markerfacecolor'] = series.marker_facecolor
        plot_kwargs['markeredgecolor'] = series.marker_edgecolor
        plot_kwargs['markeredgewidth'] = series.marker_edgewidth
    
    # THE ACTUAL PLOTTING!
    # This one call handles lines, scatter, and combined!
    
    # Set z-order if specified (controls draw order)
    if series.z_order is not None:
        plot_kwargs['zorder'] = series.z_order
    
    line = ax.plot(series.x, series.y, **plot_kwargs)
    
    # ========== Area Fill ==========
    # Fill between curve and bottom of plot (if enabled)
    if series.fill_below:
        fill_kwargs = {
            'color': series.fill_color,
            'alpha': series.fill_alpha,
        }
        
        # Add hatch pattern if specified
        if series.fill_hatch:
            fill_kwargs['hatch'] = series.fill_hatch
            fill_kwargs['edgecolor'] = series.hatch_color  # Use hatch_color for hatch lines
        
        # Set z-order for fill (slightly below line if z-order specified)
        if series.z_order is not None:
            fill_kwargs['zorder'] = series.z_order - 0.5
        
        # Fill between curve and zero
        ax.fill_between(series.x, series.y, 0, **fill_kwargs)


def _apply_global_formatting(ax: plt.Axes, config: PlotConfig):
    """
    Apply global formatting to axes.
    
    This includes everything from PlotConfig:
    - Text sizing
    - Grid
    - Legend
    - Axis scales and limits
    - Spines
    - Labels
    
    This is separated for clarity and reusability.
    """
    
    # ========== Labels ==========
    if config.x_label:
        ax.set_xlabel(
            config.x_label,
            fontsize=config.x_axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            fontstyle=config.axis_label_style,
            color=config.axis_label_color
        )
    
    if config.y_label:
        ax.set_ylabel(
            config.y_label,
            fontsize=config.y_axis_label_size,
            fontfamily=config.axis_label_family,
            fontweight=config.axis_label_weight,
            fontstyle=config.axis_label_style,
            color=config.axis_label_color
        )
    
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
    
    # ========== Text Sizing ==========
    # Tick label sizes
    ax.tick_params(axis='x', labelsize=config.x_tick_label_size)
    ax.tick_params(axis='y', labelsize=config.y_tick_label_size)
    
    # Tick label font properties
    for label in ax.get_xticklabels():
        label.set_fontfamily(config.tick_label_family)
        label.set_fontweight(config.tick_label_weight)
        label.set_color(config.tick_label_color)
    
    for label in ax.get_yticklabels():
        label.set_fontfamily(config.tick_label_family)
        label.set_fontweight(config.tick_label_weight)
        label.set_color(config.tick_label_color)
    
    # ========== Axes Configuration ==========
    # Scale
    ax.set_xscale(config.x_scale)
    ax.set_yscale(config.y_scale)
    
    # Limits
    if config.x_limits:
        ax.set_xlim(config.x_limits)
    if config.y_limits:
        ax.set_ylim(config.y_limits)
    
    # Custom ticks
    if config.x_ticks:
        ax.set_xticks(config.x_ticks)
    if config.y_ticks:
        ax.set_yticks(config.y_ticks)
    
    # Custom tick labels
    if config.x_tick_labels:
        ax.set_xticklabels(config.x_tick_labels)
    if config.y_tick_labels:
        ax.set_yticklabels(config.y_tick_labels)
    
    # Minor ticks
    if config.show_minor_ticks:
        ax.minorticks_on()
    
    # ========== Grid ==========
    if config.show_grid:
        ax.grid(
            True,
            which=config.grid_which,
            axis=config.grid_axis,
            alpha=config.grid_alpha,
            linestyle=config.grid_style,
            linewidth=config.grid_linewidth,
            color=config.grid_color
        )
    
    # ========== Legend ==========
    if config.show_legend:
        # Check if there are any labeled artists before creating legend
        handles, labels = ax.get_legend_handles_labels()
        if handles and labels:
            # Create proper font properties object (Windows-compatible!)
            font_props = FontProperties(
                family=config.legend_font_family,
                size=config.legend_font_size
            )
            
            ax.legend(
                loc=config.legend_location,
                frameon=config.legend_frameon,
                framealpha=config.legend_framealpha,
                shadow=config.legend_shadow,
                prop=font_props
            )
    
    # ========== Spines ==========
    ax.spines['top'].set_visible(config.show_top_spine)
    ax.spines['right'].set_visible(config.show_right_spine)
    ax.spines['bottom'].set_visible(config.show_bottom_spine)
    ax.spines['left'].set_visible(config.show_left_spine)


# ========== Convenience Functions ==========

def save_plot(
    fig: Figure,
    filepath: str,
    dpi: Optional[int] = None,
    transparent: bool = False,
    bbox_inches: str = 'tight',
    **kwargs
):
    """
    Save figure to file.
    
    Args:
        fig: matplotlib Figure object
        filepath: Output path (.png, .pdf, .svg, .eps)
        dpi: Resolution (default: from figure)
        transparent: Transparent background
        bbox_inches: Bounding box ('tight' removes whitespace)
        **kwargs: Additional arguments for fig.savefig()
    """
    fig.savefig(
        filepath,
        dpi=dpi or fig.dpi,
        transparent=transparent,
        bbox_inches=bbox_inches,
        **kwargs
    )
