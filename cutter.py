from PIL import Image
import glob
import os


def create_output_folder() -> None:
    if not os.path.isdir('out'):
        os.mkdir('out')


def cut(filename: str) -> None:
    im = Image.open(filename)
    x, y = im.size
    x1, y1 = [], []
    first_pixel = im.getpixel((1,1))


    for i in range(1,x,3):
        for j in range(1,y,3):
            res = im.getpixel((i,j))
            if res != first_pixel:
                x1.append(i)
                y1.append(j)

    new_im = im.crop((min(x1),min(y1),max(x1),max(y1)))
    new_im.save(f'out/{filename}')

    im.close()


if __name__ == '__main__':
    create_output_folder()

    image_names = glob.glob('*.png')
    for filename in image_names:
        cut(filename)
        os.remove(filename)
