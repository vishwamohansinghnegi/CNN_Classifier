import os
from PIL import Image

def clean_dataset(dataset_path):
    # Print the path being processed for debugging
    print(f"Cleaning dataset in: {os.path.abspath(dataset_path)}")

    # Iterate over each class directory (Cat/Dog directories)
    for class_dir in os.listdir(dataset_path):
        class_dir_path = os.path.join(dataset_path, class_dir)

        # Ensure it is a directory
        if os.path.isdir(class_dir_path):
            # Iterate over each image in the class directory
            for img_file in os.listdir(class_dir_path):
                img_path = os.path.join(class_dir_path, img_file)

                try:
                    # Try to open the image to verify it is valid
                    with Image.open(img_path) as img:
                        img.verify()  # Will throw an exception if the image is not valid
                except (IOError, SyntaxError) as e:
                    # Print which image is being deleted
                    print(f"Deleting corrupted image: {img_path}")
                    os.remove(img_path)  # Remove corrupted images

# Adjust the relative path using os
if __name__ == "__main__":
    # Dynamically resolve the relative path to PetImages directory
    current_file_path = os.path.abspath(__file__)
    dataset_path = os.path.join(os.path.dirname(current_file_path), '..', '..', '..', 'artifacts', 'data_ingestion', 'PetImages')

    # For debugging, print the fully resolved dataset path
    print(f"Resolved dataset path: {dataset_path}")

    # Call the clean_dataset function with the resolved path
    clean_dataset(dataset_path)
