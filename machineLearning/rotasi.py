from PIL import Image
import os

def rotate_images_in_folder(folder_path):
    # Pastikan path folder benar dan folder tidak kosong
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("Folder tidak ditemukan atau kosong.")
        return

    # Loop melalui setiap folder dalam folder utama
    for subfolder_name in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder_name)

        # Pastikan bahwa itu adalah folder dan bukan file
        if os.path.isdir(subfolder_path):
            # Loop melalui setiap file dalam folder tersebut
            for file_name in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file_name)

                # Cek apakah itu file gambar (misalnya, JPEG atau PNG)
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        # Buka gambar
                        image = Image.open(file_path)

                        # Rotasi 180 derajat
                        rotated_image_180 = image.rotate(180)
                        save_rotated_image(rotated_image_180, subfolder_path, file_name, "180")

                        # Rotasi 90 derajat ke kanan
                        rotated_image_right = image.rotate(-90)
                        save_rotated_image(rotated_image_right, subfolder_path, file_name, "right")

                        # Rotasi 90 derajat ke kiri
                        rotated_image_left = image.rotate(90)
                        save_rotated_image(rotated_image_left, subfolder_path, file_name, "left")

                    except Exception as e:
                        print(f"Error saat memproses {file_name}: {str(e)}")

def save_rotated_image(rotated_image, folder_path, original_file_name, direction):
    # Dapatkan nama file baru dengan menambahkan awalan "rotated_{direction}_" pada nama file asli
    new_file_name = f"rotated_{direction}_{original_file_name}"

    # Gabungkan path untuk file baru di folder yang sama
    new_file_path = os.path.join(folder_path, new_file_name)

    # Simpan gambar yang telah dirotasi ke file baru
    rotated_image.save(new_file_path)

    print(f"Rotasi {direction} berhasil: {new_file_name}")

if __name__ == "__main__":
    dataset_path = "machineLearning/dataSet"  # Ganti dengan path folder dataset yang sesuai
    rotate_images_in_folder(dataset_path)
