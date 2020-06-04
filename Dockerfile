FROM python:3.7-alpine
COPY . /
WORKDIR /
RUN ls
RUN pip install -r requirements.txt
CMD ["py","Main.py"]
