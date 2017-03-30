FROM ubuntu:16.04

#############
# Arg & Env #
#############

ARG PROFILE_NAME

ENV PROJECT_NAME backend
ENV PACKAGE_NAME wp_test
ENV PROFILE_NAME ${PROFILE_NAME:-local}

ENV PROJECT_PATH /app
ENV PACKAGE_PATH ${PROJECT_PATH}/${PACKAGE_NAME}

ENV PYTHONUNBUFFERED 1

#########################
# System & Requirements #
#########################

RUN set -ex \
	&& persistentDeps="python2.7 gettext" \
	&& buildDeps="gcc python-dev python-pip libsasl2-dev libldap2-dev libssl-dev libffi-dev libpq-dev" \
	&& apt-get update \
	&& apt-get install -y $persistentDeps $buildDeps --no-install-recommends

COPY ./requirements/ ./requirements/

RUN pip install --upgrade pip
RUN pip install setuptools

RUN pip install -U pip -r ./requirements/${PROFILE_NAME}.txt \
	&& rm -r ./requirements \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/* \
	&& apt-get purge -y --auto-remove $buildDeps

#######
# App #
#######

WORKDIR ${PROJECT_PATH}

COPY ./manage.py ./
COPY ./${PACKAGE_NAME} ./${PACKAGE_NAME}/