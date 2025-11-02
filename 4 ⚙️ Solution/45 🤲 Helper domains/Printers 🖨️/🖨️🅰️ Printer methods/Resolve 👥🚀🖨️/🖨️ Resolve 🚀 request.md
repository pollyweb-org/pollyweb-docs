<!-- https://quip.com/U97qAoGmSPAn#temp:C:HKUfb3022130c644b3faa5b9cce8 -->

# 👥🚀🖨️ Resolve @ Printer

> Purpose
* A [Printer 🖨️ domain](<../../🖨️🤲 Printer helper.md>) returns the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of an alias, if any.
* No locator means that it’s free for grabs.

> Used in 
* [🧑‍🦰👉🤗 Scan printer QR](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🧑‍🦰 Tap alias locator ⏩ flow.md>).

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-printer.dom
    Subject: Resolve@Printer

Body: 
    Alias: ANY-ALIAS
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|domain| Caller [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) name
||`To`|domain| [Printer 🖨️ domain](<../../🖨️🤲 Printer helper.md>) name
|| `Subject`| string | `Resolve@Printer`
|Body|`Alias`| string | Unique [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) ID on the [Printer 🖨️ ](<../../🖨️🤲 Printer helper.md>)
|


<br/>

## Synchronous Response

```yaml
Locator: .HOST,any-host.dom,any-key
```

Property|Type|Description
|-|-|-
| Locator | string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
|

<br/>

## Handler


```yaml
# Verify the signature.
- VERIFY|$.Msg

# Get from the table.
- GET >> $alias:
    Set: PrinterAliases
    Key: $.Msg.Alias

# Respond with the Locator.
- REEL:
    Locator: $alias.Locator
```