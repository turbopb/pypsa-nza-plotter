"""
Box Plot Plotter - PlotLib v2.5.0

Creates box plots for statistical data visualization with comprehensive customization.

DESIGN PHILOSOPHY:
------------------
- Uses same PlotConfig for global settings
- Box-specific parameters for statistical options
- Comprehensive customization (colors, widths, whiskers, outliers)
- Returns (fig, ax) for consistency

USAGE:
------
Single box plot:
    data = [np.random.randn(100)]
    labels = ['Sample']
    fig, ax = create_box_plot(data, labels, config)

Multiple box plots (comparison):
    data = [sample1, sample2, sample3]
    labels = ['Group A', 'Group B', 'Group C']
    fig, ax = create_box_plot(data, labels, config)

Grouped box plots:
    data = [[g1_s1, g1_s2], [g2_s1, g2_s2]]
    labels = [['A', 'B'], ['A', 'B']]
    group_labels = ['Group 1', 'Group 2']
    fig, ax = create_box_plot(data, labels, config, grouped=True, 
                              group_labels=group_labels)
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


def create_box_plot(
    data: Union[List[np.ndarray], List[List[np.ndarray]]],
    labels: Union[List[str], List[List[str]]],
    config: Optional[PlotConfig] = None,
    colors: Optional[List[str]] = None,
    orientation: str = 'vertical',
    show_means: bool = True,
    show_outliers: bool = True,
    notch: bool = False,
    box_width: float = 0.5,
    grouped: bool = False,
    group_labels: Optional[List[str]] = None,
    whisker_range: float = 1.5,
    patch_artist: bool = True
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create box plot(s) for statistical data visualization.
    
    Args:
        data: List of arrays (simple) or list of lists (grouped)
        labels: Box labels (simple) or nested labels (grouped)
        config: PlotConfig for global settings (optional)
        colors: List of colors for boxes (optional)
        orientation: 'vertical' or 'horizontal' (default 'vertical')
        show_means: Show mean markers (default True)
        show_outliers: Show outlier points (default True)
        notch: Use notched boxes (default False)
        box_width: Width of boxes 0-1 (default 0.5)
        grouped: Create grouped box plots (default False)
        group_labels: Labels for groups (for grouped plots)
        whisker_range: IQR multiplier for whiskers (default 1.5)
        patch_artist: Use filled boxes (default True)
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Examples:
        >>> # Single box plot
        >>> data = [np.random.randn(100)]
        >>> labels = ['Sample']
        >>> fig, ax = create_box_plot(data, labels, config)
        
        >>> # Multiple box plots
        >>> data = [sample1, sample2, sample3]
        >>> labels = ['Control', 'Treatment A', 'Treatment B']
        >>> fig, ax = create_box_plot(data, labels, config, 
        ...                           colors=['#0066CC', '#CC6666', '#00CC66'])
        
        >>> # Grouped box plots
        >>> data = [[control_male, control_female], 
        ...         [treat_male, treat_female]]
        >>> labels = [['Male', 'Female'], ['Male', 'Female']]
        >>> group_labels = ['Control', 'Treatment']
        >>> fig, ax = create_box_plot(data, labels, config, grouped=True,
        ...                           group_labels=group_labels)
        
        >>> # Horizontal orientation
        >>> fig, ax = create_box_plot(data, labels, config, 
        ...                           orientation='horizontal')
    """
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Validate orientation
    if orientation not in ['vertical', 'horizontal']:
        raise ValueError("orientation must be 'vertical' or 'horizontal'")
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, facecolor=config.axes_facecolor)
    
    # Create box plots based on type
    if grouped:
        _create_grouped_box_plot(
            ax, data, labels, colors, orientation, show_means,
            show_outliers, notch, box_width, group_labels, whisker_range,
            patch_artist
        )
    else:
        _create_simple_box_plot(
            ax, data, labels, colors, orientation, show_means,
            show_outliers, notch, box_width, whisker_range, patch_artist
        )
    
    # Apply global formatting
    _apply_global_formatting(ax, config, orientation)
    
    return fig, ax


