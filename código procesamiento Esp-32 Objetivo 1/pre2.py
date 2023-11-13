# Define the input and output file paths
input_file_path = 'output0.txt'    # Replace with your input file path
output_file_path = 'output1.txt'  # Replace with your output file path

# Read data from the input file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Process and extract timestamp, signal power, and information element IDs
processed_data = []
for line in lines:
    parts = line.strip().split(' ')
    timestamp = parts[0]
    signal_power = parts[1]
    information_elements = parts[2:]  # Skip the timestamp, signal, MAC, and channel
    ids = [element.split()[0] for element in information_elements[::3]]
    processed_data.append((timestamp, signal_power, ids))

# Save processed data to the output file
with open(output_file_path, 'w') as output_file:
    for timestamp, signal_power, ids in processed_data:
        output_file.write(f"{timestamp},{signal_power},[{', '.join(ids)}]\n")

