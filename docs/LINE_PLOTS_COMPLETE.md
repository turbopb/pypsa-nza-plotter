# Line & Scatter Plots - PlotLib v2.0 📈

## ✅ COMPLETE LINE PLOT GUIDE

Line and scatter plot support with **comprehensive customization** including multiple series, line styles, markers, and publication-ready formatting.

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Line Styling:**
- ✅ **Line styles** - `-`, `--`, `:`, `-.`
- ✅ **Line widths** - Any thickness (0.5 to 4.0+)
- ✅ **Line colors** - Any color code

### **Markers:**
- ✅ **Marker types** - `o`, `s`, `^`, `D`, `*`, `+`, `x`, etc.
- ✅ **Marker sizes** - Any size
- ✅ **Pure scatter** - Markers only (no lines)
- ✅ **Line + markers** - Combined

### **Multiple Series:**
- ✅ **Overlay** - Multiple lines on same plot
- ✅ **Auto legend** - Automatic legend generation
- ✅ **Per-series styling** - Independent colors/styles

---

## 📝 QUICK START

### **Basic Line Plot:**

```python
from plotlib import create_line_plot, save_plot
from models import SeriesConfig, PlotConfig
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Series
series = SeriesConfig(
    x=x,
    y=y,
    line_style='-',
    line_width=2.0,
    color='#0066CC',
    label='sin(x)'
)

# Config
config = PlotConfig(
    title='Basic Line Plot',
    x_label='x',
    y_label='y',
    show_grid=True
)

# Create
fig, ax = create_line_plot(series, config)
save_plot(fig, 'line.png')
```

---

## 📊 ALL LINE PLOT TYPES

### **1. Basic Line Plot**

```python
series = SeriesConfig(
    x=x, y=y,
    line_style='-',
    line_width=2.0,
    color='#0066CC'
)

fig, ax = create_line_plot(series, config)
```

**Use:** Single data series, trends

---

### **2. Multiple Series**

```python
series1 = SeriesConfig(x=x, y=y1, color='#0066CC', label='Series 1')
series2 = SeriesConfig(x=x, y=y2, color='#CC6666', label='Series 2')
series3 = SeriesConfig(x=x, y=y3, color='#00CC66', label='Series 3')

fig, ax = create_line_plot([series1, series2, series3], config)
```

**Use:** Compare multiple datasets

---

### **3. Scatter Plot (Markers Only)**

```python
series = SeriesConfig(
    x=x, y=y,
    line_style='',      # No line!
    marker='o',
    marker_size=6,
    color='#0066CC'
)

fig, ax = create_line_plot(series, config)
```

**Use:** Data points without trends

---

### **4. Line with Markers**

```python
series = SeriesConfig(
    x=x, y=y,
    line_style='-',     # Line
    marker='o',         # + markers
    marker_size=6,
    line_width=2.0,
    color='#0066CC'
)

fig, ax = create_line_plot(series, config)
```

**Use:** Emphasize data points on trend

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Line Styles**

```python
# Solid line
series1 = SeriesConfig(x=x, y=y1, line_style='-', label='Solid')

# Dashed line
series2 = SeriesConfig(x=x, y=y2, line_style='--', label='Dashed')

# Dotted line
series3 = SeriesConfig(x=x, y=y3, line_style=':', label='Dotted')

# Dash-dot line
series4 = SeriesConfig(x=x, y=y4, line_style='-.', label='Dash-dot')

fig, ax = create_line_plot([series1, series2, series3, series4], config)
```

**Available styles:** `-`, `--`, `:`, `-.`

---

### **Example 2: Line Widths**

```python
# Very thin
series1 = SeriesConfig(x=x, y=y1, line_width=0.5, label='Width 0.5')

# Thin
series2 = SeriesConfig(x=x, y=y2, line_width=1.0, label='Width 1.0')

# Medium
series3 = SeriesConfig(x=x, y=y3, line_width=2.0, label='Width 2.0')

# Thick
series4 = SeriesConfig(x=x, y=y4, line_width=4.0, label='Width 4.0')

fig, ax = create_line_plot([series1, series2, series3, series4], config)
```

