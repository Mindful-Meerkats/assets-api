from PIL import Image

im1 = Image.open('hill/0.png')
im2 = Image.open('fitness/0.png')
eyes = Image.open('eyes.png')

base = Image.open('hill/0.png')
base = Image.alpha_composite(base,Image.open('back_leg.png'))



base = Image.alpha_composite(base,Image.open('fitness/0.png'))
base = Image.alpha_composite(base,Image.open('happiness/0.png'))
base = Image.alpha_composite(base,Image.open('eyes_fur.png'))
base = Image.alpha_composite(base,Image.open('eyes.png'))
base = Image.alpha_composite(base,Image.open('head_fur.png'))


out = Image.alpha_composite(im1,im2)
out = Image.alpha_composite(out,eyes)
base.save('result.png')