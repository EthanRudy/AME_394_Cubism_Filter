from PIL import Image # Image manipulation
from enum import Enum # Enumeration functionality
# Also whos bright idea was to ship a modern lang without enums built in?
# I didn't even know this wasn't a shipped feature! Wacky stuff, wacky stuff
import random
import time

image = None

Direction = Enum('Direction', [('CW', 1), ('CCW', 2), ('180', 3), ('RANDOM', 4) ])

'''
Cubism Filter

@param image: Image to modify
@param c_width: Cube Width
@param c_height: Cube Height
@param direction: Rotation Direction
'''
def cubism_filter(image, c_width=10, c_height=10, direction=Direction.CW):

    print("Applying Cubism Filter:")
    
    width, height = image.width, image.height
    print(f"\tImage Dimensions: ({width}, {height})")
    print(f"\tCube Dimensions: ({c_width}, {c_height})")
    match direction:
        case 1:
            print("\tDirection: CW")
        case 2:
            print("\tDirection: CCW")
        case 3:
            print("\tDirection: 180 degrees")
        case 4:
            print("\tDirection: Random")
    print(f"\t# of Cubes = {int(width / c_width) * int(height / c_height)}")

    # Loop across every cube
    for c_x in range(0, width, c_width):
        for c_y in range(0, height, c_height):

            region = image.crop((c_x, c_y, c_x + c_width, c_y + c_height))
            rotated_region = None

            # Randomize handler   
            randomize = False
            if direction == 4: 
                direction = random.randint(1, 3)
                randomize = True

            # CW
            if direction == 1:
                rotated_region = region.transpose(Image.ROTATE_270)

            # CCW
            if direction == 2:
                rotated_region = region.transpose(Image.ROTATE_90)

            # 180
            if direction == 3:
                rotated_region = region.transpose(Image.ROTATE_180)

            if randomize:
                direction = 4

            image.paste(rotated_region, (c_x, c_y))
    return image
            

# Load Image
try:
    image = Image.open("portrait.JPG")

    # image.show()
except FileNotFoundError:
    print("ERROR: Invalid image path")
except Exception as e:
    print(f"ERROR: {e}")



# W: 2400 H: 3000
# I'm chosing cube dimensions 200x200
start_time = time.time()
new_image = cubism_filter(image, 10, 10, 4)
end_time = time.time()
print(end_time - start_time)

image.save("output.jpg")