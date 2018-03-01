FROM python:3.6.4
MAINTAINER dmigo

RUN apt-get update && apt-get install -y curl
RUN apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev git

COPY ./requirements.txt ./backend
RUN pip3 install -r ./backend/requirements.txt

CMD python3 --version
CMD pip3 --version

COPY . ./backend
WORKDIR ./backend
CMD sh ./start.sh