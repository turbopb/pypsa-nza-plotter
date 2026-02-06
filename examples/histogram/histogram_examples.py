"""
Histogram Examples - PlotLib v2.0

Demonstrates all histogram types:
1. Single histogram (basic distribution)
2. Overlapping histograms (compare distributions)
3. Stacked histograms (cumulative view)
4. Custom bins
5. Density vs count
6. Cumulative distribution
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from pypsa_nza_plotter import create_histogram, save_plot
from models import SeriesConfig, PlotConfig


# ============================================================================
# EXAMPLE 1: Single Histogram - Basic Distribution
# ============================================================================

def example_1_single_histogram():
    """
    Basic histogram of a normal distribution.
    """
    print("Example 1: Single histogram...")
    
    # Generate random normal data
    np.random.seed(42)
    data = np.random.randn(1000)
    
    # Create series (use .y for histogram data)
    series = SeriesConfig(
        y=data,
        color='#0066CC',
        label='Normal Distribution'
    )
    
    # Config
    config = PlotConfig(
        title='Single Histogram - Normal Distribution',
        x_label='Value',
        y_label='Frequency',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create histogram
    fig, ax = create_histogram(series, config, bins=30)
    
    save_plot(fig, 'hist_example1_single.png', dpi=300)
    print("  ✓ Created hist_example1_single.png")


# ============================================================================
# EXAMPLE 2: Overlapping Histograms - Compare Distributions
# ============================================================================

def example_2_overlapping():
    """
    Compare two different distributions.
    """
    print("\nExample 2: Overlapping histograms...")
    
    # Generate two different distributions
    np.random.seed(42)
    data1 = np.random.randn(1000) * 1.0 + 0.0  # Mean=0, std=1
    data2 = np.random.randn(1000) * 1.5 + 2.0  # Mean=2, std=1.5
    
    # Create series
    series1 = SeriesConfig(
        y=data1,
        color='#0066CC',
        label='Group A (μ=0, σ=1)'
    )
    
    series2 = SeriesConfig(
        y=data2,
        color='#CC6666',
        label='Group B (μ=2, σ=1.5)'
    )
    
    # Config
    config = PlotConfig(
        title='Overlapping Histograms - Compare Distributions',
        x_label='Value',
        y_label='Frequency',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create overlapping histograms (alpha=0.7 for transparency)
    fig, ax = create_histogram([series1, series2], config, bins=30, alpha=0.7)
    
    save_plot(fig, 'hist_example2_overlapping.png', dpi=300)
    print("  ✓ Created hist_example2_overlapping.png")


# ============================================================================
# EXAMPLE 3: Stacked Histogram
# ============================================================================

def example_3_stacked():
    """
    Stacked histogram showing cumulative distribution.
    """
    print("\nExample 3: Stacked histogram...")
    
    # Generate data - load distribution (example)
    np.random.seed(42)
    peak_load = np.random.gamma(5, 2, 800) * 100 + 2000  # Peak hours
    offpeak_load = np.random.gamma(3, 2, 600) * 80 + 1500  # Off-peak hours
    
    # Create series
    series_peak = SeriesConfig(
        y=peak_load,
        color='#CC6666',
        label='Peak Hours'
    )
    
    series_offpeak = SeriesConfig(
        y=offpeak_load,
        color='#0066CC',
        label='Off-Peak Hours'
    )
    
    # Config
    config = PlotConfig(
        title='Load Distribution - Stacked Histogram',
        x_label='Load (MW)',
        y_label='Frequency',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create stacked histogram
    fig, ax = create_histogram(
        [series_peak, series_offpeak],
        config,
        bins=25,
        stacked=True,
        alpha=0.9
    )
    
    save_plot(fig, 'hist_example3_stacked.png', dpi=300)
    print("  ✓ Created hist_example3_stacked.png")


# ============================================================================
# EXAMPLE 4: Custom Bins
# ============================================================================

def example_4_custom_bins():
    """
    Histogram with explicit bin edges.
    """
    print("\nExample 4: Custom bin edges...")
    
    # Generate data - wind speed distribution
    np.random.seed(42)
    wind_speed = np.abs(np.random.randn(1000) * 3 + 8)  # Mean ~8 m/s
    
    # Define custom bin edges (wind speed categories)
    bin_edges = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    # Create series
    series = SeriesConfig(
        y=wind_speed,
        color='#00CC66',
        label='Wind Speed Distribution'
    )
    
    # Config
    config = PlotConfig(
        title='Wind Speed Distribution - Custom Bins',
        x_label='Wind Speed (m/s)',
        y_label='Hours',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create histogram with custom bins
    fig, ax = create_histogram(series, config, bins=bin_edges, alpha=0.8)
    
    save_plot(fig, 'hist_example4_custom_bins.png', dpi=300)
    print("  ✓ Created hist_example4_custom_bins.png")


# ============================================================================
# EXAMPLE 5: Density (Normalized) Histogram
# ============================================================================

def example_5_density():
    """
    Normalized histogram (probability density).
    """
    print("\nExample 5: Density histogram...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.randn(1000) * 2 + 5
    
    # Create series
    series = SeriesConfig(
        y=data,
        color='#CC9900',
        label='Normalized Distribution'
    )
    
    # Config
    config = PlotConfig(
        title='Density Histogram (Normalized)',
        x_label='Value',
        y_label='Probability Density',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create density histogram (normalized)
    fig, ax = create_histogram(series, config, bins=30, density=True, alpha=0.8)
    
    save_plot(fig, 'hist_example5_density.png', dpi=300)
    print("  ✓ Created hist_example5_density.png")


# ============================================================================
# EXAMPLE 6: Cumulative Distribution
# ============================================================================

def example_6_cumulative():
    """
    Cumulative distribution function (CDF).
    """
    print("\nExample 6: Cumulative histogram...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.randn(1000) * 2 + 10
    
    # Create series
    series = SeriesConfig(
        y=data,
        color='#9966CC',
        label='Cumulative Distribution'
    )
    
    # Config
    config = PlotConfig(
        title='Cumulative Distribution Function (CDF)',
        x_label='Value',
        y_label='Cumulative Frequency',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create cumulative histogram
    fig, ax = create_histogram(series, config, bins=30, cumulative=True, alpha=0.8)
    
    save_plot(fig, 'hist_example6_cumulative.png', dpi=300)
    print("  ✓ Created hist_example6_cumulative.png")


# ============================================================================
# EXAMPLE 7: Generation Output Distribution (Realistic)
# ============================================================================

def example_7_realistic():
    """
    Realistic example: Power station output distribution.
    """
    print("\nExample 7: Realistic power generation example...")
    
    # Simulate power station output over a year (hourly data)
    np.random.seed(42)
    # Base load + some variation
    base_output = 250  # MW
    variation = np.random.randn(8760) * 30  # Some random variation
    maintenance = np.random.choice([0, 1], 8760, p=[0.95, 0.05])  # 5% maintenance
    
    output = np.maximum(0, (base_output + variation) * (1 - maintenance))
    
    # Create series
    series = SeriesConfig(
        y=output,
        color='#0066CC',
        marker_edgecolor='black',
        marker_edgewidth=0.5,
        label='Huntly Unit Output'
    )
    
    # Config
    config = PlotConfig(
        title='Huntly Power Station - Annual Output Distribution',
        x_label='Output (MW)',
        y_label='Hours per Year',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True
    )
    
    # Create histogram
    fig, ax = create_histogram(series, config, bins=40, alpha=0.85)
    
    save_plot(fig, 'hist_example7_realistic.png', dpi=300)
    print("  ✓ Created hist_example7_realistic.png")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("HISTOGRAM EXAMPLES - PLOTLIB V2.0")
    print("="*70)
    print("\nDemonstrating all histogram types:")
    print("  1. Single histogram (basic distribution)")
    print("  2. Overlapping histograms (compare distributions)")
    print("  3. Stacked histogram (cumulative view)")
    print("  4. Custom bin edges")
    print("  5. Density (normalized)")
    print("  6. Cumulative distribution (CDF)")
    print("  7. Realistic power generation example")
    print("="*70)
    
    example_1_single_histogram()
    example_2_overlapping()
    example_3_stacked()
    example_4_custom_bins()
    example_5_density()
    example_6_cumulative()
    example_7_realistic()
    
    print("\n" + "="*70)
    print("✓ All histogram examples completed successfully!")
    print("="*70)
    print("\nCreated 7 example plots:")
    print("  • hist_example1_single.png - Basic distribution")
    print("  • hist_example2_overlapping.png - Compare distributions")
    print("  • hist_example3_stacked.png - Stacked histogram")
    print("  • hist_example4_custom_bins.png - Custom bin edges")
    print("  • hist_example5_density.png - Normalized (density)")
    print("  • hist_example6_cumulative.png - CDF")
    print("  • hist_example7_realistic.png - Power generation")
    print("="*70)
