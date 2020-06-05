# Base image is python 3.5 using conda package manager
FROM continuumio/miniconda3

WORKDIR /usr/src/app

# Copy requirements to Docker image and install all
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Scripts/ .
COPY Algorithms/ .

CMD ["py","-u", "Main.py"]


# BUILD WITH:
# docker build -t '<NAME>' .

# RUN WITH:
# docker run --env.list-file ./env.list.list -d
