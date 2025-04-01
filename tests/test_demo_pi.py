from demo_pi import calculate_area, calculate_volume
import numpy as np

def test_calculate_area():
    assert round(calculate_area(3), 2) == round(np.pi * 9, 2)

def test_calculate_volume():
    assert round(calculate_volume(3), 2) == round((4 / 3) * np.pi * 27, 2)
