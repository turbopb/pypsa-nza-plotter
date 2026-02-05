# 3D Surface Plots - PlotLib v2.9.0 📐

## ✅ 3D SURFACE PLOTS COMPLETE! PHASE 2: 83% DONE!

3D surface plot support for **3D function visualization** with surface, wireframe, and 3D contour plots. Perfect for response surfaces, parameter spaces, and 3D data!

---

## 🎨 COMPLETE CUSTOMIZATION OPTIONS

### **Plot Types:**
- ✅ **Surface plots** - Filled 3D surfaces
- ✅ **Wireframe plots** - 3D mesh structure
- ✅ **3D contour plots** - Contour lines in 3D space

### **Customization:**
- ✅ **Colormaps** - Any matplotlib colormap
- ✅ **Viewing angles** - Elevation and azimuth control
- ✅ **Transparency** - Alpha control
- ✅ **Edge styling** - Color, width
- ✅ **Resolution** - Sampling control
- ✅ **Color bars** - Show/hide, custom labels

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
config.z_label = 'Z'

# Create surface
fig, ax = create_surface_plot(X, Y, Z, config)
save_plot(fig, 'surface.png')
```

---

## 📊 ALL PLOT TYPES

### **1. Surface Plot (Default)**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    plot_type='surface',
    cmap='viridis'
)
```

**Use:** Visualize 3D functions, response surfaces

---

### **2. Wireframe Plot**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    plot_type='wireframe',
    linewidth=1.0
)
```

**Use:** Show mesh structure, transparency needed

---

### **3. 3D Contour Plot**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    plot_type='contour3d',
    linewidth=2.0
)
```

**Use:** Show level sets in 3D space

---

### **4. From Function (Convenience)**

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
```

**Use:** Quick plotting from mathematical functions

---

### **5. Custom Viewing Angle**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    elev=20,    # Elevation angle (degrees)
    azim=-45    # Azimuth angle (degrees)
)
```

**Use:** Find best viewing angle for your data

---

## 📋 COMPLETE API

### **`create_surface_plot()` Parameters:**

```python
create_surface_plot(
    X,                             # 2D meshgrid x
    Y,                             # 2D meshgrid y
    Z,                             # 2D function values
    config=None,                   # PlotConfig
    plot_type='surface',           # 'surface', 'wireframe', 'contour3d'
    cmap='viridis',                # Colormap
    alpha=1.0,                     # Transparency
    edgecolor='none',              # Edge color
    linewidth=0.0,                 # Edge width
    cbar=True,                     # Color bar
    cbar_label=None,               # Bar label
    elev=30,                       # Elevation (degrees)
    azim=-60,                      # Azimuth (degrees)
    stride=1,                      # Sampling stride
    antialiased=True,              # Antialiasing
    shade=True,                    # Shading
    vmin=None,                     # Min colormap value
    vmax=None                      # Max colormap value
) → (fig, ax)
```

---

### **`create_surface_from_function()` Convenience:**

```python
create_surface_from_function(
    func,                          # Function(x, y) → z
    x_range,                       # (xmin, xmax)
    y_range,                       # (ymin, ymax)
    config=None,                   # PlotConfig
    resolution=50,                 # Grid resolution
    **kwargs                       # → create_surface_plot
) → (fig, ax)
```

**Automatically creates meshgrid and evaluates function!**

---

## 🎨 CUSTOMIZATION EXAMPLES

### **Example 1: Response Surface**

```python
# Parameter optimization
alpha = np.linspace(0.5, 2.5, 40)
beta = np.linspace(1.0, 4.0, 40)
Alpha, Beta = np.meshgrid(alpha, beta)

# Response function
Response = compute_response(Alpha, Beta)

config = PlotConfig(
    title='Response Surface',
    x_label='Parameter α',
    y_label='Parameter β'
)
config.z_label = 'Response'

fig, ax = create_surface_plot(
    Alpha, Beta, Response, config,
    cmap='viridis',
    edgecolor='gray',
    linewidth=0.1,
    cbar_label='Response Value'
)

# Mark optimum
opt_idx = np.unravel_index(Response.argmax(), Response.shape)
ax.scatter(
    Alpha[opt_idx], Beta[opt_idx], Response[opt_idx],
    color='red', s=100, marker='*'
)
```

**Perfect for:** Optimization, design of experiments

---

### **Example 2: Temperature Field**

```python
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(x, y)

Temperature = compute_temperature(X, Y)

config = PlotConfig(
    title='Temperature Distribution',
    x_label='Position X (cm)',
    y_label='Position Y (cm)'
)
config.z_label = 'Temperature (°C)'

fig, ax = create_surface_plot(
    X, Y, Temperature, config,
    cmap='RdYlBu_r',    # Red-Yellow-Blue
    cbar_label='Temperature (°C)'
)
```

**Perfect for:** Field visualization, spatial data

---

### **Example 3: Transparent Surface**

```python
fig, ax = create_surface_plot(
    X, Y, Z, config,
    alpha=0.6,          # Transparent
    edgecolor='black',  # Black edges
    linewidth=0.3       # Thin edges
)
```

**Perfect for:** Seeing through surfaces, showing structure

---

### **Example 4: Publication Style**

```python
config = PlotConfig(
    title='Surface Analysis',
    title_weight='normal',
    x_label='X (mm)',
    y_label='Y (mm)',
    tick_label_size=9
)
config.z_label = 'Value (units)'

fig, ax = create_surface_plot(
    X, Y, Z, config,
    cmap='viridis',
    edgecolor='gray',
    linewidth=0.1,
    alpha=0.9,
    elev=25,
    azim=-60
)

save_plot(fig, 'figure1.png', dpi=300)
```

---

## 💡 DESIGN TIPS

