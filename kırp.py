from PIL import Image
import os

# Klasör yolunu belirle
folder_path = "photos"

# Klasördeki dosya adlarını al
file_names = os.listdir(folder_path)

# Her dosya için işlem yap
for file_name in file_names:
    # Dosya yolunu belirle
    file_path = os.path.join(folder_path, file_name)
    # Dosya uzantısını kontrol et
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        # Dosyayı aç
        with Image.open(file_path) as img:
            # Resmin boyutunu al
            width, height = img.size
            # Kırpmak istediğimiz yükseklik hesapla
            crop_height = min(90, height)
            # Resmi kırp
            cropped_img = img.crop((0, 0, width, height - crop_height))
            # Kırpılmış resmi kaydet
            cropped_img.save(file_path)