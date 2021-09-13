FROM python:3.7-slim-buster
LABEL maintainer='brampande@gmail.com'
ENV WORKDIR=/usr/local/bitcoin \
    PYTHONPATH="${PYTHONPATH}:/usr/local/bitcoin"

RUN mkdir $WORKDIR
COPY . $WORKDIR
RUN apt-get clean && \
    apt-get update && \
    apt-get install -yqq --no-install-recommends curl

RUN pip install -U pip \
    pip install -U requests==2.25.1 \
    clint==0.5.1 \
    pandas==1.3.3

WORKDIR $WORKDIR

ENTRYPOINT ["python3", "scripts/module/bitcoin_data_transformation.py"]



