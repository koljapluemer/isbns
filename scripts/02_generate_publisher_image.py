import PIL.Image
import tqdm
import random
import os
import json

# ------------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------------
INPUT="data/publisher_ranges.json"
output_filename = "data/images/publisher_ranges.png"
smaller_scale = 50  # Controls downscaling factor
ISBN_BASE = 978000000000  # Lowest ISBN
MAX_ISBN = 979999999999  # Highest ISBN
IMAGE_WIDTH = 100000 // smaller_scale  # Wide representation
IMAGE_HEIGHT = 20000 // smaller_scale  # High representation

# load publisher ranges 
with open(INPUT, "r") as f:
    publisher_ranges = json.load(f)

# Assign unique random colors to each publisher
publisher_colors = {
    code: (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    for code in publisher_ranges.keys()
}

# make sure the output directory exists
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

# ------------------------------------------------------------------------------
# 1) Map ISBN Ranges to Pixels
# ------------------------------------------------------------------------------
last_prefix = "xxx"
last_color = (255, 255, 255)
def get_publisher_color(isbn):
    global last_prefix
    global last_color
    """
    Given an ISBN number, determine the corresponding publisher and return its color.
    """
    isbn_str = str(isbn)
    if isbn_str.startswith(last_prefix.replace("-", "")):
        return last_color
    for prefix, publisher in publisher_ranges.items():
        if isbn_str.startswith(prefix.replace("-", "")):  # Match without hyphens
            last_prefix = prefix
            last_color = publisher_colors[prefix]
            return publisher_colors[prefix]
    return (255, 255, 255)  # Default to white if no match

# ------------------------------------------------------------------------------
# 2) Generate Image with Proper 2D Range Coloring
# ------------------------------------------------------------------------------
print(f"Generating ISBN publisher range visualization: {output_filename}")

# Create an empty RGB image
image = PIL.Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255))

# Iterate through ISBNs and color them properly in 2D space
for position in tqdm.tqdm(range(IMAGE_WIDTH * IMAGE_HEIGHT), desc="Processing Image"):
    # Map `position` into 2D (x, y) coordinates: **column-first traversal**
    x = (position // IMAGE_HEIGHT)  # Move right every full column
    y = (position % IMAGE_HEIGHT)  # Move down within the column

    # Convert `position` into an ISBN number
    isbn = ISBN_BASE + int((position / (IMAGE_WIDTH * IMAGE_HEIGHT)) * (MAX_ISBN - ISBN_BASE))
    color = get_publisher_color(isbn)

    # Set pixel color
    image.putpixel((x, y), color)

# ------------------------------------------------------------------------------
# 3) Save the Final Image
# ------------------------------------------------------------------------------
image.save(output_filename)
print(f"Image saved: {output_filename}")
