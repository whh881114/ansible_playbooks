# prometheus配置身份验证

## 官方文档
- https://prometheus.io/docs/guides/basic-auth/
- https://prometheus.io/docs/alerting/latest/https/
- https://github.com/prometheus/pushgateway#tls-and-basic-authentication

## 生成用户名和密码
  ```shell
    # yum -y install httpd-tools
    # htpasswd -b -B -c prometheus-basic-auth.data prometheus prometheus
  ```

## 生成配置web.yml配置文件，请查阅prometheus/configmap.yaml文件。

## 启动prometheus时，需要指定`--web.config.file`配置项，请查阅prometheus/statefulset.yaml文件。
