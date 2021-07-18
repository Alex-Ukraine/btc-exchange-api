FROM python:3.8

RUN useradd --create-home wincity18
WORKDIR /btc-exchange-api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .. .

RUN chown -R wincity18:wincity18 ./
USER wincity18