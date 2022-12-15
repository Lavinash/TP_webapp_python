FROM python:3.8.5
COPY . /app
#RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 8000
CMD ["python", "main.py"]
