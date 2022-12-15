FROM python:3.11.1
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
CMD ["python3", "main.py"]
