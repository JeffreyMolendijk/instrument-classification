#!/bin/bash

# Create directories
mkdir -p models/ data/processed/ data/raw/ data/external/

# Download the OpenMIC dataset
echo "Downloading OpenMIC-2018 dataset..."
wget -P data/external/ https://zenodo.org/records/1432913/files/openmic-2018-v1.0.0.tgz

# Extract the dataset
echo "Extracting dataset..."
tar -xzf data/external/openmic-2018-v1.0.0.tgz -C data/raw/

echo "Setup complete."
