# Bar Charts - PlotLib v2.0 📊

## ✅ BAR CHARTS COMPLETE!

Bar chart support has been added to PlotLib v2.0 with full feature parity to line plots.

---

## 🎯 WHAT'S INCLUDED

### **Bar Chart Types:**
- ✅ **Single series** - Basic vertical bars
- ✅ **Grouped bars** - Multiple series side-by-side
- ✅ **Stacked bars** - Multiple series stacked on top
- ✅ **Horizontal bars** - Flipped orientation

### **Features:**
- ✅ Uses SeriesConfig and PlotConfig (same as line plots)
- ✅ Returns (fig, ax) for composability
- ✅ Full formatting control
- ✅ YAML-compatible
- ✅ Customizable bar width

---

## 📝 QUICK START

### **Single Series:**

```python
from plotlib import create_bar_plot, save_plot
from models import SeriesConfig, PlotConfig

# Data
categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [120, 145, 135, 160]

# Series
series = SeriesConfig(
    x=categories,
    y=values,
    color='#0066CC',
    label='Sales'
)

# Config
config = PlotConfig(
    title='Quarterly Sales',
    x_label='Quarter',
    y_label='Sales ($ millions)'
)

# Create plot
fig, ax = create_bar_plot(series, config)
save_plot(fig, 'sales.png', dpi=300)
```

---

## 📊 ALL BAR CHART TYPES

### **1. Single Series (Default)**

```python
fig, ax = create_bar_plot(series, config)
```

**Output:** Vertical bars, one series

---

### **2. Grouped Bars**

```python
series1 = SeriesConfig(x=categories, y=values1, label='2023', color='#CC6666')
series2 = SeriesConfig(x=categories, y=values2, label='2024', color='#0066CC')

fig, ax = create_bar_plot([series1, series2], config, grouped=True)
```

**Output:** Bars side-by-side for comparison

---

### **3. Stacked Bars**

```python
series1 = SeriesConfig(x=months, y=hydro, label='Hydro', color='#0066CC')
series2 = SeriesConfig(x=months, y=gas, label='Gas', color='#CC6666')
series3 = SeriesConfig(x=months, y=wind, label='Wind', color='#00CC66')

fig, ax = create_bar_plot([series1, series2, series3], config, stacked=True)
```

**Output:** Bars stacked on top of each other (cumulative)

---

### **4. Horizontal Bars**

```python
fig, ax = create_bar_plot(series, config, orientation='horizontal')
```

**Output:** Bars oriented horizontally (categories on y-axis)

---

## 🎨 CUSTOMIZATION

### **Bar Width:**

```python
# Default width (0.8)
fig, ax = create_bar_plot(series, config)

# Narrow bars (0.5)
fig, ax = create_bar_plot(series, config, bar_width=0.5)

# Wide bars (0.95)
fig, ax = create_bar_plot(series, config, bar_width=0.95)
```

**Value range:** 0.0 to 1.0 (fraction of space)

---

### **Bar Colors:**

```python
# Single color
series = SeriesConfig(x=cats, y=vals, color='#0066CC')

# Multiple colors (one per series)
series1 = SeriesConfig(x=cats, y=vals1, color='#0066CC')
series2 = SeriesConfig(x=cats, y=vals2, color='#CC6666')
series3 = SeriesConfig(x=cats, y=vals3, color='#00CC66')
```

---

### **Bar Edges:**

```python
series = SeriesConfig(
    x=categories,
    y=values,
    color='#0066CC',
    marker_edge_color='black',  # Edge color
    marker_edge_width=1.5       # Edge width
)
```

---

## 📋 COMPLETE API

### **`create_bar_plot()` Parameters:**

