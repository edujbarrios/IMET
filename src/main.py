#!/usr/bin/env python3

from image_processor import extract_metadata
from data_handler import save_metadata_to_files
from io_handler import get_image_paths, process_images_parallel
from cli import display_menu, get_user_input, handle_single_image, handle_directory

def main():
    """Main application entry point."""
    while True:
        display_menu()
        choice = get_user_input()

        if choice == '1':
            handle_single_image(
                extract_metadata,
                [save_metadata_to_files]
            )
        elif choice == '2':
            handle_directory(
                get_image_paths,
                lambda paths: process_images_parallel(extract_metadata, paths),
                [save_metadata_to_files]
            )
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
