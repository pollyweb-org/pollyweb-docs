# 👥🚀🖨️ Grab @ Printer

> A [Printer 🖨️ domain](<../../🖨️🤲 Printer helper.md>) grabs an available alias. 

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-printer.dom
    Subject: Grab@Printer

Body: 
    Alias: ANY-ALIAS
    Locator: .HOST,any-host.dom,any-key
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string| Caller [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
||`To`|string| [Printer 🖨️ domain](<../../🖨️🤲 Printer helper.md>) name
|| `Subject`| string | `Grab@Printer`
|Body|`Alias`| string | Unique alias on the [Printer 🖨️](<../../🖨️🤲 Printer helper.md>)
|| `Locator` | string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
|

<br/>

## Synchronous Response

```yaml
Status: OK
```

| Property  | Value | Description
|-|-|-
| `Status`  | `OK` | Grabbed successfully
|| `UNHOST` | Locator not supported - not [`.HOST` 🧩](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
|| `BLOCKED` | Alias already occupied - use another
|

<br/>
