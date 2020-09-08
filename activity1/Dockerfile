FROM ubuntu:18.04
RUN apt-get update && \
apt-get install -y vim && \
apt-get install -y nano && \
apt-get install -y x11vnc xvfb && \
apt-get install -y wget && \
apt-get install -y unzip && \
apt-get install -y git && \
apt-get install -y openjdk-8-jdk && \
mkdir tools
ADD https://www.cs.allegheny.edu/sites/amohan/upload/jbe.zip /tools/
RUN unzip tools/jbe.zip -d "tools/" && \
mkdir ~/.vnc && \
x11vnc -storepasswd 1234 ~/.vnc/passwd
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
