# 👥⏩ DNS configuration

> Part of [Domain 👥](<../👥 Domain.md>)

<br/>

1. **What does a domain DNS look like?**
    
    Consider the following sample DNS configuration for the domain name [`any-domain.dom`]().
    
    
    | Record Name | Type | Value 
    |-|-|-|
    | 👉 Name servers from the DNS register
    | [`any-domain.dom`]() | `NS` | `{name servers}`
    | 👉 Endpoint for inbound [messages 📨](<../../../30 🧩 Data/📨 Messages/📨 Message.md>)  
    | `nlweb`.[`any-domain.dom`]() | `A` | `1234.any-api.com`
    | 👉 [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) for outbound and [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
    | `pk6`.`_domainkey`.[`any-domain.dom`]() | `TXT` | `v=DKIM1;k=rsa;p=...` 
    | 👉 Old [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) for old [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
    | `pk5`.`_domainkey`.[`any-domain.dom`]() | `TXT` | `v=DKIM1;k=rsa;p=...` 

    

    ---
    <br/>