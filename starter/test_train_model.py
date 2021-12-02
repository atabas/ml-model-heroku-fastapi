from pathlib import Path
from train_model import train


def test_check_perf_on_slices():
    train()
    assert Path('./starter/model/model.joblib').is_file()
    assert Path('./starter/model/encoder.joblib').is_file()
    assert Path('./starter/model/lb.joblib').is_file()