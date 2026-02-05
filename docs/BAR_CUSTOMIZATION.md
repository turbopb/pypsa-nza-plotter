# Bar Chart Customization Guide 🎨

## Complete Guide to Customizing Bar Charts

---

## **🔧 1. CROSS-HATCHING (HATCH PATTERNS)**

### **What is Hatching?**

Hatching adds patterns to bars - useful for:
- Black & white printing
- Distinguishing series without color
- Academic publications
- Emphasizing certain data

### **How to Use:**

**In SeriesConfig:**

```python
series = SeriesConfig(
    x=categories,
    y=values,
    color='#0066CC',
    hatch='///',              # ← Add hatch pattern here!
    marker_edgecolor='black', # Recommended with hatching
    marker_edgewidth=1.0
)
```

### **Available Patterns:**

| Pattern | Description | Example Use |
|---------|-------------|-------------|
| `''` or `None` | No pattern (solid) | Default |
| `'/'` | Diagonal lines (/) | Light distinction |
| `'\\'` | Diagonal lines (\) | Alternative diagonal |
| `'|'` | Vertical lines | Strong vertical |
| `'-'` | Horizontal lines | Strong horizontal |
| `'+'` | Crossed lines | Grid pattern |
| `'x'` | X pattern | Diagonal cross |
| `'o'` | Small circles | Dotted texture |
| `'O'` | Large circles | Bubble texture |
| `'.'` | Dots | Fine texture |
| `'*'` | Stars | Star texture |

### **Combining Patterns:**

You can combine patterns by repeating characters:

```python
hatch='//'      # Double diagonal
hatch='///'     # Triple diagonal (denser)
hatch='|||'     # Triple vertical
hatch='xxx'     # Dense X pattern
hatch='...'     # Dense dots
```

Mix patterns:
```python
hatch='/o'      # Diagonal lines with circles
hatch='\\|'     # Backslash with vertical
```

### **Example - Grouped Bars with Hatching:**

```python
# Series 1: Solid (no hatch)
series1 = SeriesConfig(
    x=['Q1', 'Q2', 'Q3'],
    y=[100, 120, 110],
    color='#0066CC',
    hatch=None,              # Solid
    label='Actual'
)

# Series 2: Hatched
series2 = SeriesConfig(
    x=['Q1', 'Q2', 'Q3'],
    y=[95, 115, 105],
    color='#CC6666',
    hatch='///',             # Diagonal pattern
    marker_edgecolor='black',
    marker_edgewidth=1.0,
    label='Target'
)

fig, ax = create_bar_plot([series1, series2], config, grouped=True)
```

---

## **📏 2. BAR WIDTH CONTROL**

### **Global Bar Width:**

Control spacing between bars with `bar_width` parameter:

```python
fig, ax = create_bar_plot(series, config, bar_width=0.8)
```

**Value range:** 0.0 to 1.0 (fraction of available space)

### **Width Guidelines:**

| Width | Spacing | Use Case |
|-------|---------|----------|
| `0.95` | Minimal | Emphasize continuity |
| `0.8` | Normal (default) | Standard charts |
| `0.6` | Moderate | Clear separation |
| `0.4` | Wide | Emphasize individual bars |
| `0.2` | Very wide | Sparse data |

### **Examples:**

**Wide bars (minimal spacing):**
```python
fig, ax = create_bar_plot(series, config, bar_width=0.95)
```

**Narrow bars (more spacing):**
```python
fig, ax = create_bar_plot(series, config, bar_width=0.4)
```

### **For Grouped Bars:**

The `bar_width` is **divided** among series:

```python
# 2 series, bar_width=0.8
# Each bar gets: 0.8 / 2 = 0.4 width
fig, ax = create_bar_plot([series1, series2], config, 
                          grouped=True, bar_width=0.8)

# 3 series, bar_width=0.9
# Each bar gets: 0.9 / 3 = 0.3 width
fig, ax = create_bar_plot([series1, series2, series3], config,
                          grouped=True, bar_width=0.9)
```

**Recommendation:** For grouped bars with 3+ series, use `bar_width=0.9` to minimize gaps.

---

## **🎨 3. EDGE COLORS AND WIDTHS**

### **Bar Edges:**

Control the outline of each bar:

```python
series = SeriesConfig(
    x=categories,
    y=values,
    color='#0066CC',          # Fill color
    marker_edgecolor='black', # ← Edge color
    marker_edgewidth=1.5      # ← Edge width
)
```

### **Edge Color Options:**

```python
marker_edgecolor='black'     # Black outline (crisp)
marker_edgecolor='#333333'   # Dark gray outline
marker_edgecolor='white'     # White outline (for dark backgrounds)
marker_edgecolor=None        # No edge (uses fill color)
```

### **Edge Width Guidelines:**

| Width | Appearance | Use Case |
|-------|------------|----------|
| `0` | No edge | Clean, minimal |
| `0.5` | Thin edge | Subtle definition |
| `1.0` | Normal edge | Standard charts |
| `1.5` | Thick edge | Emphasis |
| `2.0+` | Very thick | Bold/graphic style |

### **Example - Bold Style:**

```python
series = SeriesConfig(
    x=['Q1', 'Q2', 'Q3', 'Q4'],
    y=[100, 120, 110, 130],
    color='#0066CC',
    marker_edgecolor='black',  # Black outline
    marker_edgewidth=2.0       # Thick edge
)
```

---

## **🔥 4. COMBINING CUSTOMIZATIONS**

