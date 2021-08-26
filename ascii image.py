from PIL import Image

# create a list of ASCII characters to build our output image
ASCII_chars = ["@", "#", "$", "%", "?", "*", "+", ",", ".", ":", ";"]


# resize image
def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# now convert the image into grayscale image
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# now convert pixels to ASCII characters
def pixel_to_ASCII(image):
    pixels = image.getdata()
    characters = "".join([ASCII_chars[pixel // 25] for pixel in pixels])
    return characters


def main():
    # we will attempt to open an image for this project
    path = input("Enter the image path:\n")
    new_width = int(input("Enter required width: "))
    try:
        image = Image.open(path)
    except:
        print(path, " is not valid")
        return

    # converting image to ASCII
    new_image = pixel_to_ASCII(grayify(resize_image(image, new_width)))

    # formating method
    ASCII_image = "\n".join(
        [new_image[index:(index + new_width)] for index in range(0, len(new_image), new_width)])

    print(ASCII_image)


main()
