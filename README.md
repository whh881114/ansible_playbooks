# ansible_playbooks 更新日志

## TODO-LIST（日期不定）
- foreman服务器部署prometheus，当前仅用于监控虚拟机。

- foreman服务器部署单机的elasticsearch+filebeat+kibana+fluentd。

- 创建mysql_exporter角色，用于监控虚拟机上部署的mysql。

- 将foreman中的置备模板中初始化主机操作步骤（安装配置基础软件）转为php处理逻辑，即在%post后的过程中执行一条curl请求来完成操作。这样的好处是置备模板以后不会改，php中处理的逻辑会更自由。


## TODO-LIST 完成清单
- 创建docker角色。日期：2021/09/07，进度100%。

- 部署harbor服务器。日期：2021/09/07，进度100%。

## TODO-LIST 日期：2021/09/02
- 创建`scripts`目录，用于存放些自动化脚本。

- `000-base-000-common`角色中，repo类型增加katello逻辑处理，需要完成主机自动订阅。进度100%。

- katello中管理的yum源需要增加mysql-5.7/zabbix-5.0-lts。进度100%。

- 创建mysql角色，需要完成部署安装，初始化配置文件及root密码默认为空。进度100%。

- 创建zabbix角色，部署zabbix监控服务器。进度100%。


## 2020-01-05
- 将原k8s_learning_scripts仓库中的ansible_playbooks作为一个单独的仓库。