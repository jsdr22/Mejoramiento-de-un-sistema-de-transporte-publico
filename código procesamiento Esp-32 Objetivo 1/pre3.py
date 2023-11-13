import re
# Define the input and output file paths
input_file_path = "output1.txt"
output_file_path = "output1_1.txt"

# Open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Read each line from the input file
    for line in input_file:
        # Split the line by comma to extract timestamp and other information
        parts = line.strip().split(",")
        if len(parts) >= 2:
            timestamp = parts[0]
            # Modify the timestamp to the new format (keeping only HH:MM:SS)
            modified_timestamp = timestamp[:8]
            
            # Reconstruct the modified line with the modified timestamp
            modified_line = f"{modified_timestamp},{','.join(parts[1:])}\n"
            
            # Write the modified line to the output file
            output_file.write(modified_line)

# Print a message to indicate the process is complete
print("Timestamps have been modified and saved to 'output.txt'")


import csv
# Read the probe request packets from the text file
with open("output1_1.txt", "r") as f:
    reader = csv.reader(f, delimiter=",")
    packets = list(reader)
# Filter the packets that have a signal power greater than -60 dBm
filtered_packets = []
for packet in packets:
    signal_power = int(packet[1])
    if signal_power > -60:
        filtered_packets.append(packet)
# Save the filtered packets to a new text file
with open("output1_2.txt", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(filtered_packets)

with open("output1_2.txt", "r") as f:
    lines = f.readlines()

with open("output2.txt", "w") as f:
    for line in lines:
        # Buscar y extraer la información entre corchetes
        match = re.search(r"\[(.*?)\]", line)
        if match:
            info_between_brackets = match.group(1)
            
            # Buscar y extraer el timestamp
            timestamp_match = re.match(r"(\d{2}:\d{2}:\d{2}),", line)
            if timestamp_match:
                timestamp = timestamp_match.group(1)
            
            # Escribir el timestamp y la información entre corchetes en el archivo de salida
            f.write(f'{timestamp},[{info_between_brackets}]\n')
