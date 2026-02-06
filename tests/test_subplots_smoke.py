import matplotlib
matplotlib.use("Agg")

import numpy as np
from pypsa_nza_plotter import PlotConfig, create_subplots, save_plot

def test_subplots_smoke(tmp_path):
    cfg = PlotConfig(title="subplot test")
    fig, axes = create_subplots(2, 1, cfg, sharex=True, subplot_titles=["a", "b"])

    x = np.linspace(0, 1, 10)
    axes[0].plot(x, x)
    axes[1].plot(x, x**2)

    out = tmp_path / "subplots.png"
    save_plot(fig, out, dpi=150)
    assert out.exists()
