FROM python:3.9-slim

# send output straight to the container logs instead of buffering
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system packages
RUN apt-get update \
  && apt-get install -y \
    gettext \
    python3-dev \
    # Please add new system packages above this line. Each line must ends with a backslash "\"
  && exit 0 # terminate last backslash. So we will have clear git blame

# update pip
RUN pip install --no-cache-dir --upgrade pip

# install python packages from prod.requirements.txt
# copy prod.requirements.txt only to use Docker cache.

COPY prod.requirements.txt /opt/assoi/
WORKDIR /opt/assoi
RUN pip install -Ur prod.requirements.txt

COPY . /opt/assoi
