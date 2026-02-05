"""
Configuration Example - Extended PlotConfig

Demonstrates the new comprehensive text formatting options added to PlotConfig.

NEW FEATURES:
- Title weight changed to 'normal' (was 'bold')
- Week labels positioned at bottom (0.1) instead of top (0.95)
- Full control over all text formatting
"""

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
from models import SeriesConfig, PlotConfig


# ============================================================================
# EXAMPLE 1: Using New PlotConfig Options
# ============================================================================

def example_1_extended_config():
    """
    Demonstrate extended PlotConfig with all new formatting options.
    """
    print("Example 1: Extended PlotConfig...")
    
    # Load data
    df = load_timeseries_csv('202407_gen_agg_MWh.csv')
    x, y, _ = select_columns(df, 'HLY')
    
    # Create series
    series = SeriesConfig(
        x=x, y=y,
        line_style='-',
        line_width=1.5,
        color='#0066CC',
        label='Huntly Generation'
    )
    
    # Create config with NEW EXTENDED OPTIONS
    config = PlotConfig(
        # Title - NOW WITH FULL CONTROL
        title='Huntly Generation - Extended Formatting Demo',
        title_size=14,
        title_weight='normal',      # ✨ NEW: Changed from 'bold' (user request)
        title_style='normal',       # ✨ NEW: 'normal', 'italic', 'oblique'
        title_color='#000000',      # ✨ NEW: Custom color
        title_pad=10,               # ✨ NEW: Padding above plot
        
        # Axis labels - EXTENDED
        x_label='Time Step (30-min intervals)',
        y_label='Generation (MWh)',
        axis_label_size=12,
        axis_label_weight='normal',
        axis_label_color='#000000',  # ✨ NEW
        axis_label_style='normal',   # ✨ NEW
        
        # Tick labels - EXTENDED
        tick_label_size=10,
        tick_label_weight='normal',
        tick_label_color='#000000',  # ✨ NEW
        
        # Legend - EXTENDED
        show_legend=True,
        legend_location='upper right',
        legend_font_size=10,
        legend_font_weight='normal',  # ✨ NEW
        
        # Grid
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create plot
    fig, ax = create_line_plot(series, config)
    
    # Add features with NEW POSITIONING OPTIONS
    fill_under_curve(ax, x, y, color='#0066CC', alpha=0.15)
    add_boundary_lines(ax, x, linewidth=0.75)
    
    # Week separators with NEW LABEL POSITIONING
    add_week_separators(
        ax, df,
        linewidth=2.5,
        center_labels=True,
        include_first=True,
        label_y_position=0.1,      # ✨ NEW: Bottom instead of top (user request)
        label_fontsize=8,          # ✨ NEW: Configurable size
        label_color='#666666',     # ✨ NEW: Configurable color
        label_weight='normal'      # ✨ NEW: Configurable weight
    )
    
    save_plot(fig, 'config_extended_example1.png', dpi=300)
    print("  ✓ Created config_extended_example1.png")
    print("  ✓ Title: Normal weight (not bold)")
    print("  ✓ Week labels: Bottom of plot (y=0.1)")


# ============================================================================
# EXAMPLE 2: Custom Styling Demo
# ============================================================================

def example_2_custom_styling():
    """
    Demonstrate custom styling with different color scheme.
    """
    print("\nExample 2: Custom styling...")
    
    # Load data
    df = load_timeseries_csv('202407_gen_agg_MWh.csv')
    x, y, _ = select_columns(df, 'MAN')
    
    # Create series
    series = SeriesConfig(
        x=x, y=y,
        line_style='-',
        line_width=1.5,
        color='#CC0000',
        label='Manapouri'
    )
    
    # Custom styled config
    config = PlotConfig(
        title='Custom Styled Plot - Manapouri Generation',
        title_size=16,
        title_weight='bold',        # Can still use bold if desired!
        title_style='italic',       # Italic title
        title_color='#CC0000',      # Red to match line color
        
        x_label='Time Step',
        y_label='Generation (MWh)',
        axis_label_color='#333333',  # Dark gray labels
        axis_label_weight='bold',
        
        tick_label_color='#666666',  # Medium gray ticks
        
        show_legend=True,
        legend_location='upper right',
        legend_font_weight='bold',
        
        show_grid=True,
        grid_alpha=0.2
    )
    
    # Create plot
    fig, ax = create_line_plot(series, config)
    
    # Add features
    fill_under_curve(ax, x, y, color='#CC0000', alpha=0.15)
    add_boundary_lines(ax, x, linewidth=0.75, color='#CC0000')
    
    # Custom styled week separators
    add_week_separators(
        ax, df,
        color='#CC0000',           # Red separators
        linewidth=2.0,
        center_labels=True,
        include_first=True,
        label_y_position=0.1,
        label_fontsize=9,
        label_color='#CC0000',     # Red labels
        label_weight='bold'        # Bold labels
    )
    
    save_plot(fig, 'config_extended_example2.png', dpi=300)
    print("  ✓ Created config_extended_example2.png")
    print("  ✓ Custom colors throughout")
    print("  ✓ Bold, italic title")
    print("  ✓ Red week separators and labels")


# ============================================================================
# EXAMPLE 3: Professional Publication Style
# ============================================================================

def example_3_publication_style():
    """
    Clean, professional style suitable for publication.
    """
    print("\nExample 3: Publication style...")
    
    # Load data
    df = load_timeseries_csv('202407_gen_agg_MWh.csv')
    
    # Get all generation columns
    all_columns = [col for col in df.columns if col != 'DATE']
    x, y, _ = select_columns(df, all_columns)
    
    # Create series
    series = SeriesConfig(
        x=x, y=y,
        line_style='-',
        line_width=1.0,
        color='#000000',           # Black for publication
        label='Total NZ Generation'
    )
    
    # Professional config
    config = PlotConfig(
        title='New Zealand Total Electricity Generation - July 2024',
        title_size=12,             # Smaller, professional
        title_weight='normal',     # Not bold - cleaner look
        title_style='normal',
        title_color='#000000',
        
        x_label='Time Step (30-minute intervals)',
        y_label='Generation (MWh)',
        axis_label_size=11,
        axis_label_weight='normal',
        axis_label_color='#000000',
        
        tick_label_size=9,
        tick_label_weight='normal',
        tick_label_color='#000000',
        
        show_legend=True,
        legend_location='upper right',
        legend_font_size=9,
        legend_font_weight='normal',
        
        show_grid=True,
        grid_alpha=0.2,
        
        # Publication dimensions
        figure_width=6.0,
        figure_height=4.0
    )
    
    # Create plot
    fig, ax = create_line_plot(series, config)
    
    # Subtle fill
    fill_under_curve(ax, x, y, color='#CCCCCC', alpha=0.3)
    add_boundary_lines(ax, x, linewidth=0.5, color='#666666')
    
    # Minimal week separators
    add_week_separators(
        ax, df,
        color='#666666',
        linewidth=1.0,
        alpha=0.5,
        center_labels=True,
        include_first=True,
        label_y_position=0.05,     # Very bottom
        label_fontsize=7,          # Small
        label_color='#999999',     # Light gray
        label_weight='normal'
    )
    
    save_plot(fig, 'config_extended_example3.png', dpi=300)
    print("  ✓ Created config_extended_example3.png")
    print("  ✓ Clean publication style")
    print("  ✓ All black/gray, no bold")
    print("  ✓ Minimal, professional appearance")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("EXTENDED PLOTCONFIG DEMONSTRATION")
    print("="*70)
    print("\nNew features:")
    print("  ✨ Title weight changed to 'normal' (was 'bold')")
    print("  ✨ Week labels positioned at bottom (0.1)")
    print("  ✨ Full control over text formatting")
    print("  ✨ Colors, weights, styles all configurable")
    print("="*70)
    
    example_1_extended_config()
    example_2_custom_styling()
    example_3_publication_style()
    
    print("\n" + "="*70)
    print("✓ All examples completed successfully!")
    print("="*70)
    print("\nKEY CHANGES:")
    print("  • PlotConfig.title_weight default = 'normal' (not 'bold')")
    print("  • add_week_separators label_y_position default = 0.1 (bottom)")
    print("  • All text elements fully configurable")
    print("="*70)
