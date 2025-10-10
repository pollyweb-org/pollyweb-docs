# 🔃🚀🗃️ Uploaded @ Resourcer


<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <link-uuid>
    To: any-resourcer.com
    Subject: Uploaded@Resourcer
Body:
    Map: <map-uuid>
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | 
|           | `To`          | string    | [Resourcer 🗃️](<../../4 ⚙️ Solution/30 🫥 Agents/20 🗃️ Resourcers/01 🗃️ Index.md>) domain name
|           | `Subject`     | string    | `Uploaded@Resourcer`
| Body      | `Map`         | uuid    | ID from [`Map@Resourcer`](<20 🔃🚀🗃️ Map.md>)
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
- Missing file > /path/file-1.yaml
- Missing part 2 of 6 > /path/file-2.yaml
- Map already done.
```