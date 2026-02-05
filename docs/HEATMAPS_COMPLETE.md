# Heatmaps - PlotLib v2.6.0 🔥

## ✅ HEATMAPS COMPLETE! PHASE 2 CONTINUES!

Heatmap support with **comprehensive customization** including annotations, colormaps, grid lines, and publication-ready formatting.

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Data Visualization:**
- ✅ **2D data matrices** - Any numeric data
- ✅ **Correlation matrices** - Convenience function
- ✅ **Confusion matrices** - Classification results
- ✅ **Parameter sweeps** - Multi-parameter visualization

### **Colormaps:**
- ✅ **Sequential** - viridis, plasma, Blues, YlOrRd, etc.
- ✅ **Diverging** - RdBu_r, coolwarm (centered at zero)
- ✅ **Custom ranges** - vmin, vmax control
- ✅ **Center value** - For diverging colormaps

### **Annotations:**
- ✅ **Cell values** - Show data in cells
- ✅ **Format control** - Integers, decimals, scientific
- ✅ **Font size** - Adjustable text size
- ✅ **Auto color** - Black/white based on cell value

### **Layout:**
- ✅ **Grid lines** - Between cells
- ✅ **Square cells** - Equal aspect ratio
- ✅ **Color bar** - Show/hide, custom label
- ✅ **Row/column labels** - Custom labels

---

## 📝 QUICK START

### **Basic Heatmap:**

```python
from plotlib import create_heatmap, save_plot
from models import PlotConfig
import numpy as np

# Data
data = np.random.randn(8, 10)

# Config
config = PlotConfig(
    title='Heatmap',
    tick_label_size=10
)

# Create
fig, ax = create_heatmap(data, config)
save_plot(fig, 'heatmap.png')
```

---

## 📊 ALL HEATMAP TYPES

### **1. Basic Heatmap**

```python
data = np.random.randn(8, 10)

fig, ax = create_heatmap(data, config)
```

**Use:** Visualize 2D data matrix

---

### **2. With Annotations**

```python
fig, ax = create_heatmap(
    data, config,
    annot=True,       # Show values
    fmt='.2f',        # Format: .2f, .1f, d (integer)
    annot_size=10
)
```

**Use:** Show exact values in cells

---

### **3. Correlation Matrix**

```python
from plotlib import create_correlation_heatmap

# Data: each column is a variable
data = np.random.randn(100, 5)
labels = ['Var1', 'Var2', 'Var3', 'Var4', 'Var5']

fig, ax = create_correlation_heatmap(
    data,
    labels=labels,
    config=config
)
```

**Use:** Show correlations between variables

---

### **4. Diverging Colormap**

```python
fig, ax = create_heatmap(
    data, config,
    cmap='RdBu_r',    # Red-Blue
    center=0,         # Center at zero
    annot=True
)
```

**Use:** Data centered around zero (deviations, changes)

---

### **5. With Grid Lines**

```python
fig, ax = create_heatmap(
    data, config,
    linewidths=0.5,   # Grid line width
    linecolor='white' # Grid line color
)
```

**Use:** Separate cells clearly

---

### **6. Square Cells**

```python
fig, ax = create_heatmap(
    data, config,
    square=True       # Equal aspect ratio
)
```

**Use:** Symmetric matrices (correlation, confusion)

---

## 📋 COMPLETE API

### **`create_heatmap()` Parameters:**

