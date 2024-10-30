# Image Metadata Extraction Tool

A comprehensive Python tool for extracting and analyzing image metadata, designed specifically to aid in neural network preprocessing and computer vision tasks.

## Overview

This tool extracts detailed metadata from images, including both technical specifications and advanced image analysis metrics that are particularly valuable for machine learning preprocessing. It processes both single images and entire directories, providing normalized outputs in both CSV and JSON formats.

## Features

- **Comprehensive Metadata Extraction:**
  - Basic image properties (dimensions, format, color mode)
  - Color statistics and distributions
  - Texture analysis using Local Binary Patterns (LBP)
  - Edge detection metrics
  - Shape analysis using contours
  - EXIF data processing
  - Color space analysis (LAB color space)

- **Neural Network Preprocessing Benefits:**
  - Normalized numerical outputs for direct ML pipeline integration
  - Feature extraction metrics useful for data preprocessing
  - Batch processing capabilities for large datasets
  - Consistent data formatting across different image types

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install dependencies:
```bash
pip install pillow numpy scikit-image pandas
```

## Usage

### Command Line Interface

The tool provides an interactive CLI with the following options:

1. Process a single image:
```bash
python src/main.py
# Select option 1 and enter the image path
```

2. Process all images in a directory:
```bash
python src/main.py
# Select option 2 and enter the directory path
```

### Using as a Module

```python
from src.image_processor import extract_metadata
from src.data_handler import save_metadata_to_files

# Process single image
metadata = extract_metadata("path/to/image.jpg")
save_metadata_to_files([metadata])
```

## Output Format

The tool generates two types of output files:
- `metadata_normalized.csv`: Normalized metadata in CSV format
- `metadata_normalized.json`: Complete metadata in JSON format

## Project Structure

```
src/
├── __init__.py
├── cli.py             # Command-line interface
├── data_handler.py    # Data processing and saving
├── image_processor.py # Core metadata extraction
├── io_handler.py      # File I/O operations
└── main.py           # Main application entry point
```

## Importance for Neural Network Preprocessing

This tool is particularly valuable for neural network preprocessing because:

1. **Feature Normalization:**
   - Automatically normalizes numerical features
   - Provides consistent scaling across datasets
   - Enables direct integration into ML pipelines

2. **Quality Assessment:**
   - Extracts image quality metrics
   - Identifies potential preprocessing needs
   - Helps in dataset cleaning and filtering

3. **Dataset Analysis:**
   - Provides statistical insights about your dataset
   - Helps identify biases in image collections
   - Enables informed preprocessing decisions

4. **Preprocessing Optimization:**
   - Identifies images requiring specific preprocessing
   - Enables automated preprocessing workflows
   - Supports batch processing for large datasets

## Technical Details

### Metadata Extraction Features

- **Color Analysis:**
  - RGB/LAB color space statistics
  - Color histogram analysis
  - Dominant color extraction

- **Texture Analysis:**
  - Local Binary Patterns (LBP)
  - Shannon entropy calculation
  - Statistical texture measures

- **Shape Analysis:**
  - Contour detection and analysis
  - Edge density calculation
  - Shape complexity metrics

### Performance Considerations

- Multi-threaded processing for directory operations
- Efficient memory management for large images
- Robust error handling and recovery

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

Personal use is granted, however any icense is given without the author's permission if you want to re-distribute and / or re-use the software.
