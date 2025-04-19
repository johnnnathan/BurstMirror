
import os
import yaml

CHALLENGES_DIR = "_challenges"

# Function to update front matter
def update_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Find the start and end of the front matter block
    front_matter_start = None
    front_matter_end = None
    for i, line in enumerate(content):
        if line.strip() == '---':
            if front_matter_start is None:
                front_matter_start = i
            else:
                front_matter_end = i
                break

    if front_matter_start is not None and front_matter_end is not None:
        # Extract front matter lines
        front_matter = content[front_matter_start + 1:front_matter_end]
        
        # Check if the layout key is already in front matter
        front_matter_dict = yaml.safe_load('\n'.join(front_matter))
        
        if 'layout' not in front_matter_dict:
            # Add layout if not present
            front_matter_dict['layout'] = 'default'
            
            # Rebuild the front matter with the new layout
            updated_front_matter = yaml.dump(front_matter_dict, default_flow_style=False).strip().splitlines()

            # Update the content with the new front matter
            content[front_matter_start + 1:front_matter_end] = [line + '\n' for line in updated_front_matter]
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(content)
            print(f"Updated {file_path}")
        else:
            print(f"Layout already present in {file_path}")
    else:
        print(f"No front matter found in {file_path}")

# Loop through the _challenges folder
for folder in os.listdir(CHALLENGES_DIR):
    folder_path = os.path.join(CHALLENGES_DIR, folder)
    if os.path.isdir(folder_path):
        index_file_path = os.path.join(folder_path, "index.md")
        if os.path.isfile(index_file_path):
            update_front_matter(index_file_path)
