# Use a specific version of Ubuntu for reproducibility
FROM ubuntu:18.04

# Update package list and install necessary packages
RUN apt-get update && \
    apt-get install -y \
        bash \
        build-essential \
        curl \
        iproute2 \
        iputils-ping \
        passwd \
        sudo \
        vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a new group called "CISCO" and a new user called "cisco" with the password "cisco"
RUN groupadd CISCO \
    && useradd -m cisco \
    && echo 'cisco:cisco' | chpasswd \
    && usermod -aG sudo cisco \
    && usermod -aG CISCO cisco \
    && chsh -s /bin/bash cisco


# Set the default user to be "cisco"
USER cisco

# Set the working directory to be the home directory of the "cisco" user
WORKDIR /home/cisco

RUN mkdir Desktop Downloads Music Public Templates Documents labs Pictures snap Videos
RUN mkdir labs/lab1-demo labs/lab2-demo

# Start a bash shell as the default command
CMD ["/bin/bash"]