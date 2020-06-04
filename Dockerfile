FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN dir
RUN pip install -r /app/requirements.txt
CMD ["py","Main.py"]
