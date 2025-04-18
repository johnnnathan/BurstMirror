
import os
import re

CHALLENGES_DIR = "_challenges"

# Regex pattern to find the incorrect 'assign' line
assign_pattern = re.compile(r'{%\s*assign\s+file\s*=\s*site\.static_files.*?keygen\.py.*?%}\s*')

# Loop through each subfolder inside _challenges
for folder in os.listdir(CHALLENGES_DIR):
    folder_path = os.path.join(CHALLENGES_DIR, folder)
    index_path = os.path.join(folder_path, "index.md")

    if os.path.isdir(folder_path) and os.path.isfile(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        modified = False
        new_lines = []

        for line in lines:
            if assign_pattern.search(line):
                print(f"Fixing assignment in: {index_path}")
                # You can choose to comment it out, delete, or replace.
                # Let's REPLACE it with a blank line.
                new_lines.append("<!-- Removed static_files assign -->\n")
                modified = True
            else:
                new_lines.append(line)

        if modified:
            with open(index_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
