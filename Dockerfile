FROM python:3.13.5-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY --from=datadog/serverless-init:1 /datadog-init /app/datadog-init
RUN pip install --target /dd_tracer/python/ ddtrace
ENV DD_SERVICE=datadog-demo-run-python
ENV DD_ENV=datadog-demo
ENV DD_VERSION=1
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
ENTRYPOINT ["/app/datadog-init"]
CMD ["/dd_tracer/python/bin/ddtrace-run", "python", "app.py"]