**Range:** 0.5 to 4.0+ (any value)

---

### **Example 3: Marker Styles**

```python
# Circle markers
series1 = SeriesConfig(x=x, y=y1, marker='o', label='Circle')

# Square markers
series2 = SeriesConfig(x=x, y=y2, marker='s', label='Square')

# Triangle markers
series3 = SeriesConfig(x=x, y=y3, marker='^', label='Triangle')

# Diamond markers
series4 = SeriesConfig(x=x, y=y4, marker='D', label='Diamond')

# Star markers
series5 = SeriesConfig(x=x, y=y5, marker='*', label='Star')

fig, ax = create_line_plot([series1, series2, series3, series4, series5], config)
```

**Available markers:** `o`, `s`, `^`, `v`, `<`, `>`, `D`, `*`, `+`, `x`, `p`, `h`

---

### **Example 4: Custom Colors**

```python
series1 = SeriesConfig(x=x, y=y1, color='#FF6B6B', label='Red')
series2 = SeriesConfig(x=x, y=y2, color='#4ECDC4', label='Teal')
series3 = SeriesConfig(x=x, y=y3, color='#FFE66D', label='Yellow')

fig, ax = create_line_plot([series1, series2, series3], config)
```

**Any color:** Hex codes, named colors, RGB tuples

---

### **Example 5: Publication-Ready**

```python
# Black lines with different styles
series_data = SeriesConfig(
    x=t, y=data,
    line_style='-',
    line_width=2.0,
    color='#000000',      # Black
    label='Data'
)

series_model = SeriesConfig(
    x=t, y=model,
    line_style='--',
    line_width=2.0,
    color='#000000',
    label='Model'
)

config = PlotConfig(
    title='Experimental Results',
    title_weight='normal',  # Not bold
    x_label='Time (s)',
    y_label='Amplitude (mV)',
    show_grid=True,
    grid_alpha=0.3,
    show_top_spine=False,
    show_right_spine=False
)

fig, ax = create_line_plot([series_data, series_model], config)
save_plot(fig, 'figure1.png', dpi=300)  # High DPI
```

---

## 📋 COMPLETE API

### **`create_line_plot()` Parameters:**

```python
create_line_plot(
    series,    # SeriesConfig or list of SeriesConfig
    config     # PlotConfig
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

### **SeriesConfig for Line Plots:**

```python
SeriesConfig(
    x=x_data,              # X coordinates (required)
    y=y_data,              # Y coordinates (required)
    
    # Line properties
    line_style='-',        # '-', '--', ':', '-.'
    line_width=2.0,        # Line thickness
    color='#0066CC',       # Line color
    
    # Marker properties (optional)
    marker='o',            # Marker type
    marker_size=6,         # Marker size
    
    label='Series Name'    # Legend label
)
```

---

## 🎯 LINE STYLES

| Style | Description | Code |
|-------|-------------|------|
| Solid | Continuous line | `'-'` |
| Dashed | Dashed line | `'--'` |
| Dotted | Dotted line | `':'` |
| Dash-dot | Alternating dashes and dots | `'-.'` |
| None | No line (scatter only) | `''` |

---

## 🎯 MARKER STYLES

| Marker | Description | Code |
|--------|-------------|------|
| Circle | Filled circle | `'o'` |
| Square | Filled square | `'s'` |
| Triangle up | Upward triangle | `'^'` |
| Triangle down | Downward triangle | `'v'` |
| Diamond | Filled diamond | `'D'` |
| Star | Star shape | `'*'` |
| Plus | Plus sign | `'+'` |
| X | X mark | `'x'` |
| Pentagon | Pentagon | `'p'` |
| Hexagon | Hexagon | `'h'` |

---

## 💡 DESIGN TIPS

### **Tip 1: Multiple Series - Use Different Styles**

```python
# Combine colors AND styles for clarity
series1 = SeriesConfig(x=x, y=y1, line_style='-', color='#0066CC')
series2 = SeriesConfig(x=x, y=y2, line_style='--', color='#CC6666')
series3 = SeriesConfig(x=x, y=y3, line_style=':', color='#00CC66')
```

### **Tip 2: Scatter - Remove Line**

```python
# Set line_style to empty string for pure scatter
series = SeriesConfig(x=x, y=y, line_style='', marker='o')
```

### **Tip 3: Emphasize Data - Use Markers**

```python
# Combine line and markers
series = SeriesConfig(
    x=x, y=y,
    line_style='-',
    marker='o',
    marker_size=6
)
```

### **Tip 4: Publication - Keep It Simple**

```python
# Black/gray, solid/dashed, clean
config = PlotConfig(
    title_weight='normal',
    show_top_spine=False,
    show_right_spine=False
)
```

### **Tip 5: Limit Series Count**

- **Good:** 3-5 series
- **Max:** 7 series
- **Too many?** Use multiple subplots

---

## 📊 REALISTIC USE CASES

### **Time-Series Analysis:**

```python
# Stock prices, sensor data, etc.
series = SeriesConfig(
    x=timestamps,
    y=values,
    line_style='-',
    line_width=1.5,
    color='#0066CC',
    label='Power (MW)'
)
```

### **Scientific Data:**

```python
# Experimental results with model fit
series_data = SeriesConfig(x=x, y=data, line_style='', marker='o', label='Data')
series_fit = SeriesConfig(x=x, y=fit, line_style='-', label='Fit')
```

### **Comparison:**

```python
# Compare scenarios
series_baseline = SeriesConfig(x=x, y=baseline, line_style='-', label='Baseline')
series_optimized = SeriesConfig(x=x, y=optimized, line_style='--', label='Optimized')
```

---

## ✅ COMPATIBILITY

All PlotConfig options work identically:
- Text formatting (titles, labels)
- Grid settings
- Legend settings
- Spine visibility

**Mix and match:**

```python
config = PlotConfig(
    title_weight='normal',
    show_grid=True,
    grid_alpha=0.3
)

