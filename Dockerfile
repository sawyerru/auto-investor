FROM python:3.7-alpine
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY Main.py /Main.py
CMD ["py","Main.py"]