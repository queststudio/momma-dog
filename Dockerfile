FROM nginx:1.13.9
MAINTAINER dmigo

RUN apt-get update && apt-get install -y curl gnupg2 gnupg1
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -y nodejs python python-pip python3 python3-pip
RUN apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev git

COPY ./backend ./backend
RUN pip3 install -r ./backend/requirements.txt

#COPY ./deployment/nginx.conf /etc/nginx/nginx.conf


CMD nginx -v
CMD node --version
CMD npm --version
CMD python3 --version
CMD pip3 --version


WORKDIR ./backend
CMD gunicorn -c './gunicorn_config.py' src:app

#CMD ["nginx", "-g", "daemon off;"] nginx for the win, but a bit later