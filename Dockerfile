FROM nvidia/cuda:12.3.2-base-ubuntu22.04

# System updates
RUN apt-get update && apt-get install -y python3 python3-pip git && apt-get clean

# Install runpod SDK
RUN pip3 install runpod

# Copy handler
COPY handler.py /handler.py

# Start the worker
CMD ["python3", "-u", "/handler.py"]
