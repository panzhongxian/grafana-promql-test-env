FROM python:3.10
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD python metrics_exposer.py
