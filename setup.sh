#!/bin/bash
echo "****************************************"
echo " Setting up Environment"
echo "****************************************"

echo "Updating package manager..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

# echo "Installing Python 3.8 and Virtual Environment"
# sudo apt-get update
# sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3.8-venv

echo "Creating a Python virtual environment"
python3 -m venv env

echo "Checking the Python version..."
python3 --version

echo "Activating the enviroment..."
source env/bin/activate

echo "Installing Python depenencies..."
python3 -m pip install --upgrade pip wheel
pip install -r requirements.txt

echo "****************************************"
echo " Environment Setup Complete"
echo "****************************************"