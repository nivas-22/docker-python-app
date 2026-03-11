FROM - Take Base Image (Take from docker hub)

LABELS - Key value pairs, give project name or author name

RUN - Execute commands

ADD/COPY - Add files and folders into image

ENTRYPOINT - Allows you to configure a container that will run as an executable

VOLUME - Creates a mount point and marks it as holding externally mounted volumes

EXPOSE - Container listens on the specific network ports at runtime

ENV - To set an environmemt variable

USER - Sets the username

WORKDIR - Sets the working directory

ARG - Define a variables that user can pass at build time

ONBUILD - Adds to the image trigger instruction to be executed at a later time
