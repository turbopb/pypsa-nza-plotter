# Contour Plots - PlotLib v2.8.0 🗺️

## ✅ CONTOUR PLOTS COMPLETE! PHASE 2: 67% DONE!

Contour plot support for **2D function visualization** with filled contours, line contours, labels, and publication-ready formatting. Perfect for thesis work!

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Plot Types:**
- ✅ **Filled contours** - Color-filled regions
- ✅ **Line contours** - Contour lines only
- ✅ **Combined** - Both filled and lines
- ✅ **Labeled** - Show values on contour lines

### **Customization:**
- ✅ **Custom levels** - Number of levels or specific values
- ✅ **Colormaps** - Any matplotlib colormap
- ✅ **Line styling** - Color, width, style
- ✅ **Transparency** - Alpha control
- ✅ **Color bar** - Show/hide, custom label

### **Convenience:**
- ✅ **From meshgrid** - X, Y, Z arrays
- ✅ **From function** - Direct function evaluation

---

## 📝 QUICK START

### **Basic Filled Contour:**

```python
from plotlib import create_contour_plot, save_plot
from models import PlotConfig
import numpy as np

# Generate data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Config
config = PlotConfig(
    title='Contour Plot',
    x_label='X',
    y_label='Y'
)

# Create filled contour
fig, ax = create_contour_plot(X, Y, Z, config, filled=True)
save_plot(fig, 'contour.png')
```

---

## 📊 ALL CONTOUR TYPES

### **1. Filled Contours**

```python
fig, ax = create_contour_plot(
    X, Y, Z, config,
    filled=True,
    cbar_label='Z Value'
)
```

**Use:** Show continuous variation with color

---

### **2. Line Contours with Labels**

```python
fig, ax = create_contour_plot(
    X, Y, Z, config,
    filled=False,
    lines=True,
    labels=True,
    line_colors='black',
    line_widths=1.5
)
```

**Use:** Show specific level values clearly

---

### **3. Both Filled and Lines**

```python
fig, ax = create_contour_plot(
    X, Y, Z, config,
    filled=True,
    lines=True,
    line_colors='black',
    line_widths=0.5
)
```

**Use:** Combine color and clear boundaries

---

### **4. Custom Levels**

```python
# Specify exact levels
levels = [-1.0, -0.5, 0, 0.5, 1.0]

fig, ax = create_contour_plot(
    X, Y, Z, config,
    filled=True,
    levels=levels
)
```

**Use:** Control which values to show

---

### **5. From Function (Convenience)**

```python
from plotlib import create_contour_from_function

def my_function(x, y):
    return np.sin(x) * np.cos(y)

fig, ax = create_contour_from_function(
    my_function,
    x_range=(-5, 5),
    y_range=(-5, 5),
    config=config,
    resolution=100,
    filled=True
)
```

**Use:** Quick plotting from mathematical functions

---

## 📋 COMPLETE API

### **`create_contour_plot()` Parameters:**

```python
create_contour_plot(
    X,                             # 2D array (from meshgrid)
    Y,                             # 2D array (from meshgrid)
    Z,                             # 2D array (function values)
    config=None,                   # PlotConfig
    filled=True,                   # Show filled contours
    lines=False,                   # Show line contours
    levels=None,                   # Number or list of levels
    cmap='viridis',                # Colormap name
    labels=False,                  # Show contour labels
    label_fontsize=9,              # Label font size
    label_format='%1.1f',          # Label format string
    cbar=True,                     # Show color bar
    cbar_label=None,               # Color bar label
    line_colors='black',           # Contour line color
    line_widths=1.0,               # Contour line width
    line_styles='solid',           # Line style
    alpha=1.0,                     # Transparency
    vmin=None,                     # Min colormap value
    vmax=None                      # Max colormap value
) → (fig, ax)
```

---

### **`create_contour_from_function()` Convenience:**

```python
create_contour_from_function(
    func,                          # Function(x, y) → z
    x_range,                       # (x_min, x_max)
    y_range,                       # (y_min, y_max)
    config=None,                   # PlotConfig
    resolution=100,                # Grid resolution
    **kwargs                       # → create_contour_plot
) → (fig, ax)
```

**Automatically creates meshgrid and evaluates function!**

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Parameter Space Exploration**

