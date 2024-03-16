import requests
from PIL import Image
from io import BytesIO

def get_random_image():
    url = "https://picsum.photos/200"
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def pixelate_image(image, pixel_size=10):
    pixels = image.load()
    width, height = image.size
    for x in range(0, width, pixel_size):
        for y in range(0, height, pixel_size):
            pixels[x, y] = get_pixel_average(image, x, y, pixel_size)
    return image

def get_pixel_average(image, x, y, pixel_size):
    pixel_values = []
    width, height = image.size
    for i in range(x, min(x + pixel_size, width)):
        for j in range(y, min(y + pixel_size, height)):
            pixel_values.append(image.getpixel((i, j)))
    r_sum, g_sum, b_sum = 0, 0, 0
    for r, g, b in pixel_values:
        r_sum += r
        g_sum += g
        b_sum += b
    pixel_count = len(pixel_values)
    if pixel_count > 0:
        return (r_sum // pixel_count, g_sum // pixel_count, b_sum // pixel_count)
    else:
        return (0, 0, 0)

# Example usage
image = get_random_image()
pixelated_image = pixelate_image(image, pixel_size=15)
pixelated_image.show()