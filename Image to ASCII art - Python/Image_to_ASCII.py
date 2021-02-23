import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%","/","*", "+", "-", ";", ":", "," , "." ]


#Resize the image to your preferred size
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width

    new_height = int(ratio*new_width)

    resized_image = image.resize((new_width, new_height))

    return resized_image

#Convert each pixel to grayscale
def to_grayscale(image):
    grayscaled_image = image.convert("L")
    return grayscaled_image


#Convert each of the grayscaled pixel to ascii characters
def to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])

    return characters

def main():
    path = input("\nEnter a valid image path: ")
    new_width = int(input("\nEnter desired width: "))

    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid input")

    final_ascii_string = to_ascii(to_grayscale(resize_image(image,new_width)))

    num_pixels = len(final_ascii_string)

    ascii_image = "\n".join(final_ascii_string[i:(i+new_width)] for i in range(0,num_pixels,new_width))

    print(ascii_image)

    with open("ascii_art.txt","w") as file:
        file.write(ascii_image)

main()