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
|           | `To`          | string    | [Resourcer 🗃️](<../../4 ⚙️ Solution/30 🫥 Agents/20 🗃️ Resourcers/01 🗃️ Index.md>) domain name
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
|| `Map`         | uuid      | ID for [`Push@`](<30 🔃🚀🗃️ Push.md>) and [`Pushed@`](<50 🔃🚀🗃️ Pushed.md>)
|