FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip && \
    pip3 install --no-cache-dir requests && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt

COPY http_check.py .

CMD ["python3", "http_check.py"]