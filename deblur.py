import cv2
import os

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
