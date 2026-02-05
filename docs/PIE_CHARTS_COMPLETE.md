# Pie Charts - PlotLib v2.0 🥧

## ✅ PIE CHARTS COMPLETE! PHASE 1 FINISHED! 🎉

Pie chart support has been added with **comprehensive customization** including cross-hatching, donut charts, exploded slices, and more!

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Slice Styling:**
- ✅ **Custom colors** - Per-slice colors
- ✅ **Cross-hatching** - `/`, `\`, `|`, `-`, `+`, `x`, `o`, `.`, `*`
- ✅ **Edge colors** - Per-slice or global
- ✅ **Edge width** - Border thickness

### **Chart Types:**
- ✅ **Simple pie** - Standard pie chart
- ✅ **Donut chart** - Pie with hole in center
- ✅ **Exploded slices** - Pull out specific wedges

### **Labels & Text:**
- ✅ **Slice labels** - Show/hide names
- ✅ **Percentages** - Show/hide values
- ✅ **Label distance** - Adjust position
- ✅ **Custom format** - Percentage format

### **Layout:**
- ✅ **Start angle** - Rotate chart
- ✅ **Shadow** - Optional shadow effect

---

## 📝 QUICK START

### **Simple Pie Chart:**

```python
from plotlib import create_pie_chart, save_plot
from models import PlotConfig

# Data
labels = ['Hydro', 'Wind', 'Solar', 'Gas']
values = [3200, 800, 400, 1500]
colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900']

# Config
config = PlotConfig(
    title='Generation Mix 2024',
    figure_width=8,
    figure_height=6
)

# Create pie chart
fig, ax = create_pie_chart(labels, values, colors, config)
save_plot(fig, 'pie.png')
```

---

## 🥧 ALL PIE CHART TYPES

### **1. Simple Pie**

```python
fig, ax = create_pie_chart(labels, values, colors, config)
```

**Use:** Show proportions, composition

---

### **2. Donut Chart**

```python
fig, ax = create_pie_chart(
    labels, values, colors, config,
    donut=True,           # ← Donut!
    donut_width=0.4       # Size of hole
)
```

**Use:** Modern look, center can display total

---

### **3. Exploded Slices**

```python
# Pull out specific slices
explode = [0.1, 0.15, 0, 0]  # First two pulled out

fig, ax = create_pie_chart(
    labels, values, colors, config,
    explode=explode       # ← Explode!
)
```

**Use:** Emphasize important slices

---

### **4. Cross-Hatching (B&W Publication)**

```python
colors = ['white', 'white', 'white', 'white']
hatches = ['///', '|||', 'xxx', '...']
edge_colors = ['black', 'black', 'black', 'black']

fig, ax = create_pie_chart(
    labels, values, colors, config,
    hatches=hatches,           # ← Patterns!
    edge_colors=edge_colors,   # ← Black edges
    edge_width=1.5
)
```

**Use:** Black & white publications

---

### **5. Donut + Hatching**

```python
fig, ax = create_pie_chart(
    labels, values, colors, config,
    donut=True,
    donut_width=0.35,
    hatches=hatches,
    edge_colors=edge_colors
)
```

**Use:** B&W publication with modern look

---

### **6. Exploded Donut**

```python
explode = [0.1, 0, 0, 0]

