import os
import random
from PIL import Image

# Define the dimensions of the gaming mat design
mat_width = 6400  # Set the width of the gaming mat design in pixels
mat_height = 4800  # Set the height of the gaming mat design in pixels

# Directory where the icons are located
icons_directory = 'icons'

# Initialize a list to store the icons
icons = []

# Recursively search for matching high resolution icons
for root, dirs, files in os.walk(icons_directory):
    for file in files:
        if file.endswith('@5x.png'):
            icon_path = os.path.join(root, file)
            icons.append(icon_path)

# Shuffle the list of icons randomly
random.shuffle(icons)

# Calculate the aspect ratio of the gaming mat design
aspect_ratio = mat_width / mat_height

# Calculate the number of rows and columns while maintaining the aspect ratio
num_rows = int((len(icons) / aspect_ratio) ** 0.5)
num_cols = int(num_rows * aspect_ratio)

# Calculate the size of each grid cell
cell_width = mat_width // num_cols
cell_height = mat_height // num_rows

# Calculate the space between icons in both dimensions
space_between_icons_x = 20
space_between_icons_y = 20

# Create the gaming mat design as a blank image
gaming_mat = Image.new('RGB', (mat_width, mat_height), (35, 47, 62))

# Initialize variables to keep track of the current row and column
current_row = 0
current_col = 0

# Function to place an icon at the current position
def place_icon(icon_path, x, y):
    # Open the icon
    icon = Image.open(icon_path)
    icon = icon.convert('RGBA')

    # Calculate the size of the icon after considering the space
    icon_width = cell_width - space_between_icons_x
    icon_height = cell_height - space_between_icons_y

    # Ensure the icon size is not negative
    icon_width = max(icon_width, 1)
    icon_height = max(icon_height, 1)

    # Resize the icon
    icon = icon.resize((icon_width, icon_height))

    # Paste the icon onto the gaming mat design
    gaming_mat.paste(icon, (x, y), icon)

# Place icons in a grid pattern with space
for _ in range(num_rows):
    for _ in range(num_cols):
        if icons:
            icon_path = icons.pop(0)
            x = current_col * cell_width + space_between_icons_x // 2
            y = current_row * cell_height + space_between_icons_y // 2
            place_icon(icon_path, x, y)
            current_col += 1

    # Move to the next row
    current_row += 1
    current_col = 0

# Save the gaming mat to a file
gaming_mat.save('gaming_mat.png')

print("Yay!!! Enjoy the Gaming Mat!")
