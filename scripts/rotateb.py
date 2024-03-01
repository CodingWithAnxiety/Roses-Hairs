import os
import subprocess

# Function to get the root directory from the user
def get_root_directory():
    while True:
        root_dir = input("Please enter the path to the root directory of your project: ").strip()
        if os.path.exists(root_dir):
            return root_dir
        else:
            print("The provided directory does not exist. Please try again.")

# Function to count PNG files in a directory
def count_png_files(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += sum(file.lower().endswith('.png') for file in files)
    return count

# Ask user for the root directory
root_dir = get_root_directory()

# Set a threshold for the maximum number of images to process at once
max_images_threshold = 50  # You can adjust this value as needed

# Count PNG files in the directory
total_png_files = count_png_files(root_dir)
if total_png_files > max_images_threshold:
    print(f"Warning: The directory contains {total_png_files} PNG files, which exceeds the set threshold of {max_images_threshold}.")
    proceed = input("Do you want to proceed anyway? (yes/no): ").strip().lower()
    if proceed != 'yes':
        print("Operation cancelled by user.")
        exit()

# Walk through the directory
for subdir, dirs, files in os.walk(root_dir):
    if subdir.endswith("exports\\textures"):  # Change this line to "exports/textures" on Unix-based systems
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
