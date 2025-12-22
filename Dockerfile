# setup image
FROM python:3.9-alpine3.13

# maintainer
LABEL maintainer="ainooebenezer05@gmail.com"

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
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /recipe_venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /recipe_venv/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --home /home/user \
        django-user 


ENV PATH="/recipe_venv/bin:$PATH"

USER django-user