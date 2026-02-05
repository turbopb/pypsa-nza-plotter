"""
Heatmap Examples - PlotLib v2.6.0

Demonstrates all heatmap capabilities with COMPREHENSIVE examples:
1. Basic heatmap
2. With annotations
3. Correlation matrix
4. Custom colormap
5. Diverging colormap
6. With grid lines
7. Square cells
8. Without color bar
9. Large matrix with labels
10. Publication-ready style
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from plotlib import create_heatmap, create_correlation_heatmap, save_plot
from models import PlotConfig


# ============================================================================
# EXAMPLE 1: Basic Heatmap
# ============================================================================

def example_1_basic():
    """
    Basic heatmap with random data.
    """
    print("Example 1: Basic heatmap...")
    
    # Generate random data
    np.random.seed(42)
    data = np.random.randn(8, 10)
    
    # Config
    config = PlotConfig(
        title='Basic Heatmap',
        tick_label_size=10
    )
    
    # Create heatmap
    fig, ax = create_heatmap(data, config)
    
    save_plot(fig, 'heatmap_example1_basic.png', dpi=300)
    print("  ✓ Created heatmap_example1_basic.png")


# ============================================================================
# EXAMPLE 2: With Annotations
# ============================================================================

def example_2_annotations():
    """
    Heatmap with data values annotated in cells.
    """
    print("\nExample 2: With annotations...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.randint(0, 100, (6, 8))
    
    # Config
    config = PlotConfig(
        title='Heatmap with Annotations',
        tick_label_size=10
    )
    
    # Create heatmap with annotations
    fig, ax = create_heatmap(
        data, config,
        annot=True,           # Show values
        fmt='d',              # Integer format
        annot_size=10
    )
    
    save_plot(fig, 'heatmap_example2_annotations.png', dpi=300)
    print("  ✓ Created heatmap_example2_annotations.png")
    print("     - Values shown in cells")


# ============================================================================
# EXAMPLE 3: Correlation Matrix
# ============================================================================

def example_3_correlation():
    """
    Correlation matrix heatmap.
    """
    print("\nExample 3: Correlation matrix...")
    
    # Generate correlated data
    np.random.seed(42)
    n_samples = 100
    n_vars = 5
    
    # Create some correlations
    data = np.random.randn(n_samples, n_vars)
    data[:, 1] = data[:, 0] + np.random.randn(n_samples) * 0.5  # Correlated
    data[:, 2] = -data[:, 0] + np.random.randn(n_samples) * 0.5  # Anti-correlated
    
    labels = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5']
    
    # Config
    config = PlotConfig(
        title='Correlation Matrix',
        tick_label_size=10
    )
    
    # Create correlation heatmap (convenience function)
    fig, ax = create_correlation_heatmap(
        data,
        labels=labels,
        config=config
    )
    
    save_plot(fig, 'heatmap_example3_correlation.png', dpi=300)
    print("  ✓ Created heatmap_example3_correlation.png")
    print("     - Correlation matrix with diverging colormap")


# ============================================================================
# EXAMPLE 4: Custom Colormap
# ============================================================================

def example_4_custom_colormap():
    """
    Heatmap with custom colormap.
    """
    print("\nExample 4: Custom colormap...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.rand(10, 12) * 100
    
    # Config
    config = PlotConfig(
        title='Custom Colormap - Plasma',
        tick_label_size=10
    )
    
    # Create heatmap with plasma colormap
    fig, ax = create_heatmap(
        data, config,
        cmap='plasma',        # Plasma colormap
        cbar_label='Value'
    )
    
    save_plot(fig, 'heatmap_example4_colormap.png', dpi=300)
    print("  ✓ Created heatmap_example4_colormap.png")
    print("     - Plasma colormap")


# ============================================================================
# EXAMPLE 5: Diverging Colormap
# ============================================================================

def example_5_diverging():
    """
    Diverging colormap centered at zero.
    """
    print("\nExample 5: Diverging colormap...")
    
    # Generate data centered around zero
    np.random.seed(42)
    data = np.random.randn(8, 10) * 10
    
    # Config
    config = PlotConfig(
        title='Diverging Colormap - Red-Blue',
        tick_label_size=10
    )
    
    # Create heatmap with diverging colormap
    fig, ax = create_heatmap(
        data, config,
        cmap='RdBu_r',        # Red-Blue diverging
        center=0,             # Center at zero
        cbar_label='Deviation'
    )
    
    save_plot(fig, 'heatmap_example5_diverging.png', dpi=300)
    print("  ✓ Created heatmap_example5_diverging.png")
    print("     - Centered at zero, red-blue colormap")


# ============================================================================
# EXAMPLE 6: With Grid Lines
# ============================================================================

def example_6_grid():
    """
    Heatmap with grid lines between cells.
    """
    print("\nExample 6: With grid lines...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.rand(6, 8) * 50 + 25
    
    # Config
    config = PlotConfig(
        title='Heatmap with Grid Lines',
        tick_label_size=10
    )
    
    # Create heatmap with grid
    fig, ax = create_heatmap(
        data, config,
        cmap='YlOrRd',
        linewidths=0.5,       # Grid line width
        linecolor='white',    # Grid line color
        annot=True,
        fmt='.1f',
        annot_size=9
    )
    
    save_plot(fig, 'heatmap_example6_grid.png', dpi=300)
    print("  ✓ Created heatmap_example6_grid.png")
    print("     - White grid lines")


# ============================================================================
# EXAMPLE 7: Square Cells
# ============================================================================

def example_7_square():
    """
    Heatmap with square cells (equal aspect ratio).
    """
    print("\nExample 7: Square cells...")
    
    # Generate correlation-like data
    np.random.seed(42)
    n = 6
    data = np.random.rand(n, n)
    # Make symmetric
    data = (data + data.T) / 2
    np.fill_diagonal(data, 1.0)
    
    labels = [f'Feature {i+1}' for i in range(n)]
    
    # Config
    config = PlotConfig(
        title='Similarity Matrix - Square Cells',
        tick_label_size=10
    )
    
    # Create heatmap with square cells
    fig, ax = create_heatmap(
        data, config,
        row_labels=labels,
        col_labels=labels,
        cmap='viridis',
        square=True,          # Square cells!
        annot=True,
        fmt='.2f',
        cbar_label='Similarity'
    )
    
    save_plot(fig, 'heatmap_example7_square.png', dpi=300)
    print("  ✓ Created heatmap_example7_square.png")
    print("     - Square aspect ratio")


# ============================================================================
# EXAMPLE 8: Without Color Bar
# ============================================================================

def example_8_no_colorbar():
    """
    Heatmap without color bar (cleaner look).
    """
    print("\nExample 8: Without color bar...")
    
    # Generate data
    np.random.seed(42)
    data = np.random.randint(1, 10, (5, 7))
    
    row_labels = ['Row A', 'Row B', 'Row C', 'Row D', 'Row E']
    col_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Config
    config = PlotConfig(
        title='Weekly Schedule - No Color Bar',
        tick_label_size=11
    )
    
    # Create heatmap without color bar
    fig, ax = create_heatmap(
        data, config,
        row_labels=row_labels,
        col_labels=col_labels,
        cmap='Blues',
        cbar=False,           # No color bar
        annot=True,
        fmt='d',
        annot_size=12,
        linewidths=1,
        linecolor='white'
    )
    
    save_plot(fig, 'heatmap_example8_no_cbar.png', dpi=300)
    print("  ✓ Created heatmap_example8_no_cbar.png")
    print("     - No color bar, cleaner appearance")


# ============================================================================
# EXAMPLE 9: Large Matrix with Labels
# ============================================================================

def example_9_large_matrix():
    """
    Larger matrix with meaningful labels.
    """
    print("\nExample 9: Large matrix...")
    
    # Generate data - confusion matrix style
    np.random.seed(42)
    n_classes = 10
    data = np.random.randint(0, 50, (n_classes, n_classes))
    # Add diagonal emphasis (correct predictions)
    for i in range(n_classes):
        data[i, i] += 100
    
    labels = [f'Class {i}' for i in range(n_classes)]
    
    # Config
    config = PlotConfig(
        title='Confusion Matrix - 10 Classes',
        x_label='Predicted',
        y_label='Actual',
        tick_label_size=9
    )
    
    # Create large heatmap
    fig, ax = create_heatmap(
        data, config,
        row_labels=labels,
        col_labels=labels,
        cmap='Blues',
        annot=True,
        fmt='d',
        annot_size=8,
        cbar_label='Count'
    )
    
    save_plot(fig, 'heatmap_example9_large.png', dpi=300)
    print("  ✓ Created heatmap_example9_large.png")
    print("     - 10×10 confusion matrix")


# ============================================================================
# EXAMPLE 10: Publication-Ready Style
# ============================================================================

def example_10_publication():
    """
    Publication-ready heatmap with clean styling.
    """
    print("\nExample 10: Publication-ready...")
    
    # Generate correlation data
    np.random.seed(42)
    n_samples = 200
    
    # Create variables with known correlations
    x1 = np.random.randn(n_samples)
    x2 = 0.8 * x1 + 0.2 * np.random.randn(n_samples)
    x3 = -0.6 * x1 + 0.4 * np.random.randn(n_samples)
    x4 = np.random.randn(n_samples)
    
    data = np.column_stack([x1, x2, x3, x4])
    labels = ['Temperature', 'Pressure', 'Humidity', 'Wind Speed']
    
    # Config
    config = PlotConfig(
        title='Variable Correlations',
        title_weight='normal',
        tick_label_size=11
    )
    
    # Create publication-style correlation heatmap
    fig, ax = create_correlation_heatmap(
        data,
        labels=labels,
        config=config,
        linewidths=0.5,
        linecolor='gray'
    )
    
    save_plot(fig, 'heatmap_example10_publication.png', dpi=300)
    print("  ✓ Created heatmap_example10_publication.png")
    print("     - Publication-ready correlation matrix")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("HEATMAP EXAMPLES - PLOTLIB V2.6.0")
    print("="*70)
    print("\nDemonstrating all heatmap capabilities:")
    print("  1. Basic heatmap")
    print("  2. With annotations")
    print("  3. Correlation matrix")
    print("  4. Custom colormap (plasma)")
    print("  5. Diverging colormap (red-blue)")
    print("  6. With grid lines")
    print("  7. Square cells")
    print("  8. Without color bar")
    print("  9. Large matrix (10×10)")
    print("  10. Publication-ready")
    print("="*70)
    
    example_1_basic()
    example_2_annotations()
    example_3_correlation()
    example_4_custom_colormap()
    example_5_diverging()
    example_6_grid()
    example_7_square()
    example_8_no_colorbar()
    example_9_large_matrix()
    example_10_publication()
    
    print("\n" + "="*70)
    print("✓ All heatmap examples completed successfully!")
    print("="*70)
    print("\nCreated 10 example plots:")
    print("  • heatmap_example1_basic.png - Basic heatmap")
    print("  • heatmap_example2_annotations.png - With values")
    print("  • heatmap_example3_correlation.png - Correlation matrix")
    print("  • heatmap_example4_colormap.png - Plasma colormap")
    print("  • heatmap_example5_diverging.png - Red-blue diverging")
    print("  • heatmap_example6_grid.png - With grid lines")
    print("  • heatmap_example7_square.png - Square cells")
    print("  • heatmap_example8_no_cbar.png - No color bar")
    print("  • heatmap_example9_large.png - 10×10 confusion matrix")
    print("  • heatmap_example10_publication.png - Publication style")
    print("="*70)
    print("\nHEATMAP FEATURES:")
    print("  Data Visualization:")
    print("    • 2D data matrices")
    print("    • Correlation matrices")
    print("    • Confusion matrices")
    print("    • Parameter sweeps")
    print("  Colormaps:")
    print("    • Sequential: viridis, plasma, Blues, etc.")
    print("    • Diverging: RdBu_r, coolwarm (centered)")
    print("    • Custom vmin/vmax ranges")
    print("  Customization:")
    print("    • Annotations (values in cells)")
    print("    • Grid lines")
    print("    • Square cells")
    print("    • Color bar (show/hide)")
    print("    • Row/column labels")
    print("="*70)
    print("\n🎉 HEATMAPS COMPLETE! 🎉")
    print("="*70)
