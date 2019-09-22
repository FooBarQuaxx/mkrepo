FROM centos:7

SHELL ["/bin/bash", "-x", "-c"]

RUN yum -y install \
           epel-release \
 && yum -y install \
           createrepo \
           python-pip \
 && yum clean all

RUN pip install -U pip setuptools

ADD . /usr/src/mkrepo

RUN pip install /usr/src/mkrepo

RUN rm -rf /usr/src/mkrepo
