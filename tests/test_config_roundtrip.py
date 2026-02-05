import tempfile
from pypsa_nza_plotter import PlotConfig

def test_yaml_roundtrip(tmp_path):
    cfg = PlotConfig(title="roundtrip test", tick_label_size=9)
    p = tmp_path / "t.yml"
    cfg.to_yaml(str(p))
    cfg2 = PlotConfig.from_yaml(str(p))
    assert cfg2.title == "roundtrip test"
    assert cfg2.tick_label_size == 9
