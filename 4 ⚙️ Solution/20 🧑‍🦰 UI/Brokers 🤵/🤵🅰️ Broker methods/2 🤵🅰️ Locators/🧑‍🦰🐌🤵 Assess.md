# 🧑‍🦰🐌🤵 Assess @ Broker

* Part of [🤵⏩🧑‍🦰 Assess 🔆 flow](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Assess 🔆.md>):
    * precedes [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)

* Parses the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>).
    * If the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) is [`.ALIAS 🧩`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>) 
    * then it needs to be be resolved by a [Printer 🖨️ helper domain](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>)
    * into the final [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-id>
    To: any-broker.dom
    Subject: Assess@Broker
    
Body:
    Locator: .ALIAS,any-printer.dom,7V8KD3G
    Hook: <hook-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Assess@Broker`
|Body  |`Locator` |string| [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of types [`.HOST`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) [`.ALIAS`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
|| `Hook` | uuid | Hook for [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|


<br/>

## Logic

![alt text](<.📎 Assets/⚙️ Assess locator.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🚀🖨️ `Resolve@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Resolve.md>) | Get the underlying [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>) | Ask [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) to introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
||


<br/>

## Handler

```yaml
# Get the Wallet item
- GET|Wallets@Broker|$.Msg.From >> $wallet

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey

# Parse the locator
- PARSE|$.Msg.Body.Locator >> $locator

# Resolve any ALIAS locator
- IF|$locator.IsAlias:
    Then: 
        # Send the request to the Printer
        - SEND >> $resolved:
            To: $locator.Host
            Subject: Resolve@Printer
            Locator: $.Msg.Locator
        # Parse the locator again
        - PARSE|$resolved >> $locator

# Open a Chat on the Wallet app
- RUN|⏩ Converse
```

> Continues on [🤵⏩🧑‍🦰 Converse 💬](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>)

```yaml
# Ask Finders to introduce Hosts
- SEND:
    To: $wallet.Finder
    Subject: Introduce@Finder
    Chat: $chat.Chat
    Host: $chat.Chat
```

> Continues on [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>)


<br/>

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Wallet 🪣 item](<../../🤵🪣 Broker tables/🤵🪣 Wallets.md>)
|⤵️ [`IF`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/IF ⤵️.md>) |Verify if it is an [ALIAS 🧩 locator](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
| 📬 [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| 🔆 [`PARSE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/PARSE 🔆.md>) | Parse the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔐 [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
|