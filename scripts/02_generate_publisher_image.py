import numpy as np
import PIL.Image
import tqdm
import random
import os
import json
from collections import defaultdict

# ------------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------------
INPUT = "data/publisher_ranges.json"
output_filename = "data/images/publisher_ranges.png"
smaller_scale = 10  # Controls downscaling factor
ISBN_BASE = 978000000000  # Lowest ISBN
MAX_ISBN = 979999999999  # Highest ISBN
IMAGE_WIDTH = 100000 // smaller_scale  # Wide representation
IMAGE_HEIGHT = 20000 // smaller_scale  # High representation

# Load publisher ranges
with open(INPUT, "r") as f:
    publisher_ranges = json.load(f)

# Assign unique random colors to each publisher
publisher_colors = {
    code: (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    for code in publisher_ranges.keys()
}

# Ensure output directory exists
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

# ------------------------------------------------------------------------------
# Build Fast Lookup Structure: Prefix Trie
# ------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.color = None

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix, color):
        node = self.root
        for char in prefix.replace("-", ""):  # Ignore hyphens in lookup
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.color = color  # Store color at the end of the prefix

    def search(self, isbn):
        node = self.root
        last_color = (255, 255, 255)  # Default white
        for char in str(isbn):
            if char in node.children:
                node = node.children[char]
                if node.color:
                    last_color = node.color
            else:
                break
        return last_color

# Construct the Trie
prefix_trie = PrefixTrie()
for prefix, color in publisher_colors.items():
    prefix_trie.insert(prefix, color)

# ------------------------------------------------------------------------------
# Generate Image Efficiently Using NumPy (Column-Major Order)
# ------------------------------------------------------------------------------
print(f"Generating ISBN publisher range visualization: {output_filename}")

# Create a NumPy array for faster pixel manipulation
image_array = np.full((IMAGE_HEIGHT, IMAGE_WIDTH, 3), 255, dtype=np.uint8)  # White background

# Compute ISBNs in column-major order
total_pixels = IMAGE_WIDTH * IMAGE_HEIGHT
isbn_values = np.linspace(ISBN_BASE, MAX_ISBN, total_pixels, dtype=np.int64)

# Reshape ISBNs into a column-major format
isbn_values = isbn_values.reshape((IMAGE_WIDTH, IMAGE_HEIGHT)).T  # Transpose to ensure column-major order

# Convert each ISBN to color
colors = np.array([[prefix_trie.search(isbn) for isbn in row] for row in tqdm.tqdm(isbn_values, desc="Mapping ISBNs")], dtype=np.uint8)

# Convert NumPy array to PIL image
image = PIL.Image.fromarray(colors, "RGB")

# ------------------------------------------------------------------------------
# Save the Final Image
# ------------------------------------------------------------------------------
image.save(output_filename)
print(f"Image saved: {output_filename}")
