<!-- Docs: -->
<!-- Source: -->
<!-- Test: -->


# 🔎🚀⭐ Reviews @ [Reviewer](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>)

> Implementation
* Implements the [Reviewer ⭐ agent](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>)

> Flow
* Part of the [`Present` ⏩ flow](<../../Finders 🔎/🔎⏩ Finder flows/Present 🔎⏩🧑‍🦰/🔎 Present ⏩ flow.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-finder.dom
    To: any-reviewer.dom
    Subject: Reviews@Reviewer

Body:
    Domain: any-domain.dom
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header |`From`|string| [Finder 🔎](<../../Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Present@Finder`](<../../Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|        |`To`|string| [Reviewer ⭐](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | [`Present@Finder`](<../../Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|        | `Subject` | string | `Reviews@Reviewer`
| Body   | `Domain`  | domain | [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Present@Finder`](<../../Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|

<br/>

# Synchronous response

```yaml
Rating: 4.6
Description: |
    User feedback:
    - 4.7⭐ delivery by 357 users
    - 3.5⭐ support by 21 users
Options:
    - /List reviews § .HOST,any-reviewer.dom,domain
```