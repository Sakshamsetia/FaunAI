import os
import shutil

# Path where all the animal folders are located
source_dir = "/home/saksham/.cache/kagglehub/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals/versions/5/animals/animals"

# Destination directory where all images will be gathered
dest_dir = "/home/saksham/Desktop/GenAI/FaunAI/all_animals"

os.makedirs(dest_dir, exist_ok=True)

for animal in os.listdir(source_dir):
    animal_path = os.path.join(source_dir, animal)
    if os.path.isdir(animal_path):  # make sure it's a folder
        for file_name in os.listdir(animal_path):
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                src_path = os.path.join(animal_path, file_name)
                
                # Add animal name prefix to avoid conflicts
                new_name = f"{animal}_{file_name}"
                dest_path = os.path.join(dest_dir, new_name)

                # Copy file
                shutil.copy2(src_path, dest_path)

print("✅ All images successfully copied to:", dest_dir)
