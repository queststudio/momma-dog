FROM nginx:latest
MAINTAINER dmigo

RUN apt-get update && apt-get install -y curl gnupg gnupg1 gnupg2
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -y nodejs
     
COPY ./deploy/nginx.conf ./etc/nginx/nginx.conf
COPY . ./frontend
WORKDIR ./frontend
RUN npm install
RUN npm run build

CMD sh ./start.sh