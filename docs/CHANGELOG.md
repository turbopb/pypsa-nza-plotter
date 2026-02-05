# Changelog

All notable changes to PlotLib v2 are documented in this file.

---

## [2.4.1] - 2025-12-30 - Line Plot Examples

### Added - Line Plot Examples
- Comprehensive line plot examples (10 examples)
- Basic line plot
- Multiple series (3 functions)
- Line styles comparison (4 styles)
- Line widths comparison (4 widths)
- Pure scatter plot (markers only)
- Line with markers
- Custom colors and styling
- Publication-ready scientific plot
- Different marker styles (5 markers)
- Exponential growth/decay curves

### Documentation
- Complete line plot guide (LINE_PLOTS_COMPLETE.md)
- API reference for line plots
- Design tips and best practices

### Summary
- **Examples:** 56 total (10 new line examples)
- **Documentation:** 12 guides (1 new)
- **Status:** Phase 1 Complete with Full Line Documentation

---

## [2.4.0] - 2025-12-29 - PHASE 1 COMPLETE ✅

### Added - Pie Charts
- Pie chart plotter with comprehensive customization
- Simple pie charts with custom colors
- Donut charts (pie with hole in center)
- Exploded slices (pull out specific wedges)
- Cross-hatching support for B&W publications
- Per-slice edge colors and widths
- Configurable start angle and rotation
- Show/hide percentages and labels
- 9 complete working examples

### Fixed
- Unpacking error when `show_percentages=False` in pie charts

### Summary
- **Plot Types:** 6 of 6 complete (100%)
- **Examples:** 46 total working examples
- **Status:** Phase 1 Complete, Production Ready

---

## [2.3.0] - 2025-12-29 - Area Plots

### Added - Area Plots
- Area plot plotter with comprehensive customization
- Single area (fill under curve)
- Stacked areas (multiple layers)
- Fill between two curves (confidence intervals)
- Overlapping areas with transparency
- Cross-hatching support for fills
- Edge color and width control
- Line on/off toggle with custom styling
- Line width and style customization
- 8 complete working examples

### Documentation
- Complete area plot guide
- Design tips and use cases
- Publication-ready B&W examples

---

## [2.2.0] - 2025-12-29 - Histograms

### Added - Histograms
- Histogram plotter for frequency distributions
- Single histogram (basic distribution)
- Overlapping histograms (compare distributions)
- Stacked histograms (cumulative view)
- Density (normalized) histograms
- Cumulative distribution function (CDF)
- Custom bin edges and ranges
- Cross-hatching support
- Edge color and width control
- 7 basic examples + 5 customization examples

### Fixed
- SeriesConfig now allows `x=None` for histograms (only `y` required)
- `__post_init__` handles `x=None` correctly

### Documentation
- Complete histogram guide
- Customization examples
- Statistical use cases

---

## [2.1.0] - 2025-12-29 - Bar Charts

### Added - Bar Charts
- Bar chart plotter with full customization
- Single, grouped, and stacked bar charts
- Horizontal and vertical orientations
- Custom bar widths
- Cross-hatching support for B&W publications
- Edge color and width control per series
- 6 basic examples + 8 customization examples

