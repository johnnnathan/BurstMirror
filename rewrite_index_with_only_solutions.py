
import os

root_dir = './_challenges'

template = '''---
title: {title}
---

{{% capture solution %}}
{{% include_relative solution.txt %}}
{{% endcapture %}}

## 📝 Solution

{{{{ solution | markdownify }}}}
'''

for subdir, _, files in os.walk(root_dir):
    # Normalize the filenames
    filenames = [f.lower() for f in files]

    # Check for a solution.txt and absence of any keygen.*
    has_solution = 'solution.txt' in filenames
    has_keygen = any(f.startswith('keygen.') for f in filenames)

    if has_solution and not has_keygen:
        index_path = os.path.join(subdir, 'index.md')
        folder_name = os.path.basename(subdir)

        # Clean up the title: replace _ or - with space, capitalize words
        title = folder_name.replace('_', ' ').replace('-', ' ').title()

        # Format and write the new index.md
        new_content = template.format(title=title)

        if os.path.isfile(index_path):
            with open(index_path, 'w') as f:
                f.write(new_content)
            print(f'✅ Updated index.md for: {folder_name}')

print("🎉 All done!")
