# pull official base image
FROM python:3.10-slim-buster

RUN mkdir -p /usr/tagby-consumer
RUN mkdir -p /usr/tagby-consumer/logs

# set work directory
WORKDIR /usr/tagby-consumer

# copy requirements file
COPY ./requirements.txt $WORKDIR/requirements.txt

# install dependencies
RUN apt-get update -yqq \
    && apt-get install -y git \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get install -y uwsgi-plugin-python3 && apt-get install -y gcc python3-dev \
    && apt-get install -y unzip xvfb libxi6 libgconf-2-4 && apt-get install -y curl unzip wget && apt-get install -y gpg && apt-get install -y vim jq procps \
    && apt-get install libmariadb-dev-compat libmariadb-dev -y && apt-get install -y fontconfig fonts-unfonts-core

RUN pip install --upgrade pip setuptools wheel psutil \
    && pip install --no-cache-dir -r $WORKDIR/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . $WORKDIR