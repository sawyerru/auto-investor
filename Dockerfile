## Base image is python 3.5 using conda package manager
FROM python:3.7

WORKDIR /usr/src/app

# Copy requirements to Docker image and install all
COPY requirements.txt .
RUN pip install -r --no-cache-dir requirements.txt

COPY Scripts/ .
COPY Algorithms/ .
COPY Main.py .

CMD ["py", "-u", "Main.py"]


#ENTRYPOINT ["conda", "run", "-n", "magical", "python", "run.py"]


# BUILD WITH:
# docker build -t '<NAME>' .

# RUN WITH:
# docker run --env.list-file ./env.list.list -d

#FROM continuumio/miniconda3
#
#WORKDIR /app
#
## Create the environment:
#COPY environment.yml .
#RUN conda env create -f environment.yml
#
#COPY Scripts/ .
#COPY Algorithms/ .
#COPY Main.py .
#
## Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "magical", "/bin/bash", "-c"]
#
## Make sure the environment is activated:
##RUN echo "Make sure flask is installed:"
##RUN python -c "import flask"
#
## The code to run when container is started:
#COPY run.py .
#ENTRYPOINT ["conda", "run", "-n", "magical", "python", "Main.py"]
