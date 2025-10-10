# 🔃🚀🗃️ Upload @ Resourcer


<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <clone-uuid>
    To: any-resourcer.com
    Subject: Upload@Resourcer
Body:
    Map: <map-uuid>
    File: /folder-C/folder-C1/file-C12.yaml
    Parts: 1
    Part: 1
    Base46: False
    Content: <content>
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<10 🔃🚀🗃️ Clone.md>) response
|           | `To`          | string    | [Resourcer 🗃️ domain](<../../9 😃 Talkers/90 ☁️ Hosters/02 🗃️🎭 Resourcer role.md>) name
|           | `Subject`     | string    | `Upload@Resourcer`
| Body      | `Map`         | uuid    | ID from [`Map@Resourcer`](<20 🔃🚀🗃️ Map.md>)
|           | `File`        | string | Path like `/dir/file.ext`
|           | `Parts`       | int    | Number of file parts
|           | `Part`        | int    | Current file part
|           | `Base64`      | bool   | Convert Base46 to binary
|           | `Content`     | string | Content in text
|

<br/>

## Synchronous Response

```yaml
# HTTP 200
```

|| Property | Type | Description
|-|-|-|-
|| -        | -      | Empty response on success

```yaml
# HTTP 409
Errors:
- There's a more recent Map.
- File not in Map > /path/file-1.yaml
- Map already done.
```

|| Property | Type | Description
|-|-|-|-
|| None        | None      | Empty response on success
|| `Errors`    | string[]  | List of errors on failure
|