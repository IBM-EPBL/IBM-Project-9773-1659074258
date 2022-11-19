FROM python:3.8.5-slim-buster
WORKDIR /app
ADD . /app
COPY requirement.txt /app
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
EXPOSE 8000
CMD ["python","covidsafe.py"]