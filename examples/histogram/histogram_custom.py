"""
Histogram Customization Examples

Demonstrates customization options for histograms:
1. Single histogram with full customization
2. Multiple histograms with hatching
3. Edge colors and widths
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from plotlib import create_histogram, save_plot
from models import SeriesConfig, PlotConfig


# ============================================================================
# EXAMPLE 1: Single Histogram - Full Customization
# ============================================================================

def example_1_single_custom():
    """
    Single histogram with all customization options.
    """
    print("Example 1: Single histogram with full customization...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.randn(1000) * 2 + 10
    
    # Fully customized series
    series = SeriesConfig(
        y=data,
        color='#0066CC',           # Fill color
        hatch='///',               # Cross-hatch pattern
        marker_edgecolor='black',  # Edge color
        marker_edgewidth=1.5,      # Edge width
        label='Distribution'
    )
    
    # Config
    config = PlotConfig(
        title='Single Histogram - Full Customization',
        x_label='Value',
        y_label='Frequency',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create histogram
    fig, ax = create_histogram(series, config, bins=30, alpha=0.85)
    
    save_plot(fig, 'hist_custom1_single.png', dpi=300)
    print("  ✓ Created hist_custom1_single.png")
    print("     - Hatch pattern: ///")
    print("     - Black edges (1.5 width)")


# ============================================================================
# EXAMPLE 2: Multiple Histograms with Different Hatching
# ============================================================================

def example_2_multiple_hatching():
    """
    Multiple histograms with different hatch patterns.
    """
    print("\nExample 2: Multiple histograms with hatching...")
    
    # Generate data
    np.random.seed(42)
    data1 = np.random.randn(800) * 1.5 + 5
    data2 = np.random.randn(800) * 2.0 + 8
    
    # Series with different hatch patterns
    series1 = SeriesConfig(
        y=data1,
        color='#0066CC',
        hatch='///',               # Diagonal
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Group A (///)'
    )
    
    series2 = SeriesConfig(
        y=data2,
        color='#CC6666',
        hatch='|||',               # Vertical
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Group B (|||)'
    )
    
    # Config
    config = PlotConfig(
        title='Multiple Histograms with Different Hatch Patterns',
        x_label='Value',
        y_label='Frequency',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create overlapping histograms
    fig, ax = create_histogram([series1, series2], config, bins=25, alpha=0.7)
    
    save_plot(fig, 'hist_custom2_hatching.png', dpi=300)
    print("  ✓ Created hist_custom2_hatching.png")
    print("     - Different hatch per series")
    print("     - Overlapping with transparency")


# ============================================================================
# EXAMPLE 3: Black & White Publication Style
# ============================================================================

def example_3_bw_publication():
    """
    Black & white style for publication.
    """
    print("\nExample 3: Black & white publication style...")
    
    # Generate data
    np.random.seed(42)
    data1 = np.random.randn(1000) + 10
    data2 = np.random.randn(1000) * 1.2 + 12
    data3 = np.random.randn(1000) * 0.8 + 14
    
    # Different patterns for B&W distinction
    series1 = SeriesConfig(
        y=data1,
        color='white',            # White fill
        hatch='///',              # Diagonal
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Scenario A'
    )
    
    series2 = SeriesConfig(
        y=data2,
        color='white',            # White fill
        hatch='|||',              # Vertical
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Scenario B'
    )
    
    series3 = SeriesConfig(
        y=data3,
        color='white',            # White fill
        hatch='xxx',              # X pattern
        marker_edgecolor='black',
        marker_edgewidth=1.0,
        label='Scenario C'
    )
    
    # Config
    config = PlotConfig(
        title='Publication Style - Black & White',
        x_label='Value',
        y_label='Frequency',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create overlapping histograms
    fig, ax = create_histogram([series1, series2, series3], config, 
                               bins=20, alpha=0.9)
    
    save_plot(fig, 'hist_custom3_bw.png', dpi=300)
    print("  ✓ Created hist_custom3_bw.png")
    print("     - Black & white only")
    print("     - Different patterns for distinction")


# ============================================================================
# EXAMPLE 4: Colorful with Patterns (Accessible)
# ============================================================================

def example_4_colorful_accessible():
    """
    Color + pattern for accessibility.
    """
    print("\nExample 4: Colorful with patterns (accessible)...")
    
    # Generate data
    np.random.seed(42)
    peak = np.random.gamma(5, 2, 600) * 100 + 2000
    offpeak = np.random.gamma(3, 2, 800) * 80 + 1500
    
    # Color + pattern for redundancy
    series_peak = SeriesConfig(
        y=peak,
        color='#CC6666',          # Red
        hatch='///',              # Hatched
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Peak Hours'
    )
    
    series_offpeak = SeriesConfig(
        y=offpeak,
        color='#0066CC',          # Blue
        hatch='',                 # Solid (no hatch)
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Off-Peak Hours'
    )
    
    # Config
    config = PlotConfig(
        title='Load Distribution - Color + Pattern',
        x_label='Load (MW)',
        y_label='Hours',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create overlapping histograms
    fig, ax = create_histogram([series_peak, series_offpeak], config, 
                               bins=25, alpha=0.75)
    
    save_plot(fig, 'hist_custom4_accessible.png', dpi=300)
    print("  ✓ Created hist_custom4_accessible.png")
    print("     - Color AND pattern")
    print("     - Accessible to colorblind users")


# ============================================================================
# EXAMPLE 5: Dense Hatching Examples
# ============================================================================

def example_5_dense_hatching():
    """
    Show different hatch densities.
    """
    print("\nExample 5: Different hatch densities...")
    
    # Generate data
    np.random.seed(42)
    
    # Four distributions with different hatch densities
    patterns = ['/', '//', '///', '////']
    means = [10, 12, 14, 16]
    colors = ['#0066CC', '#00CC66', '#CC6666', '#CC9900']
    
    all_series = []
    for i, (pattern, mean, color) in enumerate(zip(patterns, means, colors)):
        data = np.random.randn(600) * 1.5 + mean
        series = SeriesConfig(
            y=data,
            color=color,
            hatch=pattern,
            marker_edgecolor='black',
            marker_edgewidth=0.8,
            label=f'{pattern} ({len(pattern)}x density)'
        )
        all_series.append(series)
    
    # Config
    config = PlotConfig(
        title='Hatch Pattern Density Examples',
        x_label='Value',
        y_label='Frequency',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create overlapping histograms
    fig, ax = create_histogram(all_series, config, bins=20, alpha=0.6)
    
    save_plot(fig, 'hist_custom5_density.png', dpi=300)
    print("  ✓ Created hist_custom5_density.png")
    print("     - /, //, ///, //// patterns")
    print("     - Increasing density")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("HISTOGRAM CUSTOMIZATION EXAMPLES")
    print("="*70)
    print("\nDemonstrating:")
    print("  • Hatch patterns")
    print("  • Edge colors and widths")
    print("  • Black & white publication style")
    print("  • Accessible color + pattern")
    print("="*70)
    
    example_1_single_custom()
    example_2_multiple_hatching()
    example_3_bw_publication()
    example_4_colorful_accessible()
    example_5_dense_hatching()
    
    print("\n" + "="*70)
    print("✓ All customization examples completed!")
    print("="*70)
    print("\nCreated 5 example plots:")
    print("  • hist_custom1_single.png - Full customization")
    print("  • hist_custom2_hatching.png - Different hatch patterns")
    print("  • hist_custom3_bw.png - Black & white publication")
    print("  • hist_custom4_accessible.png - Color + pattern")
    print("  • hist_custom5_density.png - Hatch density examples")
    print("="*70)
    print("\nSUPPORT SUMMARY:")
    print("  Single histogram:")
    print("    ✓ Fill color")
    print("    ✓ Hatch pattern")
    print("    ✓ Edge color")
    print("    ✓ Edge width")
    print("  Multiple histograms:")
    print("    ✓ Fill color (per-series)")
    print("    ✓ Hatch pattern (per-series)")
    print("    ⚠ Edge color (first series only)")
    print("    ⚠ Edge width (first series only)")
    print("="*70)
