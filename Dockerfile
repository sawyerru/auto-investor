FROM python:3.7-alpine
COPY . /app
RUN pip install -r requirements.txt
CMD ["py","Main.py"]
