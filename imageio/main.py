import imageio as iio

filenames = ['pic1.png', 'pic2.png']
image = [ ]

for filename in filenames:
    image.append(iio.imread(filename))
    
iio.imwrite('pic.gif', image, duration = 500, loop = 0)



# 'team.gif': This is the name you want to give to your new GIF file.
# images: The list containing the image data.
# duration = 500: How long each picture should show in the GIF, in milliseconds.
# loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).