```python
# Generate parameter space
alpha = np.linspace(0.1, 2.0, 100)
beta = np.linspace(0.5, 3.0, 100)
Alpha, Beta = np.meshgrid(alpha, beta)

# Performance function
Performance = compute_performance(Alpha, Beta)

config = PlotConfig(
    title='Parameter Optimization Landscape',
    x_label='Parameter α',
    y_label='Parameter β'
)

fig, ax = create_contour_plot(
    Alpha, Beta, Performance, config,
    filled=True,
    lines=True,
    levels=15,
    line_colors='black',
    line_widths=0.5,
    labels=True,
    cbar_label='Performance Score'
)

# Mark optimal point
opt_idx = np.unravel_index(Performance.argmax(), Performance.shape)
ax.plot(Alpha[opt_idx], Beta[opt_idx], 'r*', markersize=15)
```

**Perfect for:** Optimization studies, parameter tuning

---

### **Example 2: Temperature Distribution**

```python
# Spatial coordinates
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

# Temperature field
Temperature = compute_temperature_field(X, Y)

config = PlotConfig(
    title='Temperature Distribution',
    x_label='Position X (cm)',
    y_label='Position Y (cm)'
)

fig, ax = create_contour_plot(
    X, Y, Temperature, config,
    filled=True,
    lines=True,
    cmap='RdYlBu_r',  # Red-Yellow-Blue
    line_colors='black',
    line_widths=0.5,
    cbar_label='Temperature (°C)'
)
```

**Perfect for:** Field visualization, spatial data

---

### **Example 3: Gradient Field**

```python
# Coarse grid for vectors
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Fine grid for contours
x_fine = np.linspace(-2, 2, 100)
y_fine = np.linspace(-2, 2, 100)
X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
Potential = X_fine**2 + Y_fine**2

# Gradient
U = -2 * X  # ∂V/∂x
V = -2 * Y  # ∂V/∂y

# Create plot
fig, ax = plt.figure(), plt.gca()
cs = ax.contour(X_fine, Y_fine, Potential, levels=10)
ax.clabel(cs, inline=True, fontsize=8)
ax.quiver(X, Y, U, V, color='red')
```

**Perfect for:** Vector fields, gradient visualization

---

### **Example 4: Publication Style**

```python
config = PlotConfig(
    title='Field Distribution',
    title_weight='normal',
    x_label='X (mm)',
    y_label='Y (mm)',
    tick_label_size=10
)

fig, ax = create_contour_plot(
    X, Y, Z, config,
    filled=True,
    lines=True,
    levels=12,
    cmap='viridis',
    line_colors='black',
    line_widths=0.5,
    alpha=0.8,
    cbar_label='Field Strength'
)

save_plot(fig, 'figure1.png', dpi=300)
```

---

## 💡 DESIGN TIPS

### **Tip 1: Choose Right Colormap**

```python
# Sequential: continuous variation
cmap='viridis'  # General (default)
cmap='plasma'   # High contrast
cmap='YlOrRd'   # Yellow-Orange-Red

# Diverging: data around center
cmap='RdBu_r'   # Red-Blue (reversed)
cmap='coolwarm' # Cool-Warm
cmap='seismic'  # Blue-White-Red
```

### **Tip 2: Number vs List of Levels**

```python
# Number: automatic spacing
levels=10

# List: specific values
levels=[0, 0.25, 0.5, 0.75, 1.0]
```

### **Tip 3: Combine Filled + Lines**

```python
# Filled for overview, lines for precise values
filled=True,
lines=True,
line_colors='black',
line_widths=0.5
```

### **Tip 4: Label Important Contours**

```python
# Add labels to line contours
labels=True,
label_fontsize=9,
label_format='%1.2f'  # Two decimals
```

### **Tip 5: Use From Function for Quick Plots**

```python
# Instead of creating meshgrid manually
fig, ax = create_contour_from_function(
    lambda x, y: np.sin(x) * np.cos(y),
    (-5, 5), (-5, 5),
    config
)
```

---

## 📊 REALISTIC USE CASES

### **Thesis - Response Surface:**

```python
# Design of experiments
factor1 = np.linspace(low1, high1, 50)
factor2 = np.linspace(low2, high2, 50)
F1, F2 = np.meshgrid(factor1, factor2)

# Fitted response
Response = fitted_model(F1, F2)

fig, ax = create_contour_plot(
    F1, F2, Response, config,
    filled=True,
    lines=True,
    labels=True,
    cbar_label='Response'
)
```

### **Engineering - Stress Analysis:**

