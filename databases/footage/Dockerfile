# pull official base image
FROM postgres:12-alpine

RUN mkdir cron

# set work directory
WORKDIR /cron

# copy entrypoint.sh
COPY backup.sh /etc/periodic/15min/backup.sh
RUN chmod a+x /etc/periodic/15min/backup.sh

RUN mkdir backups

RUN crond start