fig, ax = create_pie_chart(
    labels, values, colors, config,
    donut=True,
    explode=explode,
    edge_width=2.0
)
```

**Use:** Emphasis + modern style

---

## 📋 COMPLETE API

### **`create_pie_chart()` Parameters:**

```python
create_pie_chart(
    labels,                    # List of slice labels
    values,                    # List of slice values
    colors=None,               # List of colors (optional)
    config=None,               # PlotConfig (optional)
    explode=None,              # List of explosion distances
    hatches=None,              # List of hatch patterns
    edge_colors=None,          # List of edge colors
    edge_width=1.0,            # Edge thickness
    start_angle=90,            # Starting angle (degrees)
    donut=False,               # True = donut chart
    donut_width=0.3,           # Width of donut ring (0-1)
    show_percentages=True,     # Show percentage labels
    show_labels=True,          # Show slice labels
    label_distance=1.1,        # Distance of labels from center
    autopct_format='%1.1f%%',  # Percentage format string
    shadow=False               # Add shadow effect
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Simple with Custom Colors**

```python
labels = ['Hydro', 'Wind', 'Solar', 'Gas']
values = [3200, 800, 400, 1500]
colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900']

fig, ax = create_pie_chart(labels, values, colors, config)
```

---

### **Example 2: Donut Chart**

```python
fig, ax = create_pie_chart(
    labels, values, colors, config,
    donut=True,
    donut_width=0.4  # 0.0 = no hole, 1.0 = all hole
)
```

---

### **Example 3: Exploded Renewables**

```python
labels = ['Hydro', 'Wind', 'Solar', 'Gas', 'Coal']
values = [3200, 800, 400, 1500, 200]
colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900', '#666666']

# Pull out renewables
explode = [0.1, 0.15, 0.15, 0, 0]

fig, ax = create_pie_chart(labels, values, colors, config, explode=explode)
```

---

### **Example 4: Black & White Publication**

```python
colors = ['white'] * 4
hatches = ['///', '|||', 'xxx', '...']
edge_colors = ['black'] * 4

fig, ax = create_pie_chart(
    labels, values, colors, config,
    hatches=hatches,
    edge_colors=edge_colors,
    edge_width=1.5
)
```

---

### **Example 5: Labels Only (No Percentages)**

```python
fig, ax = create_pie_chart(
    labels, values, colors, config,
    show_percentages=False  # No percentages
)
```

---

### **Example 6: Custom Start Angle**

```python
fig, ax = create_pie_chart(
    labels, values, colors, config,
    start_angle=0  # Start at east (default is 90 = north)
)
```

---

### **Example 7: Accessible (Color + Pattern)**

```python
colors = ['#0066CC', '#00CC66', '#FFCC00', '#CC9900']
hatches = ['', '///', 'xxx', '|||']  # Redundant encoding
edge_colors = ['black'] * 4

fig, ax = create_pie_chart(
    labels, values, colors, config,
    hatches=hatches,
    edge_colors=edge_colors
)
```

---

## 🎨 HATCH PATTERNS

Same as other charts:

| Pattern | Description |
|---------|-------------|
| `'/'` | Diagonal |
| `'\\'` | Diagonal (other way) |
| `'|'` | Vertical |
| `'-'` | Horizontal |
| `'+'` | Crossed |
| `'x'` | X pattern |
| `'o'` | Circles |
| `'.'` | Dots |
| `'*'` | Stars |
| `'//'`, `'///'` | Denser patterns |

---

## 💡 DESIGN TIPS

### **Tip 1: Use Donut for Modern Look**

```python
# Modern style
donut=True, donut_width=0.4
```

### **Tip 2: Explode Important Slices**

```python
# Emphasize first slice
explode = [0.1, 0, 0, 0]
```

### **Tip 3: Cross-Hatching for B&W**

```python
# Publication-ready
colors = ['white'] * n
hatches = ['///', '|||', 'xxx', ...]
edge_colors = ['black'] * n
```

### **Tip 4: Keep Slices Under 7**

Too many slices make charts hard to read.
- **Good:** 3-6 slices
- **Max:** 7 slices
- **Too many?** Group small slices into "Other"

### **Tip 5: Order by Size**

```python
# Sort largest to smallest
sorted_data = sorted(zip(values, labels, colors), reverse=True)
values, labels, colors = zip(*sorted_data)
```

### **Tip 6: Color + Pattern for Accessibility**

```python
# Both color AND pattern
# Accessible to colorblind users
colors = ['#0066CC', '#00CC66', '#FFCC00']
hatches = ['', '///', 'xxx']
```

---

## 📊 REALISTIC USE CASES

### **Power Generation Mix:**

```python
labels = ['Hydro', 'Geothermal', 'Wind', 'Gas', 'Coal']
values = [3200, 1000, 800, 1500, 200]
colors = ['#0066CC', '#CC6666', '#00CC66', '#CC9900', '#666666']

config = PlotConfig(title='NZ Generation Mix 2024')
fig, ax = create_pie_chart(labels, values, colors, config)
```

### **Load Distribution:**

```python
labels = ['Peak', 'Shoulder', 'Off-Peak']
values = [30, 35, 35]
colors = ['#CC6666', '#FFCC00', '#00CC66']

# Donut with exploded peak
fig, ax = create_pie_chart(labels, values, colors, config,
                           donut=True, explode=[0.1, 0, 0])
```

### **Energy Sources (B&W Publication):**

```python
labels = ['Renewable', 'Fossil']
values = [5000, 1700]
colors = ['white', 'white']
hatches = ['///', '|||']
edge_colors = ['black', 'black']

fig, ax = create_pie_chart(labels, values, colors, config,
                           hatches=hatches, edge_colors=edge_colors,
                           explode=[0.1, 0], edge_width=2.0)
```

---

## ✅ COMPATIBILITY

### **PlotConfig Works Identically:**

```python
config = PlotConfig(
    title='My Pie Chart',
    title_weight='normal',
    figure_width=8,
    figure_height=6,
    tick_label_size=11
)

# Works for all plot types
fig, ax = create_line_plot(series, config)
fig, ax = create_bar_plot(series, config)
fig, ax = create_histogram(series, config, bins=20)
fig, ax = create_area_plot(series, config)
fig, ax = create_pie_chart(labels, values, colors, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Simple pie:**
```python
fig, ax = create_pie_chart(labels, values, colors, config)
```

### **Donut:**
```python
fig, ax = create_pie_chart(labels, values, colors, config, donut=True)
```

### **Exploded:**
```python
explode = [0.1, 0, 0, 0]
fig, ax = create_pie_chart(labels, values, colors, config, explode=explode)
```

### **With hatching:**
```python
hatches = ['///', '|||', 'xxx']
fig, ax = create_pie_chart(labels, values, colors, config, hatches=hatches)
```

### **B&W publication:**
```python
colors = ['white'] * n
hatches = ['///', '|||', 'xxx']
edge_colors = ['black'] * n
fig, ax = create_pie_chart(labels, values, colors, config, 
                           hatches=hatches, edge_colors=edge_colors, edge_width=1.5)
```

---

## 📚 EXAMPLES

See `examples/pie_examples.py` for 9 complete working examples:

1. **Simple pie** - Basic chart
2. **Donut** - Hole in center
3. **Exploded** - Pull out slices
4. **Cross-hatching** - B&W patterns
5. **Donut + hatching** - Combined
6. **Exploded donut** - Emphasis + modern
7. **No percentages** - Labels only
8. **Rotated** - Custom start angle
9. **Accessible** - Color + pattern

**Run them:**

```powershell
cd examples
python pie_examples.py
```

**Creates 9 PNG files demonstrating all features!**

---

## 🎉 PHASE 1 COMPLETE!

**All plot types implemented:**
- ✅ Line/Scatter plots
- ✅ Time-series utilities
- ✅ Bar charts
- ✅ Histograms
- ✅ Area plots
- ✅ **Pie charts** ← JUST COMPLETED!

**Total plot types:** 6 of 6 complete! 🎯

---

**Pie charts with comprehensive customization are production-ready!** 🥧

**PHASE 1 IS COMPLETE!** 🎉
