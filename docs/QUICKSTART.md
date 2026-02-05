# Quick Start Guide - PlotLib v2.4.0

**Get started in 5 minutes!**

---

## 1️⃣ Installation

```bash
cd plotlib_v2_consolidated
pip install -e .
```

**That's it!** PlotLib is now installed.

---

## 2️⃣ Your First Plot (30 seconds)

Create a file called `test.py`:

```python
from plotlib import create_line_plot, save_plot
from models import SeriesConfig, PlotConfig
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Series
series = SeriesConfig(x=x, y=y, color='#0066CC', label='Sine')

# Config
config = PlotConfig(title='My First Plot', x_label='X', y_label='Y')

# Create and save
fig, ax = create_line_plot(series, config)
save_plot(fig, 'test.png')
print("✓ Created test.png!")
```

**Run it:**

```bash
python test.py
```

**You should see:** `test.png` created!

---

## 3️⃣ All Plot Types (2 minutes)

### Line Plot

```python
from plotlib import create_line_plot

series = SeriesConfig(x=x, y=y, line_style='-', line_width=2.0)
fig, ax = create_line_plot(series, config)
```

### Bar Chart

```python
from plotlib import create_bar_plot

series = SeriesConfig(x=['Q1','Q2','Q3'], y=[100,120,110], color='#0066CC')
fig, ax = create_bar_plot(series, config)
```

### Histogram

```python
from plotlib import create_histogram

data = np.random.randn(1000)
series = SeriesConfig(y=data, color='#0066CC')
fig, ax = create_histogram(series, config, bins=30)
```

### Area Plot

```python
from plotlib import create_area_plot

series = SeriesConfig(x=x, y=y, color='#0066CC')
fig, ax = create_area_plot(series, config, alpha=0.6)
```

### Pie Chart

```python
from plotlib import create_pie_chart

labels = ['A', 'B', 'C']
values = [30, 45, 25]
colors = ['#0066CC', '#00CC66', '#FFCC00']
fig, ax = create_pie_chart(labels, values, colors, config)
```

---

## 4️⃣ Common Customizations (3 minutes)

### Cross-Hatching (B&W Publications)

```python
series = SeriesConfig(
    x=categories, y=values,
    color='white',
    hatch='///',              # ← Pattern!
    marker_edgecolor='black',
    marker_edgewidth=1.5
)
```

**Patterns:** `/`, `\`, `|`, `-`, `+`, `x`, `o`, `.`, `*`

### Grouped Bars

```python
series1 = SeriesConfig(x=cats, y=vals1, color='#0066CC', label='2023')
series2 = SeriesConfig(x=cats, y=vals2, color='#CC6666', label='2024')

fig, ax = create_bar_plot([series1, series2], config, grouped=True)
```

### Stacked Areas

```python
series1 = SeriesConfig(x=x, y=y1, color='#0066CC', label='Hydro')
series2 = SeriesConfig(x=x, y=y2, color='#00CC66', label='Wind')

fig, ax = create_area_plot([series1, series2], config, stacked=True)
```

### Donut Chart

```python
fig, ax = create_pie_chart(labels, values, colors, config, donut=True)
```

---

## 5️⃣ Full Configuration (1 minute)

```python
config = PlotConfig(
    # Figure
    figure_width=10,
    figure_height=6,
    dpi=100,
    
    # Title & labels
    title='My Plot',
    title_size=14,
    x_label='X Axis',
    y_label='Y Axis',
    axis_label_size=12,
    
    # Grid
    show_grid=True,
    grid_alpha=0.3,
    
    # Legend
    show_legend=True,
    legend_location='best'
)
```

---

## 6️⃣ Run Examples (2 minutes)

```bash
cd examples

# Line/scatter and time-series
python timeseries_clean.py

# Bar charts (6 examples)
python bar_examples.py

# Histograms (7 examples)  
python histogram_examples.py

# Area plots (8 examples)
python area_examples.py

# Pie charts (9 examples)
python pie_examples.py

# Customization demos
python bar_custom.py
python histogram_custom.py
python config_extended.py
```

**Result:** 46 PNG files showing all features!

---

## 7️⃣ Common Patterns

### Publication-Ready B&W

```python
series = SeriesConfig(
    x=x, y=y,
    color='white',
    hatch='///',
    marker_edgecolor='black',
    marker_edgewidth=1.5
)

config = PlotConfig(
    title='Figure 1',
    show_grid=True,
    grid_alpha=0.3
)

fig, ax = create_bar_plot(series, config)
save_plot(fig, 'figure1.png', dpi=300)  # High DPI!
```

### Multiple Series

```python
series_list = [
    SeriesConfig(x=x, y=y1, label='Series 1', color='#0066CC'),
    SeriesConfig(x=x, y=y2, label='Series 2', color='#CC6666'),
    SeriesConfig(x=x, y=y3, label='Series 3', color='#00CC66')
]

fig, ax = create_line_plot(series_list, config)
```

### Save High Resolution

```python
save_plot(fig, 'output.png', dpi=300)  # For publications
save_plot(fig, 'output.png', dpi=150)  # For presentations
save_plot(fig, 'output.png', dpi=100)  # For web
```

---

## 8️⃣ Getting Help

### Check Documentation

- **README.md** - Overview and quick start
- **CHANGELOG.md** - Version history
- **BAR_CHARTS_COMPLETE.md** - Bar chart guide
- **HISTOGRAMS_COMPLETE.md** - Histogram guide
- **AREA_PLOTS_COMPLETE.md** - Area plot guide
- **PIE_CHARTS_COMPLETE.md** - Pie chart guide

### Look at Examples

All examples are in `examples/` - they're well-commented!

### Common Issues

**Q: Import error?**  
A: Make sure you ran `pip install -e .` from the package directory

**Q: Plot looks wrong?**  
A: Check the relevant example in `examples/` directory

**Q: Need more customization?**  
A: Check the complete guides in the docs

---

## 9️⃣ Next Steps

1. ✅ Run the examples to see what's possible
2. ✅ Read the relevant guide for your plot type
3. ✅ Start creating your own plots!
4. ✅ Check CHANGELOG.md for recent updates

---

## 🎯 You're Ready!

**In 5 minutes you've:**
- ✅ Installed PlotLib
- ✅ Created your first plot
- ✅ Learned all plot types
- ✅ Seen common patterns
- ✅ Know where to get help

**Start plotting!** 🚀

---

## 📝 Cheat Sheet

```python
# Imports
from plotlib import create_line_plot, create_bar_plot, create_histogram, create_area_plot, create_pie_chart, save_plot
from models import SeriesConfig, PlotConfig
import numpy as np

# Series
series = SeriesConfig(x=x, y=y, color='#0066CC', label='Data')

# Config
config = PlotConfig(title='Title', x_label='X', y_label='Y', show_grid=True)

# Create
fig, ax = create_line_plot(series, config)
fig, ax = create_bar_plot(series, config)
fig, ax = create_histogram(series, config, bins=30)
fig, ax = create_area_plot(series, config)
fig, ax = create_pie_chart(labels, values, colors, config)

# Save
save_plot(fig, 'output.png', dpi=300)

# Common options
SeriesConfig(..., hatch='///', marker_edgecolor='black', line_style='--')
create_bar_plot(..., grouped=True, stacked=True, bar_width=0.6)
create_area_plot(..., stacked=True, alpha=0.7, show_line=False)
create_pie_chart(..., donut=True, explode=[0.1,0,0])
```

---

**That's all you need to get started!** 🎉

For more details, check the complete documentation in the package.
