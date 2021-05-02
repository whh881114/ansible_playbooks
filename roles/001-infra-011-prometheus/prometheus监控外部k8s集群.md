# prometheus监控外部k8s集群

## 参考资料
- https://www.qikqiak.com/post/monitor-external-k8s-on-prometheus/
- https://blog.csdn.net/yanggd1987/article/details/108807171
- https://help.aliyun.com/document_detail/123394.html


## 部署
- 创建用于Prometheus访问Kubernetes资源对象的RBAC对象，文件在`files/k8s-prometheus-rbac.yaml`。

- 获取token。
  - `kubectl get sa prometheus -n default -o yaml`，获取对应的secret名字。
    ```
      secrets:
        - name: prometheus-token-4jbqs
      ```
  - `kubectl get secret prometheus-token-4jbqs -n default`，获取secret所对应的token。
      ```
        apiVersion: v1
        data:
          ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM1ekNDQWMrZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EVXdNakUwTXpFeU0xb1hEVE14TURRek1ERTBNekV5TTFvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTmdtCjdlK1NoanM5Zk5iOXhGN1lpc2NpV3p2OFB5bWdPU0NuQU03cHFEbjVCSEVjYWZSSGVxSEMwVnprTGsxTmZSNUIKaGNNQ0YvSGV4cGxIbXh6eGg2UzRZYlVabWtreFE2cDZxU3I3UHVsaHhXRkdsQnhUYS81RmtLcU1pZ2lpeUlubwprV2ZJUG8rdlI2ODRJd1dHYllobDFPNGh1NC9kNkV5NnQ4ak9JdEQ0TlVNVmpMclhHRExJVUg5TmlmVWVvRUVjCmNXNGw5ZUxEYmZqME9CaVRLZG1EYnlmMURERWJjR0pMSmdKWWhRV2V4ZmFvNGU1T1l6Tm9IVVZJSjJnRkh2WWoKNDRsSGZLN1RSSWhGbVJ5TXdoZi93V3dZN3dWS0t1bzVkZWc5VUYrRWIrREZNbkZyQm1LRWlyWVVCL2FnWlJJNwoyWWZUbEpTeWJDOTJ1enI0L0RzQ0F3RUFBYU5DTUVBd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZCVnp3V3g5cW12dGw5d3lhbFdXU1hYTVAva3BNQTBHQ1NxR1NJYjMKRFFFQkN3VUFBNElCQVFBcWlNTGlKaDZDeTRuRm9JRHFHVEhxWXdoTzhwVFVmZ2FZSGdod2xaTHBPVnBmUWloNApjZzVyM0Q3M04ra1ZQUmltcDBUUFhpTUJGQlFucWJvbnZ6b3BBVkRWanNpRmgrM2h3UVR2Z2NraWg0UUpTT2U1CnFkY3hhYy9VRHZKY2dQby9xMjBtaExtNzA5aE1vV2Y1MExBbjNzRGwzM3VjWGdCNE5EMkk3SXBRdnE4OFRxeEsKbm5xaEFYbGExbWlYM3NMaGkvYXg0Mi9ucjY3Z3NjWTlqdkVnNEFIZC8zYXp5MFNpNWI1UTEzZ2NpaDNXYWxoaApaaXlFUzE5dllwWkRZTG5UcVY5QmJHNElqZUxGLzlnRjNtQ2RpSlhROElKNEJ1U0FabXVvRVp4anVsMmJVcndKCnZRZ1A5TnA0eEdLcVFIUUdsVE14SUJEOXduWUhDWlM4eGhoRgotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
          namespace: ZGVmYXVsdA==
          token: ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkltd3hlV3hNYzA5RWVVRlRhbmROWWtWNGNqVm5OV2RmVG5Od09VeE1NbGs0Um1kRWJ6QnZaa3B5VFhjaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUprWldaaGRXeDBJaXdpYTNWaVpYSnVaWFJsY3k1cGJ5OXpaWEoyYVdObFlXTmpiM1Z1ZEM5elpXTnlaWFF1Ym1GdFpTSTZJbkJ5YjIxbGRHaGxkWE10ZEc5clpXNHRZbTF3WjNZaUxDSnJkV0psY201bGRHVnpMbWx2TDNObGNuWnBZMlZoWTJOdmRXNTBMM05sY25acFkyVXRZV05qYjNWdWRDNXVZVzFsSWpvaWNISnZiV1YwYUdWMWN5SXNJbXQxWW1WeWJtVjBaWE11YVc4dmMyVnlkbWxqWldGalkyOTFiblF2YzJWeWRtbGpaUzFoWTJOdmRXNTBMblZwWkNJNkltUXhabUZoTlRRd0xUVm1PREF0TkRGaVpTMDVZV0ptTFRBNFpqWm1NMk5tTURJeE5TSXNJbk4xWWlJNkluTjVjM1JsYlRwelpYSjJhV05sWVdOamIzVnVkRHBrWldaaGRXeDBPbkJ5YjIxbGRHaGxkWE1pZlEuSWxxWWUyTENhaVdodGxSOFdqRkVqaGZnbWxsLXJhR19BUlFSRF9EMjRXNV9FbHduVDF2S3ZfdjZqbk5GY1IybFF0TFJDLU1VNHdmazc4YzNBMFF3c0RiTkViV2ZBck5GQkxwN0pkTEhUVFRRM2VITjJBamo2U3VFUUprckV6eE95RkdvM0k2cG9Pa2NGbEN3SVA2azlnSW1lemV4Nmo3VHFCOWhoRHRJVlI5VWlrajVpdFNkZmpIQ09QRWxVS3VGay1IenJvanhxX29hTm9EaU9ISDJZN19DYnpQSG5NQV9RNDN6X2tqSW5wN3BwVGp6ZXBzeC1fXzBtV20xUVN0cmozRFlOLW5xTklObk9BMmNxZWxNcVVrWkxqbXVlSUItaXNPeExUeVJlTU93NjhDNWZYeFhDWE9La0lrcmd5cXBZakdPTnpvYmNMODNCblZ6OEF4YVRn
        kind: Secret
        metadata:
          annotations:
            kubernetes.io/service-account.name: prometheus
            kubernetes.io/service-account.uid: d1faa540-5f80-41be-9abf-08f6f3cf0215
          creationTimestamp: "2021-05-02T15:27:44Z"
          managedFields:
          - apiVersion: v1
            fieldsType: FieldsV1
            fieldsV1:
              f:data:
                .: {}
                f:ca.crt: {}
                f:namespace: {}
                f:token: {}
              f:metadata:
                f:annotations:
                  .: {}
                  f:kubernetes.io/service-account.name: {}
                  f:kubernetes.io/service-account.uid: {}
              f:type: {}
            manager: kube-controller-manager
            operation: Update
            time: "2021-05-02T15:27:44Z"
          name: prometheus-token-bmpgv
          namespace: default
          resourceVersion: "18054"
          selfLink: /api/v1/namespaces/default/secrets/prometheus-token-bmpgv
          uid: 622841ae-123d-43ca-bf5b-6c513ff340e4
        type: kubernetes.io/service-account-token
      ```
  - `echo "xxxxxxxx" | base64 -d`，解密token。


- 配置prometheus配置文件，具体查看`defaults/main.yml`中的`prometheus_scrape_configs`变量配置。