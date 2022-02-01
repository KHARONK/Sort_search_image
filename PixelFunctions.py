from PIL import Image, ImageDraw

def compare_pixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]  # only comparing red values
# end def compare_pixels(pix1, pix2):

def store_pixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array = []
    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))  # make an i, j tuple before passing
            pixel_array.append([(r, g, b), (i, j)])  # store pixels in double tuple
        # end for i
        return pixel_array  # send array back to main
# end def store_pixels(im):

def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg
# end def pixels_to_image(im, pixels):

def pixels_to_points(im, pixels):
    # writes pixels passed in to image passed in
    for p in pixels:
        im.putpixel(p[1], p[0])  # pixels at their coordinate
    im.show()
# end def pixels_to_points(size, pixels):

def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
        draw.point(px[1], (gray_av, gray_av, gray_av))
# end def grayscale(im, pixels):
