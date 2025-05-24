import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 100

df = pd.DataFrame({
    'kinetic_energy': np.random.uniform(10000, 50000, n_samples),
    'potential_energy': np.random.uniform(1000, 10000, n_samples),
    'average_speed': np.random.uniform(30, 90, n_samples),
    'stops_count': np.random.randint(0, 10, n_samples),
    'trip_duration': np.random.uniform(30, 300, n_samples),
    'idle_time': np.random.uniform(5, 60, n_samples),
    'elevation_gain': np.random.uniform(0, 500, n_samples),
    'vehicle_load': np.random.uniform(1000, 4000, n_samples),
    'ambient_temperature': np.random.uniform(15, 40, n_samples),
    'tire_pressure': np.random.uniform(28, 36, n_samples),
})

df['average_fuel_consumption'] = (
    35 + 0.0001 * df['kinetic_energy']
    + 0.0002 * df['potential_energy']
    - 0.1 * df['average_speed']
    + 0.5 * df['stops_count']
    + 0.02 * df['idle_time']
    + 0.01 * df['elevation_gain']
    + 0.005 * df['vehicle_load']
    + 0.1 * (40 - df['ambient_temperature'])
    + 0.2 * (32 - df['tire_pressure'])
)

df.to_csv('data/heavy_vehicle_data.csv', index=False)
print("Dummy dataset saved to 'data/heavy_vehicle_data.csv'")