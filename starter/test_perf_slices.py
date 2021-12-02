from pathlib import Path
from perf_slices import check_perf_on_slices


def test_check_perf_on_slices():
    check_perf_on_slices()
    output_file = Path('./starter/model/perf_slices.txt')
    assert output_file.is_file()
    fline=open('./starter/model/perf_slices.txt').read().split('\n', 1)[0]
    assert "Category:workclass, Col:Private, Precision:" in fline