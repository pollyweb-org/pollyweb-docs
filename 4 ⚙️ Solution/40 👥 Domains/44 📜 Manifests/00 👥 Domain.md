👥 Domain FAQ
===

1. **What is a domain in NLWeb?**

    In NLWeb, a domain is any web service that exposes an HTTPS API compatible with the NLWeb communication protocol for a specific DNS domain name (e.g., `any-domain.com`) is an NLWeb domain if it has an NLWeb compatible API at `https://nlweb.any-domain.com`).

    ---


1. **What are the key components of a domain?**

    Its key components are:
    - a registered DNS name (e.g., `any-domain.com`)
    - an NLWeb [DNS 🌐](<../../../5 ⏩ Flows/01 👥⏩ Domains/01 👥⏩🌐 Config DNS.md>) subname with DNSSEC (e.g., `nlweb.any-domain.com`)
    - a [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) Outbox public key (e.g., `pk1._domainkey.any-domain.com`)
    - an NLWeb inbox API with SSL (e.g., `https://nlweb.any-domain.com`)

    ---

