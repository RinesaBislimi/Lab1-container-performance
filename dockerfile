FROM python:3.11-slim

WORKDIR /app
COPY app.py .
RUN pip install matplotlib
RUN mkdir -p /app/output

CMD ["python", "app.py"]
