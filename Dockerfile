FROM nvidia/cuda:12.3.2-base-ubuntu22.04

WORKDIR /workspace

COPY requirements.txt .
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

COPY handler.py .

CMD ["python3", "handler.py"]
