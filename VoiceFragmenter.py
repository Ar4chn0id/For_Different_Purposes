import os
import subprocess

#uygulama, bir ses dosyasını 2 saniyelik parçalara böler ve her bir parçayı çıktı dizinine ekler
# MP3 dosyasının yolunu girin 
mp3_file = "negative/voice10.mp3"

# Çıktı klasörünün yolunu girin
try:
    os.makedirs("negative_out/out10")
except:
    pass

output_dir = "negative_out/out10" 

# MP3'ü 2 saniyelik parçalara böl
subprocess.run(["ffmpeg", "-i", mp3_file, "-f", "segment", "-segment_time", "2", "-c", "copy", os.path.join(output_dir, "out%03d.mp3")])

# Parçalara bölünmüş MP3'leri klasöre kopyala
for f in os.listdir(output_dir):
    if f.endswith(".mp3"):
        os.rename(os.path.join(output_dir, f), os.path.join(output_dir, f"{f.replace('out', '')}.mp3")) 