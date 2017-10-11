# Protokoll

## Installation
Zur Installation von Jekins wurde ein Docker Container auf Basis des offiziellen Jekins Docker Images erstellt.
Das fertige Image findet sich unter https://hub.docker.com/re1coy/sew-jenkins/.

``` Dockerfile
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
# Back to jenkins
USER jenkins

EXPOSE 8083
```

Nach der Installation wurden die Plugins gewählt wobei unter anderem die Git und GitHub Plugin Installationen fehlschlugen.
