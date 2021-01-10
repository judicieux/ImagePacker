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
**rotate**
```py
rotated_image = image.rotate(90, expand=True, resample=Image.BICUBIC)
```
**crop**
```py
crop = image.crop((50, 100, 90, 30))
```
**resize**
```py
resize = image.resize((1920, 1080))
```
**invert**
```py
invert = ImageOps.invert(image)
```
**flip**
```py
flip = ImageOps.flip(image)
```
**mirror**
```py
mirror = ImageOps.mirror(image)
```
