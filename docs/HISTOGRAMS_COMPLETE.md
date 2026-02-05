# Histograms - PlotLib v2.0 📈

## ✅ HISTOGRAMS COMPLETE!

Histogram support has been added to PlotLib v2.0 for frequency distributions and statistical analysis.

---

## 🎯 WHAT'S INCLUDED

### **Histogram Types:**
- ✅ **Single histogram** - Basic frequency distribution
- ✅ **Overlapping histograms** - Compare multiple distributions
- ✅ **Stacked histograms** - Cumulative view
- ✅ **Density histograms** - Normalized (probability density)
- ✅ **Cumulative histograms** - CDF

### **Features:**
- ✅ Uses SeriesConfig and PlotConfig (same as other plots)
- ✅ Returns (fig, ax) for composability
- ✅ Customizable bins (number or explicit edges)
- ✅ Transparency control for overlapping
- ✅ Full formatting control

---

## 📝 QUICK START

### **Single Histogram:**

```python
from plotlib import create_histogram, save_plot
from models import SeriesConfig, PlotConfig
import numpy as np

# Data
data = np.random.randn(1000)

# Series (use .y for histogram data)
series = SeriesConfig(
    y=data,
    color='#0066CC',
    label='Distribution'
)

# Config
config = PlotConfig(
    title='Frequency Distribution',
    x_label='Value',
    y_label='Frequency'
)

# Create histogram
fig, ax = create_histogram(series, config, bins=30)
save_plot(fig, 'histogram.png', dpi=300)
```

---

## 📊 ALL HISTOGRAM TYPES

### **1. Single Histogram (Default)**

```python
fig, ax = create_histogram(series, config, bins=20)
```

**Output:** Basic frequency distribution

---

### **2. Overlapping Histograms**

Compare multiple distributions:

```python
series1 = SeriesConfig(y=data1, label='Group A', color='#0066CC')
series2 = SeriesConfig(y=data2, label='Group B', color='#CC6666')

fig, ax = create_histogram([series1, series2], config, bins=20, alpha=0.7)
```

**Output:** Two histograms overlapping with transparency

---

### **3. Stacked Histogram**

```python
fig, ax = create_histogram([series1, series2], config, bins=20, stacked=True)
```

**Output:** Histograms stacked on top of each other

---

### **4. Density (Normalized)**

```python
fig, ax = create_histogram(series, config, bins=20, density=True)
```

**Output:** Probability density (area under curve = 1)

---

### **5. Cumulative Distribution (CDF)**

```python
fig, ax = create_histogram(series, config, bins=20, cumulative=True)
```

**Output:** Cumulative frequency distribution

---

## 🎨 CUSTOMIZATION

### **Number of Bins:**

```python
# Default (10 bins)
fig, ax = create_histogram(series, config)

# More bins (30)
fig, ax = create_histogram(series, config, bins=30)

# Fewer bins (5)
fig, ax = create_histogram(series, config, bins=5)
```

**Guideline:** Use 10-50 bins depending on data size

---

### **Custom Bin Edges:**

```python
# Explicit bin edges
bin_edges = [0, 10, 20, 30, 40, 50, 100]

fig, ax = create_histogram(series, config, bins=bin_edges)
```

**Use case:** Non-uniform bin widths (e.g., wind speed categories)

---

### **Transparency (Alpha):**

```python
# Default (0.7 for overlapping)
fig, ax = create_histogram([s1, s2], config, alpha=0.7)

# More transparent (better for many overlapping)
fig, ax = create_histogram([s1, s2, s3], config, alpha=0.5)

# More opaque (single histogram)
fig, ax = create_histogram(series, config, alpha=0.9)
```

**Range:** 0.0 (transparent) to 1.0 (opaque)

---

### **Bin Range:**

Limit the histogram to a specific data range:

```python
# Only show data between 0 and 100
fig, ax = create_histogram(series, config, bins=20, bin_range=(0, 100))
```

---

### **Colors and Edges:**

```python
series = SeriesConfig(
    y=data,
    color='#0066CC',           # Fill color
    marker_edgecolor='black',  # Edge color
    marker_edgewidth=0.5       # Edge width
)
```

---

## 📋 COMPLETE API

### **`create_histogram()` Parameters:**

