import json

# Load the JSON data from the file
with open('challenges.json', 'r') as file:
    data = json.load(file)

# Sort the 'challenges' list with uppercase variants first
data["challenges"] = sorted(data["challenges"], key=lambda x: (x.lower(), x))

# Write the sorted data back to the file
with open('challenges.json', 'w') as file:
    json.dump(data, file, indent=4)
