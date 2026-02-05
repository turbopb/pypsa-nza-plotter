# 3D Surface Plots - PlotLib v2.9.0 🏔️

## ✅ 3D SURFACE PLOTS COMPLETE! PHASE 2: 83% DONE!

3D surface plot support for **visualizing 3D functions**, response surfaces, and field distributions. Perfect for thesis work!

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Plot Types:**
- ✅ **Surface plots** - Filled 3D surfaces
- ✅ **Wireframe plots** - Line-based 3D frames
- ✅ **Combined** - Surface + wireframe overlay

### **Customization:**
- ✅ **Colormaps** - Any matplotlib colormap
- ✅ **Viewing angles** - Elevation and azimuth control
- ✅ **Contour projections** - Project contours on bottom plane
- ✅ **Transparency** - Alpha control
- ✅ **Edge styling** - Color, width

### **Convenience:**
- ✅ **From meshgrid** - X, Y, Z arrays
- ✅ **From function** - Direct function evaluation

---

## 📝 QUICK START

### **Basic 3D Surface:**

```python
from plotlib import create_surface_plot, save_plot
from models import PlotConfig
import numpy as np

# Generate data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Config
config = PlotConfig(
    title='3D Surface Plot',
    x_label='X',
    y_label='Y'
)

# Create surface
fig, ax = create_surface_plot(X, Y, Z, config)
ax.set_zlabel('Z')

save_plot(fig, 'surface.png')
```

---

## 📊 ALL SURFACE TYPES

### **1. Surface Plot (Filled)**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    plot_type='surface',
    cbar_label='Z Value'
)
ax.set_zlabel('Z')
```

**Use:** Show continuous 3D surface

---

### **2. Wireframe Plot**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    plot_type='wireframe',
    cbar=False
)
ax.set_zlabel('Z')
```

**Use:** Show structure clearly, less visual clutter

---

### **3. Combined (Surface + Wireframe)**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    plot_type='both',
    alpha=0.7
)
ax.set_zlabel('Z')
```

**Use:** Best of both - color and structure

---

### **4. With Contour Projections**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    contour_proj=True,
    cbar_label='Z'
)
ax.set_zlabel('Z')
```

**Use:** Show contours on bottom plane for reference

---

### **5. From Function (Convenience)**

```python
from plotlib import create_surface_from_function

def my_function(x, y):
    return np.sin(x) * np.cos(y)

fig, ax = create_surface_from_function(
    my_function,
    x_range=(-5, 5),
    y_range=(-5, 5),
    config=config,
    resolution=50
)
ax.set_zlabel('f(x, y)')
```

**Use:** Quick plotting from mathematical functions

---

### **6. Custom Viewing Angle**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    elev=45,      # Elevation angle
    azim=-30      # Azimuthal angle
)
ax.set_zlabel('Z')
```

**Use:** Best perspective for your data

---

## 📋 COMPLETE API

### **`create_surface_plot()` Parameters:**

```python
create_surface_plot(
    X,                             # 2D meshgrid x
    Y,                             # 2D meshgrid y
    Z,                             # 2D function values
    config=None,                   # PlotConfig
    plot_type='surface',           # 'surface', 'wireframe', 'both'
    cmap='viridis',                # Colormap
    alpha=0.9,                     # Transparency
    edgecolor='none',              # Edge color
    linewidth=0,                   # Edge line width
    antialiased=True,              # Smooth shading
    cbar=True,                     # Show color bar
    cbar_label=None,               # Color bar label
    elev=30,                       # Elevation angle (degrees)
    azim=-60,                      # Azimuthal angle (degrees)
    contour_proj=False,            # Show contour projections
    contour_offset=None,           # Contour Z-offset
    vmin=None,                     # Min colormap value
    vmax=None,                     # Max colormap value
    rstride=1,                     # Row stride
    cstride=1                      # Column stride
) → (fig, ax)
```

---

### **`create_surface_from_function()` Convenience:**

```python
create_surface_from_function(
    func,                          # Function(x, y) → z
    x_range,                       # (xmin, xmax)
    y_range,                       # (ymin, ymax)
    config=None,
    resolution=50,
    **kwargs                       # → create_surface_plot
) → (fig, ax)
```

**Automatically creates meshgrid and evaluates function!**

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Response Surface**

```python
# Optimization / DOE response surface
temp = np.linspace(50, 150, 50)
pressure = np.linspace(1, 5, 50)
Temp, Press = np.meshgrid(temp, pressure)