# Works for all plot types!
fig, ax = create_line_plot(series, config)
fig, ax = create_bar_plot(series, config)
fig, ax = create_area_plot(series, config)
```

---

## 🎯 QUICK REFERENCE

### **Basic line:**
```python
series = SeriesConfig(x=x, y=y, line_style='-', line_width=2.0)
fig, ax = create_line_plot(series, config)
```

### **Multiple series:**
```python
fig, ax = create_line_plot([s1, s2, s3], config)
```

### **Scatter only:**
```python
series = SeriesConfig(x=x, y=y, line_style='', marker='o')
fig, ax = create_line_plot(series, config)
```

### **Line with markers:**
```python
series = SeriesConfig(x=x, y=y, line_style='-', marker='o')
fig, ax = create_line_plot(series, config)
```

### **Custom style:**
```python
series = SeriesConfig(x=x, y=y, line_style='--', line_width=3.0, color='#FF6B6B')
fig, ax = create_line_plot(series, config)
```

---

## 📚 EXAMPLES

See `examples/line_examples.py` for 10 complete working examples:

1. **Basic line** - Single series
2. **Multiple series** - Three trigonometric functions
3. **Line styles** - Solid, dashed, dotted, dash-dot
4. **Line widths** - 0.5 to 4.0
5. **Scatter plot** - Markers only
6. **Line with markers** - Combined
7. **Custom styling** - Custom colors and thick lines
8. **Publication-ready** - Scientific format
9. **Marker styles** - Five different markers
10. **Exponential** - Growth and decay

**Run them:**

```powershell
cd examples
python line_examples.py
```

**Creates 10 PNG files demonstrating all features!**

---

## 📈 PLOT TYPE COMPARISON

| Feature | Line Plot | Other Types |
|---------|-----------|-------------|
| Continuous data | ✅ Perfect | ❌ |
| Trends | ✅ Excellent | ⚠️ |
| Comparisons | ✅ Multiple series | ✅ |
| Categories | ❌ | ✅ Bar/Pie |
| Distributions | ❌ | ✅ Histogram |

---

**Line and scatter plots with comprehensive customization are complete!** 📈

**Total examples now: 56 (46 + 10 new line examples)!** 🎉
