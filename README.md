# Image Deblur Script

This project provides a Python script to deblur images using OpenCV. The script processes all images in an input folder, applies a combination of Bilateral Filtering and Laplacian enhancement to remove noise and sharpen the image, and saves the results to an output folder.

## Features

- **Noise Removal:** Utilizes Bilateral Filtering to reduce noise while preserving edges.
- **Detail Enhancement:** Applies a Laplacian filter to sharpen image details.
- **Batch Processing:** Automatically processes all valid image files in the input folder.
- **Supported Formats:** Works with `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.tiff` image files.

## Folder Structure

```
.
├── image/                # Input folder containing images to be deblurred
├── image_deblur/         # Output folder where deblurred images will be saved
├── deblur.py             # Python script for deblurring images
```

## Requirements

- Python 3.6 or later
- OpenCV library

Install the required dependencies using:

```bash
pip install opencv-python
```

## Usage

1. Place the images you want to deblur in the `image/` folder.
2. Run the script using:

   ```bash
   python deblur.py
   ```

3. The deblurred images will be saved in the `image_deblur/` folder.

## How It Works

1. **Bilateral Filter:** Reduces noise while preserving edge information.
2. **Laplacian Filter:** Enhances details and sharpens the image.
3. **Conversion Steps:**
   - Convert to grayscale for processing.
   - Apply the filters.
   - Convert back to a color format before saving.

## Script Details

```python
# Folder input dan output
input_folder = './image'
output_folder = './image_deblur'

# Membuat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Fungsi deblur menggunakan Bilateral Filter dan filter Laplacian
def deblur_image(image):
    # Menghilangkan noise dengan Bilateral Filter
    denoised = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)
    
    # Menambahkan detail dengan Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)  # Menggunakan tipe data float64 untuk operasi
    laplacian = cv2.convertScaleAbs(laplacian)   # Konversi kembali ke 8-bit
    sharp = cv2.addWeighted(gray, 1.5, laplacian, -0.5, 0)  # Menyesuaikan tipe data
    
    # Konversi kembali ke format warna
    deblurred = cv2.cvtColor(sharp, cv2.COLOR_GRAY2BGR)
    return deblurred

# Mendeblur semua gambar dalam folder
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)
    
    # Memastikan hanya file gambar yang diproses
    if os.path.isfile(input_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # Membaca gambar
        image = cv2.imread(input_path)
        if image is None:
            print(f"File {file_name} tidak dapat dibuka.")
            continue
        
        # Mendeblur gambar
        deblurred_image = deblur_image(image)
        
        # Menyimpan gambar hasil
        cv2.imwrite(output_path, deblurred_image)
        print(f"{file_name} berhasil dideblur dan disimpan di {output_folder}.")
    else:
        print(f"{file_name} bukan file gambar yang valid.")

print("Proses deblur selesai.")
```

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or create an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
