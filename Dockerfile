# setup image
FROM python:3.9-alpine3.13

# maintainer
LABEL maintainer="https://ainoo.netlify.app"

ENV PYTHONUNBUFFERED=1

# set work directory
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
# configuration setups
RUN python -m venv /recipe_venv && \
    /recipe_venv/bin/pip install --upgrade pip && \
    /recipe_venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /recipe_venv/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --home /home/user \
        django-user 


ENV PATH="/recipe_venv/bin:$PATH"

USER django-user