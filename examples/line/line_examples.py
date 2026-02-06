"""
Line Plot Examples - PlotLib v2.0

Demonstrates all line and scatter plot capabilities with COMPREHENSIVE examples:
1. Basic line plot
2. Multiple series
3. Line styles (solid, dashed, dotted, dash-dot)
4. Line widths (thin, medium, thick)
5. Scatter plot (markers only, no lines)
6. Line with markers (combined)
7. Custom colors and styling
8. Publication-ready scientific plot
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
import numpy as np
from pypsa_nza_plotter import create_line_plot, save_plot
from models import SeriesConfig, PlotConfig


# ============================================================================
# EXAMPLE 1: Basic Line Plot
# ============================================================================

def example_1_basic_line():
    """
    Basic line plot - single series.
    """
    print("Example 1: Basic line plot...")
    
    # Generate data - sine wave
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Series configuration
    series = SeriesConfig(
        x=x,
        y=y,
        line_style='-',      # Solid line
        line_width=2.0,
        color='#0066CC',
        label='sin(x)'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Basic Line Plot',
        x_label='x',
        y_label='y',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create line plot
    fig, ax = create_line_plot(series, config)
    plt.show()
    
    save_plot(fig, 'line_example1_basic.png', dpi=300)
    print("  ✓ Created line_example1_basic.png")


# ============================================================================
# EXAMPLE 2: Multiple Series
# ============================================================================

def example_2_multiple_series():
    """
    Multiple line series on same plot.
    """
    print("\nExample 2: Multiple series...")
    
    # Generate data - multiple functions
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    # Three series with different colors
    series1 = SeriesConfig(
        x=x, y=y1,
        line_style='-',
        line_width=2.0,
        color='#0066CC',
        label='sin(x)'
    )
    
    series2 = SeriesConfig(
        x=x, y=y2,
        line_style='-',
        line_width=2.0,
        color='#CC6666',
        label='cos(x)'
    )
    
    series3 = SeriesConfig(
        x=x, y=y3,
        line_style='-',
        line_width=2.0,
        color='#00CC66',
        label='sin(x)·cos(x)'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Multiple Series - Trigonometric Functions',
        x_label='x (radians)',
        y_label='y',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot with multiple series
    fig, ax = create_line_plot([series1, series2, series3], config)
    plt
    
    save_plot(fig, 'line_example2_multiple.png', dpi=300)
    print("  ✓ Created line_example2_multiple.png")
    print("     - Three trigonometric functions")


# ============================================================================
# EXAMPLE 3: Line Styles
# ============================================================================

def example_3_line_styles():
    """
    Different line styles (solid, dashed, dotted, dash-dot).
    """
    print("\nExample 3: Line styles...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y_base = np.exp(-x/5)
    
    # Different line styles
    series1 = SeriesConfig(
        x=x, y=y_base + 0.3,
        line_style='-',      # Solid
        line_width=2.0,
        color='#0066CC',
        label='Solid (-)'
    )
    
    series2 = SeriesConfig(
        x=x, y=y_base + 0.2,
        line_style='--',     # Dashed
        line_width=2.0,
        color='#CC6666',
        label='Dashed (--)'
    )
    
    series3 = SeriesConfig(
        x=x, y=y_base + 0.1,
        line_style=':',      # Dotted
        line_width=2.0,
        color='#00CC66',
        label='Dotted (:)'
    )
    
    series4 = SeriesConfig(
        x=x, y=y_base,
        line_style='-.',     # Dash-dot
        line_width=2.0,
        color='#FFCC00',
        label='Dash-dot (-.)'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Line Styles Comparison',
        x_label='Time (s)',
        y_label='Signal',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot([series1, series2, series3, series4], config)
    
    save_plot(fig, 'line_example3_styles.png', dpi=300)
    print("  ✓ Created line_example3_styles.png")
    print("     - Four line styles demonstrated")


# ============================================================================
# EXAMPLE 4: Line Widths
# ============================================================================

def example_4_line_widths():
    """
    Different line widths (thin, medium, thick, very thick).
    """
    print("\nExample 4: Line widths...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y_base = 2 + 0.5 * np.sin(x)
    
    # Different line widths
    series1 = SeriesConfig(
        x=x, y=y_base + 0.6,
        line_style='-',
        line_width=0.5,      # Very thin
        color='#0066CC',
        label='Width 0.5'
    )
    
    series2 = SeriesConfig(
        x=x, y=y_base + 0.4,
        line_style='-',
        line_width=1.0,      # Thin
        color='#CC6666',
        label='Width 1.0'
    )
    
    series3 = SeriesConfig(
        x=x, y=y_base + 0.2,
        line_style='-',
        line_width=2.0,      # Medium
        color='#00CC66',
        label='Width 2.0'
    )
    
    series4 = SeriesConfig(
        x=x, y=y_base,
        line_style='-',
        line_width=4.0,      # Thick
        color='#FFCC00',
        label='Width 4.0'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Line Width Comparison',
        x_label='x',
        y_label='y',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot([series1, series2, series3, series4], config)
    
    save_plot(fig, 'line_example4_widths.png', dpi=300)
    print("  ✓ Created line_example4_widths.png")
    print("     - Four line widths (0.5 to 4.0)")


# ============================================================================
# EXAMPLE 5: Scatter Plot (Markers Only)
# ============================================================================

def example_5_scatter():
    """
    Pure scatter plot - markers only, no connecting lines.
    """
    print("\nExample 5: Scatter plot (markers only)...")
    
    # Generate scattered data
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y = 2 * x + 1 + np.random.randn(50) * 2
    
    # Scatter configuration (no line)
    series = SeriesConfig(
        x=x,
        y=y,
        line_style='',       # No line!
        marker='o',          # Circle markers
        marker_size=6,
        color='#0066CC',
        label='Data Points'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Scatter Plot - Data Points Only',
        x_label='x',
        y_label='y',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create scatter plot
    fig, ax = create_line_plot(series, config)
    
    save_plot(fig, 'line_example5_scatter.png', dpi=300)
    print("  ✓ Created line_example5_scatter.png")
    print("     - Pure scatter (no lines)")


# ============================================================================
# EXAMPLE 6: Line with Markers
# ============================================================================

def example_6_line_with_markers():
    """
    Line plot with markers at data points.
    """
    print("\nExample 6: Line with markers...")
    
    # Generate data (less dense for visible markers)
    x = np.linspace(0, 10, 20)
    y1 = np.exp(-x/5) * np.cos(x)
    y2 = np.exp(-x/5) * np.sin(x)
    
    # Line with markers
    series1 = SeriesConfig(
        x=x, y=y1,
        line_style='-',
        line_width=2.0,
        marker='o',          # Circle markers
        marker_size=6,
        color='#0066CC',
        label='Damped Cosine'
    )
    
    series2 = SeriesConfig(
        x=x, y=y2,
        line_style='--',
        line_width=2.0,
        marker='s',          # Square markers
        marker_size=6,
        color='#CC6666',
        label='Damped Sine'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Line Plot with Markers',
        x_label='Time (s)',
        y_label='Amplitude',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot([series1, series2], config)
    
    save_plot(fig, 'line_example6_markers.png', dpi=300)
    print("  ✓ Created line_example6_markers.png")
    print("     - Lines with markers at data points")


# ============================================================================
# EXAMPLE 7: Custom Colors and Styling
# ============================================================================

def example_7_custom_styling():
    """
    Custom colors, thick lines, different styles.
    """
    print("\nExample 7: Custom styling...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y1 = 3 + 2 * np.sin(x)
    y2 = 3 + 2 * np.sin(x - np.pi/4)
    y3 = 3 + 2 * np.sin(x - np.pi/2)
    
    # Custom styled series
    series1 = SeriesConfig(
        x=x, y=y1,
        line_style='-',
        line_width=3.0,      # Thick
        color='#FF6B6B',     # Custom red
        label='Phase 0°'
    )
    
    series2 = SeriesConfig(
        x=x, y=y2,
        line_style='--',
        line_width=3.0,
        color='#4ECDC4',     # Custom teal
        label='Phase 45°'
    )
    
    series3 = SeriesConfig(
        x=x, y=y3,
        line_style=':',
        line_width=3.0,
        color='#FFE66D',     # Custom yellow
        label='Phase 90°'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Custom Styling - Phase Shifted Signals',
        x_label='Time',
        y_label='Signal',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot([series1, series2, series3], config)
    
    save_plot(fig, 'line_example7_custom.png', dpi=300)
    print("  ✓ Created line_example7_custom.png")
    print("     - Custom colors and thick lines")


# ============================================================================
# EXAMPLE 8: Publication-Ready Scientific Plot
# ============================================================================

def example_8_publication():
    """
    Publication-ready plot with proper formatting.
    """
    print("\nExample 8: Publication-ready...")
    
    # Generate realistic scientific data
    t = np.linspace(0, 24, 100)
    
    # Simulated power generation profiles
    solar = np.maximum(0, 1000 * np.sin((t - 6) * np.pi / 12))
    wind = 300 + 200 * np.sin(t * np.pi / 6)
    baseline = 500 * np.ones_like(t)
    
    # Series with publication styling
    series_solar = SeriesConfig(
        x=t, y=solar,
        line_style='-',
        line_width=2.0,
        color='#000000',     # Black for publication
        label='Solar'
    )
    
    series_wind = SeriesConfig(
        x=t, y=wind,
        line_style='--',
        line_width=2.0,
        color='#000000',
        label='Wind'
    )
    
    series_baseline = SeriesConfig(
        x=t, y=baseline,
        line_style=':',
        line_width=1.5,
        color='#666666',     # Gray
        label='Baseline'
    )
    
    # Publication configuration
    config = PlotConfig(
        title='Renewable Generation Profile',
        title_weight='normal',  # Not bold for publications
        x_label='Hour of Day',
        y_label='Power Generation (MW)',
        tick_label_size=11,
        axis_label_size=12,
        show_grid=True,
        grid_alpha=0.3,
        grid_style='--',
        show_legend=True,
        legend_location='upper right',
        show_top_spine=False,
        show_right_spine=False
    )
    
    # Create publication plot
    fig, ax = create_line_plot([series_solar, series_wind, series_baseline], config)
    
    save_plot(fig, 'line_example8_publication.png', dpi=300)
    print("  ✓ Created line_example8_publication.png")
    print("     - Publication-ready format")


# ============================================================================
# EXAMPLE 9: Different Marker Styles
# ============================================================================

def example_9_marker_styles():
    """
    Different marker styles for scatter/line plots.
    """
    print("\nExample 9: Marker styles...")
    
    # Generate data
    x = np.linspace(0, 10, 15)
    y_base = 2
    
    # Different marker styles
    markers = [
        ('o', 'Circle', 0.8),
        ('s', 'Square', 0.6),
        ('^', 'Triangle Up', 0.4),
        ('D', 'Diamond', 0.2),
        ('*', 'Star', 0.0)
    ]
    
    series_list = []
    colors = ['#0066CC', '#CC6666', '#00CC66', '#FFCC00', '#9966CC']
    
    for i, (marker, label, offset) in enumerate(markers):
        series = SeriesConfig(
            x=x,
            y=y_base + offset + 0.1 * np.sin(x),
            line_style='-',
            line_width=1.5,
            marker=marker,
            marker_size=8,
            color=colors[i],
            label=label
        )
        series_list.append(series)
    
    # Plot configuration
    config = PlotConfig(
        title='Marker Styles - Lines with Different Markers',
        x_label='x',
        y_label='y',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='right'
    )
    
    # Create plot
    fig, ax = create_line_plot(series_list, config)
    
    save_plot(fig, 'line_example9_markers.png', dpi=300)
    print("  ✓ Created line_example9_markers.png")
    print("     - Five different marker styles")


# ============================================================================
# EXAMPLE 10: Exponential Growth/Decay
# ============================================================================

def example_10_exponential():
    """
    Exponential growth and decay curves.
    """
    print("\nExample 10: Exponential curves...")
    
    # Generate data
    t = np.linspace(0, 5, 100)
    
    # Exponential functions
    growth = np.exp(t)
    decay = np.exp(-t)
    moderate = np.exp(0.5 * t)
    
    # Series
    series_growth = SeriesConfig(
        x=t, y=growth,
        line_style='-',
        line_width=2.0,
        color='#CC6666',
        label='Growth: e^t'
    )
    
    series_decay = SeriesConfig(
        x=t, y=decay,
        line_style='-',
        line_width=2.0,
        color='#0066CC',
        label='Decay: e^(-t)'
    )
    
    series_moderate = SeriesConfig(
        x=t, y=moderate,
        line_style='--',
        line_width=2.0,
        color='#00CC66',
        label='Moderate: e^(0.5t)'
    )
    
    # Plot configuration
    config = PlotConfig(
        title='Exponential Functions',
        x_label='Time (t)',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create plot
    fig, ax = create_line_plot([series_growth, series_moderate, series_decay], config)
    
    save_plot(fig, 'line_example10_exponential.png', dpi=300)
    print("  ✓ Created line_example10_exponential.png")
    print("     - Exponential growth and decay")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("LINE PLOT EXAMPLES - PLOTLIB V2.0")
    print("="*70)
    print("\nDemonstrating all line and scatter plot capabilities:")
    print("  1. Basic line plot")
    print("  2. Multiple series")
    print("  3. Line styles (solid, dashed, dotted, dash-dot)")
    print("  4. Line widths (0.5 to 4.0)")
    print("  5. Scatter plot (markers only)")
    print("  6. Line with markers")
    print("  7. Custom colors and styling")
    print("  8. Publication-ready scientific plot")
    print("  9. Different marker styles")
    print("  10. Exponential growth/decay")
    print("="*70)
    
    example_1_basic_line()
    example_2_multiple_series()
    example_3_line_styles()
    example_4_line_widths()
    example_5_scatter()
    example_6_line_with_markers()
    example_7_custom_styling()
    example_8_publication()
    example_9_marker_styles()
    example_10_exponential()
    
    print("\n" + "="*70)
    print("✓ All line plot examples completed successfully!")
    print("="*70)
    print("\nCreated 10 example plots:")
    print("  • line_example1_basic.png - Basic line")
    print("  • line_example2_multiple.png - Multiple series")
    print("  • line_example3_styles.png - Line styles")
    print("  • line_example4_widths.png - Line widths")
    print("  • line_example5_scatter.png - Pure scatter")
    print("  • line_example6_markers.png - Line with markers")
    print("  • line_example7_custom.png - Custom styling")
    print("  • line_example8_publication.png - Publication-ready")
    print("  • line_example9_markers.png - Marker styles")
    print("  • line_example10_exponential.png - Exponential curves")
    print("="*70)
    print("\nLINE PLOT FEATURES:")
    print("  Styling:")
    print("    • line_style: '-', '--', ':', '-.'")
    print("    • line_width: 0.5 to 4.0 (or any value)")
    print("    • color: Any color code")
    print("  Markers:")
    print("    • marker: 'o', 's', '^', 'D', '*', '+', 'x', etc.")
    print("    • marker_size: Any size")
    print("    • line_style='' for scatter only")
    print("  Multiple Series:")
    print("    • Pass list of SeriesConfig objects")
    print("    • Automatic legend generation")
    print("="*70)
