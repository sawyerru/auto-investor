FROM python:3.7-alpine
COPY . /app
RUN ls
RUN cat Dockerfile
RUN cd app/
RUN cat Main.py
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["py","Main.py"]
