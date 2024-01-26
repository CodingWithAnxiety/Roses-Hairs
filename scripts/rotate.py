import os
import subprocess

# Set the root directory of your project
root_dir = "./"  # Place file in root directory of project or change to ../ to run from here and rotate automatically. 

# Walk through the directory
for subdir, dirs, files in os.walk(root_dir):
    if subdir.endswith("exports\\textures"):  # Change this line to "exports/textures" on Unix-based system, such as linux.
        for angle in [90, 180, 270]:
            # Create angle-specific sub-directory inside 'rotated' if it doesn't exist
            angle_dir = os.path.join(subdir, "rotated", str(angle))
            if not os.path.exists(angle_dir):
                os.makedirs(angle_dir)

        for file in files:
            if file.lower().endswith(".png"):
                full_file_path = os.path.join(subdir, file)
                for angle in [90, 180, 270]:
                    angle_dir = os.path.join(subdir, "rotated", str(angle))
                    output_file_path = os.path.join(angle_dir, f"{os.path.splitext(file)[0]}_{angle}.png")
                    # Use ImageMagick's convert command to rotate images
                    subprocess.run(["magick", "convert", full_file_path, "-rotate", str(angle), output_file_path])
                    print(f"Rotated {file} by {angle} degrees and saved to {output_file_path}")

print("Rotation process completed.")
