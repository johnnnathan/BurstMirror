import os
import html

CHALLENGES_DIR = "challenges"
KEYGEN_NAMES = ["keygen.py", "keygen.sh", "keygen.c"]


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    body {{
      font-family: sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
      text-align: center;
      background-color: #fdfdfd;
      font-size: 1.2rem; /* Increase base font size */
    }}
    pre {{
      text-align: left;
      background: #f0f0f0;
      padding: 1rem;
      white-space: pre-wrap;
      word-wrap: break-word;
      font-size: 1.1rem; /* Increase font size for preformatted text */
    }}
    h1, h2 {{
      margin-top: 2rem;
    }}
  </style>
</head>
<body>

<h1>{title}</h1>

<h2>📝 Solution</h2>
<pre>{solution}</pre>

{keygen_section}

</body>
</html>
"""

KEYGEN_TEMPLATE = """
<h2>🔑 Keygen</h2>
<pre>{keygen_content}</pre>
"""

def format_title(folder_name):
    return folder_name.replace("_", " ").title()

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return html.escape(f.read())
    return ""

def get_keygen_code(folder_path):
    for name in KEYGEN_NAMES:
        path = os.path.join(folder_path, name)
        if os.path.isfile(path):
            return read_file(path)
    return ""

def main():
    for folder in os.listdir(CHALLENGES_DIR):
        folder_path = os.path.join(CHALLENGES_DIR, folder)
        if not os.path.isdir(folder_path):
            continue

        title = format_title(folder)
        solution = read_file(os.path.join(folder_path, "solution.txt"))
        keygen_code = get_keygen_code(folder_path)

        keygen_section = ""
        if keygen_code:
            keygen_section = KEYGEN_TEMPLATE.format(keygen_content=keygen_code)

        html_output = HTML_TEMPLATE.format(
            title=title,
            solution=solution,
            keygen_section=keygen_section
        )

        output_path = os.path.join(folder_path, "index.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_output)

        print(f"✅ Generated: {output_path}")

if __name__ == "__main__":
    main()
