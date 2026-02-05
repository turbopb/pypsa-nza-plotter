"""
Subplot Examples - PlotLib v2.7.0

Demonstrates all subplot capabilities with COMPREHENSIVE examples:
1. Simple 2×2 grid
2. Vertical stack with shared x-axis
3. Horizontal with shared y-axis
4. Mixed plot types in grid
5. Custom spacing
6. With subplot titles
7. With subplot labels (a, b, c, d)
8. Custom width/height ratios
9. Publication-ready figure
10. Complex multi-panel figure
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from plotlib import (
    create_subplots, add_subplot_labels, save_plot
)
from models import PlotConfig, SeriesConfig


# ============================================================================
# EXAMPLE 1: Simple 2×2 Grid
# ============================================================================

def example_1_simple_grid():
    """
    Simple 2×2 grid with line plots.
    """
    print("Example 1: Simple 2×2 grid...")
    
    # Config
    config = PlotConfig(
        title='2×2 Subplot Grid',
        figure_width=10,
        figure_height=8,
        tick_label_size=9
    )
    
    # Create 2×2 grid
    fig, axes = create_subplots(2, 2, config)
    
    # Generate data
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    
    # Plot 1: Sine
    axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].set_ylabel('Amplitude')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Cosine
    axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
    axes[0, 1].set_title('Cosine Wave')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Exponential
    axes[1, 0].plot(x, np.exp(-x/5), 'g-', linewidth=2)
    axes[1, 0].set_title('Exponential Decay')
    axes[1, 0].set_xlabel('Time (s)')
    axes[1, 0].set_ylabel('Amplitude')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Polynomial
    axes[1, 1].plot(x, x**2/20, 'm-', linewidth=2)
    axes[1, 1].set_title('Quadratic')
    axes[1, 1].set_xlabel('Time (s)')
    axes[1, 1].grid(True, alpha=0.3)
    
    save_plot(fig, 'subplot_example1_grid.png', dpi=300)
    print("  ✓ Created subplot_example1_grid.png")


# ============================================================================
# EXAMPLE 2: Vertical Stack with Shared X-Axis
# ============================================================================

def example_2_vertical_stack():
    """
    Vertical stack with shared x-axis (common for time-series).
    """
    print("\nExample 2: Vertical stack...")
    
    # Config
    config = PlotConfig(
        title='Time-Series Stack - Shared X-Axis',
        figure_width=10,
        figure_height=8,
        tick_label_size=9
    )
    
    # Create 3×1 grid with shared x-axis
    fig, axes = create_subplots(3, 1, config, sharex=True)
    
    # Generate data
    np.random.seed(42)
    t = np.linspace(0, 24, 100)
    signal1 = 10 + np.sin(t * 0.5) + np.random.randn(100) * 0.5
    signal2 = 20 + np.cos(t * 0.3) + np.random.randn(100) * 0.8
    signal3 = 15 + np.sin(t * 0.7) * np.cos(t * 0.2) + np.random.randn(100) * 0.3
    
    # Plot 1
    axes[0].plot(t, signal1, 'b-', linewidth=1.5)
    axes[0].set_ylabel('Signal 1', fontsize=11)
    axes[0].grid(True, alpha=0.3)
    
    # Plot 2
    axes[1].plot(t, signal2, 'r-', linewidth=1.5)
    axes[1].set_ylabel('Signal 2', fontsize=11)
    axes[1].grid(True, alpha=0.3)
    
    # Plot 3
    axes[2].plot(t, signal3, 'g-', linewidth=1.5)
    axes[2].set_ylabel('Signal 3', fontsize=11)
    axes[2].set_xlabel('Time (hours)', fontsize=11)
    axes[2].grid(True, alpha=0.3)
    
    save_plot(fig, 'subplot_example2_vertical.png', dpi=300)
    print("  ✓ Created subplot_example2_vertical.png")
    print("     - Shared x-axis")


# ============================================================================
# EXAMPLE 3: Horizontal with Shared Y-Axis
# ============================================================================

def example_3_horizontal():
    """
    Horizontal layout with shared y-axis.
    """
    print("\nExample 3: Horizontal with shared y...")
    
    # Config
    config = PlotConfig(
        title='Side-by-Side Comparison - Shared Y-Axis',
        figure_width=12,
        figure_height=4,
        tick_label_size=9
    )
    
    # Create 1×3 grid with shared y-axis
    fig, axes = create_subplots(1, 3, config, sharey=True)
    
    # Generate data
    np.random.seed(42)
    categories = ['A', 'B', 'C', 'D']
    
    data1 = np.random.rand(4) * 10
    data2 = np.random.rand(4) * 10
    data3 = np.random.rand(4) * 10
    
    # Plot 1
    axes[0].bar(categories, data1, color='#0066CC')
    axes[0].set_title('Dataset 1')
    axes[0].set_ylabel('Value', fontsize=11)
    axes[0].grid(True, alpha=0.3, axis='y')
    
    # Plot 2
    axes[1].bar(categories, data2, color='#CC6666')
    axes[1].set_title('Dataset 2')
    axes[1].grid(True, alpha=0.3, axis='y')
    
    # Plot 3
    axes[2].bar(categories, data3, color='#00CC66')
    axes[2].set_title('Dataset 3')
    axes[2].grid(True, alpha=0.3, axis='y')
    
    save_plot(fig, 'subplot_example3_horizontal.png', dpi=300)
    print("  ✓ Created subplot_example3_horizontal.png")
    print("     - Shared y-axis")


# ============================================================================
# EXAMPLE 4: Mixed Plot Types
# ============================================================================

def example_4_mixed_types():
    """
    Grid with different plot types in each subplot.
    """
    print("\nExample 4: Mixed plot types...")
    
    # Config
    config = PlotConfig(
        title='Mixed Plot Types',
        figure_width=12,
        figure_height=8,
        tick_label_size=9
    )
    
    # Create 2×2 grid
    fig, axes = create_subplots(2, 2, config)
    
    # Generate data
    np.random.seed(42)
    
    # Plot 1: Line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.exp(-x/10)
    axes[0, 0].plot(x, y, 'b-', linewidth=2)
    axes[0, 0].set_title('(a) Line Plot')
    axes[0, 0].set_ylabel('Amplitude')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Bar chart
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [85, 92, 88, 95]
    axes[0, 1].bar(categories, values, color=['#0066CC', '#CC6666', '#00CC66', '#FFCC00'])
    axes[0, 1].set_title('(b) Bar Chart')
    axes[0, 1].set_ylabel('Sales ($1000s)')
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # Plot 3: Box plot
    data = [np.random.randn(100) * 10 + 50 for _ in range(3)]
    bp = axes[1, 0].boxplot(data, labels=['Group A', 'Group B', 'Group C'])
    axes[1, 0].set_title('(c) Box Plot')
    axes[1, 0].set_xlabel('Groups')
    axes[1, 0].set_ylabel('Value')
    axes[1, 0].grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Scatter plot
    x_scatter = np.random.randn(50) * 2 + 5
    y_scatter = x_scatter * 2 + np.random.randn(50) * 3
    axes[1, 1].scatter(x_scatter, y_scatter, c='purple', alpha=0.6, s=50)
    axes[1, 1].set_title('(d) Scatter Plot')
    axes[1, 1].set_xlabel('X Variable')
    axes[1, 1].grid(True, alpha=0.3)
    
    save_plot(fig, 'subplot_example4_mixed.png', dpi=300)
    print("  ✓ Created subplot_example4_mixed.png")
    print("     - Different plot types in each panel")


# ============================================================================
# EXAMPLE 5: Custom Spacing
# ============================================================================

def example_5_custom_spacing():
    """
    Control spacing between subplots.
    """
    print("\nExample 5: Custom spacing...")
    
    # Config
    config = PlotConfig(
        title='Custom Subplot Spacing',
        figure_width=10,
        figure_height=8,
        tick_label_size=9
    )
    
    # Create grid with custom spacing
    fig, axes = create_subplots(
        2, 2, config,
        hspace=0.4,  # Vertical spacing
        wspace=0.3   # Horizontal spacing
    )
    
    # Generate data
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    
    for i in range(2):
        for j in range(2):
            y = np.sin(x + i + j) * (i + j + 1)
            axes[i, j].plot(x, y, linewidth=2)
            axes[i, j].set_title(f'Panel {i*2 + j + 1}')
            axes[i, j].grid(True, alpha=0.3)
            if i == 1:
                axes[i, j].set_xlabel('X')
            if j == 0:
                axes[i, j].set_ylabel('Y')
    
    save_plot(fig, 'subplot_example5_spacing.png', dpi=300)
    print("  ✓ Created subplot_example5_spacing.png")
    print("     - Custom hspace and wspace")


# ============================================================================
# EXAMPLE 6: With Subplot Titles
# ============================================================================

def example_6_titles():
    """
    Subplots with custom titles.
    """
    print("\nExample 6: Subplot titles...")
    
    # Config
    config = PlotConfig(
        title='Subplot Titles Example',
        figure_width=10,
        figure_height=6,
        tick_label_size=9
    )
    
    # Define titles
    titles = [
        'Temperature Over Time',
        'Pressure Variations',
        'Humidity Levels'
    ]
    
    # Create 1×3 grid with titles
    fig, axes = create_subplots(1, 3, config, subplot_titles=titles)
    
    # Generate data
    np.random.seed(42)
    t = np.linspace(0, 24, 100)
    
    temp = 20 + 5 * np.sin(t * 0.3) + np.random.randn(100) * 2
    pressure = 1013 + 10 * np.cos(t * 0.2) + np.random.randn(100) * 5
    humidity = 60 + 15 * np.sin(t * 0.4) + np.random.randn(100) * 5
    
    axes[0].plot(t, temp, 'r-', linewidth=1.5)
    axes[0].set_ylabel('°C')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(t, pressure, 'b-', linewidth=1.5)
    axes[1].set_xlabel('Hour')
    axes[1].set_ylabel('hPa')
    axes[1].grid(True, alpha=0.3)
    
    axes[2].plot(t, humidity, 'g-', linewidth=1.5)
    axes[2].set_ylabel('%')
    axes[2].grid(True, alpha=0.3)
    
    save_plot(fig, 'subplot_example6_titles.png', dpi=300)
    print("  ✓ Created subplot_example6_titles.png")


# ============================================================================
# EXAMPLE 7: With Subplot Labels (a, b, c, d)
# ============================================================================

def example_7_labels():
    """
    Add publication-style labels to subplots.
    """
    print("\nExample 7: Subplot labels (a, b, c, d)...")
    
    # Config
    config = PlotConfig(
        title='Publication Figure with Panel Labels',
        figure_width=10,
        figure_height=8,
        tick_label_size=9
    )
    
    # Create 2×2 grid
    fig, axes = create_subplots(2, 2, config)
    
    # Generate data
    np.random.seed(42)
    
    # Four different datasets
    for i in range(2):
        for j in range(2):
            x = np.linspace(0, 10, 50)
            y = np.random.randn(50) * (i + j + 1) + (i * 5 + j * 3)
            axes[i, j].plot(x, y, 'o-', linewidth=1.5, markersize=4)
            axes[i, j].grid(True, alpha=0.3)
            if i == 1:
                axes[i, j].set_xlabel('X Variable')
            if j == 0:
                axes[i, j].set_ylabel('Y Variable')
    
    # Add (a), (b), (c), (d) labels
    add_subplot_labels(fig, axes)
    
    save_plot(fig, 'subplot_example7_labels.png', dpi=300)
    print("  ✓ Created subplot_example7_labels.png")
    print("     - Panel labels: (a), (b), (c), (d)")


# ============================================================================
# EXAMPLE 8: Custom Width/Height Ratios
# ============================================================================

def example_8_custom_ratios():
    """
    Custom width and height ratios for subplots.
    """
    print("\nExample 8: Custom width/height ratios...")
    
    # Config
    config = PlotConfig(
        title='Custom Subplot Ratios',
        figure_width=12,
        figure_height=8,
        tick_label_size=9
    )
    
    # Create grid with custom ratios
    # Left plot 2x wider than right plots
    fig, axes = create_subplots(
        2, 2, config,
        width_ratios=[2, 1],   # Left column twice as wide
        height_ratios=[1, 1]   # Equal heights
    )
    
    # Generate data
    np.random.seed(42)
    
    # Main plot (large, left side)
    x = np.linspace(0, 10, 200)
    y = np.sin(x) * np.exp(-x/10)
    axes[0, 0].plot(x, y, 'b-', linewidth=2)
    axes[0, 0].set_title('Main Plot (2× width)')
    axes[0, 0].set_ylabel('Signal')
    axes[0, 0].grid(True, alpha=0.3)
    
    axes[1, 0].plot(x, np.cos(x) * np.exp(-x/10), 'r-', linewidth=2)
    axes[1, 0].set_xlabel('Time')
    axes[1, 0].set_ylabel('Signal')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Side plots (smaller, right side)
    data = np.random.randn(100)
    axes[0, 1].hist(data, bins=20, color='green', alpha=0.7)
    axes[0, 1].set_title('Distribution')
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    axes[1, 1].boxplot([data])
    axes[1, 1].set_title('Summary')
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    
    save_plot(fig, 'subplot_example8_ratios.png', dpi=300)
    print("  ✓ Created subplot_example8_ratios.png")
    print("     - Custom width ratios")


# ============================================================================
# EXAMPLE 9: Publication-Ready Figure
# ============================================================================

def example_9_publication():
    """
    Clean publication-ready multi-panel figure.
    """
    print("\nExample 9: Publication-ready...")
    
    # Config
    config = PlotConfig(
        title='Experimental Results',
        title_weight='normal',
        figure_width=10,
        figure_height=6,
        tick_label_size=10
    )
    
    # Create 1×3 grid
    fig, axes = create_subplots(1, 3, config)
    
    # Generate data
    np.random.seed(42)
    
    # Panel A: Time series
    t = np.linspace(0, 10, 100)
    signal = np.sin(t) * np.exp(-t/5) + np.random.randn(100) * 0.1
    axes[0].plot(t, signal, 'k-', linewidth=1.5)
    axes[0].set_xlabel('Time (s)')
    axes[0].set_ylabel('Signal (mV)')
    axes[0].grid(True, alpha=0.3)
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    
    # Panel B: Bar comparison
    groups = ['Control', 'Treatment']
    means = [45, 68]
    errors = [5, 7]
    axes[1].bar(groups, means, yerr=errors, capsize=5, 
               color=['#CCCCCC', '#666666'], edgecolor='black', linewidth=1.5)
    axes[1].set_ylabel('Response (units)')
    axes[1].grid(True, alpha=0.3, axis='y')
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    
    # Panel C: Distribution
    control_data = np.random.randn(100) * 10 + 45
    treatment_data = np.random.randn(100) * 10 + 68
    bp = axes[2].boxplot([control_data, treatment_data], labels=groups, 
                         patch_artist=True)
    for patch, color in zip(bp['boxes'], ['#CCCCCC', '#666666']):
        patch.set_facecolor(color)
    axes[2].set_ylabel('Response (units)')
    axes[2].grid(True, alpha=0.3, axis='y')
    axes[2].spines['top'].set_visible(False)
    axes[2].spines['right'].set_visible(False)
    
    # Add panel labels
    add_subplot_labels(fig, axes, labels=['A', 'B', 'C'], 
                      offset=(-0.15, 1.05))
    
    save_plot(fig, 'subplot_example9_publication.png', dpi=300)
    print("  ✓ Created subplot_example9_publication.png")
    print("     - Publication-ready with panel labels")


# ============================================================================
# EXAMPLE 10: Complex Multi-Panel Figure
# ============================================================================

def example_10_complex():
    """
    Complex figure with many panels.
    """
    print("\nExample 10: Complex multi-panel...")
    
    # Config
    config = PlotConfig(
        title='Complex Multi-Panel Analysis',
        figure_width=14,
        figure_height=10,
        tick_label_size=8
    )
    
    # Create 3×3 grid
    fig, axes = create_subplots(3, 3, config, hspace=0.3, wspace=0.3)
    
    # Generate various plots
    np.random.seed(42)
    
    for i in range(3):
        for j in range(3):
            if (i + j) % 3 == 0:
                # Line plot
                x = np.linspace(0, 10, 50)
                y = np.sin(x + i + j) * (i + 1)
                axes[i, j].plot(x, y, linewidth=1.5)
            elif (i + j) % 3 == 1:
                # Bar plot
                data = np.random.rand(4) * 10
                axes[i, j].bar(['A', 'B', 'C', 'D'], data)
            else:
                # Scatter plot
                x = np.random.randn(30)
                y = x * 2 + np.random.randn(30)
                axes[i, j].scatter(x, y, alpha=0.6)
            
            axes[i, j].set_title(f'Panel {i*3 + j + 1}', fontsize=9)
            axes[i, j].grid(True, alpha=0.3)
            axes[i, j].tick_params(labelsize=8)
    
    save_plot(fig, 'subplot_example10_complex.png', dpi=300)
    print("  ✓ Created subplot_example10_complex.png")
    print("     - 3×3 grid with mixed plot types")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("SUBPLOT EXAMPLES - PLOTLIB V2.7.0")
    print("="*70)
    print("\nDemonstrating all subplot capabilities:")
    print("  1. Simple 2×2 grid")
    print("  2. Vertical stack (shared x-axis)")
    print("  3. Horizontal (shared y-axis)")
    print("  4. Mixed plot types")
    print("  5. Custom spacing")
    print("  6. Subplot titles")
    print("  7. Subplot labels (a, b, c, d)")
    print("  8. Custom width/height ratios")
    print("  9. Publication-ready")
    print("  10. Complex 3×3 grid")
    print("="*70)
    
    example_1_simple_grid()
    example_2_vertical_stack()
    example_3_horizontal()
    example_4_mixed_types()
    example_5_custom_spacing()
    example_6_titles()
    example_7_labels()
    example_8_custom_ratios()
    example_9_publication()
    example_10_complex()
    
    print("\n" + "="*70)
    print("✓ All subplot examples completed successfully!")
    print("="*70)
    print("\nCreated 10 example plots:")
    print("  • subplot_example1_grid.png - 2×2 grid")
    print("  • subplot_example2_vertical.png - Vertical stack")
    print("  • subplot_example3_horizontal.png - Horizontal")
    print("  • subplot_example4_mixed.png - Mixed plot types")
    print("  • subplot_example5_spacing.png - Custom spacing")
    print("  • subplot_example6_titles.png - Subplot titles")
    print("  • subplot_example7_labels.png - Panel labels (a,b,c,d)")
    print("  • subplot_example8_ratios.png - Custom ratios")
    print("  • subplot_example9_publication.png - Publication-ready")
    print("  • subplot_example10_complex.png - 3×3 complex")
    print("="*70)
    print("\nSUBPLOT FEATURES:")
    print("  Layout:")
    print("    • Grid layouts (any rows × cols)")
    print("    • Shared axes (x, y, or both)")
    print("    • Custom spacing (hspace, wspace)")
    print("    • Custom width/height ratios")
    print("  Labeling:")
    print("    • Subplot titles")
    print("    • Panel labels (a, b, c, d)")
    print("    • Figure title")
    print("  Integration:")
    print("    • Works with ALL plot types")
    print("    • Mix different plots in same figure")
    print("    • Publication-ready layouts")
    print("="*70)
    print("\n🎉 SUBPLOTS COMPLETE! 🎉")
    print("="*70)
