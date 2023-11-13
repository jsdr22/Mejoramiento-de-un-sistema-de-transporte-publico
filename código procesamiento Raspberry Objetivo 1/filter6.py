from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

# Define the time interval (2 minutes)
time_interval = timedelta(minutes=1)

# Create a defaultdict to store packet counts per time interval
packet_counts = defaultdict(int)

# Read the data from the file
with open("output4_1.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            timestamp_str = parts[0]
            try:
                timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
                interval_start = timestamp - (timestamp - datetime.min) % time_interval
                packet_counts[interval_start] += 1
            except ValueError:
                print("Error parsing timestamp:", timestamp_str)

# Write the packet counts to a new text file
output_file_path = "output7.txt"
with open(output_file_path, "w") as output_file:
    for interval_start, count in sorted(packet_counts.items()):
        interval_end = interval_start + time_interval
        output_file.write(f" {count}\n")

print(f"Packet counts written to {output_file_path}")

# Read data from the text file
with open('output7.txt', 'r') as file:
    data = [int(line.strip()) for line in file]



# Calculate the mean value of the data
mean_value = np.mean(data)

# Create a wider figure
plt.figure(figsize=(12, 6))

# Create a histogram with narrower bars and adjusted color
plt.hist(data, bins=20, edgecolor='black', color='#007BA7', alpha=0.7)  # Use '#87CEEB' for sky blue

# Add a vertical line for the mean value
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean')

# Add labels and title
plt.xlabel('probe request/2m', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histograma paquetes filtrados en TM -Ids Samsung A71', fontsize=14)

# Set custom tick positions and labels for the x-axis
x_tick_ranges = np.arange(min(data), max(data) + 1, step=10)  # Adjust step as needed
plt.xticks(x_tick_ranges, fontsize=10)

# Add the mean value as a text label in the left upper corner
plt.text(0.02, 0.95, f'Mean: {mean_value:.2f}', color='red', fontsize=12, transform=plt.gca().transAxes)

# Customize grid
plt.grid(True, linestyle='--', alpha=0.5)

# Add a legend
plt.legend(loc='upper right')

# Show the histogram
plt.show()