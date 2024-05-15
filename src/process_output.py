import re

# Define a regular expression pattern to match lines containing FPS and AVG_FPS
pattern = r'FPS:\s*(\d+\.\d+)\s+AVG_FPS:\s*(\d+\.\d+)'

# Open the text file containing the output
with open('output.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

    # List to store FPS and AVG_FPS values extracted from the lines
    fps_values = []

    # Iterate over each line
    for line in lines:
        # Use regex to search for FPS and AVG_FPS values in the line
        match = re.search(pattern, line)
        if match:
            # Extract FPS and AVG_FPS values from the matched pattern
            fps = float(match.group(1))
            avg_fps = float(match.group(2))
            # Append the extracted values to the list
            fps_values.append((fps, avg_fps))

# Print the extracted FPS and AVG_FPS values
for fps, avg_fps in fps_values:
    print(f"{fps}, {avg_fps}")
