# Box Plots - PlotLib v2.5.0 📊

## ✅ BOX PLOTS COMPLETE! PHASE 2 STARTED!

Box plot support with **comprehensive customization** including grouped plots, outliers, notches, and publication-ready formatting.

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Statistical Features:**
- ✅ **Quartiles** - Q1, median (Q2), Q3
- ✅ **Whiskers** - IQR-based (customizable range)
- ✅ **Outliers** - Show/hide outlier points
- ✅ **Means** - Show/hide mean markers
- ✅ **Notches** - Confidence intervals around median

### **Layout:**
- ✅ **Orientation** - Vertical or horizontal
- ✅ **Grouped** - Multiple groups with subgroups
- ✅ **Box width** - Narrow to wide (0.1-1.0)
- ✅ **Custom colors** - Per-box colors

---

## 📝 QUICK START

### **Single Box Plot:**

```python
from plotlib import create_box_plot, save_plot
from models import PlotConfig
import numpy as np

# Data
data = [np.random.randn(100)]
labels = ['Sample']

# Config
config = PlotConfig(
    title='Box Plot',
    y_label='Value',
    show_grid=True
)

# Create
fig, ax = create_box_plot(data, labels, config)
save_plot(fig, 'box.png')
```

---

## 📊 BOX PLOT ANATOMY

```
    outlier  →  ○
                │
    whisker  →  ├─────
                │
    Q3       →  ┌─────┐
                │     │
    median   →  ├─────┤  ← box
                │  ×  │  ← mean (optional)
    Q1       →  └─────┘
                │
    whisker  →  ├─────
                │
    outlier  →  ○
```

**Components:**
- **Box:** Q1 to Q3 (interquartile range, IQR)
- **Median line:** Red line inside box
- **Mean marker:** Green diamond (optional)
- **Whiskers:** Extend to 1.5×IQR (default)
- **Outliers:** Points beyond whiskers (red circles)
- **Notch:** Confidence interval (optional)

---

## 📊 ALL BOX PLOT TYPES

### **1. Single Box Plot**

```python
data = [np.random.randn(100)]
labels = ['Sample']

fig, ax = create_box_plot(data, labels, config)
```

**Use:** Single distribution summary

---

### **2. Multiple Box Plots**

```python
data = [sample1, sample2, sample3]
labels = ['Control', 'Treatment A', 'Treatment B']
colors = ['#0066CC', '#CC6666', '#00CC66']

fig, ax = create_box_plot(data, labels, config, colors=colors)
```

**Use:** Compare multiple groups

---

### **3. Horizontal Box Plots**

```python
fig, ax = create_box_plot(
    data, labels, config,
    orientation='horizontal'
)
```

**Use:** Long labels, compare distributions side-by-side

---

### **4. Grouped Box Plots**

```python
# 2 groups × 2 subgroups
data = [
    [control_male, control_female],
    [treatment_male, treatment_female]
]
labels = [
    ['Male', 'Female'],
    ['Male', 'Female']
]
group_labels = ['Control', 'Treatment']
colors = ['#0066CC', '#CC6666']

fig, ax = create_box_plot(
    data, labels, config,
    grouped=True,
    group_labels=group_labels,
    colors=colors
)
```

**Use:** Factorial designs, interaction effects

---

### **5. Notched Box Plots**

```python
fig, ax = create_box_plot(
    data, labels, config,
    notch=True  # Confidence intervals
)
```

**Use:** Test if medians differ (non-overlapping notches suggest significance)

---

### **6. Without Outliers**

```python
fig, ax = create_box_plot(
    data, labels, config,
    show_outliers=False
)
```

**Use:** Focus on central distribution, cleaner appearance

---

## 📋 COMPLETE API

### **`create_box_plot()` Parameters:**

