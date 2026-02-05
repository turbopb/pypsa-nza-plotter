"""
Pie Chart Examples - PlotLib v2.0

Demonstrates all pie chart types with COMPREHENSIVE customization:
1. Simple pie chart
2. Donut chart
3. Exploded slices
4. Custom colors
5. Cross-hatching (B&W publication)
6. Multiple customizations combined
7. Generation mix example
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plotlib import create_pie_chart, save_plot
from models import PlotConfig


# ============================================================================
# EXAMPLE 1: Simple Pie Chart
# ============================================================================

def example_1_simple_pie():
    """
    Basic pie chart with custom colors.
    """
    print("Example 1: Simple pie chart...")
    
    # Data - NZ generation mix
    labels = ['Hydro', 'Geothermal', 'Wind', 'Gas', 'Coal']
    values = [3200, 1000, 800, 1500, 200]
    colors = ['#0066CC', '#CC6666', '#00CC66', '#CC9900', '#666666']
    
    # Config
    config = PlotConfig(
        title='New Zealand Generation Mix 2024',
        figure_width=8,
        figure_height=6,
        tick_label_size=11
    )
    
    # Create pie chart
    fig, ax = create_pie_chart(labels, values, colors, config)
    
    save_plot(fig, 'pie_example1_simple.png', dpi=300)
    print("  ✓ Created pie_example1_simple.png")


# ============================================================================
# EXAMPLE 2: Donut Chart
# ============================================================================

def example_2_donut():
    """
    Donut chart (pie with hole in center).
    """
    print("\nExample 2: Donut chart...")
    
    # Data
    labels = ['Residential', 'Commercial', 'Industrial']
    values = [3500, 2800, 4200]
    colors = ['#0066CC', '#00CC66', '#FFCC00']
    
    # Config
    config = PlotConfig(
        title='Electricity Demand by Sector',
        figure_width=8,
        figure_height=6,
        tick_label_size=12
    )
    
    # Create donut chart
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        donut=True,           # ← Donut!
        donut_width=0.4       # Width of ring
    )
    
    save_plot(fig, 'pie_example2_donut.png', dpi=300)
    print("  ✓ Created pie_example2_donut.png")
    print("     - Donut chart (hole in center)")


# ============================================================================
# EXAMPLE 3: Exploded Slices
# ============================================================================

def example_3_exploded():
    """
    Pie chart with exploded slices (pull out certain wedges).
    """
    print("\nExample 3: Exploded slices...")
    
    # Data
    labels = ['Hydro', 'Wind', 'Solar', 'Gas', 'Coal']
    values = [3200, 800, 400, 1500, 200]
    colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900', '#666666']
    
    # Explode renewable sources
    explode = [0.1, 0.15, 0.15, 0, 0]  # Pull out hydro, wind, solar
    
    # Config
    config = PlotConfig(
        title='Generation Mix - Renewables Highlighted',
        figure_width=8,
        figure_height=6,
        tick_label_size=11
    )
    
    # Create exploded pie
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        explode=explode        # ← Explode slices!
    )
    
    save_plot(fig, 'pie_example3_exploded.png', dpi=300)
    print("  ✓ Created pie_example3_exploded.png")
    print("     - Renewables pulled out")


# ============================================================================
# EXAMPLE 4: Cross-Hatching (B&W Publication)
# ============================================================================

def example_4_hatching():
    """
    Black & white pie chart with hatch patterns.
    """
    print("\nExample 4: Cross-hatching for B&W...")
    
    # Data
    labels = ['Hydro', 'Wind', 'Solar', 'Gas']
    values = [3200, 800, 400, 1500]
    
    # White slices with different patterns
    colors = ['white', 'white', 'white', 'white']
    hatches = ['///', '|||', 'xxx', '...']  # Different patterns!
    edge_colors = ['black', 'black', 'black', 'black']
    
    # Config
    config = PlotConfig(
        title='Generation Mix - Publication Style',
        figure_width=8,
        figure_height=6,
        tick_label_size=11
    )
    
    # Create hatched pie
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        hatches=hatches,           # ← Hatch patterns!
        edge_colors=edge_colors,   # ← Black edges
        edge_width=1.5
    )
    
    save_plot(fig, 'pie_example4_hatching.png', dpi=300)
    print("  ✓ Created pie_example4_hatching.png")
    print("     - Black & white with patterns")


# ============================================================================
# EXAMPLE 5: Donut with Hatching
# ============================================================================

def example_5_donut_hatching():
    """
    Donut chart with hatch patterns.
    """
    print("\nExample 5: Donut with hatching...")
    
    # Data
    labels = ['Peak', 'Shoulder', 'Off-Peak']
    values = [30, 35, 35]
    
    # Patterns for distinction
    colors = ['white', 'white', 'white']
    hatches = ['///', '|||', 'xxx']
    edge_colors = ['black', 'black', 'black']
    
    # Config
    config = PlotConfig(
        title='Load Profile Distribution',
        figure_width=8,
        figure_height=6,
        tick_label_size=12
    )
    
    # Create donut with hatching
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        donut=True,
        donut_width=0.35,
        hatches=hatches,
        edge_colors=edge_colors,
        edge_width=1.5
    )
    
    save_plot(fig, 'pie_example5_donut_hatching.png', dpi=300)
    print("  ✓ Created pie_example5_donut_hatching.png")
    print("     - Donut + patterns")


# ============================================================================
# EXAMPLE 6: Exploded Donut with Custom Colors
# ============================================================================

def example_6_exploded_donut():
    """
    Exploded donut chart with custom styling.
    """
    print("\nExample 6: Exploded donut...")
    
    # Data
    labels = ['Renewables', 'Fossil Fuels', 'Other']
    values = [5000, 1700, 300]
    colors = ['#00CC66', '#CC6666', '#CCCCCC']
    explode = [0.1, 0, 0]  # Emphasize renewables
    
    # Config
    config = PlotConfig(
        title='Energy Sources - Renewables at 71%',
        figure_width=8,
        figure_height=6,
        tick_label_size=12
    )
    
    # Create exploded donut
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        donut=True,
        donut_width=0.3,
        explode=explode,
        edge_width=2.0
    )
    
    save_plot(fig, 'pie_example6_exploded_donut.png', dpi=300)
    print("  ✓ Created pie_example6_exploded_donut.png")
    print("     - Exploded + donut + thick edges")


# ============================================================================
# EXAMPLE 7: No Percentages (Labels Only)
# ============================================================================

def example_7_no_percentages():
    """
    Pie chart with labels only (no percentages).
    """
    print("\nExample 7: Labels only (no percentages)...")
    
    # Data
    labels = ['Hydro', 'Wind', 'Solar', 'Gas', 'Coal', 'Geothermal']
    values = [3200, 800, 400, 1500, 200, 1000]
    colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900', '#666666', '#CC6666']
    
    # Config
    config = PlotConfig(
        title='Generation Mix - Labels Only',
        figure_width=8,
        figure_height=6,
        tick_label_size=11
    )
    
    # Create pie without percentages
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        show_percentages=False  # ← No percentages!
    )
    
    save_plot(fig, 'pie_example7_no_percentages.png', dpi=300)
    print("  ✓ Created pie_example7_no_percentages.png")


# ============================================================================
# EXAMPLE 8: Start Angle Rotation
# ============================================================================

def example_8_rotated():
    """
    Pie chart with custom start angle.
    """
    print("\nExample 8: Rotated start angle...")
    
    # Data
    labels = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [2500, 2800, 2600, 3100]
    colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC6666']
    
    # Config
    config = PlotConfig(
        title='Quarterly Revenue - Rotated',
        figure_width=8,
        figure_height=6,
        tick_label_size=12
    )
    
    # Create pie with custom start angle
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        start_angle=0  # ← Start at 0 degrees (east)
    )
    
    save_plot(fig, 'pie_example8_rotated.png', dpi=300)
    print("  ✓ Created pie_example8_rotated.png")
    print("     - Starts at 0° (east)")


# ============================================================================
# EXAMPLE 9: Color + Pattern (Accessible)
# ============================================================================

def example_9_accessible():
    """
    Pie chart with both color AND pattern for accessibility.
    """
    print("\nExample 9: Accessible (color + pattern)...")
    
    # Data
    labels = ['Hydro', 'Wind', 'Solar', 'Gas']
    values = [3200, 800, 400, 1500]
    
    # Color + pattern for redundancy
    colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900']
    hatches = ['', '///', 'xxx', '|||']  # First solid, others patterned
    edge_colors = ['black', 'black', 'black', 'black']
    
    # Config
    config = PlotConfig(
        title='Generation Mix - Accessible Design',
        figure_width=8,
        figure_height=6,
        tick_label_size=11
    )
    
    # Create accessible pie
    fig, ax = create_pie_chart(
        labels, values, colors, config,
        hatches=hatches,
        edge_colors=edge_colors,
        edge_width=1.0
    )
    
    save_plot(fig, 'pie_example9_accessible.png', dpi=300)
    print("  ✓ Created pie_example9_accessible.png")
    print("     - Color AND pattern")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("PIE CHART EXAMPLES - PLOTLIB V2.0")
    print("="*70)
    print("\nDemonstrating all pie chart types with customization:")
    print("  1. Simple pie chart")
    print("  2. Donut chart")
    print("  3. Exploded slices")
    print("  4. Cross-hatching (B&W publication)")
    print("  5. Donut with hatching")
    print("  6. Exploded donut")
    print("  7. Labels only (no percentages)")
    print("  8. Rotated start angle")
    print("  9. Accessible (color + pattern)")
    print("="*70)
    
    example_1_simple_pie()
    example_2_donut()
    example_3_exploded()
    example_4_hatching()
    example_5_donut_hatching()
    example_6_exploded_donut()
    example_7_no_percentages()
    example_8_rotated()
    example_9_accessible()
    
    print("\n" + "="*70)
    print("✓ All pie chart examples completed successfully!")
    print("="*70)
    print("\nCreated 9 example plots:")
    print("  • pie_example1_simple.png - Simple pie")
    print("  • pie_example2_donut.png - Donut chart")
    print("  • pie_example3_exploded.png - Exploded slices")
    print("  • pie_example4_hatching.png - B&W with patterns")
    print("  • pie_example5_donut_hatching.png - Donut + patterns")
    print("  • pie_example6_exploded_donut.png - Exploded donut")
    print("  • pie_example7_no_percentages.png - Labels only")
    print("  • pie_example8_rotated.png - Custom start angle")
    print("  • pie_example9_accessible.png - Color + pattern")
    print("="*70)
    print("\nCUSTOMIZATION OPTIONS:")
    print("  Slice styling:")
    print("    • colors - Per-slice colors")
    print("    • hatches - Cross-hatch patterns ('///', '|||', 'xxx', '...')")
    print("    • edge_colors - Per-slice edge colors")
    print("    • edge_width - Edge thickness")
    print("  Layout:")
    print("    • donut - Pie with hole (donut chart)")
    print("    • donut_width - Size of center hole")
    print("    • explode - Pull out slices")
    print("    • start_angle - Rotation")
    print("  Labels:")
    print("    • show_percentages - Show/hide percentages")
    print("    • show_labels - Show/hide labels")
    print("    • label_distance - Distance from center")
    print("="*70)
    print("\n🎉 PHASE 1 COMPLETE! ALL PLOT TYPES IMPLEMENTED! 🎉")
    print("="*70)
