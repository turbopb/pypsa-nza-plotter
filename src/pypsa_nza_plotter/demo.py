 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless-safe (CI/reviewers)

import numpy as np

from pypsa_nza_plotter import PlotConfig, SeriesConfig, create_line_plot, create_histogram, save_plot

from pypsa_nza_plotter import (
    PlotConfig,
    SeriesConfig,
    create_line_plot,
    create_histogram,
    create_subplots,
    save_plot,
)


def demo_line(outdir: Path) -> Path:
    x = np.linspace(0, 1, 400)
    y = np.sin(2 * np.pi * x)

    cfg = PlotConfig(
        title="Demo: Line plot",
        x_label="x",
        y_label="sin(2px)",
    )

    s = SeriesConfig(x=x, y=y, label="sin", color="#0066CC")

    # One subplot containing one (or many) series => list-of-lists form
    fig, ax = create_line_plot([[s]], cfg)

    out = outdir / "demo_line.png"
    save_plot(fig, out, dpi=300)
    return out


def demo_histogram(outdir: Path) -> Path:
    rng = np.random.default_rng(0)
    data = rng.normal(loc=0.0, scale=1.0, size=2000)

    cfg = PlotConfig(
        title="Demo: Histogram",
        x_label="value",
        y_label="count",
    )

    # create_histogram expects SeriesConfig objects (uses .y internally)
    s = SeriesConfig(y=data, label="N(0,1)", color="#0066CC")

    # Many of your plotters use list-of-lists input normalisation patterns.
    # Histogram_plotter expects an iterable of SeriesConfig -> pass [s].
    fig, ax = create_histogram([s], cfg)

    out = outdir / "demo_histogram.png"
    save_plot(fig, out, dpi=300)
    return out

def demo_subplots(outdir: Path) -> Path:
    x = np.linspace(0, 1, 200)

    cfg = PlotConfig(
        title="Demo: Subplots (2 x 1)",
        x_label="x",
        y_label="y",
    )

    fig, axes = create_subplots(2, 1, cfg, sharex=True, subplot_titles=["sin", "cos"])

    axes[0].plot(x, np.sin(2 * np.pi * x))
    axes[1].plot(x, np.cos(2 * np.pi * x))

    out = outdir / "demo_subplots.png"
    save_plot(fig, out, dpi=300)
    return out



def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate demo figures using pypsa-nza-plotter."
    )
    parser.add_argument(
        "--outdir",
        type=str,
        default="demo_output",
        help="Output directory for generated images (default: demo_output).",
    )
    args = parser.parse_args()

    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    created = []
    created.append(demo_line(outdir))
    created.append(demo_histogram(outdir))
    created.append(demo_subplots(outdir))


    print("\nDemo figures created:")
    for p in created:
        print(f"  - {p}")


if __name__ == "__main__":
    main()
