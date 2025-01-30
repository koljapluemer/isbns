import os
import json
import matplotlib.cm as cm
from PIL import Image
import json
import tqdm

# ------------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------------
INPUT_JSONL = "data/publishers.jsonl"  # Path to your JSONL file
OUTPUT = "data/publisher_ranges.json"
MAX_DEPTH = 5         # Generate depths 3..MAX_DEPTH
SKIP_IF_EXISTS = True # Skip tile generation if PNG exists

TILE_WIDTH  = 1000
TILE_HEIGHT = 800

smaller_scale = 50
SCALE = smaller_scale * smaller_scale  # 2500

ISBN_BASE = 978000000000

isbn_range_to_publisher = {}


with open(INPUT_JSONL, "r", encoding="utf-8") as f:
    for line in tqdm.tqdm(f):
        line = line.strip()
        if not line:
            continue
        
        data = json.loads(line)
        record = data["metadata"]["record"]
        publisher_name = record["registrant_name"]

        # "isbns" is a list of dicts with "isbn": "978-0-000", "isbn_type": "prefix"
        isbns_list = record.get("isbns", [])
        for isbn_info in isbns_list:
            raw_isbn = isbn_info["isbn"]  # e.g. "978-0-00"
            # remove dashes
            isbn_stripped = raw_isbn.replace("-", "")  # "978000"
            # one isbn range may have several publishers, so we save a list
            if publisher_name:
                publisher_name = publisher_name.strip()
                if isbn_stripped in isbn_range_to_publisher:
                    isbn_range_to_publisher[isbn_stripped].append(publisher_name)
                else:
                    isbn_range_to_publisher[isbn_stripped] = [publisher_name]
        
# print sample
for isbn_range, publishers in list(isbn_range_to_publisher.items())[:5]:
    print(isbn_range, publishers)


# make a dict where publisher are joined with "/" and dump to json
isbn_range_to_publisher_to_joined = {}
for isbn_range, publishers in isbn_range_to_publisher.items():
    joined = " / ".join(publishers)
    isbn_range_to_publisher_to_joined[isbn_range] = joined

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(isbn_range_to_publisher_to_joined, f, indent=2, ensure_ascii=False)