import matplotlib.pyplot as plt

def filter_hashes(input_file, output_file, target_hashes):
    filtered_data = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        timestamp, hash_value = line.strip().split(',')
        if hash_value in target_hashes:
            filtered_data.append(line)

    with open(output_file, 'w') as f:
        f.writelines(filtered_data)

if __name__ == "__main__":
    input_file = "output4.txt"
    output_file = "output4_1.txt"
    target_hashes = [
        #"e5dca78cb46fbb446470922c1f5782a413fa9c97a88d2ba1cb472a4d8d44913d", #samsung s22
        #"39f550c7f92cf87c097c4acf98d287dc9a114edf8c3b1e7ebb928d448fbb5286"#xiaomi mi9 
        "95df0edc8d88234e4bbe0812e75c2aed5d4bcb436b21f6bc99f7450fb3df858a" # samsung A71
        #"0f843ec0e2f804261519a069724555ec01ba310851fc8ea2cdb622f622189e65"
    ]

    filter_hashes(input_file, output_file, target_hashes)
    print("Filtered data saved to", output_file)

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def create_histogram(data):
    hex_string_frequency = {}
    hex_strings = []
    for line in data:
        _, hex_string = line.strip().split(',')
        if hex_string not in hex_string_frequency:
            hex_string_frequency[hex_string] = 0
            hex_strings.append(hex_string)
        hex_string_frequency[hex_string] += 1

    frequencies = [hex_string_frequency[hex_string] for hex_string in hex_strings]

    cool_color = '#007BA7'  # Cool blue color
    plt.figure(figsize=(12, 8))  # Larger figsize
    plt.bar(range(len(hex_strings)), frequencies, color=cool_color)
    plt.xlabel('Index', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Histogram of Hexadecimal String Frequency', fontsize=16, color=cool_color)  # Adding the title
    plt.xticks(range(len(hex_strings)), range(len(hex_strings)), rotation=45, ha='right')
    plt.tight_layout()

    # Save histogram information to a text file
    with open('output6.txt', 'w') as file:
        for i, hex_string in enumerate(hex_strings):
            file.write(f"{hex_string}\t{frequencies[i]}\n")

    plt.show()

if __name__ == "__main__":
    file_path = "output4_1.txt"  # Replace with the path to your data file
    data = read_data_from_file(file_path)
    create_histogram(data)
