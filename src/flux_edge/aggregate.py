"""Aggregate a per-pixel density map into anonymised per-zone metadata."""
import numpy as np


def zone_metadata(density_map: np.ndarray, grid=(2, 2), capacity_per_zone: float = 1.0) -> list[dict]:
    """Split the map into grid zones; return only aggregate values (no frames)."""
    rows = np.array_split(density_map, grid[0], axis=0)
    out = []
    for i, r in enumerate(rows):
        for j, z in enumerate(np.array_split(r, grid[1], axis=1)):
            out.append({"zone": f"{chr(65 + i * grid[1] + j)}",
                        "density": float(min(z.sum() / capacity_per_zone, 1.0))})
    return out
