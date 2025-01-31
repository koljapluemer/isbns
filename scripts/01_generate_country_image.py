country_ranges={'978-0':'English language','978-1':'English language','978-2':'French language','978-3':'German language','978-4':'Japan','978-5':'former U.S.S.R','978-600':'Iran','978-601':'Kazakhstan','978-602':'Indonesia','978-603':'Saudi Arabia','978-604':'Vietnam','978-605':'Turkey','978-606':'Romania','978-607':'Mexico','978-608':'North Macedonia','978-609':'Lithuania','978-611':'Thailand','978-612':'Peru','978-613':'Mauritius','978-614':'Lebanon','978-615':'Hungary','978-616':'Thailand','978-617':'Ukraine','978-618':'Greece','978-619':'Bulgaria','978-620':'Mauritius','978-621':'Philippines','978-622':'Iran','978-623':'Indonesia','978-624':'Sri Lanka','978-625':'Turkey','978-626':'Taiwan','978-627':'Pakistan','978-628':'Colombia','978-629':'Malaysia','978-630':'Romania','978-631':'Argentina','978-65':'Brazil','978-7': "China, People's Republic", '978-80':'former Czechoslovakia','978-81':'India','978-82':'Norway','978-83':'Poland','978-84':'Spain','978-85':'Brazil','978-86':'former Yugoslavia','978-87':'Denmark','978-88':'Italy','978-89':'Korea, Republic','978-90':'Netherlands','978-91':'Sweden','978-92':'International NGO Publishers and EU Organizations','978-93':'India','978-94':'Netherlands','978-950':'Argentina','978-951':'Finland','978-952':'Finland','978-953':'Croatia','978-954':'Bulgaria','978-955':'Sri Lanka','978-956':'Chile','978-957':'Taiwan','978-958':'Colombia','978-959':'Cuba','978-960':'Greece','978-961':'Slovenia','978-962':'Hong Kong, China','978-963':'Hungary','978-964':'Iran','978-965':'Israel','978-966':'Ukraine','978-967':'Malaysia','978-968':'Mexico','978-969':'Pakistan','978-970':'Mexico','978-971':'Philippines','978-972':'Portugal','978-973':'Romania','978-974':'Thailand','978-975':'Turkey','978-976':'Caribbean Community','978-977':'Egypt','978-978':'Nigeria','978-979':'Indonesia','978-980':'Venezuela','978-981':'Singapore','978-982':'South Pacific','978-983':'Malaysia','978-984':'Bangladesh','978-985':'Belarus','978-986':'Taiwan','978-987':'Argentina','978-988':'Hong Kong, China','978-989':'Portugal','978-9910':'Uzbekistan','978-9911':'Montenegro','978-9912':'Tanzania','978-9913':'Uganda','978-9914':'Kenya','978-9915':'Uruguay','978-9916':'Estonia','978-9917':'Bolivia','978-9918':'Malta','978-9919':'Mongolia','978-9920':'Morocco','978-9921':'Kuwait','978-9922':'Iraq','978-9923':'Jordan','978-9924':'Cambodia','978-9925':'Cyprus','978-9926':'Bosnia and Herzegovina','978-9927':'Qatar','978-9928':'Albania','978-9929':'Guatemala','978-9930':'Costa Rica','978-9931':'Algeria','978-9932': "Lao People's Democratic Republic", '978-9933':'Syria','978-9934':'Latvia','978-9935':'Iceland','978-9936':'Afghanistan','978-9937':'Nepal','978-9938':'Tunisia','978-9939':'Armenia','978-9940':'Montenegro','978-9941':'Georgia','978-9942':'Ecuador','978-9943':'Uzbekistan','978-9944':'Turkey','978-9945':'Dominican Republic','978-9946':'Korea, P.D.R.','978-9947':'Algeria','978-9948':'United Arab Emirates','978-9949':'Estonia','978-9950':'Palestine','978-9951':'Kosova','978-9952':'Azerbaijan','978-9953':'Lebanon','978-9954':'Morocco','978-9955':'Lithuania','978-9956':'Cameroon','978-9957':'Jordan','978-9958':'Bosnia and Herzegovina','978-9959':'Libya','978-9960':'Saudi Arabia','978-9961':'Algeria','978-9962':'Panama','978-9963':'Cyprus','978-9964':'Ghana','978-9965':'Kazakhstan','978-9966':'Kenya','978-9967':'Kyrgyz Republic','978-9968':'Costa Rica','978-9969':'Algeria','978-9970':'Uganda','978-9971':'Singapore','978-9972':'Peru','978-9973':'Tunisia','978-9974':'Uruguay','978-9975':'Moldova','978-9976':'Tanzania','978-9977':'Costa Rica','978-9978':'Ecuador','978-9979':'Iceland','978-9980':'Papua New Guinea','978-9981':'Morocco','978-9982':'Zambia','978-9983':'Gambia','978-9984':'Latvia','978-9985':'Estonia','978-9986':'Lithuania','978-9987':'Tanzania','978-9988':'Ghana','978-9989':'North Macedonia','978-99901':'Bahrain','978-99902':'Reserved Agency','978-99903':'Mauritius','978-99904':'Curaçao','978-99905':'Bolivia','978-99906':'Kuwait','978-99908':'Malawi','978-99909':'Malta','978-99910':'Sierra Leone','978-99911':'Lesotho','978-99912':'Botswana','978-99913':'Andorra','978-99914':'International NGO Publishers','978-99915':'Maldives','978-99916':'Namibia','978-99917':'Brunei Darussalam','978-99918':'Faroe Islands','978-99919':'Benin','978-99920':'Andorra','978-99921':'Qatar','978-99922':'Guatemala','978-99923':'El Salvador','978-99924':'Nicaragua','978-99925':'Paraguay','978-99926':'Honduras','978-99927':'Albania','978-99928':'Georgia','978-99929':'Mongolia','978-99930':'Armenia','978-99931':'Seychelles','978-99932':'Malta','978-99933':'Nepal','978-99934':'Dominican Republic','978-99935':'Haiti','978-99936':'Bhutan','978-99937':'Macau','978-99938':'Srpska, Republic of','978-99939':'Guatemala','978-99940':'Georgia','978-99941':'Armenia','978-99942':'Sudan','978-99943':'Albania','978-99944':'Ethiopia','978-99945':'Namibia','978-99946':'Nepal','978-99947':'Tajikistan','978-99948':'Eritrea','978-99949':'Mauritius','978-99950':'Cambodia','978-99951':'Reserved Agency','978-99952':'Mali','978-99953':'Paraguay','978-99954':'Bolivia','978-99955':'Srpska, Republic of','978-99956':'Albania','978-99957':'Malta','978-99958':'Bahrain','978-99959':'Luxembourg','978-99960':'Malawi','978-99961':'El Salvador','978-99962':'Mongolia','978-99963':'Cambodia','978-99964':'Nicaragua','978-99965':'Macau','978-99966':'Kuwait','978-99967':'Paraguay','978-99968':'Botswana','978-99969':'Oman','978-99970':'Haiti','978-99971':'Myanmar','978-99972':'Faroe Islands','978-99973':'Mongolia','978-99974':'Bolivia','978-99975':'Tajikistan','978-99976':'Srpska, Republic of','978-99977':'Rwanda','978-99978':'Mongolia','978-99979':'Honduras','978-99980':'Bhutan','978-99981':'Macau','978-99982':'Benin','978-99983':'El Salvador','978-99984':'Brunei Darussalam','978-99985':'Tajikistan','978-99986':'Myanmar','978-99987':'Luxembourg','978-99988':'Sudan','978-99989':'Paraguay','978-99990':'Ethiopia','978-99992':'Oman','978-99993':'Mauritius','979-10':'France','979-11':'Korea, Republic','979-12':'Italy','979-8':'United States'}


import numpy as np
import PIL.Image
import tqdm
import random
import os

# ------------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------------
output_filename = "data/images/country_ranges.png"
ISBN_BASE = 978000000000  # Lowest ISBN
MAX_ISBN = 979999999999  # Highest ISBN
smaller_scale = 5  # Controls downscaling factor

IMAGE_WIDTH = 100000 // smaller_scale  # Wide representation
IMAGE_HEIGHT = 20000 // smaller_scale  # High representation


# Assign unique random colors to each country
country_colors = {
    code: (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    for code in country_ranges.keys()
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
for prefix, color in country_colors.items():
    prefix_trie.insert(prefix, color)

# ------------------------------------------------------------------------------
# Generate Image Efficiently Using NumPy (Column-Major Order)
# ------------------------------------------------------------------------------
print(f"Generating ISBN country range visualization: {output_filename}")

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
