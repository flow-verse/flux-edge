import numpy as np
from flux_edge.aggregate import zone_metadata


def test_zone_count_and_range():
    z = zone_metadata(np.full((4, 4), 0.05), grid=(2, 2), capacity_per_zone=0.2)
    assert [d["zone"] for d in z] == ["A", "B", "C", "D"]
    assert all(0 <= d["density"] <= 1 for d in z)
