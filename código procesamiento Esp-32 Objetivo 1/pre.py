# Define the input and output file paths
input_file_path = 'prueba2_2m_esp1.txt'    # Replace with your input file path
output_file_path = 'output0.txt'  # Replace with your output file path

# Read data from the input file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Process and modify information elements as needed
processed_lines = []
for line in lines:
    parts = line.strip().split()
    timestamp = parts[0]
    power = parts[1]
    information_elements = parts[4:]  # Skip timestamp, power, MAC, and channel
    
    # Modify information elements if condition is met
    if information_elements[:2] == ['0', '0']:
        information_elements = ['0', '1', '1,2'] + information_elements[2:]
    
    modified_line = f"{timestamp} {power} {' '.join(information_elements)}\n"
    processed_lines.append(modified_line)

# Save processed data to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(processed_lines)
    



