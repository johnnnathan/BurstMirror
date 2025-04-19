import os
import json

# Path to the challenges directory
challenges_dir = 'challenges'

# Get the list of folder names in the challenges directory
challenges = [folder for folder in os.listdir(challenges_dir) if os.path.isdir(os.path.join(challenges_dir, folder))]

# Sort the challenges list with uppercase variants first
challenges = sorted(challenges, key=lambda x: (x.lower(), x))

# Create a dictionary with the challenges list
data = {"challenges": challenges}

# Write the sorted data to challenges.json
with open('challenges.json', 'w') as file:
    json.dump(data, file, indent=4)
