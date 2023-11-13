'''from datetime import datetime

# Threshold for the power signal
power_threshold = -90

# Open the input file in read mode and the output file in write mode
with open('tm2.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Read each line from the input file
    for line in infile:
        # Split the line into parts using comma as the separator
        parts = line.strip().split(',')
        
        # Extract the power signal and convert it to an integer
        power_signal = int(parts[1])
        
        # Check if the power signal is greater than the threshold
        if power_signal > power_threshold:
            # Extract the timestamp, convert it to a float and then to a datetime object
            timestamp = float(parts[0])
            dt_object = datetime.fromtimestamp(timestamp)
            
            # Format the datetime object to get only the hours, minutes, and seconds
            time_str = dt_object.strftime('%H:%M:%S')
            
            # Extract the IDs, filter out empty strings, convert the rest to integers, and put them in a list
            ids = [int(x) for x in parts[3:] if x.isdigit()]
            
            # Format the output string
            output_str = f"{time_str},{ids}\n"
            
            # Write the output string to the output file
            outfile.write(output_str)'''
from datetime import datetime

# Threshold for the power signal
power_threshold = -60

# Open the input file in read mode and the output file in write mode
with open('tm2.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Read each line from the input file
    for line in infile:
        # Split the line into parts using comma as the separator
        parts = line.strip().split(',')
        
        # Extract the power signal and convert it to an integer
        power_signal = int(parts[1])
        
        # Check if the power signal is greater than the threshold
        if power_signal > power_threshold:
            # Extract the timestamp, convert it to a float and then to a datetime object
            timestamp = float(parts[0])
            dt_object = datetime.fromtimestamp(timestamp)
            
            # Format the datetime object to get only the hours, minutes, and seconds
            time_str = dt_object.strftime('%H:%M:%S')
            
            # Extract the IDs, filter out empty strings, convert the rest to integers, and put them in a list
            ids = [int(x) for x in parts[3:] if x.isdigit()]
            
            # Format the output string
            output_str = f"{time_str},{ids}\n"
            
            # Write the output string to the output file
            outfile.write(output_str)








        
        
        

