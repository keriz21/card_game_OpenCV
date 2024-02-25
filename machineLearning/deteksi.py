from keras.models import load_model
import cv2
import numpy as np

# Load model deteksi gambar (.h5)
model_path = "machineLearning/BobotKartu.h5"
model = load_model(model_path)

label = [
    "as clubs",
    "as diamonds",
    "as hearts",
    "as spades",
    "delapan clubs",
    "delapan diamonds",
    "delapan hearts",
    "delapan spades",
    "lima clubs",
    "lima diamonds",
    "lima hearts",
    "lima spades",
    "empat clubs",
    "empat diamonds",
    "empat hearts",
    "empat spades",
    "jack clubs",
    "jack diamonds",
    "jack hearts",
    "jack spades",
    "joker",
    "king clubs",
    "king diamonds",
    "king hearts",
    "king spades",
    "sembilan clubs",
    "sembilan diamonds",
    "sembilan hearts",
    "sembilan spades",
    "queen clubs",
    "queen diamonds",
    "queen hearts",
    "queen spades",
    "tujuh clubs",
    "tujuh diamonds",
    "tujuh hearts",
    "tujuh spades",
    "enam clubs",
    "enam diamonds",
    "enam hearts",
    "enam spades",
    "sepuluh clubs",
    "sepuluh diamonds",
    "sepuluh hearts",
    "sepuluh spades",
    "tiga clubs",
    "tiga diamonds",
    "tiga hearts",
    "tiga spades",
    "dua clubs",
    "dua diamonds",
    "dua hearts",
    "dua spades"
]

# Fungsi untuk melakukan klasifikasi gambar
def classify_image(image, model):

    # Praproses gambar (sesuai dengan praproses model yang dilatih)
    # Contoh: Normalisasi nilai piksel ke rentang [0, 1]
    image = image / 255.0

    # Ubah ukuran gambar (sesuai dengan ukuran input model yang dilatih)
    image = cv2.resize(image, (128, 128))  # Ukuran input model

    # Feed into model
    img = np.expand_dims(image, axis=0)  # Menambahkan dimensi batch
    predicted_class_index = np.argmax(model.predict(img, verbose=0))

    return predicted_class_index

def deteksi_kartu(image):
    hasil = classify_image(image,model)

    return label[hasil]