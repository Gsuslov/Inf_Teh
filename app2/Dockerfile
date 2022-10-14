FROM ubuntu:latest
COPY app /app
USER root
RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r /app/requirements.txt
ENV PORT1 5555
ENV PORT2 6666
CMD ["/bin/sh","-c","/usr/bin/python3 /app/run.py"]