```python
create_box_plot(
    data,                      # List of arrays or list of lists
    labels,                    # Box labels
    config=None,               # PlotConfig (optional)
    colors=None,               # List of colors (optional)
    orientation='vertical',    # 'vertical' or 'horizontal'
    show_means=True,           # Show mean markers
    show_outliers=True,        # Show outlier points
    notch=False,               # Use notched boxes
    box_width=0.5,             # Box width (0-1)
    grouped=False,             # Create grouped boxes
    group_labels=None,         # Labels for groups
    whisker_range=1.5,         # IQR multiplier for whiskers
    patch_artist=True          # Use filled boxes
)
```

**Returns:** `(fig, ax)` - Standard matplotlib objects

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Multiple with Custom Colors**

```python
data = [control, treatment_a, treatment_b]
labels = ['Control', 'Treatment A', 'Treatment B']
colors = ['#0066CC', '#CC6666', '#00CC66']

config = PlotConfig(
    title='Treatment Comparison',
    y_label='Response (units)'
)

fig, ax = create_box_plot(data, labels, config, colors=colors)
```

---

### **Example 2: Grouped Factorial Design**

```python
# 2 treatments × 2 genders
data = [
    [control_male, control_female],
    [treatment_male, treatment_female]
]
labels = [
    ['Male', 'Female'],
    ['Male', 'Female']
]
group_labels = ['Control', 'Treatment']
colors = ['#0066CC', '#CC6666']

fig, ax = create_box_plot(
    data, labels, config,
    grouped=True,
    group_labels=group_labels,
    colors=colors
)
```

---

### **Example 3: Publication Style**

```python
data = [baseline, method_a, method_b]
labels = ['Baseline', 'Method A', 'Method B']
colors = ['#CCCCCC', '#888888', '#444444']  # Grayscale

config = PlotConfig(
    title='Method Comparison',
    title_weight='normal',
    y_label='Performance',
    show_grid=True,
    grid_alpha=0.3,
    show_top_spine=False,
    show_right_spine=False
)

fig, ax = create_box_plot(
    data, labels, config,
    colors=colors,
    show_means=True
)

save_plot(fig, 'figure1.png', dpi=300)
```

---

### **Example 4: Horizontal for Long Labels**

```python
data = [exp_dist, gamma_dist, lognormal_dist]
labels = ['Exponential Distribution', 'Gamma Distribution', 'Log-normal Distribution']

fig, ax = create_box_plot(
    data, labels, config,
    orientation='horizontal'
)
```

---

### **Example 5: Notched for Statistical Comparison**

```python
fig, ax = create_box_plot(
    data, labels, config,
    colors=colors,
    notch=True,            # Show confidence intervals
    show_means=True
)
```

**If notches don't overlap → medians likely differ!**

---

## 💡 DESIGN TIPS

### **Tip 1: Use Box Plots for Skewed Data**

Unlike bar charts with error bars, box plots show:
- Full distribution shape
- Outliers
- Quartiles
- Skewness

### **Tip 2: Horizontal for Many Groups**

```python
# Better for 5+ groups or long labels
orientation='horizontal'
```

### **Tip 3: Grouped for Factorial Designs**

```python
# 2×2, 3×2, etc. factorial designs
grouped=True
```

### **Tip 4: Notched for Statistical Tests**

```python
# Quick visual test of median differences
notch=True
```

### **Tip 5: Hide Outliers for Clean Plots**

```python
# When outliers distract from main message
show_outliers=False
```

### **Tip 6: Adjust Box Width for Aesthetics**

```python
# Narrow for many boxes
box_width=0.3

# Wide for few boxes
box_width=0.8
```

---

## 📊 STATISTICAL INTERPRETATION

### **Reading Box Plots:**

1. **Median (red line):** Central value (50th percentile)
2. **Box (IQR):** Middle 50% of data (Q1 to Q3)
3. **Whiskers:** Typical range (1.5×IQR from box)
4. **Outliers:** Unusual values beyond whiskers
5. **Mean (green diamond):** Average (if shown)

### **Comparing Box Plots:**

**Similar medians:** Centers aligned  
**Different spreads:** Box heights differ  
**Outliers:** One group more variable  
**Notches overlap:** Medians likely not different  
**Notches don't overlap:** Medians likely differ (95% CI)  

