# Area Plots - PlotLib v2.0 📉

## ✅ AREA PLOTS WITH FULL CUSTOMIZATION!

Area plot support has been added with **comprehensive formatting options** including cross-hatching, line styles, colors, edges, and more!

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Fill Customization:**
- ✅ **Fill color** - Any color
- ✅ **Cross-hatching** - `/`, `\`, `|`, `-`, `+`, `x`, `o`, `.`, `*`
- ✅ **Hatch density** - `/`, `//`, `///`
- ✅ **Transparency** - `alpha=0.0` to `1.0`
- ✅ **Edge color** - Border color
- ✅ **Edge width** - Border thickness

### **Line Customization:**
- ✅ **Line on/off** - `show_line=True/False`
- ✅ **Line style** - `-`, `--`, `:`, `-.`
- ✅ **Line width** - Any thickness
- ✅ **Line color** - Separate from fill

### **Plot Types:**
- ✅ **Single area** - Fill under curve
- ✅ **Stacked areas** - Multiple layers
- ✅ **Fill between** - Between two curves
- ✅ **Overlapping areas** - Multiple transparent areas

---

## 📝 QUICK START

### **Single Area (Basic):**

```python
from plotlib import create_area_plot, save_plot
from models import SeriesConfig, PlotConfig
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x) + 2

# Series
series = SeriesConfig(
    x=x,
    y=y,
    color='#0066CC',
    label='Solar'
)

# Config
config = PlotConfig(
    title='Solar Generation',
    x_label='Hour',
    y_label='Power (MW)'
)

# Create area plot
fig, ax = create_area_plot(series, config, alpha=0.6)
save_plot(fig, 'area.png')
```

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Area with Cross-Hatching**

```python
series = SeriesConfig(
    x=x,
    y=y,
    color='#00CC66',
    hatch='///',               # ← Cross-hatch pattern!
    marker_edgecolor='black',  # ← Edge color
    marker_edgewidth=0.5,      # ← Edge width
    label='Wind'
)

fig, ax = create_area_plot(series, config, alpha=0.7)
```

**Output:** Green area with diagonal hatching and black edges

---

### **Example 2: Custom Line on Top**

```python
series = SeriesConfig(
    x=x,
    y=y,
    color='#CC6666',
    line_style='-',      # ← Solid line
    line_width=3.0,      # ← Thick line!
    label='Hydro'
)

fig, ax = create_area_plot(series, config, 
                           alpha=0.4,        # Light fill
                           show_line=True)   # Line on top
```

**Output:** Light red fill with thick red line on top

---

### **Example 3: Stacked Areas with Patterns**

```python
series_hydro = SeriesConfig(
    x=x, y=hydro,
    color='#0066CC',
    hatch='',                  # Solid
    label='Hydro'
)

series_wind = SeriesConfig(
    x=x, y=wind,
    color='#00CC66',
    hatch='///',               # Diagonal
    marker_edgecolor='black',
    marker_edgewidth=0.5,
    label='Wind'
)

series_solar = SeriesConfig(
    x=x, y=solar,
    color='#FFCC00',
    hatch='xxx',               # X pattern
    marker_edgecolor='black',
    marker_edgewidth=0.5,
    label='Solar'
)

fig, ax = create_area_plot(
    [series_hydro, series_wind, series_solar],
    config,
    stacked=True,
    alpha=0.8
)
```

**Output:** Three stacked layers with different hatch patterns

---

### **Example 4: Fill Between with Hatching**

```python
series_upper = SeriesConfig(
    x=x, y=y_upper,
    color='#0066CC',
    hatch='///',
    line_style='-',
    line_width=1.5,
    marker_edgecolor='black',
    marker_edgewidth=0.5,
    label='Upper Bound'
)

series_lower = SeriesConfig(
    x=x, y=y_lower,
    line_style='-',
    line_width=1.5,
    label='Lower Bound'
)

fig, ax = create_area_plot(
    [series_upper, series_lower],
    config,
    fill_between=True,
    alpha=0.5,
    show_line=True
)
```

**Output:** Hatched band between two curves

---

### **Example 5: Publication Black & White**

```python
series1 = SeriesConfig(
    x=x, y=y1,
    color='white',            # ← White fill
    hatch='///',              # ← Diagonal pattern
    line_style='-',
    line_width=2.0,
    marker_edgecolor='black',
    marker_edgewidth=1.0,
    label='Peak'
)

series2 = SeriesConfig(
    x=x, y=y2,
    color='white',            # ← White fill
    hatch='|||',              # ← Vertical pattern
    line_style='--',
    line_width=2.0,
    marker_edgecolor='black',
    marker_edgewidth=1.0,
    label='Base'
)

fig, ax = create_area_plot([series1, series2], config, 
                           alpha=0.9, show_line=True)
```

**Output:** B&W publication-ready with distinct patterns

---

### **Example 6: Fill Only (No Line)**

```python
series = SeriesConfig(
    x=x, y=y,
    color='#9966CC',
    hatch='...',
    marker_edgecolor='black',
    marker_edgewidth=0.5
)

fig, ax = create_area_plot(series, config, 
                           alpha=0.7,
                           show_line=False)   # ← No line!
```

**Output:** Just the filled area, no line on top

---

## 📋 COMPLETE API

### **`create_area_plot()` Parameters:**

