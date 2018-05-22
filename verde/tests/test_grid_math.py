"""
Test the grid math functions
"""
import numpy as np
import numpy.testing as npt

from ..coordinates import grid_coordinates, scatter_points
from ..grid_math import block_reduce


def test_block_reduce():
    "Try reducing constant values in a regular grid"
    region = (-5, 0, 5, 10)
    east, north = grid_coordinates(region, spacing=0.1, pixel_register=True)
    data = 20*np.ones_like(east)
    block_coords, block_data = block_reduce((east, north), data, np.mean,
                                            spacing=1)
    assert len(block_coords[0]) == 25
    assert len(block_coords[1]) == 25
    assert len(block_data) == 25
    npt.assert_allclose(block_data, 20)
    npt.assert_allclose(block_coords[0][:5], np.linspace(-4.5, -0.5, 5))
    npt.assert_allclose(block_coords[1][::5], np.linspace(5.5, 9.5, 5))


def test_block_reduce_scatter():
    "Try reducing constant values in a dense enough scatter"
    region = (-5, 0, 5, 10)
    east, north = scatter_points(region, size=10000, random_state=0)
    data = 20*np.ones_like(east)
    block_coords, block_data = block_reduce((east, north), data, np.mean,
                                            spacing=1, region=region,
                                            center_coordinates=True)
    assert len(block_coords[0]) == 25
    assert len(block_coords[1]) == 25
    assert len(block_data) == 25
    npt.assert_allclose(block_data, 20)
    npt.assert_allclose(block_coords[0][:5], np.linspace(-4.5, -0.5, 5))
    npt.assert_allclose(block_coords[1][::5], np.linspace(5.5, 9.5, 5))