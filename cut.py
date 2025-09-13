from PIL import Image

# 25 17
size = 50

x = size * 3
y = size * 11

im = Image.open("task.jpg")
im_crop = im.crop((x, y, x + size * 20, y + size * 2))
im_crop.show()

for i in range(2):
    for j in range(20):
        im_box = im_crop.crop((j * size, i * size, j * size + size, i * size + size))
        im_box.save(f"out/{i * 20 + j}.jpg")
