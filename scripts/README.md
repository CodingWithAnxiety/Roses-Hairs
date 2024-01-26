# Scripts
This folder contains the scripts I use, primarily for **rotating images.**

## Rotation scripts

### Requirements 

- Python 3.11 
- Imagemagick
- Preferably windows. Scripts will need some modifications to work in linux.

There are two;

[rotate.py](./rotate.py) - A simple script which, when run, walks the entire directory upwards until it reaches folders with a structure of `exports/textures`, where it creates a folder called `rotated` inside of the textures folder and then rotates the images within that folder automatically. Place this script inside your root directory of your texture projects.

[rotateb.py](./rotateb.py) - An improved version of the previous script. Let's you set the root directory of your texture project from the command line. Less tested. 

> [!CAUTION]
> USE THESE CAREFULLY. THESE ARE SOLELY FOR MY USAGE. 
>
> I am not responsible for whatever any issues this causes you. 