# Yield response
Yield = compute_yield(Temp, Press)

config = PlotConfig(
    title='Yield Response Surface',
    x_label='Temperature (°C)',
    y_label='Pressure (bar)'
)

fig, ax = create_surface_plot(
    Temp, Press, Yield, config,
    cmap='RdYlGn',
    contour_proj=True,
    cbar_label='Yield (%)'
)
ax.set_zlabel('Yield (%)')

# Mark optimum
opt_idx = np.unravel_index(Yield.argmax(), Yield.shape)
ax.scatter(
    [Temp[opt_idx]], [Press[opt_idx]], [Yield[opt_idx]],
    color='red', s=100, marker='*'
)
```

**Perfect for:** Design of experiments, optimization

---

### **Example 2: Mathematical Function**

```python
def ripple(x, y):
    r = np.sqrt(x**2 + y**2)
    return np.sin(r) / (r + 0.1)

fig, ax = create_surface_from_function(
    ripple,
    x_range=(-10, 10),
    y_range=(-10, 10),
    config=config,
    resolution=60,
    cmap='plasma'
)
ax.set_zlabel('f(x, y)')
```

**Perfect for:** Mathematical visualization, teaching

---

### **Example 3: Field Distribution**

```python
# Potential field
X, Y = np.meshgrid(x_positions, y_positions)
Potential = compute_potential_field(X, Y)

config = PlotConfig(
    title='Potential Field Distribution',
    x_label='X Position (mm)',
    y_label='Y Position (mm)'
)

fig, ax = create_surface_plot(
    X, Y, Potential, config,
    cmap='viridis',
    alpha=0.95,
    edgecolor='gray',
    linewidth=0.1,
    cbar_label='Potential (V)'
)
ax.set_zlabel('Potential (V)')
```

**Perfect for:** Field visualization, spatial data

---

### **Example 4: Publication Style**

```python
config = PlotConfig(
    title='Surface Plot',
    title_weight='normal',
    x_label='X',
    y_label='Y',
    tick_label_size=9
)

fig, ax = create_surface_plot(
    X, Y, Z, config,
    cmap='viridis',
    alpha=0.95,
    elev=25,
    azim=-65,
    cbar_label='Z'
)
ax.set_zlabel('Z', fontsize=10)

save_plot(fig, 'figure1.png', dpi=300)
```

---

## 💡 DESIGN TIPS

### **Tip 1: Choose Plot Type by Purpose**

```python
# Overview of shape: surface
plot_type='surface'

# Show structure clearly: wireframe
plot_type='wireframe'

# Both shape and structure: combined
plot_type='both', alpha=0.7
```

### **Tip 2: Adjust Viewing Angle**

```python
# Standard view
elev=30, azim=-60

# Top-down view
elev=90, azim=-90

# Low angle view
elev=10, azim=-45
```

### **Tip 3: Use Contour Projections**

```python
# Helps understand 2D structure
contour_proj=True
```

### **Tip 4: Choose Colormap by Data**

```python
# Sequential: viridis, plasma, inferno
cmap='viridis'

# Diverging: coolwarm, seismic, RdBu_r
cmap='coolwarm'

# Perceptual: YlOrRd, RdYlGn
cmap='RdYlGn'
```

### **Tip 5: Resolution vs Performance**

```python
# Low resolution: faster, coarser
resolution=30

# Medium resolution: balanced
resolution=50

# High resolution: slower, smoother
resolution=100
```

---

## 📊 REALISTIC USE CASES

### **Thesis - Response Surface Methodology:**

```python
# DOE response surface
factor1 = np.linspace(low1, high1, 50)
factor2 = np.linspace(low2, high2, 50)
F1, F2 = np.meshgrid(factor1, factor2)

Response = fitted_model(F1, F2)

fig, ax = create_surface_plot(
    F1, F2, Response, config,
    contour_proj=True,
    cbar_label='Response'
)

# Mark design points
ax.scatter(design_x, design_y, design_z, 
          color='red', s=50, marker='o')
