"""
Time-Series Plotting Utilities - PlotLib v2.0 (Consolidated)

FINAL VERSION - All fixes integrated

This module provides specialized functionality for time-series data:
- Load CSV with many columns, select specific ones
- Use index (time-step number) as x-axis instead of datetime
- Add week separators with centered labels
- Add boundary lines at start/end of data
- Fill area under curves
- Aggregate/sum columns

PHILOSOPHY:
-----------
Integrates seamlessly with PlotLib v2.0:
- Uses SeriesConfig for individual series
- Uses PlotConfig for global settings
- Returns standard (fig, ax) for further customization
- All features optional and composable
"""

import pandas as pd
import numpy as np
from typing import List, Optional, Union, Tuple
import matplotlib.pyplot as plt
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import SeriesConfig, PlotConfig
from plotlib import create_line_plot


# ============================================================================
# CSV LOADING AND COLUMN SELECTION
# ============================================================================

def load_timeseries_csv(
    csv_file: str,
    date_column: str = 'DATE',
    parse_dates: bool = True
) -> pd.DataFrame:
    """
    Load CSV file with time-series data.
    
    Args:
        csv_file: Path to CSV file
        date_column: Name of date/time column (default: 'DATE')
        parse_dates: Parse date column to datetime (default: True)
    
    Returns:
        pandas DataFrame with index as time-steps (0, 1, 2, ...)
    """
    df = pd.read_csv(csv_file)
    
    if parse_dates and date_column in df.columns:
        df[date_column] = pd.to_datetime(df[date_column])
    
    df = df.reset_index(drop=True)
    
    return df


def select_columns(
    df: pd.DataFrame,
    columns: Union[str, List[str]],
    date_column: str = 'DATE'
) -> Tuple[np.ndarray, np.ndarray, List[str]]:
    """
    Select specific column(s) from DataFrame.
    
    Args:
        df: DataFrame with time-series data
        columns: Column name (str) or list of column names
        date_column: Name of date column to preserve (default: 'DATE')
    
    Returns:
        (x, y, labels) where:
            x = time-step indices (0, 1, 2, ...)
            y = data values (single column or summed if multiple)
            labels = list of column names used
    """
    if isinstance(columns, str):
        columns = [columns]
    
    x = np.arange(len(df))
    
    if len(columns) == 1:
        y = df[columns[0]].values
    else:
        y = df[columns].sum(axis=1).values
    
    return x, y, columns


def aggregate_columns(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    date_column: str = 'DATE',
    operation: str = 'sum'
) -> Tuple[np.ndarray, np.ndarray, str]:
    """
    Aggregate multiple columns with specified operation.
    
    Args:
        df: DataFrame with time-series data
        columns: List of columns to aggregate (None = all except date column)
        date_column: Name of date column to exclude (default: 'DATE')
        operation: 'sum', 'mean', 'max', 'min'
    
    Returns:
        (x, y, label) where:
            x = time-step indices
            y = aggregated values
            label = description of aggregation
    """
    if columns is None:
        columns = [col for col in df.columns if col != date_column]
    
    x = np.arange(len(df))
    
    if operation == 'sum':
        y = df[columns].sum(axis=1).values
        label = f'Total ({len(columns)} columns)'
    elif operation == 'mean':
        y = df[columns].mean(axis=1).values
        label = f'Average ({len(columns)} columns)'
    elif operation == 'max':
        y = df[columns].max(axis=1).values
        label = f'Maximum ({len(columns)} columns)'
    elif operation == 'min':
        y = df[columns].min(axis=1).values
        label = f'Minimum ({len(columns)} columns)'
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    return x, y, label


# ============================================================================
# SEPARATORS AND BOUNDARIES
# ============================================================================

def add_week_separators(
    ax: plt.Axes,
    df: pd.DataFrame,
    date_column: str = 'DATE',
    color: str = '#000000',
    linestyle: str = '-',
    alpha: float = 0.8,
    linewidth: float = 2.5,
    label_weeks: bool = True,
    center_labels: bool = True,
    include_first: bool = True,
    label_y_position: float = 0.1,  # NEW: Vertical position (0-1, user prefers 0.1)
    label_fontsize: float = 8,       # NEW: Label font size
    label_color: str = '#666666',    # NEW: Label color
    label_weight: str = 'normal'     # NEW: Label font weight
) -> None:
    """
    Add vertical lines to show week boundaries with centered labels.
    
    Args:
        ax: Matplotlib axes
        df: DataFrame with date column
        date_column: Name of date column
        color: Line color (default: black)
        linestyle: Line style (default: '-' solid)
        alpha: Transparency (default: 0.8)
        linewidth: Line width (default: 2.5)
        label_weeks: Add "W##" labels (default: True)
        center_labels: Position labels in center of week (default: True)
        include_first: Include line at start of data (default: True)
        label_y_position: Vertical position for labels, 0-1 (default: 0.1 = bottom 10%)
        label_fontsize: Font size for week labels (default: 8)
        label_color: Color for week labels (default: gray)
        label_weight: Font weight for labels (default: 'normal')
    """
    if date_column not in df.columns:
        return
    
    df_copy = df.copy()
    df_copy['week'] = pd.to_datetime(df_copy[date_column]).dt.isocalendar().week
    
    week_changes = df_copy['week'].diff() != 0
    week_indices = df_copy[week_changes].index.tolist()
    
    # Draw vertical lines
    start_idx = 0 if include_first else 1
    for idx in week_indices[start_idx:]:
        ax.axvline(x=idx, color=color, linestyle=linestyle, 
                  alpha=alpha, linewidth=linewidth, zorder=2)
    
    # Add week labels
    if label_weeks:
        if center_labels:
            # FIRST WEEK - from start to first boundary
            if len(week_indices) > 0:
                start_pos = 0
                end_pos = week_indices[0]
                center_pos = (start_pos + end_pos) / 2
                week_num = df_copy.loc[0, 'week']
                
                y_pos = ax.get_ylim()[1] * label_y_position
                ax.text(center_pos, y_pos, f'W{int(week_num)}', 
                       fontsize=label_fontsize, color=label_color, 
                       fontweight=label_weight, ha='center', va='bottom')
            
            # MIDDLE WEEKS
            for i in range(len(week_indices) - 1):
                start_pos = week_indices[i]
                end_pos = week_indices[i + 1]
                center_pos = (start_pos + end_pos) / 2
                week_num = df_copy.loc[start_pos, 'week']
                
                y_pos = ax.get_ylim()[1] * label_y_position
                ax.text(center_pos, y_pos, f'W{int(week_num)}', 
                       fontsize=label_fontsize, color=label_color,
                       fontweight=label_weight, ha='center', va='bottom')
            
            # LAST WEEK
            if len(week_indices) > 0:
                start_pos = week_indices[-1]
                end_pos = len(df) - 1
                center_pos = (start_pos + end_pos) / 2
                week_num = df_copy.loc[start_pos, 'week']
                
                y_pos = ax.get_ylim()[1] * label_y_position
                ax.text(center_pos, y_pos, f'W{int(week_num)}', 
                       fontsize=label_fontsize, color=label_color,
                       fontweight=label_weight, ha='center', va='bottom')
        else:
            # Labels AT the line
            for idx in week_indices[start_idx:]:
                week_num = df_copy.loc[idx, 'week']
                y_pos = ax.get_ylim()[1] * label_y_position
                ax.text(idx, y_pos, f'W{int(week_num)}', 
                       fontsize=label_fontsize, color=label_color,
                       fontweight=label_weight, ha='left', va='bottom')


