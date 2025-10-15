<!-- https://quip.com/U97qAoGmSPAn#temp:C:HKUfb3022130c644b3faa5b9cce8 -->

# 👥🚀🖨️ Resolve @ Printer

> A [Printer 🖨️ domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/60 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>) returns the [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) of an alias, if any.

> Used in [🧑‍🦰👉🤗 Scan printer QR](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>).

> No locator means that it’s free for grabs.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.com
    To: any-printer.com
    Subject: Resolve@Printer

Body: 
    Alias: ANY-ALIAS
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/60 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>) name
|| `Subject`| string | `Resolve@Printer`
|Body|`Alias`| string | Unique [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) ID on the [Printer 🖨️ ](<../../4 ⚙️ Solution/45 🛠️ Helper domains/60 🖨️ Printers/$ 🖨️🛠️ Printer helper.md>)
|


<br/>

## Synchronous Response

```yaml
Locator: .HOST,any-host.com,any-key
```

Property|Type|Description
|-|-|-
| Locator | string | [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) 
|