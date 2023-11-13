import matplotlib.pyplot as plt

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
    file_path = "output4.txt"  # Replace with the path to your data file
    data = read_data_from_file(file_path)
    create_histogram(data)