def add_boundary_lines(
    ax: plt.Axes,
    x: np.ndarray,
    color: str = '#888888',
    linestyle: str = '--',
    alpha: float = 0.7,
    linewidth: float = 0.75
) -> None:
    """
    Add thin vertical lines at start and end of data.
    
    Simple boundary markers - thin dashed lines at min and max x values.
    
    Args:
        ax: Matplotlib axes
        x: X-axis data (to get min and max)
        color: Line color (default: gray)
        linestyle: Line style (default: '--' dashed)
        alpha: Transparency (default: 0.7)
        linewidth: Line width (default: 0.75)
    """
    # Line at start
    ax.axvline(x=x.min(), color=color, linestyle=linestyle, 
              alpha=alpha, linewidth=linewidth, zorder=1)
    
    # Line at end
    ax.axvline(x=x.max(), color=color, linestyle=linestyle, 
              alpha=alpha, linewidth=linewidth, zorder=1)


# ============================================================================
# FILL UNDER CURVE
# ============================================================================

def fill_under_curve(
    ax: plt.Axes,
    x: np.ndarray,
    y: np.ndarray,
    color: str = '#0066CC',
    alpha: float = 0.3,
    baseline: float = 0.0
) -> None:
    """
    Fill area under the curve.
    
    Args:
        ax: Matplotlib axes
        x: X-axis data (time-steps)
        y: Y-axis data (values)
        color: Fill color (default: blue)
        alpha: Transparency (default: 0.3)
        baseline: Y-value to fill to (default: 0.0)
    """
    ax.fill_between(x, baseline, y, color=color, alpha=alpha)


# ============================================================================
# HIGH-LEVEL CONVENIENCE FUNCTION
# ============================================================================

def plot_timeseries(
    csv_file: str,
    column: Union[str, List[str]],
    config: Optional[PlotConfig] = None,
    date_column: str = 'DATE',
    fill: bool = True,
    fill_alpha: float = 0.2,
    week_separators: bool = False,
    boundary_lines: bool = False,
    aggregate_op: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    High-level function to plot time-series data with all features.
    
    Args:
        csv_file: Path to CSV file
        column: Column name(s) to plot
        config: PlotConfig (global settings), None = use default
        date_column: Name of date column (default: 'DATE')
        fill: Fill area under curve (default: True)
        fill_alpha: Fill transparency (default: 0.2)
        week_separators: Add vertical lines for weeks (default: False)
        boundary_lines: Add lines at start/end (default: False)
        aggregate_op: If set, aggregate with 'sum', 'mean', 'max', 'min'
    
    Returns:
        (fig, ax) - Standard matplotlib objects
    """
    df = load_timeseries_csv(csv_file, date_column=date_column)
    
    if aggregate_op:
        x, y, label = aggregate_columns(df, columns=column, operation=aggregate_op)
    else:
        x, y, column_list = select_columns(df, column)
        if len(column_list) == 1:
            label = column_list[0]
        else:
            label = f'Sum of {len(column_list)} columns'
    
    series = SeriesConfig(
        x=x, y=y,
        line_style='-',
        line_width=1.5,
        color='#0066CC',
        label=label
    )
    
    if config is None:
        config = PlotConfig(
            tick_label_size=12,
            axis_label_size=14,
            title_size=16,
            x_label='Time Step',
            y_label='Value',
            show_grid=True,
            grid_alpha=0.3
        )
    
    fig, ax = create_line_plot(series, config)
    
    if fill:
        fill_under_curve(ax, x, y, color='#0066CC', alpha=fill_alpha)
    
    if boundary_lines:
        add_boundary_lines(ax, x)
    
    if week_separators:
        add_week_separators(ax, df, date_column=date_column)
    
    return fig, ax