```python
create_bar_plot(
    series,              # SeriesConfig or list of SeriesConfig
    config,              # PlotConfig
    grouped=False,       # True = bars side-by-side
    stacked=False,       # True = bars stacked
    orientation='vertical',  # 'vertical' or 'horizontal'
    bar_width=0.8        # 0.0-1.0, fraction of space
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

## 🎯 DESIGN DECISIONS

### **Why SeriesConfig for bar charts?**

**Consistency!** Same config pattern across all plot types:
- Line plots use SeriesConfig
- Bar charts use SeriesConfig
- Histograms will use SeriesConfig
- etc.

**Benefits:**
- Learn once, use everywhere
- Easy to switch between plot types
- YAML configs work for all

### **Why separate `grouped` and `stacked` parameters?**

**Clarity!** One clear way to specify behavior:
- Nothing specified = single series
- `grouped=True` = side-by-side
- `stacked=True` = on top of each other
- Can't be both (validation prevents)

### **Why `bar_width` instead of individual widths?**

**Simplicity!** For grouped bars, library calculates individual widths automatically:
- `bar_width=0.8` with 2 series → each bar is 0.4 wide
- `bar_width=0.8` with 3 series → each bar is 0.267 wide
- Automatic spacing, no manual calculation

---

## 📊 EXAMPLES

See `examples/bar_examples.py` for 6 complete working examples:

1. **Single series** - Quarterly sales
2. **Grouped bars** - 2023 vs 2024 comparison
3. **Stacked bars** - Generation mix by source
4. **Horizontal bars** - Station capacity ranking
5. **Custom styling** - Current vs planned capacity
6. **Narrow bars** - Weekly load profile

**Run them:**

```powershell
cd examples
python bar_examples.py
```

**Creates 6 PNG files demonstrating all features!**

---

## ✅ COMPATIBILITY

### **Same PlotConfig as Line Plots:**

All PlotConfig options work identically:
- Text formatting (title, labels, ticks)
- Grid settings
- Legend settings
- Spine visibility
- Figure dimensions

**Mix and match:**

```python
config = PlotConfig(
    title_weight='normal',      # Extended feature
    tick_label_color='#666666', # Extended feature
    show_grid=True,
    grid_alpha=0.3
)

# Works for both:
fig, ax = create_line_plot(series, config)
fig, ax = create_bar_plot(series, config)
```

---

## 🚀 NEXT STEPS

**Completed:**
- ✅ Line/scatter plots
- ✅ Time-series utilities
- ✅ Bar charts (single, grouped, stacked, horizontal)

**Coming next:**
- 📈 Histograms (frequency distributions)
- 📉 Area plots (filled line plots, stacked areas)
- 🥧 Pie charts (simple pie/donut)

---

## 💡 USAGE TIPS

### **Tip 1: Keep category names short**

```python
# Good:
categories = ['Q1', 'Q2', 'Q3', 'Q4']

# May overlap:
categories = ['First Quarter', 'Second Quarter', ...]

# Solution for long names: Use horizontal bars
fig, ax = create_bar_plot(series, config, orientation='horizontal')
```

### **Tip 2: Limit grouped series**

**Best:** 2-3 series  
**OK:** 4 series  
**Crowded:** 5+ series

**Alternative:** Use stacked bars or separate plots

### **Tip 3: Order matters for stacking**

```python
# Series drawn in order provided:
fig, ax = create_bar_plot([series1, series2, series3], config, stacked=True)
```

**Output:** series1 on bottom, series2 in middle, series3 on top

**Tip:** Put most important series first (bottom of stack)

### **Tip 4: Use consistent colors**

```python
# Define color palette:
HYDRO_COLOR = '#0066CC'
GAS_COLOR = '#CC6666'
WIND_COLOR = '#00CC66'

# Use consistently across plots:
series_hydro = SeriesConfig(..., color=HYDRO_COLOR)
series_gas = SeriesConfig(..., color=GAS_COLOR)
```

---

## 🎨 COLOR PALETTES

### **For NZ generation mix:**

```python
COLORS = {
    'hydro': '#0066CC',      # Blue
    'gas': '#CC6666',        # Red
    'geothermal': '#CC9900', # Orange/gold
    'wind': '#00CC66',       # Green
    'solar': '#FFCC00',      # Yellow
    'coal': '#666666'        # Gray
}
```

### **For comparisons:**

```python
COLORS = {
    'current': '#666666',    # Gray (existing)
    'planned': '#00CC66',    # Green (future)
    'target': '#0066CC'      # Blue (goal)
}
```

---

**Bar charts are now production-ready!** 📊

**Next up: Histograms!** 📈
