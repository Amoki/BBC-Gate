FROM arm32v7/python:3.7-stretch
ENV PYTHONUNBUFFERED 1
ENV API_URL=http://localhost
ENV PYTHONPATH=/opt

ADD NFC-Reader-Library-4.010-2.deb /opt

RUN apt-get update && \
	apt-get install -y build-essential cmake && \
	yes | dpkg -i /opt/NFC-Reader-Library-4.010-2.deb

WORKDIR /opt
ADD requirements.txt /opt
RUN pip install -r requirements.txt
COPY ./ /opt
