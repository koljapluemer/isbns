import bencodepy
import PIL.Image
import PIL.ImageChops
import struct
import tqdm
import zstandard

# Get the latest from the `codes_benc` directory in `aa_derived_mirror_metadata`:
# https://annas-archive.org/torrents#aa_derived_mirror_metadata
input_filename = 'data/aa_isbn13_codes_20241204T185335Z.benc.zst'

isbn_data = bencodepy.bread(zstandard.ZstdDecompressor().stream_reader(open(input_filename, 'rb')))
smaller_scale = 5

def color_image(image, packed_isbns_binary, color=None, addcolor=None, scale=1):
    packed_isbns_ints = struct.unpack(f'{len(packed_isbns_binary) // 4}I', packed_isbns_binary)
    isbn_streak = True # Alternate between reading `isbn_streak` and `gap_size`.
    position = 0 # ISBN (without check digit) is `978000000000 + position`.
    for value in tqdm.tqdm(packed_isbns_ints):
        if isbn_streak:
            for _ in range(0, value):
                x = (position // scale) // image.height
                y = (position // scale) % image.height
                if color is not None:
                    image.putpixel((x, y), color)
                else:
                    image.putpixel((x, y), addcolor + image.getpixel((x,y)))
                position += 1
        else: # Reading `gap_size`.
            position += value
        isbn_streak = not isbn_streak

for prefix, packed_isbns_binary in isbn_data.items():
    filename = f"data/images/{prefix.decode()}.png"
    print(f"Generating {filename}...")
    prefix_isbns_png_smaller = PIL.Image.new("F", (100000//smaller_scale, 20000//smaller_scale), 0.0)
    color_image(prefix_isbns_png_smaller, packed_isbns_binary, addcolor=1.0/float(smaller_scale*smaller_scale), scale=(smaller_scale*smaller_scale))
    prefix_isbns_png_smaller.point(lambda x: x * 255).convert("L").save(filename)
