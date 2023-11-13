import re

def extract_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line into its fields using commas
            fields = line.strip().split(',')

            # Extract the timestamp
            timestamp = fields[0]

            # Use regular expression to find the content inside square brackets
            matches = re.findall(r'\[([^]]+)\]', line)
            if matches:
                integers_str = matches[0]

                # Extract the list of integers from the string and convert it to a list
                integers = [int(num) for num in integers_str.split(',')]

                # Write the timestamp and list of integers to the output file
                outfile.write(f"{timestamp},{integers}\n")

if __name__ == "__main__":
    input_file = "bayes1b.txt"
    output_file = "output2.txt"
    extract_data(input_file, output_file)
