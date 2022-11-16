FROM python:3.9-bullseye

LABEL author="Patrick Stöckle <patrick.stoeckle@posteo.de>"

ENV PATH="${PATH}:/home/gl_user/.local/bin"

RUN apt-get update -qq \
    && apt-get autoremove -y -qq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash gl_user

WORKDIR /home/gl_user
USER gl_user

COPY --chown=gl_user dist dist

RUN pip install --no-cache-dir --upgrade pip==22.3.1 \
    && pip install --no-cache-dir dist/*.whl \
    && rm -rf dist \
    && create-forward-pages --version
