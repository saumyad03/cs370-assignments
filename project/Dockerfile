FROM nvidia/cuda:12.4.0-devel-ubuntu22.04
WORKDIR /volume
COPY requirements.txt requirements.txt
RUN apt update && apt install libgdal-dev ffmpeg libsm6 libxext6  -y && apt install python3 -y && apt install python3-pip -y
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
