import os
from colorama import Fore
from PIL import Image, ImageOps
import sys

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def main():
	try:
		if sys.argv[1] == "rotate" and sys.argv[2] == "--help":
			print(f"{Fore.RED}[Image]: [.jpg] | Rotation > [int]")
			exit()

		elif sys.argv[1] == "crop" and sys.argv[2] == "--help":
			print(f"{Fore.RED}[Image]: [.jpg] | [PTS1]: [int] | [PTS2]: [int] | [PTS3]: [int] | [PTS4]: [int]" + "\n")
			exit()

		elif sys.argv[1] == "resize" and sys.argv[2] == "--help":
			print(f"{Fore.RED}[Image]: [.jpg] | Width > [int] | Height > [int]")
			exit()

		elif sys.argv[1] == "invert" and sys.argv[2] == "--help":
			print(f"{Fore.RED}[Image]: [.jpg]")
			exit()

		elif sys.argv[1] == "flip" and sys.argv[2] == "--help":
			print(f"{Fore.RED}[Image]: [.jpg]")
			exit()

		elif sys.argv[1] == "mirror" and sys.argv[2] == "--help":
			print(f"{Fore.RED}[Image]: [.jpg]")
			exit()

	except ValueError:
		pass

	except IndexError:
		pass

	try:
		if sys.argv[1] == "rotate":
			image = input(f"{Fore.BLUE}[Image]: ")
			global rotate_ext
			rotate_ext = image.split(".")[1]
			rotation = int(input(f"{Fore.BLUE}[Rotation]: "))
			rotate(image, rotation)

		if sys.argv[1] == "crop":
			image = input(f"{Fore.BLUE}[Image]: ")
			global crop_ext
			crop_ext = image.split(".")[1]
			pts1 = int(input(f"{Fore.BLUE}[PTS 1]: "))
			pts2 = int(input(f"{Fore.BLUE}[PTS 2]: "))
			pts3 = int(input(f"{Fore.BLUE}[PTS 3]: "))
			pts4 = int(input(f"{Fore.BLUE}[PTS 4]: "))
			crop(image, pts1, pts2, pts3, pts4)

		if sys.argv[1] == "resize":
			image = input("[Image]: ")
			global resize_ext
			resize_ext = image.split(".")[1]
			width = int(input("[Width]: "))
			height = int(input("[Height]: "))
			resize(image, width, height)
		
		if sys.argv[1] == "invert":
			image = input(f"{Fore.BLUE}[Image]: ")
			global invert_ext
			invert_ext = image.split(".")[1]
			invert(image)

		if sys.argv[1] == "flip":
			image = input(f"{Fore.BLUE}[Image]: ")
			global flip_ext
			flip_ext = image.split(".")[1]
			flip(image)

		if sys.argv[1] == "mirror":
			image = input(f"{Fore.BLUE}[Image]: ")
			global mirror_ext
			mirror_ext = image.split(".")[1]
			mirror(image)

	except IndexError:
		clear()
		logo = f"""{Fore.RED}
   ____                    ___           __          
  /  _/_ _  ___ ____ ____ / _ \___ _____/ /_____ ____
 _/ //  ' \/ _ `/ _ `/ -_) ___/ _ `/ __/  '_/ -_) __/
/___/_/_/_/\_,_/\_, /\__/_/   \_,_/\__/_/\_\\__/_/   
               /___/                                 

               Dev By Hypostat1c
               
	Usage : python3 main.py [function]

		"""
		print(logo)

	except ValueError:
		clear()
		print(f"{Fore.RED}NaN" + "\n")

	except FileNotFoundError:
		clear()
		print(f"{Fore.RED}File not found" + "\n")

def rotate(image, rotation):
	try:
		image = Image.open(image)
		rotate = image.rotate(rotation, expand=True, resample=Image.BICUBIC)
		rotate.save("rotated_saved." + rotate_ext)
		clear()
		print(f"{Fore.GREEN}Success : " + "rotated_saved." + rotate_ext)

	except ValueError:
		clear()
		print(f"{Fore.RED}[Image]: [.jpg] | [Rotation]: [int]")

def crop(image, pts1, pts2, pts3, pts4):
	try:
		image = Image.open(image)
		crop = image.crop((pts1, pts2, pts3, pts4))
		crop.save("cropped_saved." + crop_ext)
		clear()
		print(f"{Fore.GREEN}Success : " + "cropped_saved." + crop_ext)
	
	except ValueError:
		clear()
		print(f"{Fore.RED}[Image]: [.jpg] | [PTS1]: [int] | [PTS2]: [int] | [PTS3]: [int] | [PTS4]: [int]" + "\n")

def resize(image, width, height):
	image = Image.open(image)
	resize = image.resize((width, height))
	resize.save("resized_saved." + resize_ext)
	clear()
	print(f"{Fore.GREEN}Success : " + "resized_saved." + resize_ext)	

def invert(image):
	try:
		image = Image.open(image)
		invert = ImageOps.invert(image)
		invert.save("inverted_saved." + invert_ext, quality=95)
		clear()
		print(f"{Fore.GREEN}Success : " + "inverted_saved." + invert_ext)

	except AttributeError:
		clear()
		print(f"{Fore.RED}Image > [.jpg]")

def flip(image):
	image = Image.open(image)
	flip = ImageOps.flip(image)
	flip.save("flipped_saved." + flip_ext, quality=95)
	clear()
	print(f"{Fore.GREEN}Success : " + "flipped_saved." + flip_ext)

def mirror(image):
	image = Image.open(image)
	mirror = ImageOps.mirror(image)
	mirror.save("mirrored_saved." + mirror_ext)
	clear()
	print(f"{Fore.GREEN}Success : " + "mirrored_saved." + mirror_ext)	

main()
