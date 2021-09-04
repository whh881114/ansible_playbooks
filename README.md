# ansible_playbooks 更新日志

## TODO-LIST 日期：2021/09/02
- 创建`scripts`目录，用于存放些自动化脚本。

- `000-base-000-common`角色中，repo类型增加katello逻辑处理，需要完成主机自动订阅。进度100%。

- 将foreman中的置备模板中初始化主机操作步骤（安装配置基础软件）转为php处理逻辑，即在%post后的过程中执行一条curl请求来完成操作。这样的好处是置备模板以后不会改，php中处理的逻辑会更自由。

- katello中管理的yum源需要增加mysql-5.7/zabbix-5.0-lts。

- 创建mysql角色，需要完成部署安装，初始化配置文件及root密码。

- 创建mysql_exporter角色，用于监控虚拟机上部署的mysql。


## 2020-01-05
- 将原k8s_learning_scripts仓库中的ansible_playbooks作为一个单独的仓库。