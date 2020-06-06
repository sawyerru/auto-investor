## Base image is python 3.5 using conda package manager
FROM python:3.7

WORKDIR /usr/src/app

# Copy requirements to Docker image and install all
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Scripts/ .
COPY Algorithms/ .
COPY Main.py .

CMD ["py", "-u", "Main.py"]
