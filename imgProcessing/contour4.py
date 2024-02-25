import cv2
import numpy as np
from machineLearning import deteksi as dtc

def find_four_sided_contours(image, frame, roi_limits, multiple = False, counter = 0):
    # Ambil ROI dari frame berdasarkan batas yang diberikan
    x_min, x_max = roi_limits
    roi = image[:, x_min:x_max]

    prediksi = ""

    # Cari kontur pada ROI
    contours, _ = cv2.findContours(roi, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    hasil = frame.copy()

    min_area = 1000
    max_area = 20000

    four_corners_set = []

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            area = cv2.contourArea(contour)

            if min_area <= area <= max_area:
                # Dapatkan koordinat kotak pembatas
                x, y, w, h = cv2.boundingRect(contour)

                # Koreksi koordinat dalam konteks ROI
                x += x_min

                for point in approx:
                    point[0][0] += x_min

                l1 = np.array(approx[0]).tolist()
                l2 = np.array(approx[1]).tolist()
                l3 = np.array(approx[2]).tolist()
                l4 = np.array(approx[3]).tolist()

                finalOrder = []

                # Mengurutkan sudut berdasarkan koordinat x
                sortedX = sorted([l1, l2, l3, l4], key=lambda x: x[0][0])

                # Mengurutkan dua sudut pertama berdasarkan koordinat y
                finalOrder.extend(sorted(sortedX[0:2], key=lambda x: x[0][1]))

                # Mengurutkan dua sudut terakhir berdasarkan koordinat y secara terbalik
                finalOrder.extend(
                    sorted(sortedX[2:4], key=lambda x: x[0][1], reverse=True))

                four_corners_set.append(finalOrder)
                for a in approx:
                    cv2.circle(
                        hasil, (a[0][0], a[0][1]),10,(0,0,255),3
                    )
                # Gambar kotak pembatas pada citra
                if counter % 50 == 0:
                    cv2.rectangle(hasil, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    # Tambahkan teks luas area di pojok kanan atas
                    area_text = f'Area: {area:.2f}'
                    cv2.putText(hasil, area_text, (x+w-150, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                    # Untuk wrap perspektif
                    width, height = 200, 200
                    pts1 = np.float32(finalOrder)
                    # Menginisialisasi sudut sudut pada gambar datar
                    pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])

                    # Mendapatkan matriks transformasi perspektif dan menerapkannya pada gambar input
                    matrix = cv2.getPerspectiveTransform(pts1, pts2)
                    imgOutput = cv2.warpPerspective(frame, matrix, (width, height))

                    kartu_text = dtc.deteksi_kartu(imgOutput)

                    prediksi = str(kartu_text)

                # cv2.imshow('hasil', frame[y:y+h, x:x+w])
                # cv2.imshow('hasil2', imgOutput)
                    cv2.putText(hasil, str(kartu_text), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

                # Hentikan proses deteksi setelah menemukan satu kartu
                if not multiple:
                    break

    return hasil, prediksi