### **Tip 1: Choose Right Plot Type**

```python
# Solid surfaces: 'surface'
plot_type='surface'

# See structure: 'wireframe'
plot_type='wireframe'

# Level sets: 'contour3d'
plot_type='contour3d'
```

### **Tip 2: Adjust Viewing Angle**

```python
# Top-down view
elev=90, azim=0

# Side view
elev=0, azim=0

# Standard view (default)
elev=30, azim=-60
```

### **Tip 3: Use Edges for Clarity**

```python
# Show mesh structure
edgecolor='black',
linewidth=0.2
```

### **Tip 4: Transparency for Overlays**

```python
# See through surface
alpha=0.6
```

### **Tip 5: Resolution vs Performance**

```python
# Coarse (fast): 30×30
resolution=30

# Standard: 50×50
resolution=50

# Fine (slow): 100×100
resolution=100
```

---

## 📊 REALISTIC USE CASES

### **Thesis - Response Surface:**

```python
# Design of experiments
factor1 = np.linspace(low1, high1, 40)
factor2 = np.linspace(low2, high2, 40)
F1, F2 = np.meshgrid(factor1, factor2)

Response = fitted_model(F1, F2)

fig, ax = create_surface_plot(
    F1, F2, Response, config,
    cmap='viridis',
    cbar_label='Response'
)

# Mark optimal region
```

### **Engineering - Stress Distribution:**

```python
# 3D stress field
x = np.linspace(0, width, 50)
y = np.linspace(0, height, 50)
X, Y = np.meshgrid(x, y)

Stress = compute_stress(X, Y, load)

fig, ax = create_surface_plot(
    X, Y, Stress, config,
    cmap='jet',
    cbar_label='Stress (MPa)'
)
```

### **Physics - Potential Surface:**

```python
def potential(x, y):
    return compute_potential(x, y, charges)

fig, ax = create_surface_from_function(
    potential,
    x_range=(-5, 5),
    y_range=(-5, 5),
    config=config,
    cbar_label='Potential (V)'
)
```

### **Optimization - Objective Landscape:**

```python
# 2D parameter space
param1 = np.linspace(bounds1[0], bounds1[1], 50)
param2 = np.linspace(bounds2[0], bounds2[1], 50)
P1, P2 = np.meshgrid(param1, param2)

Objective = evaluate_objective(P1, P2)

fig, ax = create_surface_plot(
    P1, P2, Objective, config,
    cmap='viridis'
)

# Mark optimum
ax.scatter(opt[0], opt[1], opt_value, 
          color='red', s=200, marker='*')
```

---

## ✅ COMPATIBILITY

All PlotConfig options work:
- Text formatting
- Figure size
- Tick labels
- Grid (for 3D)

**Mix and match:**

```python
config = PlotConfig(
    tick_label_size=9,
    figure_width=10,
    figure_height=8
)

# Works for all plot types
fig, ax = create_contour_plot(X, Y, Z, config)
fig, ax = create_surface_plot(X, Y, Z, config)  # ← New!
```

---

## 🎯 QUICK REFERENCE

### **Basic surface:**
```python
fig, ax = create_surface_plot(X, Y, Z, config)
```

### **Wireframe:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, plot_type='wireframe')
```

### **3D contour:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, plot_type='contour3d')
```

### **From function:**
```python
fig, ax = create_surface_from_function(func, (-5,5), (-5,5), config)
```

### **Custom view:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, elev=20, azim=-45)
```

### **Transparent:**
```python
fig, ax = create_surface_plot(X, Y, Z, config, alpha=0.6)
```

---

## 📚 EXAMPLES

See `examples/surface3d_examples.py` for 10 complete working examples:

1. **Basic surface** - Simple 3D surface
2. **Wireframe** - Mesh structure
3. **3D contour** - Contour lines in 3D
4. **Custom colormap** - Coolwarm
5. **Custom view** - Different angles
6. **From function** - Convenience function
7. **Response surface** - Optimization
8. **Multiple** - Three surfaces
9. **Transparent** - With edges
10. **Publication** - Clean professional style

**Run them:**

```powershell
cd examples
python surface3d_examples.py
```

**Creates 10 PNG files demonstrating all features!**

---

## 📈 WHEN TO USE 3D SURFACE PLOTS

| Use Case | 3D Surface | Alternative |
|----------|------------|-------------|
| 3D functions | ✅ Perfect | Contour plot |
| Response surfaces | ✅ Perfect | Contour plot |
| Parameter spaces | ✅ Perfect | Heatmap |
| Field visualization | ✅ Perfect | Contour plot |
| Optimization landscapes | ✅ Perfect | Contour plot |

**Note:** Sometimes 2D contour plots are clearer than 3D surfaces!

---

## 🎓 VIEWING ANGLES GUIDE

### **Elevation (elev):**
- `elev=0` - Side view (horizontal)
- `elev=30` - Standard view (default)
- `elev=45` - Mid-high view
- `elev=90` - Top-down view

### **Azimuth (azim):**
- `azim=0` - Front view
- `azim=-60` - Standard view (default)
- `azim=-90` - Right side view
- `azim=180` - Back view

**Experiment to find best angle for your data!**

---

## 🔬 THESIS APPLICATIONS

### **Response Surface Methodology:**
- Design of experiments
- Factor optimization
- Interaction effects

### **Field Visualization:**
- Temperature distributions
- Stress/strain fields
- Potential surfaces

### **Parameter Studies:**
- 2D parameter sweeps
- Objective function landscapes
- Sensitivity analysis

### **3D Data:**
- Topographic data
- Spatial measurements
- Grid-based simulations

---

**3D surface plots with comprehensive customization are complete!** 📐

**Phase 2 Progress:** 5 of 6 (83%)  
**Only violin plots remain!** 🚀
