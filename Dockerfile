FROM python:3.12

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
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# Clone and build!
RUN git clone https://github.com/hashdd/sdhash.git
RUN cd sdhash && make swig-py
RUN cp sdhash/swig/python/sdbf_class.py sdhash/swig/python/_sdbf_class.so libs/linux/x86_64/algorithms/

RUN pip install --upgrade pip setuptools
RUN pip install .[all]

CMD [ "hashdd" ]

