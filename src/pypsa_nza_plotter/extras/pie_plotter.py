"""
Pie Chart Plotter - PlotLib v2.0

Creates pie charts and donut charts with comprehensive customization.

DESIGN PHILOSOPHY:
------------------
- Uses same PlotConfig for global settings
- Custom PieConfig for pie-specific settings
- Comprehensive customization (hatching, colors, edges, explosion)
- Returns (fig, ax) for consistency

USAGE:
------
Simple pie:
    labels = ['Hydro', 'Wind', 'Solar']
    values = [2500, 1200, 800]
    colors = ['#0066CC', '#00CC66', '#FFCC00']
    fig, ax = create_pie_chart(labels, values, colors, config)

Donut chart:
    fig, ax = create_pie_chart(labels, values, colors, config, donut=True)

Exploded slices:
    explode = [0.1, 0, 0]  # Pull out first slice
    fig, ax = create_pie_chart(labels, values, colors, config, explode=explode)

With hatching:
    hatches = ['///', '|||', 'xxx']
    fig, ax = create_pie_chart(labels, values, colors, config, hatches=hatches)
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


def create_pie_chart(
    labels: List[str],
    values: List[float],
    colors: Optional[List[str]] = None,
    config: Optional[PlotConfig] = None,
    explode: Optional[List[float]] = None,
    hatches: Optional[List[str]] = None,
    edge_colors: Optional[List[str]] = None,
    edge_width: float = 1.0,
    start_angle: float = 90,
    donut: bool = False,
    donut_width: float = 0.3,
    show_percentages: bool = True,
    show_labels: bool = True,
    label_distance: float = 1.1,
    autopct_format: str = '%1.1f%%',
    shadow: bool = False
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create pie chart or donut chart with comprehensive customization.
    
    Args:
        labels: List of slice labels
        values: List of slice values
        colors: List of colors (one per slice), optional
        config: PlotConfig for global settings (optional)
        explode: List of explosion distances (0-1), optional
        hatches: List of hatch patterns (one per slice), optional
        edge_colors: List of edge colors (one per slice), optional
        edge_width: Width of slice edges (default 1.0)
        start_angle: Starting angle in degrees (default 90)
        donut: If True, create donut chart (default False)
        donut_width: Width of donut ring (0-1, default 0.3)
        show_percentages: Show percentage labels (default True)
        show_labels: Show slice labels (default True)
        label_distance: Distance of labels from center (default 1.1)
        autopct_format: Format string for percentages (default '%1.1f%%')
        shadow: Add shadow effect (default False)
    
    Returns:
        (fig, ax): Matplotlib figure and axes
    
    Examples:
        >>> # Simple pie
        >>> labels = ['Hydro', 'Wind', 'Solar']
        >>> values = [2500, 1200, 800]
        >>> colors = ['#0066CC', '#00CC66', '#FFCC00']
        >>> fig, ax = create_pie_chart(labels, values, colors, config)
        
        >>> # Donut chart
        >>> fig, ax = create_pie_chart(labels, values, colors, config, donut=True)
        
        >>> # Exploded slice
        >>> explode = [0.1, 0, 0]  # Pull out first slice
        >>> fig, ax = create_pie_chart(labels, values, colors, config, explode=explode)
        
        >>> # With hatching (B&W publication)
        >>> hatches = ['///', '|||', 'xxx']
        >>> fig, ax = create_pie_chart(labels, values, ['white']*3, config, 
        ...                            hatches=hatches, edge_colors=['black']*3)
    """
    # Validate
    if len(labels) != len(values):
        raise ValueError("labels and values must have same length")
    
    # Create default config if not provided
    if config is None:
        config = PlotConfig()
    
    # Create figure
    fig = plt.figure(
        figsize=(config.figure_width, config.figure_height),
        dpi=config.dpi,
        facecolor=config.figure_facecolor
    )
    
    ax = fig.add_subplot(111, facecolor=config.axes_facecolor)
    
    # Create pie/donut chart
    # Note: ax.pie returns (wedges, texts, autotexts) if autopct is provided,
    # or (wedges, texts) if autopct is None
    pie_result = ax.pie(
        values,
        labels=labels if show_labels else None,
        colors=colors,
        autopct=autopct_format if show_percentages else None,
        startangle=start_angle,
        explode=explode,
        shadow=shadow,
        labeldistance=label_distance,
        wedgeprops={
            'linewidth': edge_width,
            'edgecolor': edge_colors[0] if edge_colors and len(edge_colors) == 1 else 'white'
        },
        textprops={
            'fontsize': config.tick_label_size,
            'fontfamily': config.tick_label_family,
            'fontweight': config.tick_label_weight,
            'color': config.tick_label_color
        }
    )
    
    # Unpack based on whether percentages are shown
    if show_percentages:
        wedges, texts, autotexts = pie_result
    else:
        wedges, texts = pie_result
        autotexts = None
    
    # Apply per-slice edge colors if specified
    if edge_colors and len(edge_colors) > 1:
        for wedge, edge_color in zip(wedges, edge_colors):
            wedge.set_edgecolor(edge_color)
    
    # Apply hatch patterns
    if hatches:
        for wedge, hatch in zip(wedges, hatches):
            if hatch:
                wedge.set_hatch(hatch)
    
    # Create donut if requested
    if donut:
        # Draw white circle in center
        centre_circle = plt.Circle(
            (0, 0),
            1 - donut_width,
            fc=config.axes_facecolor,
            linewidth=edge_width,
            edgecolor=edge_colors[0] if edge_colors else 'white'
        )
        ax.add_artist(centre_circle)
    
    # Format percentage text
    if show_percentages and autotexts:
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(config.tick_label_size)
    
    # Title
    if config.title:
        ax.set_title(
            config.title,
            fontsize=config.title_size,
            fontfamily=config.title_family,
            fontweight=config.title_weight,
            fontstyle=config.title_style,
            color=config.title_color,
            pad=config.title_pad if config.title_pad else 20
        )
    
    # Equal aspect ratio ensures circular pie
    ax.axis('equal')
    
    # Tight layout
    if config.tight_layout:
        plt.tight_layout()
    
    return fig, ax


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
