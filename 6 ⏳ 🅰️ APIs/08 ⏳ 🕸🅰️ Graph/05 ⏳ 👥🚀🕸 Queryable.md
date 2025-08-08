<!-- https://quip.com/hgz4A3clvOes#temp:C:bDA44399e7e0bfc4609a560d6c4a -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/a60df25a0f652b24793d9d0a3099aaa19bbcdd61/python/backbone/graph/GRAPH.py#L130 -->

# 👥🚀🕸 Queryable @ [Graph](<../../4 ⏳ ⚙️ Solution/40 ✅ 👥 Domains/44 ✅ 📜 Manifests/03 ✅ 🕸👥 Graph helper.md>)


## Called by

| Caller | Notes
|-|-
||



## Sample request
```json
...
"Body": {
    "Host": "any-host.org",
    "Binds": [{
        "Vault": "ec.europa.eu",
        "Code": "airlines.any-igo.org/SSR/WCHR/CRED"
    }]
}
```


## Sample response
```json
{
    "Binds": [{
        "Vault": "ec.europa.eu",
        "Code": "airlines.any-igo.org/SSR/WCHR/CRED",
        "Paths": [["<vault>", "<consumer>"]]
    }]
}
```