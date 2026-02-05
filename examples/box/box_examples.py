"""
Box Plot Examples - PlotLib v2.5.0

Demonstrates all box plot capabilities with COMPREHENSIVE examples:
1. Single box plot
2. Multiple box plots (comparison)
3. Horizontal box plots
4. Custom colors
5. Grouped box plots
6. With/without outliers
7. Notched box plots
8. Publication-ready styling
9. Wide vs narrow boxes
10. Statistical comparison
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from plotlib import create_box_plot, save_plot
from models import PlotConfig


# ============================================================================
# EXAMPLE 1: Single Box Plot
# ============================================================================

def example_1_single_box():
    """
    Basic single box plot.
    """
    print("Example 1: Single box plot...")
    
    # Generate data
    np.random.seed(42)
    data = [np.random.randn(100) * 10 + 50]
    labels = ['Sample']
    
    # Config
    config = PlotConfig(
        title='Single Box Plot',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create box plot
    fig, ax = create_box_plot(data, labels, config)
    
    save_plot(fig, 'box_example1_single.png', dpi=300)
    print("  ✓ Created box_example1_single.png")


# ============================================================================
# EXAMPLE 2: Multiple Box Plots (Comparison)
# ============================================================================

def example_2_multiple():
    """
    Multiple box plots for comparing distributions.
    """
    print("\nExample 2: Multiple box plots...")
    
    # Generate data - three groups
    np.random.seed(42)
    control = np.random.randn(100) * 10 + 50
    treatment_a = np.random.randn(100) * 10 + 55
    treatment_b = np.random.randn(100) * 12 + 60
    
    data = [control, treatment_a, treatment_b]
    labels = ['Control', 'Treatment A', 'Treatment B']
    colors = ['#0066CC', '#CC6666', '#00CC66']
    
    # Config
    config = PlotConfig(
        title='Treatment Comparison - Box Plots',
        y_label='Response (units)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create box plots
    fig, ax = create_box_plot(data, labels, config, colors=colors)
    
    save_plot(fig, 'box_example2_multiple.png', dpi=300)
    print("  ✓ Created box_example2_multiple.png")
    print("     - Three groups compared")


# ============================================================================
# EXAMPLE 3: Horizontal Box Plots
# ============================================================================

def example_3_horizontal():
    """
    Horizontal box plots (useful for long labels).
    """
    print("\nExample 3: Horizontal box plots...")
    
    # Generate data
    np.random.seed(42)
    data = [
        np.random.exponential(2, 100),
        np.random.gamma(2, 2, 100),
        np.random.lognormal(0, 0.5, 100)
    ]
    labels = ['Exponential', 'Gamma', 'Log-normal']
    colors = ['#0066CC', '#CC6666', '#00CC66']
    
    # Config
    config = PlotConfig(
        title='Distribution Comparison - Horizontal',
        x_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create horizontal box plots
    fig, ax = create_box_plot(
        data, labels, config,
        colors=colors,
        orientation='horizontal'  # Horizontal!
    )
    
    save_plot(fig, 'box_example3_horizontal.png', dpi=300)
    print("  ✓ Created box_example3_horizontal.png")
    print("     - Horizontal orientation")


# ============================================================================
# EXAMPLE 4: Custom Colors and Styling
# ============================================================================

def example_4_custom_colors():
    """
    Custom colors for different groups.
    """
    print("\nExample 4: Custom colors...")
    
    # Generate data - quarterly results
    np.random.seed(42)
    q1 = np.random.randn(80) * 5 + 100
    q2 = np.random.randn(80) * 5 + 105
    q3 = np.random.randn(80) * 6 + 110
    q4 = np.random.randn(80) * 7 + 115
    
    data = [q1, q2, q3, q4]
    labels = ['Q1', 'Q2', 'Q3', 'Q4']
    colors = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#95E1D3']
    
    # Config
    config = PlotConfig(
        title='Quarterly Performance - Custom Colors',
        y_label='Sales ($1000s)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create box plots with custom colors
    fig, ax = create_box_plot(data, labels, config, colors=colors)
    
    save_plot(fig, 'box_example4_colors.png', dpi=300)
    print("  ✓ Created box_example4_colors.png")
    print("     - Custom color scheme")


# ============================================================================
# EXAMPLE 5: Grouped Box Plots
# ============================================================================

def example_5_grouped():
    """
    Grouped box plots for factorial comparisons.
    """
    print("\nExample 5: Grouped box plots...")
    
    # Generate data - 2 treatments x 2 genders
    np.random.seed(42)
    control_male = np.random.randn(50) * 8 + 50
    control_female = np.random.randn(50) * 8 + 52
    treatment_male = np.random.randn(50) * 9 + 58
    treatment_female = np.random.randn(50) * 9 + 62
    
    # Organize as groups
    data = [
        [control_male, control_female],
        [treatment_male, treatment_female]
    ]
    labels = [
        ['Male', 'Female'],
        ['Male', 'Female']
    ]
    group_labels = ['Control', 'Treatment']
    colors = ['#0066CC', '#CC6666']
    
    # Config
    config = PlotConfig(
        title='Treatment Effect by Gender - Grouped Box Plots',
        y_label='Response',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create grouped box plots
    fig, ax = create_box_plot(
        data, labels, config,
        colors=colors,
        grouped=True,
        group_labels=group_labels
    )
    
    save_plot(fig, 'box_example5_grouped.png', dpi=300)
    print("  ✓ Created box_example5_grouped.png")
    print("     - Grouped by treatment and gender")


# ============================================================================
# EXAMPLE 6: With/Without Outliers
# ============================================================================

def example_6_outliers():
    """
    Comparison showing outliers vs no outliers.
    """
    print("\nExample 6: Outlier handling...")
    
    # Generate data with outliers
    np.random.seed(42)
    data_with_outliers = np.random.randn(100) * 10 + 50
    # Add some outliers
    data_with_outliers = np.append(data_with_outliers, [20, 25, 80, 85, 90])
    
    data = [data_with_outliers]
    labels = ['With Outliers']
    
    # Config 1 - with outliers shown
    config1 = PlotConfig(
        title='Box Plot - With Outliers',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    fig1, ax1 = create_box_plot(
        data, labels, config1,
        show_outliers=True  # Show outliers
    )
    
    save_plot(fig1, 'box_example6a_with_outliers.png', dpi=300)
    
    # Config 2 - without outliers
    config2 = PlotConfig(
        title='Box Plot - Without Outliers',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    fig2, ax2 = create_box_plot(
        data, labels, config2,
        show_outliers=False  # Hide outliers
    )
    
    save_plot(fig2, 'box_example6b_no_outliers.png', dpi=300)
    
    print("  ✓ Created box_example6a_with_outliers.png")
    print("  ✓ Created box_example6b_no_outliers.png")
    print("     - Outlier comparison")


# ============================================================================
# EXAMPLE 7: Notched Box Plots
# ============================================================================

def example_7_notched():
    """
    Notched box plots (confidence intervals around median).
    """
    print("\nExample 7: Notched box plots...")
    
    # Generate data
    np.random.seed(42)
    sample1 = np.random.randn(100) * 10 + 50
    sample2 = np.random.randn(100) * 10 + 52
    sample3 = np.random.randn(100) * 10 + 55
    
    data = [sample1, sample2, sample3]
    labels = ['Sample 1', 'Sample 2', 'Sample 3']
    colors = ['#0066CC', '#CC6666', '#00CC66']
    
    # Config
    config = PlotConfig(
        title='Notched Box Plots - Median Confidence Intervals',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create notched box plots
    fig, ax = create_box_plot(
        data, labels, config,
        colors=colors,
        notch=True  # Notched boxes!
    )
    
    save_plot(fig, 'box_example7_notched.png', dpi=300)
    print("  ✓ Created box_example7_notched.png")
    print("     - Notched (confidence intervals)")


# ============================================================================
# EXAMPLE 8: Publication-Ready Styling
# ============================================================================

def example_8_publication():
    """
    Publication-ready box plot with clean styling.
    """
    print("\nExample 8: Publication-ready...")
    
    # Generate data - experimental results
    np.random.seed(42)
    baseline = np.random.randn(80) * 5 + 100
    method_a = np.random.randn(80) * 5 + 105
    method_b = np.random.randn(80) * 5 + 110
    
    data = [baseline, method_a, method_b]
    labels = ['Baseline', 'Method A', 'Method B']
    colors = ['#CCCCCC', '#888888', '#444444']  # Grayscale
    
    # Config
    config = PlotConfig(
        title='Method Comparison',
        title_weight='normal',
        y_label='Performance (arbitrary units)',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3,
        show_top_spine=False,
        show_right_spine=False
    )
    
    # Create publication-style box plot
    fig, ax = create_box_plot(
        data, labels, config,
        colors=colors,
        show_means=True
    )
    
    save_plot(fig, 'box_example8_publication.png', dpi=300)
    print("  ✓ Created box_example8_publication.png")
    print("     - Publication-ready grayscale")


# ============================================================================
# EXAMPLE 9: Wide vs Narrow Boxes
# ============================================================================

def example_9_box_widths():
    """
    Comparison of different box widths.
    """
    print("\nExample 9: Box widths...")
    
    # Generate data
    np.random.seed(42)
    data = [
        np.random.randn(100) * 10 + 50,
        np.random.randn(100) * 10 + 55,
        np.random.randn(100) * 10 + 60
    ]
    labels = ['A', 'B', 'C']
    
    # Config 1 - narrow boxes
    config1 = PlotConfig(
        title='Box Plot - Narrow Boxes (width=0.3)',
        y_label='Value',
        tick_label_size=11,
        show_grid=True
    )
    
    fig1, ax1 = create_box_plot(
        data, labels, config1,
        box_width=0.3  # Narrow
    )
    
    save_plot(fig1, 'box_example9a_narrow.png', dpi=300)
    
    # Config 2 - wide boxes
    config2 = PlotConfig(
        title='Box Plot - Wide Boxes (width=0.8)',
        y_label='Value',
        tick_label_size=11,
        show_grid=True
    )
    
    fig2, ax2 = create_box_plot(
        data, labels, config2,
        box_width=0.8  # Wide
    )
    
    save_plot(fig2, 'box_example9b_wide.png', dpi=300)
    
    print("  ✓ Created box_example9a_narrow.png")
    print("  ✓ Created box_example9b_wide.png")
    print("     - Width comparison")


# ============================================================================
# EXAMPLE 10: Statistical Comparison
# ============================================================================

def example_10_statistical():
    """
    Box plots for clear statistical comparison.
    """
    print("\nExample 10: Statistical comparison...")
    
    # Generate data with clear differences
    np.random.seed(42)
    low_var = np.random.randn(100) * 3 + 50
    medium_var = np.random.randn(100) * 8 + 50
    high_var = np.random.randn(100) * 15 + 50
    
    data = [low_var, medium_var, high_var]
    labels = ['Low Variance', 'Medium Variance', 'High Variance']
    colors = ['#0066CC', '#FFCC00', '#CC6666']
    
    # Config
    config = PlotConfig(
        title='Variance Comparison - Box Plots',
        y_label='Value',
        tick_label_size=11,
        show_grid=True,
        grid_alpha=0.3
    )
    
    # Create box plots
    fig, ax = create_box_plot(
        data, labels, config,
        colors=colors,
        show_means=True,
        notch=True
    )
    
    save_plot(fig, 'box_example10_statistical.png', dpi=300)
    print("  ✓ Created box_example10_statistical.png")
    print("     - Clear variance differences")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("BOX PLOT EXAMPLES - PLOTLIB V2.5.0")
    print("="*70)
    print("\nDemonstrating all box plot capabilities:")
    print("  1. Single box plot")
    print("  2. Multiple box plots (comparison)")
    print("  3. Horizontal box plots")
    print("  4. Custom colors")
    print("  5. Grouped box plots")
    print("  6. With/without outliers")
    print("  7. Notched box plots")
    print("  8. Publication-ready styling")
    print("  9. Wide vs narrow boxes")
    print("  10. Statistical comparison")
    print("="*70)
    
    example_1_single_box()
    example_2_multiple()
    example_3_horizontal()
    example_4_custom_colors()
    example_5_grouped()
    example_6_outliers()
    example_7_notched()
    example_8_publication()
    example_9_box_widths()
    example_10_statistical()
    
    print("\n" + "="*70)
    print("✓ All box plot examples completed successfully!")
    print("="*70)
    print("\nCreated 11 example plots:")
    print("  • box_example1_single.png - Single box")
    print("  • box_example2_multiple.png - Multiple comparison")
    print("  • box_example3_horizontal.png - Horizontal orientation")
    print("  • box_example4_colors.png - Custom colors")
    print("  • box_example5_grouped.png - Grouped boxes")
    print("  • box_example6a_with_outliers.png - With outliers")
    print("  • box_example6b_no_outliers.png - Without outliers")
    print("  • box_example7_notched.png - Notched (CI)")
    print("  • box_example8_publication.png - Publication style")
    print("  • box_example9a_narrow.png - Narrow boxes")
    print("  • box_example9b_wide.png - Wide boxes")
    print("  • box_example10_statistical.png - Statistical comparison")
    print("="*70)
    print("\nBOX PLOT FEATURES:")
    print("  Statistical:")
    print("    • Quartiles (Q1, median, Q3)")
    print("    • Whiskers (IQR-based)")
    print("    • Outliers (optional)")
    print("    • Means (optional)")
    print("    • Notches (confidence intervals)")
    print("  Styling:")
    print("    • Custom colors per box")
    print("    • Horizontal/vertical orientation")
    print("    • Box width control")
    print("    • Grouped box plots")
    print("="*70)
    print("\n🎉 PHASE 2 STARTED! BOX PLOTS COMPLETE! 🎉")
    print("="*70)
