# Base image is python 3.5 using conda package manager
FROM continuumio/miniconda3

WORKDIR /usr/src/app

# Copy requirements to Docker image and install all
COPY environ.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "magical", "/bin/bash", "-c"]
RUN conda env list

COPY Scripts/ .
COPY Algorithms/ .
COPY Main.py .

ENTRYPOINT ["conda", "run", "-n", "magical", "python", "run.py"]


# BUILD WITH:
# docker build -t '<NAME>' .

# RUN WITH:
# docker run --env.list-file ./env.list.list -d
