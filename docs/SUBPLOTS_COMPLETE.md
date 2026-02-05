# Subplots & Facets - PlotLib v2.7.0 📐

## ✅ SUBPLOTS COMPLETE! PHASE 2: 50% DONE!

Subplot support for **multi-panel figures** with grid layouts, shared axes, and publication-ready formatting. Works with **all plot types**!

---

## 🎨 COMPLETE FEATURES

### **Layout Options:**
- ✅ **Grid layouts** - Any rows × cols configuration
- ✅ **Shared axes** - Share x, y, or both
- ✅ **Custom spacing** - Control gaps between subplots
- ✅ **Custom ratios** - Different widths/heights per row/column

### **Labeling:**
- ✅ **Subplot titles** - Individual titles for each panel
- ✅ **Panel labels** - (a), (b), (c), (d) for publications
- ✅ **Figure title** - Overall figure title

### **Integration:**
- ✅ **All plot types** - Line, bar, box, heatmap, histogram, area, pie
- ✅ **Mixed types** - Different plots in same figure
- ✅ **Publication-ready** - Clean, professional layouts

---

## 📝 QUICK START

### **Simple 2×2 Grid:**

```python
from plotlib import create_subplots, save_plot
from models import PlotConfig

# Config
config = PlotConfig(
    title='Multi-Panel Figure',
    figure_width=10,
    figure_height=8
)

# Create 2×2 grid
fig, axes = create_subplots(2, 2, config)

# Access individual subplots
# axes[0,0] - top left
# axes[0,1] - top right
# axes[1,0] - bottom left  
# axes[1,1] - bottom right

# Plot in each subplot
axes[0,0].plot(x, y1)
axes[0,1].plot(x, y2)
axes[1,0].bar(categories, values1)
axes[1,1].bar(categories, values2)

save_plot(fig, 'multi_panel.png')
```

---

## 📊 COMMON LAYOUTS

### **1. Simple Grid (2×2, 3×3, etc.)**

```python
fig, axes = create_subplots(2, 2, config)

# axes is 2D array: axes[row, col]
axes[0, 0].plot(...)  # Top left
axes[0, 1].plot(...)  # Top right
axes[1, 0].plot(...)  # Bottom left
axes[1, 1].plot(...)  # Bottom right
```

**Use:** Compare multiple related datasets

---

### **2. Vertical Stack (Shared X-Axis)**

```python
fig, axes = create_subplots(3, 1, config, sharex=True)

# axes is 1D array: axes[i]
axes[0].plot(t, signal1)
axes[1].plot(t, signal2)
axes[2].plot(t, signal3)
axes[2].set_xlabel('Time')  # Only bottom plot
```

**Use:** Time-series comparison, stacked signals

---

### **3. Horizontal (Shared Y-Axis)**

```python
fig, axes = create_subplots(1, 3, config, sharey=True)

# axes is 1D array: axes[i]
axes[0].bar(categories, data1)
axes[1].bar(categories, data2)
axes[2].bar(categories, data3)
axes[0].set_ylabel('Value')  # Only left plot
```

**Use:** Side-by-side comparison with same scale

---

### **4. Mixed Plot Types**

```python
fig, axes = create_subplots(2, 2, config)

# Different plot type in each panel
axes[0,0].plot(x, y)              # Line
axes[0,1].bar(cats, vals)         # Bar
axes[1,0].boxplot(data)           # Box
axes[1,1].imshow(matrix)          # Heatmap
```

**Use:** Multi-faceted analysis, comprehensive figures

---

## 📋 COMPLETE API

### **`create_subplots()` Parameters:**

```python
create_subplots(
    nrows=1,                       # Number of rows
    ncols=1,                       # Number of columns
    config=None,                   # PlotConfig
    sharex=False,                  # Share x-axis
    sharey=False,                  # Share y-axis
    subplot_titles=None,           # List of subplot titles
    figure_title=None,             # Overall figure title
    width_ratios=None,             # Column width ratios
    height_ratios=None,            # Row height ratios
    hspace=None,                   # Vertical spacing
    wspace=None                    # Horizontal spacing
) → (fig, axes)
```

**Returns:**
- `fig`: Figure object
- `axes`: Axes array (1D, 2D, or single Axes)

---

### **`add_subplot_labels()` - Panel Labels:**

```python
add_subplot_labels(
    fig,                           # Figure object
    axes,                          # Axes array
    labels=None,                   # Custom labels (default: a,b,c,...)
    loc='upper left',              # Label location
    fontsize=12,                   # Label font size
    fontweight='bold',             # Label weight
    offset=(-0.1, 1.05)           # Position offset
)
```

**Use:** Add (a), (b), (c), (d) labels for publications

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Vertical Stack (Time-Series)**