```python
create_heatmap(
    data,                          # 2D numpy array
    config=None,                   # PlotConfig
    row_labels=None,               # List of row labels
    col_labels=None,               # List of column labels
    cmap='viridis',                # Colormap name
    annot=False,                   # Show cell values
    fmt='.2f',                     # Value format string
    annot_size=10,                 # Annotation font size
    annot_color_threshold=None,    # Threshold for text color
    vmin=None,                     # Min value for colormap
    vmax=None,                     # Max value for colormap
    center=None,                   # Center for diverging cmap
    cbar=True,                     # Show color bar
    cbar_label=None,               # Color bar label
    square=False,                  # Square cells
    linewidths=0,                  # Grid line width
    linecolor='white'              # Grid line color
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

### **`create_correlation_heatmap()` Convenience Function:**

```python
create_correlation_heatmap(
    data,          # 2D array (samples × variables)
    labels=None,   # Variable names
    config=None,   # PlotConfig
    **kwargs       # Additional args → create_heatmap
)
```

Automatically:
- Calculates correlation matrix
- Uses diverging colormap (RdBu_r)
- Centers at 0
- Sets vmin=-1, vmax=1
- Shows annotations
- Makes square cells

---

## 🎨 COLORMAP REFERENCE

### **Sequential (One-directional):**

| Colormap | Use Case |
|----------|----------|
| `viridis` | General purpose (default) |
| `plasma` | High contrast |
| `Blues` | Single color gradient |
| `YlOrRd` | Yellow → Orange → Red |
| `Greens` | Green gradient |
| `Reds` | Red gradient |

### **Diverging (Two-directional):**

| Colormap | Use Case |
|----------|----------|
| `RdBu_r` | Red-Blue (reversed) |
| `coolwarm` | Cool-Warm |
| `seismic` | Blue-White-Red |
| `RdYlGn` | Red-Yellow-Green |

**Use diverging when:** Data represents deviations from center (0)

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Correlation Matrix**

```python
from plotlib import create_correlation_heatmap

# Generate correlated data
data = np.random.randn(100, 5)
data[:, 1] = data[:, 0] + np.random.randn(100) * 0.5  # Correlated

labels = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5']

config = PlotConfig(
    title='Feature Correlations',
    tick_label_size=10
)

fig, ax = create_correlation_heatmap(data, labels, config)
```

**Result:** Correlation matrix with diverging colormap, annotations, square cells

---

### **Example 2: Confusion Matrix**

```python
# Confusion matrix data (10 classes)
n = 10
data = np.random.randint(0, 50, (n, n))
# Emphasize diagonal (correct predictions)
for i in range(n):
    data[i, i] += 100

labels = [f'Class {i}' for i in range(n)]

config = PlotConfig(
    title='Confusion Matrix',
    x_label='Predicted',
    y_label='Actual',
    tick_label_size=9
)

fig, ax = create_heatmap(
    data, config,
    row_labels=labels,
    col_labels=labels,
    cmap='Blues',
    annot=True,
    fmt='d',              # Integer format
    annot_size=8,
    cbar_label='Count'
)
```

---

### **Example 3: Parameter Sweep**

```python
# Parameter sweep results
temps = np.arange(20, 100, 10)
pressures = np.arange(1, 6)
results = np.random.rand(len(pressures), len(temps)) * 100

config = PlotConfig(
    title='Yield vs Temperature and Pressure',
    tick_label_size=10
)

fig, ax = create_heatmap(
    results, config,
    row_labels=[f'{p} bar' for p in pressures],
    col_labels=[f'{t}°C' for t in temps],
    cmap='YlOrRd',
    annot=True,
    fmt='.1f',
    cbar_label='Yield (%)'
)
```

---

### **Example 4: Publication Style**

```python
# Clean, publication-ready
config = PlotConfig(
    title='Variable Correlations',
    title_weight='normal',
    tick_label_size=11
)

fig, ax = create_correlation_heatmap(
    data,
    labels=variable_names,
    config=config,
    linewidths=0.5,
    linecolor='gray'
)

save_plot(fig, 'figure1.png', dpi=300)
```

---

## 💡 DESIGN TIPS

### **Tip 1: Choose Right Colormap**

```python
# Sequential: one direction (more → less)
cmap='viridis'  # General

# Diverging: two directions from center
cmap='RdBu_r', center=0  # Deviations
```

### **Tip 2: Annotate Small Matrices**

```python
# Good for ≤10×10
annot=True

# Too crowded for >15×15
annot=False
```

### **Tip 3: Use Grid for Clarity**

```python
# Helps distinguish cells
linewidths=0.5,
linecolor='white'
```

### **Tip 4: Square Cells for Symmetric Data**

```python
# Correlation, similarity matrices
square=True
```

### **Tip 5: Format Annotations Appropriately**

```python
# Integers
fmt='d'

# One decimal
fmt='.1f'

# Two decimals
fmt='.2f'

# Scientific notation
fmt='.2e'
```

### **Tip 6: Hide Color Bar for Clean Look**

```python
# When annotations are present
cbar=False
```

---

## 📊 REALISTIC USE CASES

### **Research - Correlation Analysis:**

```python
# Analyze variable relationships
data = experimental_data  # n_samples × n_variables
labels = variable_names

config = PlotConfig(title='Variable Correlations')

