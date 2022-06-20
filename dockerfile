FROM python:3.10
WORKDIR /usr/local/app
COPY ./requirements.txt /usr/local/app/requirements.txt
RUN apt update
RUN apt install ffmpeg -y
RUN pip install -r requirements.txt
COPY . /usr/local/app/
CMD [ "python", "src/main.py"]