```python
config = PlotConfig(
    title='Time-Series Analysis',
    figure_width=10,
    figure_height=8
)

# Create vertical stack with shared x-axis
fig, axes = create_subplots(3, 1, config, sharex=True)

# Plot time-series data
axes[0].plot(t, temperature, 'r-')
axes[0].set_ylabel('Temp (°C)')

axes[1].plot(t, pressure, 'b-')
axes[1].set_ylabel('Pressure (hPa)')

axes[2].plot(t, humidity, 'g-')
axes[2].set_ylabel('Humidity (%)')
axes[2].set_xlabel('Time (hours)')
```

---

### **Example 2: With Subplot Titles**

```python
titles = [
    'Control Group',
    'Treatment A',
    'Treatment B',
    'Treatment C'
]

fig, axes = create_subplots(2, 2, config, subplot_titles=titles)

# Titles are automatically applied
for i, ax in enumerate(axes.flat):
    ax.plot(data[i])
```

---

### **Example 3: Publication Figure with Labels**

```python
from plotlib import add_subplot_labels

config = PlotConfig(
    title='Experimental Results',
    title_weight='normal',
    figure_width=10,
    figure_height=6
)

fig, axes = create_subplots(1, 3, config)

# Plot in each panel
axes[0].plot(...)  # Panel A
axes[1].bar(...)   # Panel B
axes[2].boxplot(...)  # Panel C

# Add panel labels (a), (b), (c)
add_subplot_labels(fig, axes)

save_plot(fig, 'figure1.png', dpi=300)
```

---

### **Example 4: Custom Width Ratios**

```python
# Left column 2× wider than right columns
fig, axes = create_subplots(
    2, 2, config,
    width_ratios=[2, 1],   # Left twice as wide
    height_ratios=[1, 1]   # Equal heights
)

# Main plot in left column
axes[0,0].plot(...)  # Large
axes[1,0].plot(...)  # Large

# Smaller plots in right column
axes[0,1].hist(...)  # Small
axes[1,1].boxplot(...)  # Small
```

---

### **Example 5: Custom Spacing**

```python
fig, axes = create_subplots(
    2, 2, config,
    hspace=0.4,  # More vertical space
    wspace=0.3   # More horizontal space
)

# Prevents overlap of labels
```

---

## 💡 DESIGN TIPS

### **Tip 1: Share Axes for Comparisons**

```python
# Time-series: share x-axis
sharex=True

# Side-by-side: share y-axis
sharey=True
```

### **Tip 2: Use Consistent Styling**

```python
# Apply same style to all subplots
config = PlotConfig(
    tick_label_size=10,
    show_grid=True,
    grid_alpha=0.3
)

for ax in axes.flat:
    ax.grid(True, alpha=0.3)
```

### **Tip 3: Label Only Outer Axes**

```python
# For shared axes
for i, ax in enumerate(axes):
    if i == len(axes) - 1:
        ax.set_xlabel('X Label')  # Only bottom
    if i == 0:
        ax.set_ylabel('Y Label')  # Only left
```

### **Tip 4: Use Panel Labels for Publications**

```python
# IEEE/ACM standard
add_subplot_labels(fig, axes)  # (a), (b), (c), (d)

# Or custom
add_subplot_labels(fig, axes, labels=['A', 'B', 'C', 'D'])
```

### **Tip 5: Adjust Figure Size for Grid**

```python
# Larger figures for more subplots
PlotConfig(
    figure_width=12,   # Wider
    figure_height=10   # Taller
)
```

---

## 📊 WORKING WITH ALL PLOT TYPES

### **With Existing PlotLib Functions:**

```python
from plotlib import create_subplots
import numpy as np

# Create grid
fig, axes = create_subplots(2, 2, config)

# You can't use create_line_plot directly (it makes its own figure)
# Instead, plot directly on the axes

# Line plot
axes[0,0].plot(x, y, linewidth=2)
axes[0,0].set_title('Line Plot')

# Bar chart
axes[0,1].bar(categories, values, color='#0066CC')
axes[0,1].set_title('Bar Chart')

# Box plot
axes[1,0].boxplot(data, labels=['A', 'B', 'C'])
axes[1,0].set_title('Box Plot')

# Heatmap
im = axes[1,1].imshow(matrix, cmap='viridis')
axes[1,1].set_title('Heatmap')
fig.colorbar(im, ax=axes[1,1])
```

---

## 📊 REALISTIC USE CASES

### **Thesis Figure - Multi-Method Comparison:**

```python
config = PlotConfig(
    title='Method Comparison',
    title_weight='normal',
    figure_width=12,
    figure_height=8
)

fig, axes = create_subplots(2, 3, config)

# Row 1: Raw data
axes[0,0].plot(t, method1_data)
axes[0,0].set_title('Method 1')

axes[0,1].plot(t, method2_data)
axes[0,1].set_title('Method 2')

axes[0,2].plot(t, method3_data)
axes[0,2].set_title('Method 3')

# Row 2: Statistical summary
axes[1,0].boxplot(method1_results)
axes[1,1].boxplot(method2_results)
axes[1,2].boxplot(method3_results)

add_subplot_labels(fig, axes)
save_plot(fig, 'thesis_chapter3_fig1.png', dpi=300)
```

