from image_processor import extract_metadata
from data_handler import save_metadata_to_files

def main():
    """Test the metadata extraction with test_image.png"""
    metadata = extract_metadata("test_image.png")
    if metadata:
        save_metadata_to_files([metadata])
        print("Successfully processed test_image.png")
    else:
        print("Failed to process test_image.png")

if __name__ == "__main__":
    main()
