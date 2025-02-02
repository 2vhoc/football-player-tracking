import cv2, os, torch
from torch.xpu import device
from ultralytics import YOLO
from pprint import pprint
from deep_sort_realtime.deepsort_tracker import DeepSort
path_video = '../test/data_test/Match_1953_2_0_subclip.mp4'
path_model = '../model/last.pt'
model = YOLO(path_model)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
tracker = DeepSort(max_age=10)
tracking_class = 1
cap = cv2.VideoCapture(path_video)
model.eval()
model.to(device)
tracks = []

output_path = '../demo/output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 25.0
frame_size = (1920, 600)


out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = frame = cv2.resize(frame, (1920, 600))
    results = model(frame)
    detect = []
    # for dtc_obj in results[0]:
    # print(results[0])
    # exit(0)
    boxes = results[0].boxes.xyxy
    classes = results[0].names
    # exit(0)
    scores = results[0].boxes.conf
    cls = results[0].boxes.cls
    # cls = cls.numpy()

    bboxs = []
    score = []
    for box in zip(boxes, cls, scores):
        # print(box)
        # print(len(box))
        # print(int(box[1]))
        # print(type(box[2]))
        # print(str(box[2].item()))
        # exit(0)
        # box = box.numpy()
        cv2.rectangle(frame, (int(box[0][0]), int(box[0][1])), (int(box[0][2]), int(box[0][3])), (0, 255, 0), 1)
        cv2.putText(frame, text=str(classes[int(box[1])]), org=(int(box[0][0]), int(box[0][1])), fontFace=1, fontScale=1, color=(0, 0, 255), thickness=1)
        cv2.putText(frame, text=str(str(box[2].item())[:4]), org=(int(box[0][0]), int(box[0][1])-10), fontFace=1, fontScale=1, color=(0, 255, 0), thickness=1)
    # tracks = tracker.update_tracks(fame)
    # exit(0)

    out.write(frame)
out.release()
cap.release()


print('Completed')
