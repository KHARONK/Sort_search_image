from PIL import Image
from SortFunctions import quick_sort
from SearchFunctions import  binary_search_sub
from PixelFunctions import  store_pixels, pixels_to_image,pixels_to_points,grayscale


def main():
    IMG_NAME = "monkey.jpeg"

    threshold = int(input("Please enter a threshold between 0-256.\n"))| 180

    # open image and read each pixel to memory as im
    with Image.open(IMG_NAME) as im:
        pixels = store_pixels(im)
        print("sorted")
        sorted_pixels = quick_sort(0,len(pixels)-1,pixels)
        print("stored")
        sorted_im = pixels_to_image(im, sorted_pixels)
        sorted_im.save("sorted" + IMG_NAME , "JPEG")
        subi = binary_search_sub(
            [r[0][0] for r in sorted_pixels], 0, len(sorted_pixels) - 1, threshold
        )
        print("Sublist of reds starts at: ", subi)
        grayscale(im,pixels)
        pixels_to_points(im, sorted_pixels[subi:])

    # save my image data from memory to a file with a difference
    im.save("neg_" + IMG_NAME, "JPEG")


if __name__ == "__main__":
    main()
