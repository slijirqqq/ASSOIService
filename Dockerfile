FROM python:3.10-alpine

# send output straight to the container logs instead of buffering
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/assoi/assoi_venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# create virtualenv
RUN python3 -m venv $VIRTUAL_ENV

# install system packages
RUN apt-get update \
  && apt-get install -y \
    gettext \
    # Please add new system packages above this line. Each line must ends with a backslash "\"
  && exit 0 # terminate last backslash. So we will have clear git blame

# update pip
RUN pip install --upgrade pip

# install python packages from prod.requirements.txt
# copy prod.requirements.txt only to use Docker cache
COPY prod.requirements.txt /opt/assoi/
WORKDIR /opt/assoi
RUN pip install -r prod.requirements.txt

COPY . /opt/assoi
