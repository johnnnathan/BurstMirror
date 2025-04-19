
import os
from jinja2 import Template
import json

# Template for the challenge page
challenge_page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Challenge: {{ title }}</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <h1>{{ title }}</h1>
    <h2>📝 Solution</h2>

    <div id="solution-container">{{ solution }}</div>

    <script src="/js/script.js"></script>
</body>
</html>
"""

# Path to the _challenges directory
challenges_dir = "_challenges"

# Get the list of all challenge folders
challenges = [f for f in os.listdir(challenges_dir) if os.path.isdir(os.path.join(challenges_dir, f))]

# Create a list to store challenge folder names for challenges.json
challenge_data = {"challenges": challenges}

# Write the list of challenges to a JSON file for JavaScript usage
with open("challenges.json", "w") as json_file:
    json.dump(challenge_data, json_file)

# Iterate over each challenge folder and generate an index.html page
for challenge in challenges:
    # Read the solution.txt file for the challenge
    solution_file = os.path.join(challenges_dir, challenge, "solution.txt")
    try:
        with open(solution_file, 'r') as f:
            solution_text = f.read()
    except FileNotFoundError:
        solution_text = "Solution not found."

    # Use Jinja2 template to fill in the details
    template = Template(challenge_page_template)
    rendered_page = template.render(title=challenge.replace('_', ' '), solution=solution_text)

    # Write the generated HTML content to the challenge folder
    output_file = os.path.join(challenges_dir, challenge, "index.html")
    with open(output_file, 'w') as f:
        f.write(rendered_page)

print("Challenge pages and challenges.json generated successfully.")
