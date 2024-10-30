import os
from concurrent.futures import ThreadPoolExecutor
from typing import List

def get_image_paths(directory: str) -> List[str]:
    """Get all supported image file paths from a directory."""
    supported_formats = ('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp', '.webp', '.heic')
    
    if not os.path.isdir(directory):
        raise ValueError(f"Error: El directorio '{directory}' no existe.")
    
    image_paths = [
        os.path.join(root, filename)
        for root, _, files in os.walk(directory)
        for filename in files
        if filename.lower().endswith(supported_formats)
    ]
    
    return image_paths

def process_images_parallel(extract_metadata_func, image_paths: List[str]) -> List[dict]:
    """Process multiple images in parallel using ThreadPoolExecutor."""
    metadata_list = []
    
    with ThreadPoolExecutor() as executor:
        results = executor.map(extract_metadata_func, image_paths)
        for metadata in results:
            if metadata:
                metadata_list.append(metadata)
    
    return metadata_list
