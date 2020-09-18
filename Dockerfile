FROM python:3.7.6

# Setup using root
USER root
WORKDIR /gl_files

RUN apt-get update -qq
RUN apt-get autoremove -y -qq
COPY src src
COPY requirements.txt ./
COPY README.* ./
COPY setup.* ./

RUN pip install -qq -r requirements.txt
RUN pip install .

RUN useradd --create-home --shell /bin/bash gl_user
USER gl_user
WORKDIR /home/gl_user