```python
# 2D stress field
x = np.linspace(0, plate_width, 200)
y = np.linspace(0, plate_height, 200)
X, Y = np.meshgrid(x, y)

Stress = compute_stress_field(X, Y, load, boundary)

fig, ax = create_contour_plot(
    X, Y, Stress, config,
    filled=True,
    cmap='jet',
    cbar_label='Stress (MPa)'
)
```

### **Physics - Potential Field:**

```python
def potential(x, y):
    # Electric potential from charges
    return compute_potential(x, y, charges)

fig, ax = create_contour_from_function(
    potential,
    x_range=(-5, 5),
    y_range=(-5, 5),
    config=config,
    filled=True,
    lines=True,
    cbar_label='Potential (V)'
)
```

### **Optimization - Objective Function:**

```python
# 2D objective landscape
param1 = np.linspace(bounds1[0], bounds1[1], 100)
param2 = np.linspace(bounds2[0], bounds2[1], 100)
P1, P2 = np.meshgrid(param1, param2)

Objective = evaluate_objective(P1, P2)

fig, ax = create_contour_plot(
    P1, P2, Objective, config,
    filled=True,
    levels=20,
    cbar_label='Objective Value'
)

# Mark optimum
ax.plot(opt[0], opt[1], 'r*', markersize=20, label='Optimum')
ax.legend()
```

---

## ✅ COMPATIBILITY

All PlotConfig options work identically:
- Text formatting
- Grid settings
- Figure size
- Tick labels

**Mix and match:**

```python
config = PlotConfig(
    tick_label_size=10,
    show_grid=True,
    figure_width=10,
    figure_height=8
)

# Works for all plot types
fig, ax = create_line_plot(series, config)
fig, ax = create_contour_plot(X, Y, Z, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Filled contour:**
```python
fig, ax = create_contour_plot(X, Y, Z, config, filled=True)
```

### **Line with labels:**
```python
fig, ax = create_contour_plot(X, Y, Z, config, 
                              filled=False, lines=True, labels=True)
```

### **Both:**
```python
fig, ax = create_contour_plot(X, Y, Z, config, 
                              filled=True, lines=True)
```

### **Custom levels:**
```python
levels = [0, 0.25, 0.5, 0.75, 1.0]
fig, ax = create_contour_plot(X, Y, Z, config, levels=levels)
```

### **From function:**
```python
fig, ax = create_contour_from_function(func, (-5,5), (-5,5), config)
```

### **Custom colormap:**
```python
fig, ax = create_contour_plot(X, Y, Z, config, cmap='coolwarm')
```

---

## 📚 EXAMPLES

See `examples/contour_examples.py` for 10 complete working examples:

1. **Basic filled** - Simple contour
2. **Line with labels** - Labeled lines
3. **Both** - Filled + lines
4. **Custom levels** - Specific values
5. **Custom colormap** - Coolwarm
6. **From function** - Convenience function
7. **Multiple** - Subplots with contours
8. **Parameter space** - Optimization landscape
9. **Gradient field** - Vector + contour
10. **Publication** - Clean professional style

**Run them:**

```powershell
cd examples
python contour_examples.py
```

**Creates 10 PNG files demonstrating all features!**

---

## 📈 WHEN TO USE CONTOUR PLOTS

| Use Case | Contour Plot | Alternative |
|----------|--------------|-------------|
| 2D functions | ✅ Perfect | 3D surface |
| Parameter spaces | ✅ Perfect | Heatmap |
| Field visualization | ✅ Perfect | Streamplot |
| Level sets | ✅ Perfect | 3D isosurface |
| Optimization landscapes | ✅ Perfect | Scatter |

---

## 🎓 READING CONTOUR PLOTS

### **Contour Lines:**
- Each line = constant function value
- Close together = steep gradient
- Far apart = gradual change
- Circular = local max/min
- Saddle point = lines cross

### **Filled Contours:**
- Color indicates value
- Smooth transitions show continuity
- Sharp boundaries = discontinuities

### **Labels:**
- Numbers on lines = exact values
- Useful for quantitative analysis

---

## 🔬 THESIS APPLICATIONS

### **Response Surface Methodology:**
- Design of experiments
- Factor interactions
- Optimal conditions

### **Field Visualization:**
- Temperature distributions
- Pressure fields
- Potential fields

### **Optimization:**
- Parameter landscapes
- Objective function visualization
- Constraint visualization

### **Spatial Analysis:**
- Spatial patterns
- Geographic data
- Concentration profiles

---

**Contour plots with comprehensive customization are complete!** 🗺️

**Phase 2 Progress:** 4 of 6 (67%)  
**Next: Violin plots or 3D surfaces?** 🚀
