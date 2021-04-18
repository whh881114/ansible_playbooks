# prometheus监控外部k8s集群

## 参考资料
- https://www.qikqiak.com/post/monitor-external-k8s-on-prometheus/
- https://blog.csdn.net/yanggd1987/article/details/108807171
- https://help.aliyun.com/document_detail/123394.html


## 部署
- 创建用于Prometheus访问Kubernetes资源对象的RBAC对象，文件在`files/k8s-prometheus-rbac.yaml`。

- 获取token。
  - `kubectl get sa prometheus -n prometheus -o yaml`，获取对应的secret名字。
    ```
      secrets:
        - name: prometheus-token-4jbqs
      ```
  - `kubectl describe secret prometheus-token-4jbqs -n prometheus`，获取secret所对应的token。
      ```
      Name:         prometheus-token-4jbqs
      Namespace:    prometheus
      Labels:       <none>
      Annotations:  kubernetes.io/service-account.name: prometheus
                    kubernetes.io/service-account.uid: 712d4d8c-8a72-440c-9a4e-c0b5d8a67ab3
      
      Type:  kubernetes.io/service-account-token
      
      Data
      ====
      namespace:  10 bytes
      token:      eyJhbGciOiJSUzI1NiIsImtpZCI6ImtKd0xpRm11V3ZJQVBWalhCd053WnM4Rzh3dU5mMGliWi16eFdtRmJ0TjgifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJwcm9tZXRoZXVzIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InByb21ldGhldXMtdG9rZW4tNGpicXMiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicHJvbWV0aGV1cyIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjcxMmQ0ZDhjLThhNzItNDQwYy05YTRlLWMwYjVkOGE2N2FiMyIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpwcm9tZXRoZXVzOnByb21ldGhldXMifQ.liwhBiZzaOHKo1_a4Ojh_6UfqVKtVGXpLRdkCAuEZUisz-OBradetS_SOVQpf2Zim5exyRMSZuuFbHvJtjfUOvjlS0o-B7PHYISob_MS4aClMJg1AM7IsjUyWxw3e8YxnOBaaMDJNg-SLw4FJpcrWXsr5k_Peb_P4qqj_14YgSs8Hx4Cstu3XBknrw9buN5Vwlwxr-2wgs7tsGiJ87bHk_gCu7EGyN2c-y0dfKaZcy2Z5ip2UoIInB5oea2lNREVjFKATcduagUAbw7fSBuaEYxECyeoLgsNfDTOfPIAyeABkz7LMjm3YW9NtfSIA7bOxNz0gMdp-aXxH-EBUt51og
      ca.crt:     526 bytes
      ```

- 配置prometheus配置文件，具体查看`defaults/main.yml`中的`prometheus_scrape_configs`变量配置。

## 待解决
- `server returned HTTP status 403 Forbidden`