---

### **Paper Figure - Results + Analysis:**

```python
titles = ['(a) Time Series', '(b) Distribution', '(c) Correlation']

fig, axes = create_subplots(1, 3, config, subplot_titles=titles)

# Panel A: Time series
axes[0].plot(t, signal, 'k-', linewidth=1.5)
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Signal (mV)')

# Panel B: Distribution
axes[1].hist(signal, bins=30, color='gray', edgecolor='black')
axes[1].set_xlabel('Signal (mV)')
axes[1].set_ylabel('Count')

# Panel C: Correlation
axes[2].scatter(signal[:-1], signal[1:], alpha=0.5)
axes[2].set_xlabel('Signal(t)')
axes[2].set_ylabel('Signal(t+1)')

save_plot(fig, 'paper_figure2.png', dpi=300)
```

---

### **Dashboard - Multiple Metrics:**

```python
config = PlotConfig(
    title='Daily Metrics Dashboard',
    figure_width=14,
    figure_height=10
)

fig, axes = create_subplots(3, 3, config, hspace=0.3, wspace=0.3)

# Fill each panel with different metric
metrics = [
    'Temperature', 'Pressure', 'Humidity',
    'Wind Speed', 'Rainfall', 'Solar Radiation',
    'Air Quality', 'Visibility', 'UV Index'
]

for i, (ax, metric) in enumerate(zip(axes.flat, metrics)):
    # Plot metric data
    ax.plot(time, data[i])
    ax.set_title(metric, fontsize=10)
    ax.grid(True, alpha=0.3)
```

---

## ✅ COMPATIBILITY

Works seamlessly with PlotConfig:
- Figure size applies to entire figure
- DPI applies to entire figure
- Can customize individual subplots

**Mix and match:**

```python
config = PlotConfig(
    figure_width=12,
    figure_height=8,
    tick_label_size=10
)

# Works perfectly
fig, axes = create_subplots(2, 2, config)
```

---

## 🎯 QUICK REFERENCE

### **Simple grid:**
```python
fig, axes = create_subplots(2, 2, config)
axes[0,0].plot(...)
```

### **Vertical stack:**
```python
fig, axes = create_subplots(3, 1, config, sharex=True)
axes[0].plot(...)
```

### **With titles:**
```python
titles = ['A', 'B', 'C']
fig, axes = create_subplots(1, 3, config, subplot_titles=titles)
```

### **With labels:**
```python
fig, axes = create_subplots(2, 2, config)
# ... plot ...
add_subplot_labels(fig, axes)  # Adds (a), (b), (c), (d)
```

### **Custom spacing:**
```python
fig, axes = create_subplots(2, 2, config, hspace=0.3, wspace=0.3)
```

### **Custom ratios:**
```python
fig, axes = create_subplots(2, 2, config, width_ratios=[2,1])
```

---

## 📚 EXAMPLES

See `examples/subplot_examples.py` for 10 complete working examples:

1. **Simple 2×2** - Basic grid
2. **Vertical stack** - Shared x-axis
3. **Horizontal** - Shared y-axis
4. **Mixed types** - Different plots per panel
5. **Custom spacing** - hspace/wspace
6. **Titles** - Subplot titles
7. **Labels** - Panel labels (a,b,c,d)
8. **Ratios** - Custom width/height
9. **Publication** - Clean professional figure
10. **Complex** - 3×3 multi-panel

**Run them:**

```powershell
cd examples
python subplot_examples.py
```

**Creates 10 PNG files demonstrating all features!**

---

## 📈 WHEN TO USE SUBPLOTS

| Use Case | Subplots | Alternative |
|----------|----------|-------------|
| Compare related datasets | ✅ Perfect | Multiple figures |
| Publication figures | ✅ Perfect | Separate plots |
| Multi-faceted analysis | ✅ Perfect | Dashboard |
| Time-series stack | ✅ Perfect | Single plot |
| Side-by-side comparison | ✅ Perfect | Overlay |

---

## 🎓 AXES INDEXING GUIDE

### **Single Subplot (1×1):**
```python
fig, axes = create_subplots(1, 1)
axes.plot(...)  # axes is single Axes object
```

### **1D Layout (Row or Column):**
```python
fig, axes = create_subplots(3, 1)  # or (1, 3)
axes[0].plot(...)  # axes is 1D array
axes[1].plot(...)
axes[2].plot(...)
```

### **2D Grid:**
```python
fig, axes = create_subplots(2, 2)
axes[0,0].plot(...)  # axes is 2D array
axes[0,1].plot(...)
axes[1,0].plot(...)
axes[1,1].plot(...)
```

### **Iterate Over All:**
```python
for ax in axes.flat:
    ax.grid(True)
```

---

**Subplots with comprehensive layout options are complete!** 📐

**Phase 2 Progress:** 3 of 6 (50%)  
**Next: Violin plots, Contour, or 3D?** 🚀
