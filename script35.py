import cv2
from pathlib import Path
from urllib.request import urlretrieve
folder = Path(__file__).resolve().parent
model = folder / "face_detection_yunet_2023mar.onnx"
if not model.exists() or model.stat().st_size < 100000:
    print("Завантажую нейромережу...")
    try:
        urlretrieve(
            "https://huggingface.co/opencv/opencv_zoo/resolve/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx",
            str(model)
        )
    except Exception as e:
        print("Не вдалося завантажити модель:", e)
        raise SystemExit
image = cv2.imread(str(folder / "photo.jpg"))
mask = cv2.imread(str(folder / "mask.png"), cv2.IMREAD_UNCHANGED)
if image is None or mask is None or model.stat().st_size < 100000:
    print("Помилка завантаження файлів")
    raise SystemExit
height, width = image.shape[:2]
net = cv2.FaceDetectorYN.create(str(model), "", (width, height), 0.4)
faces = net.detect(image)[1]
if faces is None or len(faces) < 2:
    print("Знайдено менше двох облич. Спробуй інше фото.")
    raise SystemExit
print("Знайдено облич:", len(faces))
for face in faces:
    x, y, w, h = map(int, face[:4])
    x, y = max(0, x), max(0, y)
    w, h = min(w, width - x), min(h, height - y)
    if w <= 0 or h <= 0:
        continue
    sticker = cv2.resize(mask, (w, h))
    alpha = sticker[:, :, 3] / 255.0
    for color in range(3):
        image[y:y+h, x:x+w, color] = (
            image[y:y+h, x:x+w, color] * (1 - alpha)
            + sticker[:, :, color] * alpha
        )
cv2.imwrite(str(folder / "result.jpg"), image)
print("Результат збережено у result.jpg")
cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()