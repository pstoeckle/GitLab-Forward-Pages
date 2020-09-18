FROM python:3.7.6

# Setup using root
USER root
WORKDIR /gl_files

RUN apt-get update -qq
RUN apt-get autoremove -y -qq
COPY src/gl_pages_forward src/gl_pages_forward
COPY requirements.txt ./
COPY README.* ./
COPY setup.* ./
COPY MANIFEST.* ./

RUN pip install -qq -r requirements.txt
RUN python setup.py install

RUN useradd --create-home --shell /bin/bash gl_user
USER gl_user
WORKDIR /home/gl_user
