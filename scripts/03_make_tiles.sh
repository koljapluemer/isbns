#!/bin/bash
set -e
set -o pipefail

# for filename in images/*.png; do

mkdir -p tiles
rm -rf tiles/*

for filename in data/images/*.png; do
    echo "Creating tile set for $filename..."
    vips dzsave $filename tiles/$(basename "$filename" .png) --tile-size 400 --overlap 0 --suffix .png
done 