fig, ax = create_correlation_heatmap(data, labels, config)
```

### **Machine Learning - Confusion Matrix:**

```python
from sklearn.metrics import confusion_matrix

# Classification results
cm = confusion_matrix(y_true, y_pred)

fig, ax = create_heatmap(
    cm, config,
    row_labels=class_names,
    col_labels=class_names,
    cmap='Blues',
    annot=True,
    fmt='d'
)
```

### **Experimental - Parameter Sweep:**

```python
# 2D parameter space
temps = [20, 30, 40, 50, 60]
pressures = [1, 2, 3, 4, 5]
yields = measure_yields(temps, pressures)  # 5×5 matrix

fig, ax = create_heatmap(
    yields, config,
    row_labels=[f'{p} bar' for p in pressures],
    col_labels=[f'{t}°C' for t in temps],
    cbar_label='Yield (%)'
)
```

### **Finance - Correlation Matrix:**

```python
# Stock returns correlation
returns = stock_data.pct_change()
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

fig, ax = create_correlation_heatmap(
    returns[tickers].values,
    labels=tickers,
    config=config
)
```

---

## ✅ COMPATIBILITY

All PlotConfig options work identically:
- Text formatting
- Title styling
- Tick labels
- Figure size

**Mix and match:**

```python
config = PlotConfig(
    title_weight='normal',
    tick_label_size=10,
    figure_width=10,
    figure_height=8
)

# Works for all plot types
fig, ax = create_line_plot(series, config)
fig, ax = create_box_plot(data, labels, config)
fig, ax = create_heatmap(data, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Basic:**
```python
fig, ax = create_heatmap(data, config)
```

### **With annotations:**
```python
fig, ax = create_heatmap(data, config, annot=True, fmt='.2f')
```

### **Correlation matrix:**
```python
fig, ax = create_correlation_heatmap(data, labels, config)
```

### **Custom colormap:**
```python
fig, ax = create_heatmap(data, config, cmap='plasma')
```

### **Diverging:**
```python
fig, ax = create_heatmap(data, config, cmap='RdBu_r', center=0)
```

### **With grid:**
```python
fig, ax = create_heatmap(data, config, linewidths=0.5)
```

### **Square cells:**
```python
fig, ax = create_heatmap(data, config, square=True)
```

### **No color bar:**
```python
fig, ax = create_heatmap(data, config, cbar=False)
```

---

## 📚 EXAMPLES

See `examples/heatmap_examples.py` for 10 complete working examples:

1. **Basic** - Simple heatmap
2. **Annotations** - Values in cells
3. **Correlation** - Correlation matrix
4. **Custom colormap** - Plasma
5. **Diverging** - Red-Blue centered
6. **Grid** - With grid lines
7. **Square** - Square cells
8. **No color bar** - Cleaner look
9. **Large** - 10×10 confusion matrix
10. **Publication** - Clean styling

**Run them:**

```powershell
cd examples
python heatmap_examples.py
```

**Creates 10 PNG files demonstrating all features!**

---

## 📈 WHEN TO USE HEATMAPS

| Use Case | Heatmap | Alternative |
|----------|---------|-------------|
| Correlation matrices | ✅ Perfect | Scatter matrix |
| Confusion matrices | ✅ Perfect | Bar chart |
| Parameter sweeps | ✅ Perfect | 3D surface |
| Data matrices | ✅ Perfect | Table |
| Pattern visualization | ✅ Perfect | Contour |

---

## 🎓 INTERPRETATION GUIDE

### **Sequential Colormaps:**
- **Darker/brighter** → Higher/lower values
- **One direction** → Magnitude only

### **Diverging Colormaps:**
- **Red** → Positive (above center)
- **Blue** → Negative (below center)
- **White** → Near center (neutral)

### **Correlation Matrices:**
- **+1** → Perfect positive correlation
- **0** → No correlation
- **-1** → Perfect negative correlation
- **Diagonal** → Always 1 (self-correlation)

### **Confusion Matrices:**
- **Diagonal** → Correct predictions
- **Off-diagonal** → Errors
- **Bright diagonal** → Good model
- **Bright off-diagonal** → Confusion between classes

---

**Heatmaps with comprehensive customization are complete!** 🔥

**Phase 2 Progress:** 2 of 6 (33%)  
**Next: Subplots, Violin plots, Contour, or 3D?** 🚀
