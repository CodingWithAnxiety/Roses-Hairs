# Scripts
This folder contains the scripts I use, primarily for **rotating images.** 

> [!CAUTION]
> **Are you sure you're not lost?**
>
> These scripts are purely for my usage to automate the flipping of textres. *Unless you understand how these scripts function and understand the risks of running code from the internet, please do not try to use these scripts*. Each hair series includes the **already rotated image IDs within, and the posts where these hairs are advertised includes them as well.**


## Rotation scripts

### Requirements 

- Python 3.11 
- Imagemagick
- Preferably windows. Scripts will need some modifications to work in linux.

There are two;

[rotate.py](./rotate.py) - A simple script which, when run, walks the entire directory upwards until it reaches folders with a structure of `exports/textures`. It then checks this directory for any images that end in *.png, then creates a folder called `rotated` inside of the textures folder and then rotates the images within that folder automatically. Place this script inside your root directory of your texture projects prior to running; or you can call the script from your root directory by running the command, `python ./scripts/rotate.py`

[rotateb.py](./rotateb.py) - An improved version of the previous script. Let's you set the root directory of your texture project from the command line. Less tested, however typically more functional. This script attempts to prevent accidental flipping by clouding every image it finds, *if it finds more than fifty, it informs the user of the amount of images found, and asks them if they are sure.* Pressing the **letter N** and enter will quit the script without any further action. 

As this project is fully open source, you are free to modify these scripts to fit your workflow. 

