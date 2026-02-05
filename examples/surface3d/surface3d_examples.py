"""
3D Surface Plot Examples - PlotLib v2.9.0

Demonstrates all 3D surface plot capabilities with COMPREHENSIVE examples:
1. Basic surface plot
2. Wireframe plot
3. 3D contour plot
4. Custom colormap
5. Custom viewing angle
6. From function (convenience)
7. Response surface
8. Multiple 3D plots
9. Transparent surface
10. Publication-ready
"""
import matplotlib
matplotlib.use('Qt5Agg')  # or 'Qt5Agg' if you have PyQt5

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib.pyplot as plt
from plotlib import create_surface_plot, create_surface_from_function, create_subplots, save_plot
from models import PlotConfig




# ============================================================================
# EXAMPLE 1: Basic Surface Plot
# ============================================================================

def example_1_basic():
    """
    Basic 3D surface plot.
    """
    print("Example 1: Basic 3D surface...")
    
    # Generate data
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Config
    config = PlotConfig(
        title='Basic 3D Surface Plot',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'Z'
    
    # Create surface
    fig, ax = create_surface_plot(X, Y, Z, config)
    plt.show()
    
    save_plot(fig, 'surface_example1_basic.png', dpi=300)
    print("  ✓ Created surface_example1_basic.png")


# ============================================================================
# EXAMPLE 2: Wireframe Plot
# ============================================================================

def example_2_wireframe():
    """
    3D wireframe plot.
    """
    print("\nExample 2: Wireframe...")
    
    # Generate data - Gaussian
    x = np.linspace(-3, 3, 30)
    y = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    
    # Config
    config = PlotConfig(
        title='3D Wireframe Plot',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'Amplitude'
    
    # Create wireframe
    fig, ax = create_surface_plot(
        X, Y, Z, config,
        plot_type='wireframe',
        linewidth=1.0,
        alpha=0.7
    )
    plt.show()
    save_plot(fig, 'surface_example2_wireframe.png', dpi=300)
    print("  ✓ Created surface_example2_wireframe.png")
    print("     - Wireframe style")


# ============================================================================
# EXAMPLE 3: 3D Contour Plot
# ============================================================================

def example_3_contour3d():
    """
    3D contour plot.
    """
    print("\nExample 3: 3D contour...")
    
    # Generate data
    x = np.linspace(-4, 4, 40)
    y = np.linspace(-4, 4, 40)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    
    # Config
    config = PlotConfig(
        title='3D Contour Plot',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'Z'
    
    # Create 3D contour
    fig, ax = create_surface_plot(
        X, Y, Z, config,
        plot_type='contour3d',
        linewidth=2.0
    )
    plt.show()
    save_plot(fig, 'surface_example3_contour3d.png', dpi=300)
    print("  ✓ Created surface_example3_contour3d.png")
    print("     - 3D contour lines")


# ============================================================================
# EXAMPLE 4: Custom Colormap
# ============================================================================

def example_4_colormap():
    """
    Surface with custom colormap.
    """
    print("\nExample 4: Custom colormap...")
    
    # Generate data - saddle
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    Z = X**2 - Y**2
    
    # Config
    config = PlotConfig(
        title='3D Surface - Coolwarm Colormap',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'Z'
    
    # Create surface with coolwarm colormap
    fig, ax = create_surface_plot(
        X, Y, Z, config,
        cmap='coolwarm',
        cbar_label='Value'
    )
    plt.show()
    save_plot(fig, 'surface_example4_colormap.png', dpi=300)
    print("  ✓ Created surface_example4_colormap.png")
    print("     - Coolwarm colormap")


# ============================================================================
# EXAMPLE 5: Custom Viewing Angle
# ============================================================================

def example_5_viewangle():
    """
    Surface with custom viewing angle.
    """
    print("\nExample 5: Custom viewing angle...")
    
    # Generate data - wave
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.sin(Y)
    
    # Config
    config = PlotConfig(
        title='3D Surface - Custom View (elev=20°, azim=-30°)',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'Z'
    
    # Create surface with custom view
    fig, ax = create_surface_plot(
        X, Y, Z, config,
        elev=20,    # Elevation angle
        azim=-30,   # Azimuth angle
        cmap='viridis'
    )
    plt.show()
    save_plot(fig, 'surface_example5_viewangle.png', dpi=300)
    print("  ✓ Created surface_example5_viewangle.png")
    print("     - Custom elevation and azimuth")


# ============================================================================
# EXAMPLE 6: From Function (Convenience)
# ============================================================================

def example_6_from_function():
    """
    Create surface directly from function.
    """
    print("\nExample 6: From function...")
    
    # Define function
    def my_function(x, y):
        return np.sin(np.sqrt(x**2 + y**2)) / np.sqrt(x**2 + y**2 + 0.1)
    
    # Config
    config = PlotConfig(
        title='3D Surface from Function',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'f(x,y)'
    
    # Create surface from function
    fig, ax = create_surface_from_function(
        my_function,
        x_range=(-10, 10),
        y_range=(-10, 10),
        config=config,
        resolution=60,
        cmap='plasma'
    )
    plt.show()
    save_plot(fig, 'surface_example6_function.png', dpi=300)
    print("  ✓ Created surface_example6_function.png")
    print("     - Created from mathematical function")


# ============================================================================
# EXAMPLE 7: Response Surface
# ============================================================================

def example_7_response_surface():
    """
    Response surface for optimization.
    """
    print("\nExample 7: Response surface...")
    
    # Generate parameter space
    alpha = np.linspace(0.5, 2.5, 40)
    beta = np.linspace(1.0, 4.0, 40)
    Alpha, Beta = np.meshgrid(alpha, beta)
    
    # Response function (simulated optimization problem)
    Response = 100 * np.exp(-((Alpha - 1.5)**2 + (Beta - 2.5)**2) / 2) + \
               50 * np.exp(-((Alpha - 2.0)**2 + (Beta - 2.0)**2) / 4)
    
    # Config
    config = PlotConfig(
        title='Response Surface - Parameter Optimization',
        x_label='Parameter α',
        y_label='Parameter β',
        tick_label_size=9
    )
    config.z_label = 'Response'
    
    # Create response surface
    fig, ax = create_surface_plot(
        Alpha, Beta, Response, config,
        cmap='viridis',
        edgecolor='gray',
        linewidth=0.1,
        alpha=0.9,
        cbar_label='Response Value'
    )
    
    # Mark optimal point
    opt_idx = np.unravel_index(Response.argmax(), Response.shape)
    ax.scatter(
        Alpha[opt_idx], Beta[opt_idx], Response[opt_idx],
        color='red', s=100, marker='*', label='Optimum'
    )
    ax.legend()
    plt.show()
    save_plot(fig, 'surface_example7_response.png', dpi=300)
    print("  ✓ Created surface_example7_response.png")
    print("     - Response surface with optimum marked")


# ============================================================================
# EXAMPLE 8: Multiple 3D Plots
# ============================================================================

def example_8_multiple():
    """
    Multiple 3D surfaces in subplots.
    """
    print("\nExample 8: Multiple 3D surfaces...")
    
    # Generate data
    x = np.linspace(-3, 3, 30)
    y = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, y)
    
    # Config
    config = PlotConfig(
        title='Multiple 3D Surfaces',
        figure_width=12,
        figure_height=4,
        tick_label_size=8
    )
    
    # Create figure with 3 subplots
    fig = plt.figure(figsize=(config.figure_width, config.figure_height), dpi=config.dpi)
    
    # Subplot 1: Paraboloid
    ax1 = fig.add_subplot(131, projection='3d')
    Z1 = X**2 + Y**2
    surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)
    ax1.set_title('Paraboloid', fontsize=10)
    ax1.set_xlabel('X', fontsize=9)
    ax1.set_ylabel('Y', fontsize=9)
    ax1.set_zlabel('Z', fontsize=9)
    
    # Subplot 2: Gaussian
    ax2 = fig.add_subplot(132, projection='3d')
    Z2 = np.exp(-(X**2 + Y**2))
    surf2 = ax2.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.8)
    ax2.set_title('Gaussian', fontsize=10)
    ax2.set_xlabel('X', fontsize=9)
    ax2.set_ylabel('Y', fontsize=9)
    ax2.set_zlabel('Z', fontsize=9)
    
    # Subplot 3: Saddle
    ax3 = fig.add_subplot(133, projection='3d')
    Z3 = X**2 - Y**2
    surf3 = ax3.plot_surface(X, Y, Z3, cmap='coolwarm', alpha=0.8)
    ax3.set_title('Saddle', fontsize=10)
    ax3.set_xlabel('X', fontsize=9)
    ax3.set_ylabel('Y', fontsize=9)
    ax3.set_zlabel('Z', fontsize=9)
    
    plt.tight_layout()
    plt.show()
    save_plot(fig, 'surface_example8_multiple.png', dpi=300)
    print("  ✓ Created surface_example8_multiple.png")
    print("     - Three different surfaces")


# ============================================================================
# EXAMPLE 9: Transparent Surface
# ============================================================================

def example_9_transparent():
    """
    Transparent surface with edges.
    """
    print("\nExample 9: Transparent surface...")
    
    # Generate data
    x = np.linspace(-5, 5, 30)
    y = np.linspace(-5, 5, 30)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Config
    config = PlotConfig(
        title='Transparent Surface with Edges',
        x_label='X',
        y_label='Y',
        tick_label_size=9
    )
    config.z_label = 'Z'
    
    # Create transparent surface
    fig, ax = create_surface_plot(
        X, Y, Z, config,
        cmap='viridis',
        alpha=0.6,          # Transparent
        edgecolor='black',  # Black edges
        linewidth=0.3       # Thin edges
    )
    
    save_plot(fig, 'surface_example9_transparent.png', dpi=300)
    print("  ✓ Created surface_example9_transparent.png")
    print("     - Transparent with edge lines")


# ============================================================================
# EXAMPLE 10: Publication-Ready
# ============================================================================

def example_10_publication():
    """
    Clean publication-ready 3D surface.
    """
    print("\nExample 10: Publication-ready...")
    
    # Generate realistic data - temperature distribution
    x = np.linspace(0, 10, 50)
    y = np.linspace(0, 10, 50)
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
        tick_label_size=9
    )
    config.z_label = 'Temperature (°C)'
    
    # Create publication surface
    fig, ax = create_surface_plot(
        X, Y, Temperature, config,
        cmap='RdYlBu_r',    # Red-Yellow-Blue
        edgecolor='gray',
        linewidth=0.1,
        alpha=0.9,
        elev=25,
        azim=-60,
        cbar_label='Temperature (°C)'
    )
    plt.show()
    save_plot(fig, 'surface_example10_publication.png', dpi=300)
    print("  ✓ Created surface_example10_publication.png")
    print("     - Publication-ready style")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("3D SURFACE PLOT EXAMPLES - PLOTLIB V2.9.0")
    print("="*70)
    print("\nDemonstrating all 3D surface plot capabilities:")
    print("  1. Basic surface")
    print("  2. Wireframe")
    print("  3. 3D contour")
    print("  4. Custom colormap")
    print("  5. Custom viewing angle")
    print("  6. From function (convenience)")
    print("  7. Response surface")
    print("  8. Multiple 3D plots")
    print("  9. Transparent surface")
    print("  10. Publication-ready")
    print("="*70)
    
    example_1_basic()
    example_2_wireframe()
    example_3_contour3d()
    example_4_colormap()
    example_5_viewangle()
    example_6_from_function()
    example_7_response_surface()
    example_8_multiple()
    example_9_transparent()
    example_10_publication()
    
    print("\n" + "="*70)
    print("✓ All 3D surface plot examples completed successfully!")
    print("="*70)
    print("\nCreated 10 example plots:")
    print("  • surface_example1_basic.png - Basic surface")
    print("  • surface_example2_wireframe.png - Wireframe")
    print("  • surface_example3_contour3d.png - 3D contour")
    print("  • surface_example4_colormap.png - Coolwarm cmap")
    print("  • surface_example5_viewangle.png - Custom view")
    print("  • surface_example6_function.png - From function")
    print("  • surface_example7_response.png - Response surface")
    print("  • surface_example8_multiple.png - Multiple surfaces")
    print("  • surface_example9_transparent.png - Transparent")
    print("  • surface_example10_publication.png - Publication")
    print("="*70)
    print("\n3D SURFACE PLOT FEATURES:")
    print("  Types:")
    print("    • Surface plots (filled 3D surfaces)")
    print("    • Wireframe plots (3D mesh)")
    print("    • 3D contour plots (contour lines in 3D)")
    print("  Customization:")
    print("    • Colormaps (any matplotlib colormap)")
    print("    • Viewing angles (elevation, azimuth)")
    print("    • Transparency and edges")
    print("    • Resolution control")
    print("  Use Cases:")
    print("    • Response surfaces")
    print("    • 3D function visualization")
    print("    • Parameter spaces")
    print("    • Field distributions")
    print("="*70)
    print("\n🎉 3D SURFACE PLOTS COMPLETE! 🎉")
    print("="*70)
