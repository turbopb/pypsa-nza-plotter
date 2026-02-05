"""
Utility helpers for pypsa-nza-plotter.

These helpers intentionally remain lightweight wrappers around matplotlib
functionality. They exist primarily to standardise common research workflows
such as saving publication-quality figures with consistent defaults.
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

import matplotlib.figure


PathLike = Union[str, Path]


def save_plot(
    fig: matplotlib.figure.Figure,
    filepath: PathLike,
    *,
    dpi: int = 300,
    transparent: bool = False,
    bbox_inches: str = "tight",
    pad_inches: float = 0.02,
) -> Path:
    """
    Save a matplotlib figure with sensible publication defaults.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure object returned by pypsa-nza-plotter plotting functions.

    filepath : str or Path
        Output file path (extension determines format, e.g. .png, .pdf, .svg).

    dpi : int, optional
        Output resolution. Default is 300 (publication standard).

    transparent : bool, optional
        Whether to save with transparent background.

    bbox_inches : str, optional
        Bounding box behaviour passed to matplotlib. Default is "tight".

    pad_inches : float, optional
        Padding around the figure.

    Returns
    -------
    Path
        The resolved output path.

    Notes
    -----
    This function does not close the figure. Users retain control over
    figure lifecycle.
    """

    path = Path(filepath).expanduser().resolve()

    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        path,
        dpi=dpi,
        transparent=transparent,
        bbox_inches=bbox_inches,
        pad_inches=pad_inches,
    )

    return path
