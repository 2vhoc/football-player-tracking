import cv2, os, torch
from torch.xpu import device
from ultralytics import YOLO
from pprint import pprint
from deep_sort_realtime.deepsort_tracker import DeepSort
path_video = '../test/data_test/Match_1953_2_0_subclip.mp4'
path_model = '../model/last.pt'
model = YOLO(path_model)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
tracker = DeepSort(max_age=30)
tracking_class = 1
cap = cv2.VideoCapture(path_video)
model.eval()
model.to(device)
tracks = []
class_names = ['ball', 'player']
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = frame = cv2.resize(frame, (1920, 600))
    results = model(frame)
    detect = []
    for obj in results[0]:
        conf, label, bbox = obj.boxes.conf.item(), obj.names, obj.boxes.xyxy
        cls = int(obj.boxes.cls.item())
        bbox = [int(x.item()) for x in bbox[0]]
        x1, y1, x2, y2 = bbox
        w = x2 - x1
        h = y2 - y1
        # cls_id = label[]


        detect.append([[x1, y1, w, h], conf, label[cls]])


    tracks = tracker.update_tracks(detect, frame=frame)
    for track in tracks:
        if track.is_confirmed():
            track_id = track.track_id
            ltrb = track.to_ltrb()

            class_id = track.get_det_class()


            x1, y1, x2, y2 = map(int, ltrb)
            # print(x1, y1, x2, y2)

            text = f'{class_id} {track_id}'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            cv2.putText(frame, text, (x1, y1), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=2)
    # for dtc_obj in results[0]:
    # print(results[0])
    # exit(0)
    # boxes = results[0].boxes.xyxy
    # classes = results[0].names
    # # exit(0)
    # scores = results[0].boxes.conf
    # cls = results[0].boxes.cls
    # cls = cls.numpy()

    # bboxs = []
    # score = []
    # for box in zip(boxes, cls, scores):
    #   pass
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print('Completed')