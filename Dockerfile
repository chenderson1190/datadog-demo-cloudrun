FROM python:3.13.5-slim
ENV PYTHONUNBUFFERED=1
ENV DD_ENV="demo"
ENV DD_SERVICE="Datadog Demo"
ENV DD_VERSION="0.1"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
CMD ["ddtrace-run", "python", "app.py"]