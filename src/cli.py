import sys
from typing import Callable, List

def display_menu():
    """Display the main menu options."""
    print("Extractor de Metadatos de Imágenes")
    print("-" * 40)
    print("Seleccione una opción:")
    print("1. Procesar una sola imagen")
    print("2. Procesar todas las imágenes en un directorio")
    print("0. Salir")

def get_user_input() -> str:
    """Get and validate user input."""
    return input("Ingrese su elección: ").strip()

def handle_single_image(process_func: Callable, save_funcs: List[Callable]):
    """Handle processing of a single image."""
    image_path = input("Ingrese la ruta de la imagen: ").strip()
    metadata = process_func(image_path)
    if metadata:
        for save_func in save_funcs:
            save_func([metadata])

def handle_directory(get_paths_func: Callable, 
                    process_func: Callable, 
                    save_funcs: List[Callable]):
    """Handle processing of all images in a directory."""
    directory = input("Ingrese la ruta del directorio: ").strip()
    try:
        image_paths = get_paths_func(directory)
        if image_paths:
            metadata_list = process_func(image_paths)
            for save_func in save_funcs:
                save_func(metadata_list)
        else:
            print("No se encontraron imágenes compatibles en el directorio.")
    except ValueError as e:
        print(str(e))
