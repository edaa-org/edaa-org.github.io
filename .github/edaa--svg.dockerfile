FROM debian:bullseye-slim

RUN apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    inkscape \
    npm \
    python3-pip \
    xauth \
    xvfb \
 && pip3 install svgwrite \
 && npm -g install svgo
