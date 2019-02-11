FROM python:3
#RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
#RUN apt-get install -y \
#    libffi-dev \
#    libssl-dev \
#    libxml2-dev \
#    libxslt-dev \
#    libjpeg-dev \
#    libfreetype6-dev \
#    zlib1g-dev \
#    net-tools \
#    vim \
#    python-pip
RUN pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
