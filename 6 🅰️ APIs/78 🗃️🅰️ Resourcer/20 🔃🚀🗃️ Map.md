# 🔃🚀🗃️ Map @ Resourcer



<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <link-uuid>
    To: any-resourcer.com
    Subject: Map@Resourcer
Body:
    Files: 
        - /file-1.yaml
        - /folder-A/file-A1.yaml
        - /folder-B/file-B1.yaml
        - /folder-B/file-B2.yaml
        - /folder-C/folder-C1/file-C11.yaml
        - /folder-C/folder-C1/file-C12.yaml
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid |
|           | `To`          | string    | [Resourcer 🗃️ domain](<../../9 😃 Talkers/90 ☁️ Hosters/02 🗃️🎭 Resourcer role.md>) name
|           | `Subject`     | string    | `Map@Resourcer`
| Body      | `Files`       | string[] | List of file paths
|

<br/>

## Synchronous Response

```yaml
# HTTP 200
Map: <map-uuid>
```


|| Property | Type | Description
|-|-|-|-
|| `Map`         | uuid      | ID for [`Upload@`](<30 🔃🚀🗃️ Upload.md>) and [`Uploaded@`](<50 🔃🚀🗃️ Uploaded.md>)
|