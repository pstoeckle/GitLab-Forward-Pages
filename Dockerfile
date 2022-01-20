FROM python:3.9-bullseye

ARG COMMIT=""
ARG COMMIT_SHORT=""
ARG BRANCH=""
ARG TAG=""

LABEL author="Patrick Stöckle <patrick.stoeckle@tum.de>"
LABEL edu.tum.i4.gl-pages-forward.commit=${COMMIT}
LABEL edu.tum.i4.gl-pages-forward.commit-short=${COMMIT_SHORT}
LABEL edu.tum.i4.gl-pages-forward.branch=${BRANCH}
LABEL edu.tum.i4.gl-pages-forward.tag=${TAG}

ENV COMMIT=${COMMIT}
ENV COMMIT_SHORT=${COMMIT_SHORT}
ENV BRANCH=${BRANCH}
ENV TAG=${TAG}

RUN apt-get update -qq \
    && apt-get autoremove -y -qq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash gl_user
WORKDIR /home/gl_user

COPY dist dist

RUN chown gl_user dist

USER gl_user

RUN pip install --no-cache-dir --upgrade pip==21.3.1 \
    && pip install --no-cache-dir dist/*.whl \
    && rm -rf dist

ENV PATH="${PATH}:/home/gl_user/.local/bin"

RUN create-forward-pages --version
