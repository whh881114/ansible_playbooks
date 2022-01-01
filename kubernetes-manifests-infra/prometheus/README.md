# 说明
- prometheus
    - 从kubernetes-1.16.15官方源码文件中找到的，然后根据实际情况，自己修改。地址为：https://github.com/kubernetes/kubernetes/tree/release-1.16/cluster/addons/prometheus。

- kube-state-metrics
    - https://github.com/kubernetes/kube-state-metrics/tree/master/examples/standard

- prometheus-basic-auth
    - 官方文档
        - https://prometheus.io/docs/guides/basic-auth/
        - https://prometheus.io/docs/alerting/latest/https/
        - https://github.com/prometheus/pushgateway#tls-and-basic-authentication
    - 生成用户名和密码
      ```shell
        # yum -y install httpd-tools
        # htpasswd -b -B -c prometheus-basic-auth.data prometheus prometheus
      ```
    - 生成配置web.yml配置文件，请查阅prometheus/configmap.yaml文件。
    - 启动prometheus时，需要指定`--web.config.file`配置项，请查阅prometheus/statefulset.yaml文件。
    - 注意点：需要关掉prometheus的心跳检查。