from PIL import Image, ImageDraw
import os

img = Image.new('RGBA', (800, 450), (33, 150, 243, 255))
d = ImageDraw.Draw(img)
d.rectangle((40, 40, 760, 410), fill=(255, 255, 255, 255))
d.rectangle((60, 60, 740, 390), outline=(33, 150, 243, 255), width=4)
d.text((120, 190), 'Search Page', fill=(33, 150, 243, 255))
img.save('screenshots/search-page.png')

img2 = Image.new('RGBA', (800, 450), (76, 175, 80, 255))
d2 = ImageDraw.Draw(img2)
d2.rectangle((40, 40, 760, 410), fill=(255, 255, 255, 255))
d2.rectangle((60, 60, 740, 390), outline=(76, 175, 80, 255), width=4)
d2.text((140, 190), 'Home Page', fill=(76, 175, 80, 255))
img2.save('screenshots/home-page.png')

print('created', os.path.getsize('screenshots/search-page.png'), os.path.getsize('screenshots/home-page.png'))