---

## 📊 REALISTIC USE CASES

### **Clinical Trial:**

```python
# Compare treatment effects
data = [placebo, low_dose, high_dose]
labels = ['Placebo', 'Low Dose', 'High Dose']
colors = ['#CCCCCC', '#0066CC', '#CC6666']

config = PlotConfig(
    title='Treatment Response',
    y_label='Symptom Score'
)

fig, ax = create_box_plot(data, labels, config, colors=colors, notch=True)
```

### **Quality Control:**

```python
# Manufacturing batches
data = [batch1, batch2, batch3, batch4, batch5]
labels = ['Batch 1', 'Batch 2', 'Batch 3', 'Batch 4', 'Batch 5']

config = PlotConfig(
    title='Product Quality by Batch',
    y_label='Measurement (mm)'
)

fig, ax = create_box_plot(data, labels, config)
```

### **Experimental Design:**

```python
# Factorial: temperature × pressure
data = [
    [low_temp_low_press, low_temp_high_press],
    [high_temp_low_press, high_temp_high_press]
]
labels = [['Low P', 'High P'], ['Low P', 'High P']]
group_labels = ['Low Temp', 'High Temp']

fig, ax = create_box_plot(
    data, labels, config,
    grouped=True,
    group_labels=group_labels
)
```

---

## ✅ COMPATIBILITY

All PlotConfig options work identically:
- Text formatting
- Grid settings
- Spine visibility
- Figure size

**Mix and match:**

```python
config = PlotConfig(
    title_weight='normal',
    show_grid=True,
    show_top_spine=False,
    show_right_spine=False
)

# Works for all plot types
fig, ax = create_line_plot(series, config)
fig, ax = create_bar_plot(series, config)
fig, ax = create_box_plot(data, labels, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Single box:**
```python
data = [sample]
labels = ['Sample']
fig, ax = create_box_plot(data, labels, config)
```

### **Multiple boxes:**
```python
data = [s1, s2, s3]
labels = ['A', 'B', 'C']
colors = ['#0066CC', '#CC6666', '#00CC66']
fig, ax = create_box_plot(data, labels, config, colors=colors)
```

### **Horizontal:**
```python
fig, ax = create_box_plot(data, labels, config, orientation='horizontal')
```

### **Grouped:**
```python
data = [[g1_s1, g1_s2], [g2_s1, g2_s2]]
labels = [['A', 'B'], ['A', 'B']]
group_labels = ['Group 1', 'Group 2']
fig, ax = create_box_plot(data, labels, config, grouped=True, group_labels=group_labels)
```

### **Notched:**
```python
fig, ax = create_box_plot(data, labels, config, notch=True)
```

### **No outliers:**
```python
fig, ax = create_box_plot(data, labels, config, show_outliers=False)
```

---

## 📚 EXAMPLES

See `examples/box_examples.py` for 10 complete working examples:

1. **Single box** - Basic plot
2. **Multiple** - Comparison
3. **Horizontal** - Long labels
4. **Custom colors** - Quarterly data
5. **Grouped** - Factorial design
6. **Outliers** - With/without
7. **Notched** - Confidence intervals
8. **Publication** - Grayscale
9. **Box widths** - Narrow vs wide
10. **Statistical** - Variance comparison

**Run them:**

```powershell
cd examples
python box_examples.py
```

**Creates 11 PNG files demonstrating all features!**

---

## 📈 WHEN TO USE BOX PLOTS

| Use Case | Box Plot | Alternative |
|----------|----------|-------------|
| Compare distributions | ✅ Perfect | Violin plot |
| Show outliers | ✅ Perfect | Scatter |
| Skewed data | ✅ Perfect | Histogram |
| Many groups | ✅ Good | Bar chart |
| Factorial design | ✅ Grouped | Multiple plots |
| Statistical test | ✅ Notched | t-test table |

---

**Box plots with comprehensive customization are complete!** 📊

**Phase 2 Started!** 🚀  
**Next: Violin plots or Heatmaps (your choice!)** 🎯
