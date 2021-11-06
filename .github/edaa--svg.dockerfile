FROM debian:bullseye-slim

RUN apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    curl \
    inkscape \
    npm \
    python3-pip \
    xauth \
    xvfb \
 && pip3 install svgwrite \
 && npm -g install svgo \
 && mkdir -p /usr/local/share/fonts/Teko \
 && curl -fsSL https://github.com/google/fonts/archive/refs/heads/main.tar.gz | tar xvzf - -C /usr/local/share/fonts --strip-components=3 --wildcards 'fonts-main/ofl/teko/*.ttf' \
 && fc-cache -fv \
 && fc-match Teko
