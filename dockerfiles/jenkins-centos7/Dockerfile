FROM harbor.freedom.org/freedom/common-centos7:latest

LABEL AUTHOR="Wanghaohao"
LABEL DATACENTER="DELL-R620-PERSONAL-DATACENTER"


RUN set -eux && \
    yum -y install ftp://foreman.freedom.org/pub/jenkins-2.319.1-1.1.noarch.rpm \
                   docker-ce

WORKDIR /root

VOLUME /data

EXPOSE 8080

ADD entrypoint.sh /

RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]