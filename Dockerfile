FROM python:3.13.5-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
CMD ["ddtrace-run", "flask", "run"]