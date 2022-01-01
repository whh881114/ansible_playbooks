FROM harbor.freedom.org/freedom/common-centos7:latest

LABEL AUTHOR="Wanghaohao"
LABEL DATACENTER="DELL-R620-PERSONAL-DATACENTER"

WORKDIR /root/.kube
ADD files/config .
ADD entrypoint.sh /

WORKDIR /root

# 个人数据中心的kubeneters版本为1.21.5，所以kubectl安装的版本也是这个。
RUN set -eux && \
    chmod 600 /root/.kube/config && \
    chmod 755 /entrypoint.sh && \
    yum -y install http://foreman.freedom.org/pub/jenkins-2.319.1-1.1.noarch.rpm \
                   docker-ce \
                   kubectl-1.21.5

VOLUME /data

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]