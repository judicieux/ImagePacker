<img src=/img/imagepacker.png><br><br><img src="https://forthebadge.com/images/badges/built-with-love.svg" height="40" length="40"> <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="40" length="40"> <img src="https://forthebadge.com/images/badges/fuck-it-ship-it.svg" height="40" length="40">
# ImagePacker
This script can modify and assemble images
### More specificly
* rotate image     
* crop image       
* resize image     
* invert image      
* flip image       
* mirror image
## PIL
### rotate
```py
rotated_image = image.rotate(90, expand=True, resample=Image.BICUBIC)
```
<img src="/img/rotate.gif"><br>
### crop
```py
crop = image.crop((50, 100, 90, 30))
```
<img src="/img/crop.gif"><br>
### resize
```py
resize = image.resize((1920, 1080))
```
<img src="/img/resize.gif"><br>
### invert
```py
invert = ImageOps.invert(image)
```
<img src="/img/invert.gif"><br>
### flip
```py
flip = ImageOps.flip(image)
```
<img src="/img/flip.gif"><br>
### mirror
```py
mirror = ImageOps.mirror(image)
```
<img src="/img/mirror.gif"><br>
