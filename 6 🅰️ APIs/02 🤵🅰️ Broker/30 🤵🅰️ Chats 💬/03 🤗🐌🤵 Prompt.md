<!-- #TODO -->

<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)

## Workflows



## Message 🐌

|Property|Type|Description
|-|-|-
|`From`     | string | [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>)
|`To`       | string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|`ChatID`   | UUID | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
|`PromptID` | UUID

```yaml
Header:
  From: any-host.org
  To: any-broker.org
  Subject: Prompt@Broker
Body:
  ChatID: <chat-uuid>
  PromptID: <prompt-uuid>
```
