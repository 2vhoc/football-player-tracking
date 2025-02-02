FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-runtime
RUN pip install opencv-python ultralytics deep_sort_realtime
RUN apt-get update -y
RUN apt-get install -y vim
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y libx11-xcb1
RUN apt-get install -y libxcb-xinerama0
RUN apt-get install -y libxcb1
RUN apt-get install -y libxrender1
RUN apt-get install -y libxext6
RUN apt-get install -y libxtst6
RUN apt-get install -y libqt5gui5
RUN apt-get install -y libqt5widgets5
RUN apt-get install -y libqt5core5a
RUN apt-get install -y qt5-default || cat /var/log/apt/term.log
ENV QT_QPA_PLATFORM=offscreen
CMD ["python", "setup.py"]