```python
create_area_plot(
    series,              # SeriesConfig or list of SeriesConfig
    config,              # PlotConfig
    stacked=False,       # True = stack areas
    fill_between=False,  # True = fill between two curves
    baseline=0.0,        # Y-value for baseline
    alpha=0.7,           # Fill transparency (0.0-1.0)
    show_line=True       # True = draw line on top
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

### **SeriesConfig for Area Plots:**

```python
SeriesConfig(
    x=x_data,                  # X coordinates (required)
    y=y_data,                  # Y coordinates (required)
    
    # Fill properties
    color='#0066CC',           # Fill color
    hatch='///',               # Cross-hatch pattern
    marker_edgecolor='black',  # Edge/border color
    marker_edgewidth=0.5,      # Edge/border width
    
    # Line properties (if show_line=True)
    line_style='-',            # '-', '--', ':', '-.'
    line_width=2.0,            # Line thickness
    
    label='Series Name'        # Legend label
)
```

---

## 🎨 HATCH PATTERNS

Same as bar charts and histograms:

| Pattern | Description | Example Use |
|---------|-------------|-------------|
| `''` or `None` | No pattern (solid) | Default |
| `'/'` | Diagonal lines | Light |
| `'\\'` | Diagonal (other way) | Alternative |
| `'|'` | Vertical lines | Strong vertical |
| `'-'` | Horizontal lines | Strong horizontal |
| `'+'` | Crossed lines | Grid |
| `'x'` | X pattern | Diagonal cross |
| `'o'` | Small circles | Dotted |
| `'.'` | Dots | Fine texture |
| `'*'` | Stars | Star texture |
| `'//'`, `'///'` | Denser patterns | Increase density |

---

## 📊 PLOT TYPES

### **1. Single Area (Fill Under Curve)**

```python
fig, ax = create_area_plot(series, config)
```

**Use:** Simple area fill below a line

---

### **2. Stacked Areas**

```python
fig, ax = create_area_plot(
    [series1, series2, series3],
    config,
    stacked=True
)
```

**Use:** Show composition, cumulative totals

---

### **3. Fill Between Two Curves**

```python
fig, ax = create_area_plot(
    [series_upper, series_lower],
    config,
    fill_between=True
)
```

**Use:** Confidence intervals, bounds, ranges

---

### **4. Overlapping Areas**

```python
fig, ax = create_area_plot(
    [series1, series2, series3],
    config,
    alpha=0.4  # Use transparency!
)
```

**Use:** Compare multiple scenarios

---

## 💡 DESIGN TIPS

### **Tip 1: Use Transparency for Overlapping**

```python
# Multiple overlapping areas
alpha=0.4  # More transparent for better visibility
```

### **Tip 2: Cross-Hatching for B&W**

```python
# Publication-ready black & white
series1 = SeriesConfig(..., color='white', hatch='///')
series2 = SeriesConfig(..., color='white', hatch='|||')
```

### **Tip 3: Line on Top for Clarity**

```python
# Show boundary clearly
fig, ax = create_area_plot(series, config, 
                           alpha=0.5,      # Light fill
                           show_line=True)  # Clear line
```

### **Tip 4: Stacked for Composition**

```python
# Show how parts make up whole
fig, ax = create_area_plot([s1, s2, s3], config, stacked=True)
```

### **Tip 5: Combine Color + Pattern**

```python
# Accessible to colorblind users
series = SeriesConfig(
    ...,
    color='#0066CC',   # Color
    hatch='///'        # + Pattern
)
```

---

## 📊 REALISTIC USE CASES

### **Power Generation Mix:**

```python
# Show generation sources stacked
series_hydro = SeriesConfig(x=hours, y=hydro, color='#0066CC', label='Hydro')
series_wind = SeriesConfig(x=hours, y=wind, color='#00CC66', hatch='///', label='Wind')
series_solar = SeriesConfig(x=hours, y=solar, color='#FFCC00', hatch='xxx', label='Solar')

fig, ax = create_area_plot([series_hydro, series_wind, series_solar], 
                           config, stacked=True)
```

### **Confidence Interval:**

```python
# Show forecast uncertainty
series_upper = SeriesConfig(x=time, y=forecast_upper, hatch='///')
series_lower = SeriesConfig(x=time, y=forecast_lower)

fig, ax = create_area_plot([series_upper, series_lower], 
                           config, fill_between=True, alpha=0.5)
```

### **Load Duration Curve:**

```python
# Show demand over time
series = SeriesConfig(x=hours, y=demand, color='#CC6666')
fig, ax = create_area_plot(series, config, alpha=0.6)
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
fig, ax = create_histogram(series, config, bins=20)
fig, ax = create_area_plot(series, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Basic area:**
```python
series = SeriesConfig(x=x, y=y, color='#0066CC')
fig, ax = create_area_plot(series, config)
```

### **With hatching:**
```python
series = SeriesConfig(x=x, y=y, hatch='///', marker_edgecolor='black')
fig, ax = create_area_plot(series, config, alpha=0.7)
```

### **With line:**
```python
series = SeriesConfig(x=x, y=y, line_width=3.0)
fig, ax = create_area_plot(series, config, show_line=True)
```

### **Stacked:**
```python
fig, ax = create_area_plot([s1, s2, s3], config, stacked=True)
```

### **Fill between:**
```python
fig, ax = create_area_plot([s_upper, s_lower], config, fill_between=True)
```

### **No line:**
```python
fig, ax = create_area_plot(series, config, show_line=False)
```

---

## 📚 EXAMPLES

See `examples/area_examples.py` for 8 complete working examples:

1. **Basic area** - Simple fill
2. **Cross-hatching** - Hatch patterns
3. **Custom line** - Thick line on top
4. **Stacked with patterns** - Three layers
5. **Fill between** - Confidence band
6. **Overlapping** - Multiple areas
7. **Publication B&W** - Black & white
8. **Fill only** - No line

**Run them:**

```powershell
cd examples
python area_examples.py
```

**Creates 8 PNG files demonstrating all features!**

---

**Area plots with comprehensive customization are production-ready!** 📉

**Next: Pie charts!** 🥧
