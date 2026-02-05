"""
Contour Plot Examples - PlotLib v2.8.0

Demonstrates all contour plot capabilities with COMPREHENSIVE examples:
1. Basic filled contour
2. Line contours with labels
3. Both filled and lines
4. Custom levels
5. Custom colormap
6. From function (convenience)
7. Multiple contours in subplot
8. Parameter space
9. Gradient field
10. Publication-ready
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib.pyplot as plt
from plotlib import create_contour_plot, create_contour_from_function, create_subplots, save_plot
from models import PlotConfig


# ============================================================================
# EXAMPLE 1: Basic Filled Contour
# ============================================================================

def example_1_filled():
    """
    Basic filled contour plot.
    """
    print("Example 1: Basic filled contour...")
    
    # Generate data
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    
    # Config
    config = PlotConfig(
        title='Basic Filled Contour Plot',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create filled contour
    fig, ax = create_contour_plot(
        X, Y, Z, config,
        filled=True,
        cbar_label='Z Value'
    )
    
    save_plot(fig, 'contour_example1_filled.png', dpi=300)
    print("  ✓ Created contour_example1_filled.png")


# ============================================================================
# EXAMPLE 2: Line Contours with Labels
# ============================================================================

def example_2_lines():
    """
    Line contours with value labels.
    """
    print("\nExample 2: Line contours with labels...")
    
    # Generate data - paraboloid
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    
    # Config
    config = PlotConfig(
        title='Line Contours with Labels',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create line contours with labels
    fig, ax = create_contour_plot(
        X, Y, Z, config,
        filled=False,
        lines=True,
        labels=True,
        label_fontsize=9,
        line_colors='black',
        line_widths=1.5
    )
    
    save_plot(fig, 'contour_example2_lines.png', dpi=300)
    print("  ✓ Created contour_example2_lines.png")
    print("     - Contour labels shown")


# ============================================================================
# EXAMPLE 3: Both Filled and Lines
# ============================================================================

def example_3_both():
    """
    Filled contours with line overlays.
    """
    print("\nExample 3: Both filled and lines...")
    
    # Generate data - Gaussian
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    
    # Config
    config = PlotConfig(
        title='Filled Contours with Line Overlays',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create both filled and line contours
    fig, ax = create_contour_plot(
        X, Y, Z, config,
        filled=True,
        lines=True,
        line_colors='black',
        line_widths=0.5,
        cbar_label='Intensity'
    )
    
    save_plot(fig, 'contour_example3_both.png', dpi=300)
    print("  ✓ Created contour_example3_both.png")
    print("     - Filled + lines combined")


# ============================================================================
# EXAMPLE 4: Custom Levels
# ============================================================================

def example_4_custom_levels():
    """
    Contour plot with custom levels.
    """
    print("\nExample 4: Custom levels...")
    
    # Generate data
    x = np.linspace(-4, 4, 100)
    y = np.linspace(-4, 4, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Custom levels
    levels = [-0.8, -0.4, 0, 0.4, 0.8]
    
    # Config
    config = PlotConfig(
        title='Custom Contour Levels',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create contour with custom levels
    fig, ax = create_contour_plot(
        X, Y, Z, config,
        filled=True,
        lines=True,
        levels=levels,
        line_colors='white',
        line_widths=1.0,
        labels=True,
        label_fontsize=9,
        cbar_label='Z'
    )
    
    save_plot(fig, 'contour_example4_levels.png', dpi=300)
    print("  ✓ Created contour_example4_levels.png")
    print("     - Custom level values")


# ============================================================================
# EXAMPLE 5: Custom Colormap
# ============================================================================

def example_5_colormap():
    """
    Different colormaps for contour plots.
    """
    print("\nExample 5: Custom colormap...")
    
    # Generate data - saddle point
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 - Y**2
    
    # Config
    config = PlotConfig(
        title='Custom Colormap - Coolwarm',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create contour with coolwarm colormap
    fig, ax = create_contour_plot(
        X, Y, Z, config,
        filled=True,
        cmap='coolwarm',
        cbar_label='Z'
    )
    
    save_plot(fig, 'contour_example5_colormap.png', dpi=300)
    print("  ✓ Created contour_example5_colormap.png")
    print("     - Coolwarm colormap")


# ============================================================================
# EXAMPLE 6: From Function (Convenience)
# ============================================================================

def example_6_from_function():
    """
    Create contour plot directly from function.
    """
    print("\nExample 6: From function...")
    
    # Define function
    def my_function(x, y):
        return np.sin(x) * np.exp(-y**2/10)
    
    # Config
    config = PlotConfig(
        title='Contour from Function',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create contour from function
    fig, ax = create_contour_from_function(
        my_function,
        x_range=(-5, 5),
        y_range=(-3, 3),
        config=config,
        resolution=150,
        filled=True,
        lines=True,
        line_colors='black',
        line_widths=0.5,
        cbar_label='f(x, y)'
    )
    
    save_plot(fig, 'contour_example6_function.png', dpi=300)
    print("  ✓ Created contour_example6_function.png")
    print("     - Created from function")


# ============================================================================
# EXAMPLE 7: Multiple Contours in Subplot
# ============================================================================

def example_7_multiple():
    """
    Multiple contour plots in subplots.
    """
    print("\nExample 7: Multiple contours...")
    
    # Config
    config = PlotConfig(
        title='Multiple Contour Plots',
        figure_width=12,
        figure_height=4,
        tick_label_size=9
    )
    
    # Create subplots
    fig, axes = create_subplots(1, 3, config)
    
    # Generate data
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    
    # Plot 1: sin(x) * cos(y)
    Z1 = np.sin(X) * np.cos(Y)
    cs1 = axes[0].contourf(X, Y, Z1, levels=15, cmap='viridis')
    axes[0].set_title('sin(x)·cos(y)')
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    fig.colorbar(cs1, ax=axes[0])
    
    # Plot 2: Gaussian
    Z2 = np.exp(-(X**2 + Y**2))
    cs2 = axes[1].contourf(X, Y, Z2, levels=15, cmap='plasma')
    axes[1].set_title('Gaussian')
    axes[1].set_xlabel('X')
    fig.colorbar(cs2, ax=axes[1])
    
    # Plot 3: Saddle
    Z3 = X**2 - Y**2
    cs3 = axes[2].contourf(X, Y, Z3, levels=15, cmap='coolwarm')
    axes[2].set_title('Saddle: x²-y²')
    axes[2].set_xlabel('X')
    fig.colorbar(cs3, ax=axes[2])
    
    save_plot(fig, 'contour_example7_multiple.png', dpi=300)
    print("  ✓ Created contour_example7_multiple.png")
    print("     - Three different functions")


# ============================================================================
# EXAMPLE 8: Parameter Space
# ============================================================================

def example_8_parameter_space():
    """
    Parameter space exploration with contours.
    """
    print("\nExample 8: Parameter space...")
    
    # Generate parameter space
    # Simulated: performance vs two parameters
    alpha = np.linspace(0.1, 2.0, 100)
    beta = np.linspace(0.5, 3.0, 100)
    Alpha, Beta = np.meshgrid(alpha, beta)
    
    # Performance function (simulated)
    Performance = 100 * (1 - np.exp(-Alpha * Beta / 2)) * np.exp(-(Alpha - 1)**2 - (Beta - 1.5)**2)
    
    # Config
    config = PlotConfig(
        title='Parameter Space - Performance Landscape',
        x_label='Parameter α',
        y_label='Parameter β',
        tick_label_size=10
    )
    
    # Create contour
    fig, ax = create_contour_plot(
        Alpha, Beta, Performance, config,
        filled=True,
        lines=True,
        levels=15,
        line_colors='black',
        line_widths=0.5,
        labels=True,
        label_fontsize=8,
        cbar_label='Performance Score'
    )
    
    # Mark optimal point
    opt_idx = np.unravel_index(Performance.argmax(), Performance.shape)
    ax.plot(Alpha[opt_idx], Beta[opt_idx], 'r*', markersize=15, label='Optimum')
    ax.legend()
    
    save_plot(fig, 'contour_example8_parameters.png', dpi=300)
    print("  ✓ Created contour_example8_parameters.png")
    print("     - Parameter optimization landscape")


# ============================================================================
# EXAMPLE 9: Gradient/Field Visualization
# ============================================================================

def example_9_gradient():
    """
    Visualize gradient field with contours.
    """
    print("\nExample 9: Gradient field...")
    
    # Generate data
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    
    # Potential function
    x_fine = np.linspace(-2, 2, 100)
    y_fine = np.linspace(-2, 2, 100)
    X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
    Potential = X_fine**2 + Y_fine**2
    
    # Gradient (negative gradient = force direction)
    U = -2 * X
    V = -2 * Y
    
    # Config
    config = PlotConfig(
        title='Gradient Field with Potential Contours',
        x_label='X',
        y_label='Y',
        tick_label_size=10
    )
    
    # Create figure manually for custom combination
    fig = plt.figure(figsize=(config.figure_width, config.figure_height), dpi=config.dpi)
    ax = fig.add_subplot(111)
    
    # Plot potential contours
    cs = ax.contour(X_fine, Y_fine, Potential, levels=10, cmap='viridis', alpha=0.6)
    ax.clabel(cs, inline=True, fontsize=8)
    
    # Plot gradient field
    ax.quiver(X, Y, U, V, alpha=0.8, color='red')
    
    ax.set_xlabel(config.x_label or 'X', fontsize=12)
    ax.set_ylabel(config.y_label or 'Y', fontsize=12)
    ax.set_title(config.title, fontsize=14)
    ax.grid(True, alpha=0.3)
    
    save_plot(fig, 'contour_example9_gradient.png', dpi=300)
    print("  ✓ Created contour_example9_gradient.png")
    print("     - Gradient vectors + contours")


# ============================================================================
# EXAMPLE 10: Publication-Ready
# ============================================================================

def example_10_publication():
    """
    Clean publication-ready contour plot.
    """
    print("\nExample 10: Publication-ready...")
    
    # Generate realistic data - temperature distribution
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    
    # Simulated temperature field
    Temperature = 20 + 10 * np.exp(-((X-5)**2 + (Y-5)**2)/8) + \
                  5 * np.sin(X/2) * np.cos(Y/2)
    
    # Config
    config = PlotConfig(
        title='Temperature Distribution',
        title_weight='normal',
        x_label='Position X (cm)',
        y_label='Position Y (cm)',
        tick_label_size=10
    )
    
    # Create publication contour
    fig, ax = create_contour_plot(
        X, Y, Temperature, config,
        filled=True,
        lines=True,
        levels=12,
        cmap='RdYlBu_r',  # Red-Yellow-Blue (reversed)
        line_colors='black',
        line_widths=0.5,
        alpha=0.8,
        cbar_label='Temperature (°C)'
    )
    
    save_plot(fig, 'contour_example10_publication.png', dpi=300)
    print("  ✓ Created contour_example10_publication.png")
    print("     - Publication-ready style")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("CONTOUR PLOT EXAMPLES - PLOTLIB V2.8.0")
    print("="*70)
    print("\nDemonstrating all contour plot capabilities:")
    print("  1. Basic filled contour")
    print("  2. Line contours with labels")
    print("  3. Both filled and lines")
    print("  4. Custom levels")
    print("  5. Custom colormap")
    print("  6. From function (convenience)")
    print("  7. Multiple contours in subplot")
    print("  8. Parameter space exploration")
    print("  9. Gradient field visualization")
    print("  10. Publication-ready")
    print("="*70)
    
    example_1_filled()
    example_2_lines()
    example_3_both()
    example_4_custom_levels()
    example_5_colormap()
    example_6_from_function()
    example_7_multiple()
    example_8_parameter_space()
    example_9_gradient()
    example_10_publication()
    
    print("\n" + "="*70)
    print("✓ All contour plot examples completed successfully!")
    print("="*70)
    print("\nCreated 10 example plots:")
    print("  • contour_example1_filled.png - Basic filled")
    print("  • contour_example2_lines.png - Line with labels")
    print("  • contour_example3_both.png - Filled + lines")
    print("  • contour_example4_levels.png - Custom levels")
    print("  • contour_example5_colormap.png - Coolwarm cmap")
    print("  • contour_example6_function.png - From function")
    print("  • contour_example7_multiple.png - Multiple plots")
    print("  • contour_example8_parameters.png - Parameter space")
    print("  • contour_example9_gradient.png - Gradient field")
    print("  • contour_example10_publication.png - Publication")
    print("="*70)
    print("\nCONTOUR PLOT FEATURES:")
    print("  Types:")
    print("    • Filled contours")
    print("    • Line contours")
    print("    • Combined (filled + lines)")
    print("  Customization:")
    print("    • Custom levels (number or list)")
    print("    • Colormaps (any matplotlib colormap)")
    print("    • Contour labels")
    print("    • Line colors, widths, styles")
    print("  Use Cases:")
    print("    • 2D function visualization")
    print("    • Parameter space exploration")
    print("    • Field/gradient visualization")
    print("    • Temperature/pressure distributions")
    print("="*70)
    print("\n🎉 CONTOUR PLOTS COMPLETE! 🎉")
    print("="*70)
