FROM python:3.7

WORKDIR /usr/src/app

# Copy all our hashdd files to the container
COPY . .


# We'll need to build sdhash, so lets install depends
RUN apt-get -qq -y update && apt-get -qq -y --no-install-recommends install \
        libfuzzy-dev \
        libmhash-dev \
        libffi-dev \
        libprotobuf-dev \
        protobuf-compiler \
        swig \
        libboost-thread-dev \
        software-properties-common && \
    mv /usr/bin/lsb_release /usr/bin/lsb_release.bak && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# Link Python includes somewhere that the sdhash Makefile can find
RUN ln -s /usr/local/include/python3.7m /usr/include/python3.7

# Clone and build!
RUN git clone https://github.com/hashdd/sdhash.git
RUN cd sdhash && make swig-py 
RUN cp sdhash/swig/python/sdbf_class.py sdhash/swig/python/_sdbf_class.so libs/linux/x86_64/algorithms/

RUN python setup.py install

CMD [ "hashdd" ]

