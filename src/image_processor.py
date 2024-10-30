from collections import defaultdict
import numpy as np
from PIL import Image, ExifTags, ImageStat
from skimage import io, feature, color, measure
from skimage.color import rgb2gray

def extract_metadata(image_path):
    """Extract comprehensive metadata from an image file."""
    metadata = defaultdict(lambda: None)

    try:
        with Image.open(image_path) as img:
            # Basic metadata
            metadata['file_path'] = image_path
            metadata['format'] = img.format
            metadata['mode'] = img.mode
            metadata['width'], metadata['height'] = img.size
            metadata['aspect_ratio'] = round(img.size[0] / img.size[1], 2)
            metadata['color_profile'] = img.info.get('icc_profile', 'No disponible')
            metadata['has_alpha'] = img.mode == 'RGBA'

            # Color statistics
            stat = ImageStat.Stat(img)
            metadata['mean_intensity'] = stat.mean[0] if len(stat.mean) > 0 else None
            metadata['stddev_intensity'] = stat.stddev[0] if len(stat.stddev) > 0 else None

            # LAB color space analysis
            lab_image = color.rgb2lab(np.array(img.convert("RGB")))
            metadata['mean_lab_l'] = lab_image[..., 0].mean()
            metadata['mean_lab_a'] = lab_image[..., 1].mean()
            metadata['mean_lab_b'] = lab_image[..., 2].mean()

            # Color distribution
            if img.mode in ('RGB', 'RGBA'):
                metadata['histogram'] = img.histogram()
                palette = img.convert("RGB").getcolors(maxcolors=256)
                if palette:
                    metadata['palette'] = sorted(palette, key=lambda x: -x[0])[:5]

            # Fix: Convert image to float64 for local binary pattern calculation
            img_array = np.array(img.convert("RGB"))
            gray_image = rgb2gray(img_array)
            # Ensure the image is in float64 format
            gray_image = gray_image.astype(np.float64)
            lbp = feature.local_binary_pattern(gray_image, P=8, R=1, method='uniform')
            metadata['lbp_mean'] = float(lbp.mean())
            metadata['lbp_variance'] = float(lbp.var())
            metadata['entropy'] = measure.shannon_entropy(gray_image)

            # Edge detection
            edges = feature.canny(gray_image)
            metadata['edge_density'] = float(edges.mean())

            # Shape analysis
            contours = measure.find_contours(gray_image, 0.8)
            metadata['num_contours'] = len(contours)
            if contours:
                areas = []
                for contour in contours:
                    # Fix: Calculate area using numpy's trapz function
                    x = contour[:, 0]
                    y = contour[:, 1]
                    area = np.abs(np.trapz(y, x))
                    areas.append(area)
                metadata['mean_contour_area'] = float(np.mean(areas))
                metadata['stddev_contour_area'] = float(np.std(areas))

            # EXIF data processing
            try:
                exif_data = img._getexif()
                if exif_data:
                    for tag_id, value in exif_data.items():
                        tag = ExifTags.TAGS.get(tag_id, tag_id)
                        # Convert value to string to ensure JSON serialization
                        metadata[f'exif_{tag}'] = str(value)
                    
                    # Handle orientation
                    if 'exif_Orientation' in metadata:
                        orientation = metadata['exif_Orientation']
                        if orientation == '3':
                            img = img.rotate(180, expand=True)
                        elif orientation == '6':
                            img = img.rotate(270, expand=True)
                        elif orientation == '8':
                            img = img.rotate(90, expand=True)
                    
                    # GPS information
                    gps_info = exif_data.get(34853)
                    if gps_info:
                        metadata['GPSInfo'] = str(gps_info)
                else:
                    metadata['exif'] = "No se encontraron metadatos EXIF."
            except Exception as e:
                metadata['exif'] = f"Error reading EXIF: {str(e)}"

    except Exception as e:
        print(f"Error al procesar la imagen '{image_path}': {e}")
        return None

    return dict(metadata)  # Convert defaultdict to regular dict for JSON serialization
