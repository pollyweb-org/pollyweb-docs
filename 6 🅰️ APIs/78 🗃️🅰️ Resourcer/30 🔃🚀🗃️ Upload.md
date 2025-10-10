# 🔃🚀🗃️ Upload @ Resourcer


<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <link-uuid>
    To: any-resourcer.com
    Subject: Upload@Resourcer
Body:
    Map: <map-uuid>
    File: /folder-C/folder-C1/file-C12.yaml
    Base46: False
    Parts: 1
    Part: 1
    Content: <content>
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | 
|           | `To`          | string    | [Resourcer 🗃️](<../../4 ⚙️ Solution/30 🫥 Agents/20 🗃️ Resourcers/01 🗃️ Index.md>) domain name
|           | `Subject`     | string    | `Upload@Resourcer`
| Body      | `Map`         | uuid    | ID from [`Map@Resourcer`](<20 🔃🚀🗃️ Map.md>)
|           | `File`        | string | Path like `/dir/file.ext`
|           | `Base64`      | bool   | Convert Base46 to binary
|           | `Parts`       | int    | Number of file parts
|           | `Part`        | int    | Current file part
|           | `Content`     | string | Content 
|

<br/>

## Synchronous Response

```yaml
# HTTP 200
```

```yaml
# HTTP 409
Errors:
- There's a more recent Map.
- File not in Map > /path/file-1.yaml
- Map already done.
```