def _create_simple_box_plot(
    ax, data, labels, colors, orientation, show_means, show_outliers,
    notch, box_width, whisker_range, patch_artist
):
    """Create simple (non-grouped) box plots"""
    # Create box plot
    vert = (orientation == 'vertical')
    
    bp = ax.boxplot(
        data,
        labels=labels,
        vert=vert,
        patch_artist=patch_artist,
        showmeans=show_means,
        showfliers=show_outliers,
        notch=notch,
        widths=box_width,
        whis=whisker_range
    )
    
    # Apply colors if provided
    if colors and patch_artist:
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
    
    # Style the plot elements
    _style_box_plot_elements(bp, colors)


def _create_grouped_box_plot(
    ax, data, labels, colors, orientation, show_means, show_outliers,
    notch, box_width, group_labels, whisker_range, patch_artist
):
    """Create grouped box plots"""
    if not isinstance(data[0], list):
        raise ValueError("For grouped plots, data must be list of lists")
    
    n_groups = len(data)
    n_boxes_per_group = len(data[0])
    
    # Default colors if not provided
    if colors is None:
        colors = [f'C{i}' for i in range(n_boxes_per_group)]
    
    # Calculate positions for grouped boxes
    group_gap = 1.0
    box_gap = 0.2
    positions = []
    
    for i in range(n_groups):
        group_start = i * (n_boxes_per_group * (box_width + box_gap) + group_gap)
        for j in range(n_boxes_per_group):
            pos = group_start + j * (box_width + box_gap)
            positions.append(pos)
    
    # Flatten data and track which group each box belongs to
    flat_data = []
    box_colors = []
    for group_data in data:
        flat_data.extend(group_data)
        box_colors.extend(colors)
    
    # Create box plot
    vert = (orientation == 'vertical')
    
    bp = ax.boxplot(
        flat_data,
        positions=positions,
        vert=vert,
        patch_artist=patch_artist,
        showmeans=show_means,
        showfliers=show_outliers,
        notch=notch,
        widths=box_width,
        whis=whisker_range
    )
    
    # Apply colors
    if patch_artist:
        for patch, color in zip(bp['boxes'], box_colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
    
    # Style elements
    _style_box_plot_elements(bp, box_colors)
    
    # Set x-axis labels for groups
    if group_labels:
        group_centers = []
        for i in range(n_groups):
            group_start = i * (n_boxes_per_group * (box_width + box_gap) + group_gap)
            group_center = group_start + (n_boxes_per_group - 1) * (box_width + box_gap) / 2
            group_centers.append(group_center)
        
        if vert:
            ax.set_xticks(group_centers)
            ax.set_xticklabels(group_labels)
        else:
            ax.set_yticks(group_centers)
            ax.set_yticklabels(group_labels)
    
    # Create legend for subgroups
    if labels and isinstance(labels[0], list):
        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor=color, alpha=0.7, label=labels[0][i])
                          for i, color in enumerate(colors)]
        ax.legend(handles=legend_elements, loc='best')


def _style_box_plot_elements(bp, colors):
    """Style box plot elements (whiskers, caps, medians, etc.)"""
    # Whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#333333', linewidth=1.5, linestyle='--')
    
    # Caps
    for cap in bp['caps']:
        cap.set(color='#333333', linewidth=1.5)
    
    # Medians
    for median in bp['medians']:
        median.set(color='#CC0000', linewidth=2.0)
    
    # Means (if shown)
    if 'means' in bp:
        for mean in bp['means']:
            mean.set(marker='D', markerfacecolor='green', 
                    markeredgecolor='green', markersize=6)
    
    # Fliers (outliers)
    if 'fliers' in bp:
        for flier in bp['fliers']:
            flier.set(marker='o', markerfacecolor='red', 
                     markeredgecolor='red', markersize=4, alpha=0.5)


def _apply_global_formatting(ax: plt.Axes, config: PlotConfig, orientation: str) -> None:
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
            color=config.grid_color,
            axis='y' if orientation == 'vertical' else 'x'  # Grid perpendicular to boxes
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
