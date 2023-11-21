import numpy as np

time_intervals = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
vertical_positions = np.array([0.0, 1.2, 2.1, 2.9, 3.5])

displacement = vertical_positions[-1] - vertical_positions[0]  
time_duration = time_intervals[-1] - time_intervals[0]

avg_velocity = displacement / time_duration 

print("Average velocity of the projectile is: ", avg_velocity, "m/s")
