import os

CHALLENGES_DIR = "_challenges"

TEMPLATE = """---
title: {title}
---

{{% raw %}}{{% capture solution %}}
{{% include_relative solution.txt %}}
{{% endcapture %}}

## 📝 Solution

{{{{ solution | markdownify }}}}

{keygen_block}{{% endraw %}}
"""

KEYGEN_BLOCK = """{{% raw %}}
{{% if site.static_files | where: "path", "/_challenges/{folder}/keygen.{ext}" %}}
## 🔑 Keygen ({lang})

```{ext}
{{% include_relative keygen.{ext} %}}
{{% endif %}}{{% endraw %}}"""

def detect_keygen(folder_path):
    for ext in ["py", "c"]:
        file_path = os.path.join(folder_path, f"keygen.{ext}")
        if os.path.exists(file_path):
            lang = "Python" if ext == "py" else "C"
            return ext, lang
    return None, None

for folder in os.listdir(CHALLENGES_DIR): 
    folder_path = os.path.join(CHALLENGES_DIR, folder)

    if os.path.isdir(folder_path):
        index_path = os.path.join(folder_path, "index.md")
        solution_file = os.path.join(folder_path, "solution.txt")

        if os.path.exists(solution_file):
            ext, lang = detect_keygen(folder_path)
            keygen_block = ""

            if ext:
                keygen_block = KEYGEN_BLOCK.format(folder=folder, ext=ext, lang=lang)

            with open(index_path, "w") as f:
                f.write(TEMPLATE.format(
                    title=folder.replace("-", " ").title(),
                    keygen_block=keygen_block
                ))
            print(f"✅ Generated: {index_path}")
        else:
            print(f"⏩ Skipped (no solution.txt): {folder}")
