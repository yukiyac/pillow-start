from PIL import Image
import numpy as np

row_data = np.arange(256)
hue_data = np.tile(row_data, (256, 1))
sat_data = np.transpose(hue_data)
val_data = np.full_like(hue_data, 255)
mat_data = np.stack([hue_data, sat_data, val_data], 2)

im = Image.fromarray(np.uint8(mat_data), "HSV")
im_rgb = im.convert("RGB")
im_rgb.show()