### **Example 1: Professional B&W Style**

Perfect for academic publications:

```python
series1 = SeriesConfig(
    x=categories,
    y=values1,
    color='white',           # White fill
    hatch='///',             # Diagonal hatch
    marker_edgecolor='black',
    marker_edgewidth=1.5,
    label='Group A'
)

series2 = SeriesConfig(
    x=categories,
    y=values2,
    color='white',           # White fill
    hatch='|||',             # Vertical hatch
    marker_edgecolor='black',
    marker_edgewidth=1.5,
    label='Group B'
)

fig, ax = create_bar_plot([series1, series2], config, grouped=True)
```

### **Example 2: Colorful with Hatching**

Best of both worlds:

```python
series_hydro = SeriesConfig(
    x=months,
    y=hydro,
    color='#0066CC',         # Blue fill
    hatch='',                # No hatch (solid)
    marker_edgecolor='black',
    marker_edgewidth=0.5,
    label='Hydro'
)

series_gas = SeriesConfig(
    x=months,
    y=gas,
    color='#CC6666',         # Red fill
    hatch='///',             # Diagonal hatch
    marker_edgecolor='black',
    marker_edgewidth=0.5,
    label='Gas'
)

series_wind = SeriesConfig(
    x=months,
    y=wind,
    color='#00CC66',         # Green fill
    hatch='xxx',             # X pattern
    marker_edgecolor='black',
    marker_edgewidth=0.5,
    label='Wind'
)

fig, ax = create_bar_plot([series_hydro, series_gas, series_wind],
                          config, stacked=True)
```

---

## **📋 COMPLETE PARAMETER REFERENCE**

### **SeriesConfig Parameters for Bar Charts:**

```python
SeriesConfig(
    x=categories,              # Category labels
    y=values,                  # Bar heights
    color='#0066CC',           # Fill color
    hatch='///',               # Hatch pattern (NEW!)
    marker_edgecolor='black',  # Edge color
    marker_edgewidth=1.0,      # Edge width
    label='Series Name'        # Legend label
)
```

### **create_bar_plot() Parameters:**

```python
create_bar_plot(
    series,                    # SeriesConfig or list
    config,                    # PlotConfig
    grouped=False,             # Side-by-side bars
    stacked=False,             # Stacked bars
    orientation='vertical',    # 'vertical' or 'horizontal'
    bar_width=0.8              # Bar width (0.0-1.0)
)
```

---

## **💡 DESIGN TIPS**

### **Tip 1: Hatching for Print**

If your chart will be printed in black & white:
- Use hatching instead of colors
- Use thick edges (1.5-2.0)
- Choose distinct patterns (/, |, x)

### **Tip 2: Color + Hatching = Redundancy**

For accessibility, combine color AND pattern:
```python
# Colorblind-friendly!
series_A = SeriesConfig(..., color='#0066CC', hatch='')
series_B = SeriesConfig(..., color='#CC6666', hatch='///')
```

Users can distinguish by:
- Color (for color vision)
- Pattern (for colorblind or B&W)

### **Tip 3: Match Width to Data Density**

- **Few categories (2-5):** Use wider bars (0.8-0.9)
- **Many categories (10+):** Use narrower bars (0.5-0.6)
- **Time series:** Use narrower bars to show continuity

### **Tip 4: Edge Color Contrast**

For light-colored fills:
```python
color='#FFCC00'           # Light yellow
marker_edgecolor='black'  # Dark edge for contrast
```

For dark-colored fills:
```python
color='#003366'           # Dark blue
marker_edgecolor='white'  # Light edge for contrast
```

---

## **🧪 TESTING YOUR CUSTOMIZATIONS**

### **Quick Test Script:**

```python
from plotlib import create_bar_plot, save_plot
from models import SeriesConfig, PlotConfig

# Your data
categories = ['A', 'B', 'C']
values = [100, 120, 90]

# Try different customizations
series = SeriesConfig(
    x=categories,
    y=values,
    color='#0066CC',
    hatch='///',              # ← Change this
    marker_edgecolor='black',
    marker_edgewidth=1.5      # ← Change this
)

config = PlotConfig(title='Test', x_label='X', y_label='Y')

# Try different widths
fig, ax = create_bar_plot(series, config, bar_width=0.8)  # ← Change this
save_plot(fig, 'test.png')
```

---

## **📚 EXAMPLES**

See `examples/bar_custom.py` for 5 complete working examples:

1. **Hatch patterns** - All available patterns
2. **Grouped with hatch** - Actual vs Target
3. **Bar widths** - Wide, normal, narrow
4. **Complex patterns** - Generation by source
5. **Stacked with hatch** - Multi-source generation

**Run them:**

```powershell
cd examples
python bar_custom.py
```

**Creates 8 PNG files showing all customization options!**

---

## **🎯 QUICK REFERENCE**

### **Add hatching:**
```python
series = SeriesConfig(..., hatch='///')
```

### **Change bar width:**
```python
fig, ax = create_bar_plot(series, config, bar_width=0.6)
```

### **Add black edges:**
```python
series = SeriesConfig(
    ...,
    marker_edgecolor='black',
    marker_edgewidth=1.5
)
```

### **Combine all three:**
```python
series = SeriesConfig(
    x=cats, y=vals,
    color='#0066CC',
    hatch='///',
    marker_edgecolor='black',
    marker_edgewidth=1.5
)
fig, ax = create_bar_plot(series, config, bar_width=0.7)
```

---

**All customization options are now available!** 🎨
