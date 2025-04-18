
import os

# Define the root directory where your challenges are stored
root_dir = './_challenges'

# Walk through all subdirectories
for subdir, _, files in os.walk(root_dir):
    # Check if the index.md file is present in the current directory
    if 'index.md' in files:
        index_file_path = os.path.join(subdir, 'index.md')
        
        # Read the content of the index.md file
        with open(index_file_path, 'r') as file:
            content = file.readlines()

        # Loop through lines to find the one we need to replace
        for i, line in enumerate(content):
            if 'site.static_files | where:' in line:
                # Replace the line with the correct Liquid code
                new_line = f'{{% assign file = site.static_files | where: "path", "/{subdir[2:].replace(os.sep, "/")}/keygen.py" | first %}}\n'
                content[i] = new_line
                print(f'Replaced line in {index_file_path}')
                break

        # Write the modified content back to the index.md file
        with open(index_file_path, 'w') as file:
            file.writelines(content)

print("Script completed!")
