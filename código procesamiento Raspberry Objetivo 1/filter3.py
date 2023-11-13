def process_data_line(line):
    # Split the line by comma to separate timestamp, list of numbers, and hash value
    parts = line.strip().split(',')
    timestamp = parts[0]
    hash_value = parts[-1]
    return timestamp, hash_value

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        timestamp, hash_value = process_data_line(line)
        new_line = f"{timestamp},{hash_value}\n"
        new_lines.append(new_line)

    with open(output_file, 'w') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    input_file = "output3.txt"  # Replace with the path to your input file
    output_file = "output4.txt"  # Replace with the path for the output file
    main(input_file, output_file)

