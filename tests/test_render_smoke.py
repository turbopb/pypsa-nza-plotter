"""
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np

from pypsa_nza_plotter import PlotConfig, SeriesConfig, create_line_plot
from pypsa_nza_plotter.utils import save_plot


def test_line_plot_smoke(tmp_path):
    x = np.linspace(0, 1, 10)
    y = np.sin(x)

    series = SeriesConfig(x=x, y=y, color="#0066CC", label="s")
    cfg = PlotConfig()

    fig, ax = create_line_plot([[series]], cfg)

    out = tmp_path / "out.png"
    save_plot(fig, out, dpi=150)
    assert out.exists()
    assert out.stat().st_size > 0


