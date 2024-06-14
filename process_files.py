import os
import numpy

# Loop through all files in the target directory

print(f"{numpy.__version__=}")

filepath = "files"

for filename in os.listdir(filepath):
	if filename.startswith('.'): continue
	print(f"Processing {filename} text")
