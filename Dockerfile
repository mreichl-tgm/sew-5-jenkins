FROM jenkins/jenkins:lts
# Use root
USER root
RUN apt-get update -y
# Python
RUN apt-get install python3 -y
RUN apt-get install python3-nose -y
RUN apt-get install python3-nosexcover -y
RUN apt-get install python3-mock -y
RUN apt-get install python3-sphinx -y
RUN apt-get install pylint3 -y
RUN apt-get install pylint -y

EXPOSE 8080
