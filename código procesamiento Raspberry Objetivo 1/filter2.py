import hashlib

def sha256_hash(numbers):
    hash_object = hashlib.sha256()
    # Convert the list of numbers to a string for hashing
    numbers_str = ','.join(str(num) for num in numbers)
    hash_object.update(numbers_str.encode('utf-8'))
    return hash_object.hexdigest()

def process_data(input_file, output_file):
    with open(input_file, 'r') as f_input:
        lines = f_input.readlines()

    with open(output_file, 'w') as f_output:
        for line in lines:
            line = line.strip()
            timestamp, numbers_str = line.split(',', 1)  # Split on the first comma only
            numbers = [int(num) for num in numbers_str.strip('[]').split(', ')]
            hashed_numbers = sha256_hash(numbers)
            f_output.write(f"{timestamp},{numbers_str},{hashed_numbers}\n")

if __name__ == "__main__":
    input_file = "output2.txt"
    output_file = "output3.txt"
    process_data(input_file, output_file)


