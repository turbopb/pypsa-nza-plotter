#!/usr/bin/env python3
"""
PlotLib Interactive Display Example
"""

# SET INTERACTIVE BACKEND (add these 2 lines BEFORE importing pyplot)
import matplotlib
matplotlib.use('Qt5Agg')  # or 'Qt5Agg' if you have PyQt5

import pandas as pd
import matplotlib.pyplot as plt


from models import PlotConfig, SeriesConfig
from plotlib import create_line_plot


# Sample data
data = {
    'Year': [2020, 2021, 2022, 2023, 2024],
    'Solar': [100, 150, 220, 310, 450],
    'Wind': [200, 280, 380, 490, 620]
}
df = pd.DataFrame(data)

# Plot configuration
plot_config = PlotConfig(
    title="Renewable Energy Growth",
    x_label="Year",
    y_label="Capacity (GW)",
    figure_width=10,
    figure_height=6,
    dpi=150,
    show_grid=True,
    show_legend=True
)

# Series configurations
series_configs = [
    SeriesConfig(
        x=df['Year'],
        y=df['Solar'],
        label='Solar',
        color='#FF9500',
        line_width=2.0,
        marker='o',
        marker_size=8
    ),
    SeriesConfig(
        x=df['Year'],
        y=df['Wind'],
        label='Wind',
        color='#0066CC',
        line_width=2.0,
        marker='s',
        marker_size=8
    )
]

# Create plot
fig, ax = create_line_plot(series_configs, plot_config)

# Show interactively
plt.show()