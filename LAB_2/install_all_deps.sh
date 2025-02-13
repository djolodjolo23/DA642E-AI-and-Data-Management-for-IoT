#!/bin/bash

# Create a global virtual environment if it doesn’t exist
if [ ! -d "global_env" ]; then
    python3 -m venv global_env
fi

# Activate the virtual environment
source global_env/bin/activate

echo "Installing dependencies from all subfolders into global_env..."

# Find all virtual environments and install their dependencies into global_env
for venv in $(find . -type f -name "pyvenv.cfg"); do
    venv_dir=$(dirname "$venv")
    echo "Found virtual environment in: $venv_dir"

    if [ -f "$venv_dir/requirements.txt" ]; then
        echo "Installing from $venv_dir/requirements.txt..."
        pip install -r "$venv_dir/requirements.txt"
    else
        echo "Generating requirements.txt for $venv_dir..."
        source "$venv_dir/bin/activate"
        pip freeze > "$venv_dir/requirements.txt"
        deactivate
        pip install -r "$venv_dir/requirements.txt"
    fi
done

echo "All dependencies installed in global_env!"
echo "You are now inside the global virtual environment."

