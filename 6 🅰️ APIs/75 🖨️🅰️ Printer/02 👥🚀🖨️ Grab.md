# 👥🚀🖨️ Grab @ Printer

> A [Printer 🖨️ domain](<../../4 ⚙️ Solution/45 Helpers/10 Printers/08 🖨️🏭 Printer helper.md>) grabs an available alias. 

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.com
    To: any-printer.com
    Subject: Grab@Printer
Body: 
    Alias: ANY-ALIAS
    Locator: .HOST,any-host.com,ANY-RESOURCE,A=1,B=2
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../../4 ⚙️ Solution/45 Helpers/10 Printers/08 🖨️🏭 Printer helper.md>) name
|| `Subject`| string | `Grab@Printer`
|Body|`Alias`| string | Unique alias on the [Printer 🖨️](<../../4 ⚙️ Solution/45 Helpers/10 Printers/08 🖨️🏭 Printer helper.md>)
|       | `Locator`    | string | The [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) of a [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) 
|

## Synchronous Response

| HTTP | Details
|-|-
| 200   | Success.
| 409   | Alias already occupied: <br/> - use another alias.
| 405   | Locator not supported: <br/> - only [`.HOST 🧩`](<../../7 🧩 Codes/HOST/🧩 Host.md>) is supported.
|