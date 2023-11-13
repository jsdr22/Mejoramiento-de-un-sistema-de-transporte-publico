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
        "efd31daf49027d406cb57b6ad5766d151af66ee6ac94140254c9f42fd0738091",
        "366c3e02c51a545803ed3a43c0104ae264947928a27bf9566a97c601cf2d6426"
        "bf8fb0ade873540b15bfcb83ff66bfb7b23001871d0e9c4a840084cd55edcc8c"

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
