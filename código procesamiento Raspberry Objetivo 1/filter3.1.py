input_filename = 'output3.txt'
output_filename = 'output5.txt'



# Read the content from the input file
with open(input_filename, 'r') as input_file:
    lines = input_file.readlines()

unique_mac_addresses = set()

# Extract and store unique MAC addresses
for line in lines:
    parts = line.strip().split(',')
    if len(parts) >= 2:
        mac_address_parts = parts[1:]
        formatted_mac = ",".join(mac_address_parts)
        unique_mac_addresses.add(formatted_mac)

# Write unique MAC addresses to the output file
with open(output_filename, 'w') as output_file:
    for mac_address in unique_mac_addresses:
        output_file.write(mac_address + '\n')

print(f"Extracted and saved {len(unique_mac_addresses)} unique MAC addresses to '{output_filename}'.")


