FROM node:20
WORKDIR /usr/src/app
COPY main.js .
ENTRYPOINT ["tail", "-f", "/dev/null"]