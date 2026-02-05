"""
Bar Chart Customization Examples

Demonstrates:
1. Cross-hatching (hatch patterns)
2. Controlling bar width
3. Edge colors and widths
4. Combining customizations
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plotlib import create_bar_plot, save_plot
from models import SeriesConfig, PlotConfig


# ============================================================================
# EXAMPLE 1: Cross-Hatching (Hatch Patterns)
# ============================================================================

def example_1_hatch_patterns():
    """
    Demonstrate different hatch patterns for bars.
    """
    print("Example 1: Hatch patterns...")
    
    # Data
    categories = ['Pattern 1', 'Pattern 2', 'Pattern 3', 'Pattern 4', 'Pattern 5']
    values = [100, 120, 90, 110, 105]
    
    # Different hatch patterns
    # '/' = diagonal lines
    # '\\' = diagonal lines (other direction)  
    # '|' = vertical lines
    # '-' = horizontal lines
    # '+' = crossed lines
    # 'x' = X pattern
    # 'o' = small circles
    # 'O' = large circles
    # '.' = dots
    # '*' = stars
    
    patterns = ['/', '\\', '|', '-', '+']
    
    all_series = []
    for i, (cat, val, pattern) in enumerate(zip(categories, values, patterns)):
        series = SeriesConfig(
            x=[cat],
            y=[val],
            color='#0066CC',
            hatch=pattern,              # ← Hatch pattern!
            marker_edgecolor='black',   # Black edges
            marker_edgewidth=1.5,       # Thicker edges
            label=f'Pattern: {pattern}'
        )
        all_series.append(series)
    
    # Config
    config = PlotConfig(
        title='Bar Chart Hatch Patterns',
        x_label='Pattern Type',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=False
    )
    
    # Create plot - each bar is a separate series to show different patterns
    fig, ax = create_bar_plot(all_series, config)
    
    save_plot(fig, 'bar_custom_hatch.png', dpi=300)
    print("  ✓ Created bar_custom_hatch.png")


# ============================================================================
# EXAMPLE 2: Grouped Bars with Different Hatches
# ============================================================================

def example_2_grouped_with_hatch():
    """
    Grouped bars with different hatch patterns for each series.
    """
    print("\nExample 2: Grouped bars with hatching...")
    
    # Data
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    actual = [100, 120, 110, 130]
    target = [95, 115, 115, 125]
    
    # Series 1: Solid fill
    series_actual = SeriesConfig(
        x=categories,
        y=actual,
        color='#0066CC',
        hatch=None,                  # No hatch = solid
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Actual'
    )
    
    # Series 2: Cross-hatched
    series_target = SeriesConfig(
        x=categories,
        y=target,
        color='#CC6666',
        hatch='///',                 # ← Triple diagonal lines
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Target'
    )
    
    # Config
    config = PlotConfig(
        title='Actual vs Target (with Hatch Patterns)',
        x_label='Quarter',
        y_label='Sales ($ millions)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create grouped plot
    fig, ax = create_bar_plot([series_actual, series_target], config, grouped=True)
    
    save_plot(fig, 'bar_custom_grouped_hatch.png', dpi=300)
    print("  ✓ Created bar_custom_grouped_hatch.png")


# ============================================================================
# EXAMPLE 3: Controlling Bar Width
# ============================================================================

def example_3_bar_widths():
    """
    Demonstrate different bar widths.
    """
    print("\nExample 3: Different bar widths...")
    
    # Data
    categories = ['A', 'B', 'C', 'D']
    values = [100, 120, 90, 110]
    
    series = SeriesConfig(
        x=categories,
        y=values,
        color='#0066CC',
        marker_edgecolor='black',
        marker_edgewidth=1.0
    )
    
    config = PlotConfig(
        x_label='Category',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create 3 plots with different widths
    
    # Wide bars (0.95)
    config.title = 'Wide Bars (width=0.95)'
    fig, ax = create_bar_plot(series, config, bar_width=0.95)
    save_plot(fig, 'bar_custom_width_wide.png', dpi=300)
    print("  ✓ Created bar_custom_width_wide.png (width=0.95)")
    
    # Normal bars (0.8 - default)
    config.title = 'Normal Bars (width=0.8)'
    fig, ax = create_bar_plot(series, config, bar_width=0.8)
    save_plot(fig, 'bar_custom_width_normal.png', dpi=300)
    print("  ✓ Created bar_custom_width_normal.png (width=0.8)")
    
    # Narrow bars (0.4)
    config.title = 'Narrow Bars (width=0.4)'
    fig, ax = create_bar_plot(series, config, bar_width=0.4)
    save_plot(fig, 'bar_custom_width_narrow.png', dpi=300)
    print("  ✓ Created bar_custom_width_narrow.png (width=0.4)")


# ============================================================================
# EXAMPLE 4: Complex Pattern Example
# ============================================================================

def example_4_complex_patterns():
    """
    Show complex/combined hatch patterns.
    """
    print("\nExample 4: Complex hatch patterns...")
    
    # Data - generation sources
    sources = ['Hydro', 'Gas', 'Geothermal', 'Wind', 'Solar']
    capacity = [3200, 1500, 1000, 800, 400]
    
    # Different patterns for each source
    patterns = ['', '///', '|||', 'xxx', '...']
    colors = ['#0066CC', '#CC6666', '#CC9900', '#00CC66', '#FFCC00']
    
    all_series = []
    for source, cap, pattern, color in zip(sources, capacity, patterns, colors):
        series = SeriesConfig(
            x=[source],
            y=[cap],
            color=color,
            hatch=pattern,
            marker_edgecolor='black',
            marker_edgewidth=1.5,
            label=source
        )
        all_series.append(series)
    
    config = PlotConfig(
        title='NZ Generation Capacity by Source (with Hatch Patterns)',
        x_label='Source',
        y_label='Capacity (MW)',
        tick_label_size=10,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=False
    )
    
    fig, ax = create_bar_plot(all_series, config)
    
    save_plot(fig, 'bar_custom_complex.png', dpi=300)
    print("  ✓ Created bar_custom_complex.png")


# ============================================================================
# EXAMPLE 5: Stacked Bars with Hatching
# ============================================================================

def example_5_stacked_with_hatch():
    """
    Stacked bars with different hatch patterns.
    """
    print("\nExample 5: Stacked bars with hatching...")
    
    # Data
    months = ['Jan', 'Feb', 'Mar', 'Apr']
    hydro = [2800, 2600, 2700, 2900]
    gas = [800, 900, 850, 800]
    wind = [600, 700, 650, 680]
    
    # Different patterns for each source
    series_hydro = SeriesConfig(
        x=months,
        y=hydro,
        color='#0066CC',
        hatch='',                    # Solid
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Hydro (solid)'
    )
    
    series_gas = SeriesConfig(
        x=months,
        y=gas,
        color='#CC6666',
        hatch='///',                 # Diagonal
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Gas (///)'
    )
    
    series_wind = SeriesConfig(
        x=months,
        y=wind,
        color='#00CC66',
        hatch='xxx',                 # X pattern
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Wind (xxx)'
    )
    
    config = PlotConfig(
        title='Generation Mix with Hatch Patterns (Stacked)',
        x_label='Month',
        y_label='Generation (GWh)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    fig, ax = create_bar_plot(
        [series_hydro, series_gas, series_wind],
        config,
        stacked=True
    )
    
    save_plot(fig, 'bar_custom_stacked_hatch.png', dpi=300)
    print("  ✓ Created bar_custom_stacked_hatch.png")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("BAR CHART CUSTOMIZATION EXAMPLES")
    print("="*70)
    print("\nDemonstrating:")
    print("  • Hatch patterns (cross-hatching)")
    print("  • Bar width control")
    print("  • Edge colors and widths")
    print("  • Complex combinations")
    print("="*70)
    
    example_1_hatch_patterns()
    example_2_grouped_with_hatch()
    example_3_bar_widths()
    example_4_complex_patterns()
    example_5_stacked_with_hatch()
    
    print("\n" + "="*70)
    print("✓ All customization examples completed!")
    print("="*70)
    print("\nCreated 8 example plots:")
    print("  • bar_custom_hatch.png - Different hatch patterns")
    print("  • bar_custom_grouped_hatch.png - Grouped with hatching")
    print("  • bar_custom_width_wide.png - Wide bars (0.95)")
    print("  • bar_custom_width_normal.png - Normal bars (0.8)")
    print("  • bar_custom_width_narrow.png - Narrow bars (0.4)")
    print("  • bar_custom_complex.png - Complex patterns")
    print("  • bar_custom_stacked_hatch.png - Stacked with hatching")
    print("="*70)
    print("\nKEY PARAMETERS:")
    print("  SeriesConfig.hatch = '/', '\\\\', '|', '-', '+', 'x', 'o', etc.")
    print("  create_bar_plot(..., bar_width=0.4 to 0.95)")
    print("  SeriesConfig.marker_edgecolor = 'black'")
    print("  SeriesConfig.marker_edgewidth = 1.5")
    print("="*70)