### Added - Cross-Hatching
- Complete hatch pattern support (`/`, `\`, `|`, `-`, `+`, `x`, `o`, `.`, `*`)
- Density control (`/`, `//`, `///`)
- Added to SeriesConfig as `hatch` attribute

### Fixed
- Attribute naming errors in bar plotter:
  - `marker_edge_color` → `marker_edgecolor`
  - `marker_edge_width` → `marker_edgewidth`
  - `grid_width` → `grid_linewidth`
  - `legend_frame` → `legend_frameon`
  - `legend_frame_alpha` → `legend_framealpha`
- Legend warnings when `show_legend=False`
- Fixed in both bar_plotter and line_plotter

### Documentation
- Complete bar chart guide
- Bar customization guide with examples
- Publication-ready B&W patterns

---

## [2.0.1] - 2025-12-28 - Extended PlotConfig

### Added - PlotConfig Extensions
- Title formatting: `title_weight`, `title_style`, `title_color`, `title_pad`
- Axis label formatting: `axis_label_color`, `axis_label_style`
- Tick label color: `tick_label_color`
- Legend weights: `legend_font_weight`, `legend_title_weight`
- Week separator customization in time-series:
  - `label_y_position` (default changed to 0.1)
  - `label_fontsize`, `label_color`, `label_weight`

### Changed
- Default title weight: `'bold'` → `'normal'`
- Default week label position: `0.95` → `0.1` (bottom instead of top)
- Week label vertical alignment: `'top'` → `'bottom'`

### Documentation
- Extended PlotConfig documentation
- Configuration examples

---

## [2.0.0] - 2025-12-27 - Consolidation & Time-Series

### Added - Initial Release
- Line and scatter plot support
- Time-series utilities:
  - `plot_timeseries()` for CSV data
  - `add_week_separators()` with customization
  - `add_month_separators()`
  - `add_boundary_lines()`
  - Fill-under-curve support
- Modular architecture:
  - `plotlib/` - Main plotting modules
  - `models/` - Configuration classes
  - `examples/` - Working examples

### Added - Configuration System
- `PlotConfig` - Global plot configuration (50+ parameters)
- `SeriesConfig` - Series-specific configuration
- Comprehensive text formatting
- Grid, legend, spine controls
- Figure size and DPI settings

### Documentation
- Consolidation guide
- Time-series examples
- Architecture overview

---

## Design Decisions

### Why One Function Per Plot Type?
- **Clarity:** No ambiguity about which function to use
- **Debuggability:** Easy to trace errors
- **Simplicity:** "One clear way" to do each thing
- **Maintainability:** Easier to update and extend

### Why Same Config Classes?
- **Consistency:** Learn once, use everywhere
- **Composability:** Easy to switch plot types
- **Predictability:** Same options work the same way

### Why Cross-Hatching?
- **Publications:** Essential for B&W journals
- **Accessibility:** Helps colorblind users
- **Professional:** IEEE/ACM standard practice

### Why Return (fig, ax)?
- **Composability:** Further customization possible
- **Standard:** Follows matplotlib conventions
- **Flexibility:** Can add to existing figures

---

## Bug Fixes Summary

### Phase 1 Development (Dec 27-29, 2025)

**Total Bugs Fixed:** 8

1. ✅ `marker_edge_color` → `marker_edgecolor` (attribute naming)
2. ✅ `marker_edge_width` → `marker_edgewidth` (attribute naming)
3. ✅ `grid_width` → `grid_linewidth` (attribute naming)
4. ✅ `legend_frame` → `legend_frameon` (attribute naming)
5. ✅ `legend_frame_alpha` → `legend_framealpha` (attribute naming)
6. ✅ Legend warning when `show_legend=False` (conditional check)
7. ✅ SeriesConfig x parameter requirement for histograms (made optional)
8. ✅ Pie chart unpacking when `show_percentages=False` (conditional unpack)

**All bugs identified and fixed during development. No known issues remain.**

---

## Statistics

### Development Timeline
- **Start Date:** December 27, 2025
- **End Date:** December 29, 2025
- **Duration:** 3 days (~4-5 hours actual work)
- **Status:** Phase 1 Complete ✅

### Code Metrics
- **Plot Types:** 6
- **Modules:** 6 plotters + 2 models
- **Examples:** 46 working examples
- **Documentation:** 8 comprehensive guides
- **Lines of Code:** ~3,000
- **Configuration Options:** 50+

### Quality Metrics
- **Bug Count:** 0 (all fixed)
- **Example Success Rate:** 100%
- **Documentation Coverage:** Complete
- **API Consistency:** Fully consistent

---

## Future Plans (Phase 2+)

### Phase 2: Advanced Plot Types
- 3D plots
- Contour plots
- Box plots and violin plots
- Heatmaps
- Subplots and faceting

### Phase 3: GUI Integration
- PyQt5 CSV editor integration
- Interactive plotting
- Real-time updates
- YAML config export/import

### Phase 4: Extensions
- Additional data formats
- Database connectivity
- Animation support
- Interactive widgets

---

## Contributors

- Phil - Primary Developer

---

## Version Numbering

Format: `MAJOR.MINOR.PATCH`

- **MAJOR:** Phase completion (1.x = prototype, 2.x = Phase 1)
- **MINOR:** New plot type or major feature
- **PATCH:** Bug fixes and small improvements

**Current:** 2.4.0 (Phase 1 Complete)

---

## Notes

### Lessons Learned

1. **Start Simple:** Basic functionality first, customization later
2. **Test Early:** Example-driven development catches issues fast
3. **Consistency Matters:** Same patterns everywhere = easier to use
4. **One Clear Way:** Avoid multiple approaches for same task
5. **Documentation Essential:** Examples > explanations

### Design Philosophy

> "Simple things should be simple, complex things should be possible."

PlotLib v2 makes simple plots trivial and complex customizations straightforward.

---

**Phase 1 Complete!** 🎉  
Ready for production use in academic work, thesis, and professional reports.
