import imageio.v3 as iio
from PIL import Image
import numpy as np


filenames = ["shin1.jpg", "shin2.jpg"]
images = []

base = Image.open(filenames[0])
common_size = base.size  # (width, height)

for f in filenames:
    img = Image.open(f).resize(common_size)  # force resize
    images.append(np.array(img))

# Save as GIF
iio.imwrite("shinchan.gif", images, duration=500, loop=0)
print("GIF saved as shinchan.gif")
