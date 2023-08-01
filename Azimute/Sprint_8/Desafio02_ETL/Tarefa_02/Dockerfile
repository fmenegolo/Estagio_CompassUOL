FROM amazonlinux:2.0.20200602.0
RUN yum update -y
RUN yum install -y \
python3-pip \
zip \
RUN yum -y clean all
RUN python3.7 -m pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python3.7 -m pip install -r /app/requirements.txt -t /app/python/