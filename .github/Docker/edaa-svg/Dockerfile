ARG IMAGE
ARG OS_VERSION
ARG PY_VERSION

FROM ${IMAGE}
ARG OS_VERSION
ARG PY_VERSION

# Meta information
LABEL maintainer="Patrick Lehmann <Paebbels@gmail.com>"
LABEL version="0.2"
LABEL description="Inkscape based on Debian ${OS_VERSION} (slim) with Python ${PY_VERSION}."

# Install Debian packages
RUN --mount=type=bind,target=/context \
    apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive xargs --no-run-if-empty -a /context/debian.list -- apt-get install -y --no-install-recommends \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get clean

# Install Python packages
RUN --mount=type=bind,target=/context \
    xargs --no-run-if-empty -a /context/python.list -- pip3 install

# Install NPM packages
RUN --mount=type=bind,target=/context \
    xargs --no-run-if-empty -a /context/npm.list -- npm -g install

RUN mkdir -p /usr/local/share/fonts/Teko \
 && curl -fsSL https://github.com/google/fonts/archive/refs/heads/main.tar.gz | tar xvzf - -C /usr/local/share/fonts --strip-components=3 --wildcards 'fonts-main/ofl/teko/*.ttf' \
 && fc-cache -fv \
 && fc-match Teko