```

### **Engineering - Stress Distribution:**

```python
# 3D stress field
X, Y = np.meshgrid(x_coords, y_coords)
Stress = compute_stress(X, Y, load, boundary)

fig, ax = create_surface_plot(
    X, Y, Stress, config,
    cmap='jet',
    cbar_label='Stress (MPa)'
)
ax.set_zlabel('Stress (MPa)')
```

### **Physics - Potential Field:**

```python
def potential(x, y):
    # Compute potential from charges
    return compute_potential(x, y, charges)

fig, ax = create_surface_from_function(
    potential,
    x_range=(-5, 5),
    y_range=(-5, 5),
    config=config,
    cbar_label='Potential (V)'
)
```

### **Mathematics - Function Visualization:**

```python
# Visualize complex function
def f(x, y):
    return np.sin(x) * np.cos(y) * np.exp(-(x**2 + y**2)/5)

fig, ax = create_surface_from_function(
    f,
    x_range=(-3, 3),
    y_range=(-3, 3),
    config=config,
    resolution=60,
    contour_proj=True
)
```

---

## ✅ COMPATIBILITY

All PlotConfig options work identically:
- Text formatting
- Figure size
- Tick labels
- Title styling

**Mix and match:**

```python
config = PlotConfig(
    tick_label_size=9,
    figure_width=10,
    figure_height=8,
    title_weight='normal'
)

# Works for all plot types
fig, ax = create_line_plot(series, config)
fig, ax = create_surface_plot(X, Y, Z, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Basic surface:**
```python
fig, ax = create_surface_plot(X, Y, Z, config)
ax.set_zlabel('Z')
```

### **Wireframe:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, plot_type='wireframe')
```

### **Both:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, plot_type='both')
```

### **From function:**
```python
fig, ax = create_surface_from_function(func, (-5,5), (-5,5), config)
```

### **With contours:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, contour_proj=True)
```

### **Custom view:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, elev=45, azim=-30)
```

---

## 📚 EXAMPLES

See `examples/surface_examples.py` for 10 complete working examples:

1. **Basic surface** - Simple 3D surface
2. **Wireframe** - Wireframe only
3. **Both** - Surface + wireframe
4. **Custom colormap** - Coolwarm
5. **Contour projections** - Bottom contours
6. **From function** - Direct function
7. **Viewing angles** - Two different views
8. **Response surface** - Optimization
9. **Mathematical** - Complex function
10. **Publication** - Clean professional

**Run them:**

```powershell
cd examples
python surface_examples.py
```

**Creates 11 PNG files demonstrating all features!**

---

## 📈 WHEN TO USE 3D SURFACE PLOTS

| Use Case | 3D Surface | Alternative |
|----------|------------|-------------|
| 3D functions | ✅ Perfect | Contour plot |
| Response surfaces | ✅ Perfect | Contour plot |
| Field distributions | ✅ Perfect | Heatmap |
| Optimization landscapes | ✅ Perfect | Contour plot |
| Mathematical visualization | ✅ Perfect | Multiple 2D |

---

## 🎓 READING 3D SURFACES

### **Surface Features:**
- **Peaks** - Local maxima
- **Valleys** - Local minima
- **Ridges** - Extended maxima
- **Saddle points** - Local extrema in different directions

### **Viewing Angles:**
- **elev=30, azim=-60** - Standard view
- **elev=90** - Top-down (becomes 2D)
- **elev=0** - Side view
- **Rotate azim** - Different horizontal perspectives

### **Colormaps:**
- **Sequential** - One direction (low to high)
- **Diverging** - Two directions from center
- Match colormap to data type!

---

## 🔬 THESIS APPLICATIONS

### **Response Surface Methodology:**
- Design of experiments
- Factor optimization
- Interaction visualization

### **Field Visualization:**
- Temperature distributions
- Pressure fields
- Potential fields
- Concentration profiles

### **Optimization:**
- Objective function landscapes
- Constraint surfaces
- Parameter spaces

### **Mathematical Analysis:**
- Function visualization
- Multivariable calculus
- Partial derivatives

---

**3D surface plots with comprehensive customization are complete!** 🏔️

**Phase 2 Progress:** 5 of 6 (83%)  
**Almost done! Only violin plots remain (optional)** 🚀
