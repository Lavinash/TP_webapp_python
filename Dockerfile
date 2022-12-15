FROM python:3.11.1-buster
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
#RUN pip install requests
#EXPOSE 5000
CMD ["python3", "main.py"]
