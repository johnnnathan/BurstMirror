#!/bin/bash

# Exit on error
set -e

# Configuration
REPO_URL="https://github.com/johnnnathan/Crack"
TEMP_DIR="temp_clone"
CHALLENGES_DIR="challenges"

# Step 1: Clear contents of challenges folder
echo "Clearing contents of $CHALLENGES_DIR..."
rm -rf ${CHALLENGES_DIR:?}/*

# Step 2: Clone repository
echo "Cloning repository..."
git clone "$REPO_URL" "$TEMP_DIR"

# Step 3: Copy contents into challenges folder
echo "Copying contents to $CHALLENGES_DIR..."
cp -r "$TEMP_DIR"/* "$CHALLENGES_DIR"

# Cleanup temporary clone
rm -rf "$TEMP_DIR"

# Step 4: Run Python scripts
echo "Running handle_json.py..."
python3 handle_json.py

echo "Running generate_pages.py..."
python3 generate_pages.py

# Step 5: Git add, commit, and push
echo "Committing and pushing changes..."
git add .
git commit -m "Update challenges from repository"
git push

echo "Done!"
