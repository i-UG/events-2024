
#!QOpenSys/pkgs/bin/bash

clear

echo ""
echo "  Creating virtual environment for Python 3.9"
echo ""

# Store the current directory path
current_dir=$(pwd)

# Run the Python command to create a virtual environment in the current directory
python -m venv --system-site-packages "$current_dir/.venv"

# Now use that environment
source "$current_dir/.venv/bin/activate"

echo ""
echo "  Creating virtual environment for Python 3.9 has been successfully"
echo ""