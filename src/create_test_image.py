from PIL import Image
import numpy as np

def create_test_image():
    # Create a simple test image with some patterns
    width, height = 300, 200
    image = Image.new('RGB', (width, height), 'white')
    pixels = image.load()
    
    # Add some patterns
    for x in range(width):
        for y in range(height):
            if (x + y) % 20 < 10:  # Create a diagonal pattern
                pixels[x, y] = (255, 0, 0)  # Red
            elif x % 30 < 15:      # Create vertical stripes
                pixels[x, y] = (0, 255, 0)  # Green
    
    # Save the image
    image.save('test_image.png')
    print("Test image created successfully at 'test_image.png'")

if __name__ == "__main__":
    create_test_image()
