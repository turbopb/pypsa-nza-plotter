"""
Bar Chart Examples - PlotLib v2.0

Demonstrates all bar chart types:
1. Single series (vertical bars)
2. Grouped bars (multiple series side-by-side)
3. Stacked bars (multiple series stacked)
4. Horizontal bars (orientation change)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plotlib import create_bar_plot, save_plot
from models import SeriesConfig, PlotConfig


# ============================================================================
# EXAMPLE 1: Single Series Bar Chart
# ============================================================================

def example_1_single_series():
    """
    Simple bar chart - quarterly sales data.
    """
    print("Example 1: Single series bar chart...")
    
    # Data
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [120, 145, 135, 160]
    
    # Create series
    series = SeriesConfig(
        x=categories,
        y=values,
        color='#0066CC',
        label='Sales (millions)'
    )
    
    # Config
    config = PlotConfig(
        title='Quarterly Sales - 2024',
        x_label='Quarter',
        y_label='Sales ($ millions)',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=False  # No legend needed for single series
    )
    
    # Create plot
    fig, ax = create_bar_plot(series, config)
    
    save_plot(fig, 'bar_example1_single.png', dpi=300)
    print("  ✓ Created bar_example1_single.png")


# ============================================================================
# EXAMPLE 2: Grouped Bars
# ============================================================================

def example_2_grouped_bars():
    """
    Grouped bar chart - comparing 2023 vs 2024 quarterly data.
    """
    print("\nExample 2: Grouped bars...")
    
    # Data
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values_2023 = [110, 125, 120, 140]
    values_2024 = [120, 145, 135, 160]
    
    # Create series
    series1 = SeriesConfig(
        x=categories,
        y=values_2023,
        color='#CC6666',
        label='2023'
    )
    
    series2 = SeriesConfig(
        x=categories,
        y=values_2024,
        color='#0066CC',
        label='2024'
    )
    
    # Config
    config = PlotConfig(
        title='Quarterly Sales Comparison: 2023 vs 2024',
        x_label='Quarter',
        y_label='Sales ($ millions)',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create grouped bar plot
    fig, ax = create_bar_plot([series1, series2], config, grouped=True)
    
    save_plot(fig, 'bar_example2_grouped.png', dpi=300)
    print("  ✓ Created bar_example2_grouped.png")


# ============================================================================
# EXAMPLE 3: Stacked Bars
# ============================================================================

def example_3_stacked_bars():
    """
    Stacked bar chart - generation by source.
    """
    print("\nExample 3: Stacked bars...")
    
    # Data - NZ generation by source (example data)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    hydro = [2800, 2600, 2700, 2900, 3000, 2800]
    gas = [800, 900, 850, 800, 750, 800]
    geothermal = [1200, 1200, 1200, 1200, 1200, 1200]
    wind = [600, 700, 650, 680, 720, 690]
    
    # Create series
    series_hydro = SeriesConfig(
        x=months,
        y=hydro,
        color='#0066CC',
        label='Hydro'
    )
    
    series_gas = SeriesConfig(
        x=months,
        y=gas,
        color='#CC6666',
        label='Gas'
    )
    
    series_geo = SeriesConfig(
        x=months,
        y=geothermal,
        color='#CC9900',
        label='Geothermal'
    )
    
    series_wind = SeriesConfig(
        x=months,
        y=wind,
        color='#00CC66',
        label='Wind'
    )
    
    # Config
    config = PlotConfig(
        title='NZ Generation Mix - First Half 2024',
        x_label='Month',
        y_label='Generation (GWh)',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=True,
        legend_location='upper left'
    )
    
    # Create stacked bar plot
    fig, ax = create_bar_plot(
        [series_hydro, series_gas, series_geo, series_wind],
        config,
        stacked=True
    )
    
    save_plot(fig, 'bar_example3_stacked.png', dpi=300)
    print("  ✓ Created bar_example3_stacked.png")


# ============================================================================
# EXAMPLE 4: Horizontal Bars
# ============================================================================

def example_4_horizontal_bars():
    """
    Horizontal bar chart - station capacity comparison.
    """
    print("\nExample 4: Horizontal bars...")
    
    # Data - NZ power stations by capacity (example data)
    stations = ['Manapouri', 'Huntly', 'Clyde', 'Benmore', 'Aviemore', 'Roxburgh']
    capacity_mw = [850, 1000, 432, 540, 220, 320]
    
    # Create series
    series = SeriesConfig(
        x=stations,
        y=capacity_mw,
        color='#0066CC',
        label='Installed Capacity'
    )
    
    # Config
    config = PlotConfig(
        title='NZ Power Station Capacity',
        x_label='Capacity (MW)',
        y_label='Station',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=False
    )
    
    # Create horizontal bar plot
    fig, ax = create_bar_plot(series, config, orientation='horizontal')
    
    save_plot(fig, 'bar_example4_horizontal.png', dpi=300)
    print("  ✓ Created bar_example4_horizontal.png")


# ============================================================================
# EXAMPLE 5: Grouped + Custom Styling
# ============================================================================

def example_5_custom_styling():
    """
    Grouped bars with custom colors and styling.
    """
    print("\nExample 5: Custom styled grouped bars...")
    
    # Data - Technology comparison
    technologies = ['Coal', 'Gas', 'Hydro', 'Wind', 'Solar', 'Geothermal']
    current = [25, 30, 120, 50, 20, 80]
    planned = [10, 25, 150, 80, 60, 100]
    
    # Create series with custom colors
    series_current = SeriesConfig(
        x=technologies,
        y=current,
        color='#666666',
        label='Current Capacity'
    )
    
    series_planned = SeriesConfig(
        x=technologies,
        y=planned,
        color='#00CC66',
        label='Planned by 2030'
    )
    
    # Custom config
    config = PlotConfig(
        title='Generation Capacity: Current vs Planned',
        x_label='Technology',
        y_label='Capacity (MW)',
        tick_label_size=10,
        axis_label_size=12,
        title_size=14,
        title_weight='normal',  # Not bold
        show_grid=True,
        grid_alpha=0.2,
        show_legend=True,
        legend_location='upper left',
        legend_font_weight='normal'
    )
    
    # Create plot
    fig, ax = create_bar_plot([series_current, series_planned], config, grouped=True)
    
    save_plot(fig, 'bar_example5_styled.png', dpi=300)
    print("  ✓ Created bar_example5_styled.png")


# ============================================================================
# EXAMPLE 6: Narrow Bars (Custom Width)
# ============================================================================

def example_6_narrow_bars():
    """
    Bar chart with custom bar width.
    """
    print("\nExample 6: Narrow bars...")
    
    # Data
    categories = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    values = [85, 92, 88, 90, 87, 75, 70]
    
    # Create series
    series = SeriesConfig(
        x=categories,
        y=values,
        color='#CC6666',
        label='Average Load (%)'
    )
    
    # Config
    config = PlotConfig(
        title='Weekly Load Profile',
        x_label='Day of Week',
        y_label='Average Load (%)',
        tick_label_size=11,
        axis_label_size=13,
        show_grid=True,
        grid_alpha=0.3,
        show_legend=False
    )
    
    # Create plot with narrow bars
    fig, ax = create_bar_plot(series, config, bar_width=0.5)
    
    save_plot(fig, 'bar_example6_narrow.png', dpi=300)
    print("  ✓ Created bar_example6_narrow.png")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("BAR CHART EXAMPLES - PLOTLIB V2.0")
    print("="*70)
    print("\nDemonstrating all bar chart types:")
    print("  1. Single series (vertical)")
    print("  2. Grouped bars (multiple series)")
    print("  3. Stacked bars (cumulative)")
    print("  4. Horizontal bars (flipped orientation)")
    print("  5. Custom styling")
    print("  6. Custom bar width")
    print("="*70)
    
    example_1_single_series()
    example_2_grouped_bars()
    example_3_stacked_bars()
    example_4_horizontal_bars()
    example_5_custom_styling()
    example_6_narrow_bars()
    
    print("\n" + "="*70)
    print("✓ All bar chart examples completed successfully!")
    print("="*70)
    print("\nCreated 6 example plots:")
    print("  • bar_example1_single.png - Single series")
    print("  • bar_example2_grouped.png - Grouped comparison")
    print("  • bar_example3_stacked.png - Stacked generation mix")
    print("  • bar_example4_horizontal.png - Horizontal capacity")
    print("  • bar_example5_styled.png - Custom styling")
    print("  • bar_example6_narrow.png - Narrow bars")
    print("="*70)
