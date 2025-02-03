# Player tracking
## Overview
Dự án nhận diện cầu thủ và tracking cầu thủ trong 1 trận đấu
## Tính năng chính
- Nhận diện và tracking cầu thủ


## Yêu cầu hệ thống
- Python 3.8+
- CUDA capable GPU (recommended)
- Các thư viện chính:
  - OpenCV
  - PyTorch

## Cài đặt
1. Clone repository:
```bash
https://github.com/2vhoc/football-player-tracking
cd football-player-tracking
```

2. Tạo môi trường ảo:
```bash
python -m venv pt
source pt/bin/activate  # Linux/Mac
pt\Scripts\activate     # Windows
```

3. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
```
4. Truy cập <a href="https://drive.google.com/file/d/1MIoRcOknxE85-jZN1nnpSdup_r2cfhno/view?usp=sharing">Link</a> để tải model và để nó vào: model/



5. Cài đặt Docker:
```bash
# Tự tìm hiểu và cài bản CPU nha

```




## Sử dụng

### Chạy hệ thống (build image)
```bash
sudo docker build -t football .
#wait
```
### Chạy container

```bash
sudo docker run -it --rm -v "$PWD":/workspace football bash

```

### Chạy demo (trong container)

```bash
cd src/

```
```bash
python 3 eval.py
# chạy xong vào phần demo/videos xem
```



## Model Training

### Dataset
- Sử dụng bộ dataset với 1500 ảnh trong đó 1300 là bộ train còn lại là bộ test


## Ảnh demo (chưa track)
![Demo](https://raw.githubusercontent.com/2vhoc/football-player-tracking/main/demo/images/frame.jpg)
*Hình ảnh: Đánh giá qua bộ test mà mô hình chưa gặp bao giờ*
## Ảnh demo (đã track)
![Demo](https://raw.githubusercontent.com/2vhoc/football-player-tracking/main/demo/images/Screenshot%20from%202025-02-02%2012-20-43.png)
*Hình ảnh: Đánh giá qua bộ test mà mô hình chưa gặp bao giờ*

![Demo](https://raw.githubusercontent.com/2vhoc/football-player-tracking/main/demo/videos/2025-02-02%2018-20-18.mp4)


## Đóng góp
Mọi đóng góp đều được chào đón. Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi (`git commit -m 'Add amazing feature'`)
4. Push lên branch (`git push origin feature/amazing-feature`)
5. Tạo Pull Request


## Liên hệ
- Email: 2vhoc7@gmail.com
- Website: https://2vhocblog.vercel.app
- Issues: https://github.com/2vhoc/football-player-tracking/issues

## Citation
Nếu bạn sử dụng project này trong nghiên cứu của mình, vui lòng trích dẫn:
```
@article{football-player-tracking2025,
  title={Real-time football-player-tracking Using Deep Learning},
  author={Vũ Văn Học},
  year={2025}
}
```

