FROM python:3.9-buster

# Setup using root
USER root
WORKDIR /gl_files

RUN apt-get update -qq
RUN apt-get autoremove -y -qq
COPY dist dist

RUN pip install dist/*.whl

RUN useradd --create-home --shell /bin/bash gl_user
USER gl_user
WORKDIR /home/gl_user
