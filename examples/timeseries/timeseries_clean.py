"""
Time-Series Example - Final Clean Version

Demonstrates all time-series features with Phil's electricity data.
"""
import matplotlib
matplotlib.use('Qt5Agg')  # or 'Qt5Agg' if you have PyQt5
import matplotlib.pyplot as plt

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plotlib.timeseries import (
    load_timeseries_csv,
    select_columns,
    fill_under_curve,
    add_week_separators,
    add_boundary_lines
)
from plotlib import create_line_plot, save_plot
from models import PlotConfig
from models import SeriesConfig


# ============================================================================
# EXAMPLE 1: Simple Clean Plot
# ============================================================================

def example_1_simple_clean():
    """
    Simplest time-series plot with all the features we finalized.
    """
    print("Example 1: Simple clean plot...")
    
    # Load data
    df = load_timeseries_csv('202407_gen_agg_MWh.csv')
    x, y, _ = select_columns(df, 'HLY')
    
    # Create series
    series = SeriesConfig(
        x=x, y=y,
        line_style='-',
        line_width=1.5,
        color='#0066CC',
        label='Huntly'
    )
    
    # Create config
    config = PlotConfig(
        tick_label_size=12,
        axis_label_size=14,
        title='Huntly Generation - July 2024',
        x_label='Time Step (30-min intervals)',
        y_label='Generation (MWh)',
        show_grid=True,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot(series, config)
    
    # Add features
    fill_under_curve(ax, x, y, color='#0066CC', alpha=0.15)
    add_boundary_lines(ax, x, linewidth=0.75)
    add_week_separators(ax, df, linewidth=2.5, center_labels=True, include_first=True)
    plt.show()
    save_plot(fig, 'clean_example1.png', dpi=300)
    print("  ✓ Created clean_example1.png")


# ============================================================================
# EXAMPLE 2: Multiple Stations Comparison
# ============================================================================

def example_2_comparison():
    """
    Compare multiple stations on same plot.
    """
    print("\nExample 2: Multi-station comparison...")
    
    # Load data
    df = load_timeseries_csv('202407_gen_agg_MWh.csv')
    
    # Create series for three stations
    stations = ['HLY', 'MAN', 'TKA']
    colors = ['#0066CC', '#CC0000', '#00CC66']
    
    series_list = []
    for station, color in zip(stations, colors):
        x, y, _ = select_columns(df, station)
        series = SeriesConfig(
            x=x, y=y,
            line_style='-',
            line_width=1.5,
            color=color,
            label=station
        )
        series_list.append(series)
    
    # Config
    config = PlotConfig(
        tick_label_size=12,
        axis_label_size=14,
        title='Station Comparison: HLY vs MAN vs TKA',
        x_label='Time Step',
        y_label='Generation (MWh)',
        show_grid=True,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot(series_list, config)
    
    # Add features
    add_boundary_lines(ax, x, linewidth=0.75)
    add_week_separators(ax, df, linewidth=2.5, center_labels=True, include_first=True)
    plt.show()
    save_plot(fig, 'clean_example2.png', dpi=300)
    print("  ✓ Created clean_example2.png")


# ============================================================================
# EXAMPLE 3: Total Generation (All Columns)
# ============================================================================

def example_3_total():
    """
    Plot total generation (all columns summed).
    """
    print("\nExample 3: Total generation...")
    
    # Load data
    df = load_timeseries_csv('202407_gen_agg_MWh.csv')
    
    # Get all columns except DATE
    all_columns = [col for col in df.columns if col != 'DATE']
    x, y, _ = select_columns(df, all_columns)
    
    # Create series
    series = SeriesConfig(
        x=x, y=y,
        line_style='-',
        line_width=1.5,
        color='#0066CC',
        label=f'Total NZ Generation ({len(all_columns)} sources)'
    )
    
    # Config
    config = PlotConfig(
        tick_label_size=12,
        axis_label_size=14,
        title='Total NZ Generation - July 2024',
        x_label='Time Step',
        y_label='Total Generation (MWh)',
        show_grid=True,
        show_legend=True,
        legend_location='upper right'
    )
    
    # Create plot
    fig, ax = create_line_plot(series, config)
    
    # Add features
    fill_under_curve(ax, x, y, color='#0066CC', alpha=0.15)
    add_boundary_lines(ax, x, linewidth=0.75)
    add_week_separators(ax, df, linewidth=2.5, center_labels=True, include_first=True)
    plt.show()
    save_plot(fig, 'clean_example3.png', dpi=300)
    print("  ✓ Created clean_example3.png")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("TIME-SERIES EXAMPLES - CONSOLIDATED VERSION")
    print("="*70)
    print("\nThese examples demonstrate the final, clean time-series API:")
    print("  - Boundary lines at start/end (thin dashed)")
    print("  - Week separators (thick solid with centered labels)")
    print("  - Fill under curve")
    print("  - Multi-series support")
    print("="*70)
    
    example_1_simple_clean()
    example_2_comparison()
    example_3_total()
    
    print("\n" + "="*70)
    print("✓ All examples completed successfully!")
    print("="*70)
