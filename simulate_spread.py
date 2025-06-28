import numpy as np
import rasterio
import matplotlib.pyplot as plt

def simulate_fire_spread(initial_fire_map, wind_dir_map, slope_map, fuel_map, hours=3):
    spread_map = np.copy(initial_fire_map)
    for hour in range(hours):
        new_map = spread_map.copy()
        for i in range(1, spread_map.shape[0]-1):
            for j in range(1, spread_map.shape[1]-1):
                if spread_map[i, j] == 1:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            ni, nj = i + dx, j + dy
                            if spread_map[ni, nj] == 0:
                                fire_chance = 0.2 + 0.1 * slope_map[ni, nj] + 0.1 * fuel_map[ni, nj]
                                if np.random.rand() < fire_chance:
                                    new_map[ni, nj] = 1
        spread_map = new_map.copy()
    return spread_map
