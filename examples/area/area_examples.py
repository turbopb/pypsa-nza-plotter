"""
Area Plot Examples - PlotLib v2.0

Demonstrates all area plot types with COMPREHENSIVE customization:
1. Single area - basic fill
2. Area with cross-hatching
3. Custom line formatting
4. Stacked areas with patterns
5. Fill between curves
6. Multiple customizations combined
7. Publication-ready examples
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from plotlib import create_area_plot, save_plot
from models import SeriesConfig, PlotConfig

import matplotlib.pyplot as plt

# ============================================================================
# EXAMPLE 1: Basic Area Plot
# ============================================================================

def example_1_basic_area():
    """
    Basic area plot - fill under curve.
    """
    print("Example 1: Basic area plot...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.exp(-x/10) + 2
    
    # Basic series
    series = SeriesConfig(
        x=x,
        y=y,
        color='#0066CC',
        label='Solar Generation'
    )
    
    # Config
    config = PlotConfig(
        title='Basic Area Plot',
        x_label='Hour',
        y_label='Generation (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create area plot
    fig, ax = create_area_plot(series, config, alpha=0.6)
    
    save_plot(fig, 'area_example1_basic.png', dpi=300)
    print("  ✓ Created area_example1_basic.png")


# ============================================================================
# EXAMPLE 2: Area with Cross-Hatching
# ============================================================================

def example_2_hatching():
    """
    Area plot with cross-hatch patterns.
    """
    print("\nExample 2: Area with cross-hatching...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y = 3 + 2 * np.sin(x)
    
    # Series with hatching
    series = SeriesConfig(
        x=x,
        y=y,
        color='#00CC66',
        hatch='///',               # Cross-hatch pattern!
        marker_edgecolor='black',  # Edge color
        marker_edgewidth=0.5,      # Edge width
        label='Wind Generation'
    )
    
    # Config
    config = PlotConfig(
        title='Area Plot with Cross-Hatching',
        x_label='Hour',
        y_label='Generation (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create area plot
    fig, ax = create_area_plot(series, config, alpha=0.7)
    
    save_plot(fig, 'area_example2_hatching.png', dpi=300)
    print("  ✓ Created area_example2_hatching.png")
    print("     - Hatch pattern: ///")
    print("     - Black edges")


# ============================================================================
# EXAMPLE 3: Custom Line Formatting
# ============================================================================

def example_3_line_formatting():
    """
    Area plot with custom line on top.
    """
    print("\nExample 3: Custom line formatting...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y = 5 + 3 * np.sin(x) * np.exp(-x/15)
    
    # Series with custom line
    series = SeriesConfig(
        x=x,
        y=y,
        color='#CC6666',
        line_style='-',      # Solid line
        line_width=3.0,      # Thick line!
        label='Hydro Generation'
    )
    
    # Config
    config = PlotConfig(
        title='Area Plot with Thick Line',
        x_label='Hour',
        y_label='Generation (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create area plot with line on top
    fig, ax = create_area_plot(series, config, alpha=0.4, show_line=True)
    
    save_plot(fig, 'area_example3_line.png', dpi=300)
    print("  ✓ Created area_example3_line.png")
    print("     - Line width: 3.0")
    print("     - Light fill (alpha=0.4)")


# ============================================================================
# EXAMPLE 4: Stacked Areas with Patterns
# ============================================================================

def example_4_stacked_patterns():
    """
    Stacked areas with different hatch patterns.
    """
    print("\nExample 4: Stacked areas with patterns...")
    
    # Generate data
    x = np.linspace(0, 24, 100)
    hydro = 2000 + 500 * np.sin(x * np.pi / 12)
    wind = 800 + 300 * np.sin(x * np.pi / 6)
    solar = np.maximum(0, 1000 * np.sin((x - 6) * np.pi / 12))
    
    # Series with different patterns
    series_hydro = SeriesConfig(
        x=x,
        y=hydro,
        color='#0066CC',
        hatch='',                  # Solid
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Hydro (solid)'
    )
    
    series_wind = SeriesConfig(
        x=x,
        y=wind,
        color='#00CC66',
        hatch='///',               # Diagonal
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Wind (///)'
    )
    
    series_solar = SeriesConfig(
        x=x,
        y=solar,
        color='#FFCC00',
        hatch='xxx',               # X pattern
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Solar (xxx)'
    )
    
    # Config
    config = PlotConfig(
        title='Stacked Generation Mix - Different Patterns',
        x_label='Hour of Day',
        y_label='Total Generation (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create stacked areas
    fig, ax = create_area_plot(
        [series_hydro, series_wind, series_solar],
        config,
        stacked=True,
        alpha=0.8,
        show_line=False
    )
    
    save_plot(fig, 'area_example4_stacked.png', dpi=300)
    print("  ✓ Created area_example4_stacked.png")
    print("     - Three layers with different patterns")


# ============================================================================
# EXAMPLE 5: Fill Between Curves
# ============================================================================

def example_5_fill_between():
    """
    Fill between upper and lower bounds.
    """
    print("\nExample 5: Fill between curves...")
    
    # Generate data - confidence interval
    x = np.linspace(0, 10, 100)
    y_mean = 100 + 20 * np.sin(x)
    y_upper = y_mean + 10
    y_lower = y_mean - 10
    
    # Upper and lower bounds
    series_upper = SeriesConfig(
        x=x,
        y=y_upper,
        color='#0066CC',
        hatch='///',
        line_style='-',
        line_width=1.5,
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Upper Bound'
    )
    
    series_lower = SeriesConfig(
        x=x,
        y=y_lower,
        color='#0066CC',
        line_style='-',
        line_width=1.5,
        label='Lower Bound'
    )
    
    # Config
    config = PlotConfig(
        title='Confidence Interval - Fill Between',
        x_label='Time',
        y_label='Power (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create fill-between plot
    fig, ax = create_area_plot(
        [series_upper, series_lower],
        config,
        fill_between=True,
        alpha=0.5,
        show_line=True
    )
    
    save_plot(fig, 'area_example5_fillbetween.png', dpi=300)
    print("  ✓ Created area_example5_fillbetween.png")
    print("     - Hatched confidence band")


# ============================================================================
# EXAMPLE 6: Multiple Overlapping Areas
# ============================================================================

def example_6_overlapping():
    """
    Multiple overlapping areas with different styles.
    """
    print("\nExample 6: Multiple overlapping areas...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(x)
    y2 = 3 + 1.5 * np.sin(x - 1)
    y3 = 2 + np.sin(x - 2)
    
    # Different styles
    series1 = SeriesConfig(
        x=x,
        y=y1,
        color='#0066CC',
        hatch='',
        line_style='-',
        line_width=2.0,
        label='Scenario A'
    )
    
    series2 = SeriesConfig(
        x=x,
        y=y2,
        color='#CC6666',
        hatch='///',
        line_style='--',
        line_width=2.0,
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Scenario B'
    )
    
    series3 = SeriesConfig(
        x=x,
        y=y3,
        color='#00CC66',
        hatch='|||',
        line_style=':',
        line_width=2.0,
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Scenario C'
    )
    
    # Config
    config = PlotConfig(
        title='Multiple Overlapping Areas - Different Styles',
        x_label='Time',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create overlapping areas
    fig, ax = create_area_plot(
        [series1, series2, series3],
        config,
        alpha=0.4,
        show_line=True
    )
    
    save_plot(fig, 'area_example6_overlapping.png', dpi=300)
    print("  ✓ Created area_example6_overlapping.png")
    print("     - Different hatch patterns")
    print("     - Different line styles")


# ============================================================================
# EXAMPLE 7: Publication-Ready Black & White
# ============================================================================

def example_7_publication():
    """
    Publication-ready black & white area plot.
    """
    print("\nExample 7: Publication-ready B&W...")
    
    # Generate data
    x = np.linspace(0, 24, 100)
    y1 = 2500 + 800 * np.sin(x * np.pi / 12)
    y2 = 1500 + 500 * np.sin(x * np.pi / 12 + np.pi/4)
    
    # Black & white with patterns
    series1 = SeriesConfig(
        x=x,
        y=y1,
        color='white',
        hatch='///',
        line_style='-',
        line_width=2.0,
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Peak Demand'
    )
    
    series2 = SeriesConfig(
        x=x,
        y=y2,
        color='white',
        hatch='|||',
        line_style='--',
        line_width=2.0,
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Base Load'
    )
    
    # Config
    config = PlotConfig(
        title='Daily Load Profile - Publication Style',
        x_label='Hour of Day',
        y_label='Load (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create overlapping areas
    fig, ax = create_area_plot(
        [series1, series2],
        config,
        alpha=0.9,
        show_line=True
    )
    
    save_plot(fig, 'area_example7_publication.png', dpi=300)
    print("  ✓ Created area_example7_publication.png")
    print("     - Black & white only")
    print("     - Thick edges and distinct patterns")


# ============================================================================
# EXAMPLE 8: No Lines (Fill Only)
# ============================================================================

def example_8_fill_only():
    """
    Area plot with fill only (no lines).
    """
    print("\nExample 8: Fill only (no lines)...")
    
    # Generate data
    x = np.linspace(0, 10, 100)
    y = 3 + 2 * np.sin(x) * np.exp(-x/10)
    
    # Series
    series = SeriesConfig(
        x=x,
        y=y,
        color='#9966CC',
        hatch='...',
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Geothermal'
    )
    
    # Config
    config = PlotConfig(
        title='Area Plot - Fill Only (No Line)',
        x_label='Time',
        y_label='Generation (MW)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create area plot without line
    fig, ax = create_area_plot(series, config, alpha=0.7, show_line=False)
    plt.show()
    
    save_plot(fig, 'area_example8_fillonly.png', dpi=300)
    print("  ✓ Created area_example8_fillonly.png")
    print("     - No line on top (show_line=False)")
    
    plt.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("AREA PLOT EXAMPLES - PLOTLIB V2.0")
    print("="*70)
    print("\nDemonstrating all area plot types with customization:")
    print("  1. Basic area plot")
    print("  2. Area with cross-hatching")
    print("  3. Custom line formatting")
    print("  4. Stacked areas with patterns")
    print("  5. Fill between curves")
    print("  6. Multiple overlapping areas")
    print("  7. Publication-ready B&W")
    print("  8. Fill only (no lines)")
    print("="*70)
    
    example_1_basic_area()
    example_2_hatching()
    example_3_line_formatting()
    example_4_stacked_patterns()
    example_5_fill_between()
    example_6_overlapping()
    example_7_publication()
    example_8_fill_only()
    
    print("\n" + "="*70)
    print("✓ All area plot examples completed successfully!")
    print("="*70)
    print("\nCreated 8 example plots:")
    print("  • area_example1_basic.png - Basic area")
    print("  • area_example2_hatching.png - Cross-hatching")
    print("  • area_example3_line.png - Custom line")
    print("  • area_example4_stacked.png - Stacked with patterns")
    print("  • area_example5_fillbetween.png - Fill between")
    print("  • area_example6_overlapping.png - Multiple overlapping")
    print("  • area_example7_publication.png - Publication B&W")
    print("  • area_example8_fillonly.png - Fill only")
    print("="*70)
    print("\nCUSTOMIZATION OPTIONS:")
    print("  Fill:")
    print("    • color='#0066CC'")
    print("    • hatch='///' (cross-hatch patterns)")
    print("    • alpha=0.7 (transparency)")
    print("    • marker_edgecolor='black' (edge color)")
    print("    • marker_edgewidth=0.5 (edge width)")
    print("  Lines:")
    print("    • show_line=True/False (line on/off)")
    print("    • line_style='-', '--', ':', '-.'")
    print("    • line_width=2.0")
    print("="*70)