```python
create_histogram(
    series,              # SeriesConfig or list of SeriesConfig
    config,              # PlotConfig
    bins=10,             # Number of bins or list of bin edges
    density=False,       # True = normalize to probability density
    stacked=False,       # True = stack multiple histograms
    cumulative=False,    # True = cumulative distribution (CDF)
    orientation='vertical',  # 'vertical' or 'horizontal'
    bin_range=None,      # (min, max) tuple to limit range
    alpha=0.7            # Transparency (0.0-1.0)
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

## 💡 DESIGN TIPS

### **Tip 1: Choose Appropriate Bins**

**Too few bins:** Lose detail
```python
bins=5  # May oversimplify
```

**Too many bins:** Noisy, hard to interpret
```python
bins=100  # May show too much noise
```

**Good rule:** 
- Small datasets (n < 100): 10-15 bins
- Medium datasets (100 < n < 1000): 20-30 bins  
- Large datasets (n > 1000): 30-50 bins

### **Tip 2: Use Transparency for Overlapping**

```python
# Good for 2 distributions
alpha=0.7

# Better for 3+ distributions
alpha=0.5
```

### **Tip 3: Stacked vs Overlapping**

**Use overlapping when:**
- Comparing distributions
- Want to see individual shapes

**Use stacked when:**
- Showing composition
- Want to see total count

### **Tip 4: Density for Different Sample Sizes**

When comparing distributions with different sample sizes, use density:

```python
# data1 has 1000 samples
# data2 has 500 samples
# Use density=True to make them comparable
fig, ax = create_histogram([series1, series2], config, bins=20, density=True)
```

---

## 📊 EXAMPLES

See `examples/histogram_examples.py` for 7 complete working examples:

1. **Single histogram** - Normal distribution
2. **Overlapping** - Compare two distributions
3. **Stacked** - Load distribution
4. **Custom bins** - Wind speed categories
5. **Density** - Normalized distribution
6. **Cumulative** - CDF
7. **Realistic** - Power generation distribution

**Run them:**

```powershell
cd examples
python histogram_examples.py
```

**Creates 7 PNG files demonstrating all features!**

---

## ✅ COMPATIBILITY

### **Same Config as Other Plots:**

All PlotConfig options work identically:
- Text formatting
- Grid settings
- Legend settings
- Spine visibility

**Mix and match:**

```python
config = PlotConfig(
    title_weight='normal',
    tick_label_color='#666666',
    show_grid=True,
    grid_alpha=0.3
)

# Works for all:
fig, ax = create_line_plot(series, config)
fig, ax = create_bar_plot(series, config)
fig, ax = create_histogram(series, config, bins=20)
```

---

## 🎯 QUICK REFERENCE

### **Basic histogram:**
```python
series = SeriesConfig(y=data)
fig, ax = create_histogram(series, config, bins=20)
```

### **Compare distributions:**
```python
fig, ax = create_histogram([series1, series2], config, bins=20, alpha=0.7)
```

### **Stacked:**
```python
fig, ax = create_histogram([series1, series2], config, bins=20, stacked=True)
```

### **Normalized:**
```python
fig, ax = create_histogram(series, config, bins=20, density=True)
```

### **Cumulative:**
```python
fig, ax = create_histogram(series, config, bins=20, cumulative=True)
```

### **Custom bins:**
```python
bins = [0, 10, 20, 50, 100]  # Explicit edges
fig, ax = create_histogram(series, config, bins=bins)
```

---

## 🔬 STATISTICAL USE CASES

### **1. Check Data Distribution**

```python
# Is my data normally distributed?
fig, ax = create_histogram(series, config, bins=30, density=True)
```

### **2. Compare Groups**

```python
# Before vs After treatment
series_before = SeriesConfig(y=before_data, label='Before')
series_after = SeriesConfig(y=after_data, label='After')
fig, ax = create_histogram([series_before, series_after], config, bins=20)
```

### **3. Load Duration Curve**

```python
# Power generation output distribution
fig, ax = create_histogram(series, config, bins=50, cumulative=True)
```

### **4. Wind Speed Distribution**

```python
# Custom bins for Beaufort scale
bins = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
fig, ax = create_histogram(series, config, bins=bins)
```

---

**Histograms are now production-ready!** 📈

**Next up: Area plots!** 📉
