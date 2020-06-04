FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN ls
RUN pip install -r /app/requirements.txt
CMD ["py","Main.py"]
