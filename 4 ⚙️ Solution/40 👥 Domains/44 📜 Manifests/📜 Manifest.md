📜 Domain Manifests
===


1. **How do domains publicize their identity?**

    In NLWeb, [domains 👥](<../$ 👥 Domains/👥 Domain.md>) publish their metadata in the form a [domain Manifest 📜](<📜 Manifest.md>).

    ---
    <br/>


1. **How can a domain inspect another domain's Manifest?**

    [Domains 👥](<../$ 👥 Domains/👥 Domain.md>) leverage Manifest 📜 caches, called [Graph 🕸 domains](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>), that keep up-to-date representations of NLWeb [domain Manifests 📜](<📜 Manifest.md>).
    * Manifest queries to these [Graphs 🕸](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>) are synchronous and expected to have millisecond latency.
    * This is similar to what DNS records do for Web 2.0, but with a more complex data schema. 

    ---
    <br/>


1. **How does it work?**

    ![](<.📎 Assets/📜 Manifest.png>)

    Each [domain 👥](<../$ 👥 Domains/👥 Domain.md>) sends the content of their [domain Manifests 📜](<📜 Manifest.md>) in parts or in full to a [Listener 👂 helper domain](<../../45 🤲 Helper domains/60 👂 Listeners/👂🤲 Listener helper.md>), who then propagates it to [Graph 🕸 domains](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>).

    |Step|Description
    |-|-
    |A| When a [domain 👥](<../$ 👥 Domains/👥 Domain.md>) sends a request to another
    |B| the recipient queries a [Graph 🕸 helper domain](<../../45 🤲 Helper domains/50 🕸 Graphs/🕸🤲 Graph helper.md>) for information about the sender to assess its [trustworthiness 👍](<../43 👍 Trusts/👍 Domain Trust.md>)
    |C| and only then responds successfully.
    

    ---
    <br/>

1. **What information can be added to a Manifest?**

    Manifests are defined by [`.MANIFEST` 🧩](<🧩 Manifest schemas/🧩 MANIFEST.md>) and can include the following sections.

    |Section|Purpose | Schemas
    |-|-|-
    | 🤗 [Host About](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | Domain identification (mandatory). | [`./ABOUT` 🧩](<🧩 Manifest schemas/🧩 ABOUT.md>) 
    | 👍 [Domain Trusts](<../43 👍 Trusts/👍 Domain Trust.md>) | Trusted domains, Codes, and roles. | [`./TRUST` 🧩](<🧩 Manifest schemas/🧩 TRUST.md>)
    |  🧩 [Schema Codes](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) | Defined by the domain. | [`./CODE` 🧩](<🧩 Manifest schemas/🧩 CODE.md>)  | Schema validation of a Code
    |  🧩 [Delegated Codes](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) | Codes delegated to other domains. | [`./DELEGATE` 🧩](<🧩 Manifest schemas/🧩 DELEGATE.md>)
    | 🪢 [Integrations](<../../41 🎭 Domain Roles/35 🪢 Integrators/$ 🪢🎭 Integrator role.md>) |Synchronous datasets, <br/>asynchronous supplies, <br/>and streaming endpoints. | [`./OFFER` 🧩](<🧩 Manifest schemas/🧩 OFFER.md>)
    | [Chat 💬 Flows](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) | To explain what user data is request.

    ---
    <br/>

1. **What are examples of manifests?**

    | Category | Example 📜 
    |-|-
    | `💼 Businesses` | [🏳️🧋 Any Coffee Shop](<../../../8 📜 Manifests/🌐 Businesses/📜 cafe.any-business.com.md>)
    || [🏳️🅿️ Any Parking](<../../../8 📜 Manifests/🌐 Businesses/📜 carpark.any-business.org.md>)
    || [🏳️🎰 Any Casino](<../../../8 📜 Manifests/🌐 Businesses/📜 casino.any-business.org.md>)
    || [🇸🇬💈 Any Hairdresser, Singapore](<../../../8 📜 Manifests/🌐 Businesses/📜 hairdresser.any-business.org.md>)
    |`💳 Payments`| [🏳️🪙 Any Bank](<../../../8 📜 Manifests/🌐 Payments/📜 any-bank.org.md>)
    || [🏳️🏦 Any Collector](<../../../8 📜 Manifests/🌐 Payments/📜 any-collector.org.md>)
    || [🏳️💰 Any Exchange](<../../../8 📜 Manifests/🌐 Payments/📜 any-exchange.org.md>)
    || [🏳️💳 Any Payer](<../../../8 📜 Manifests/🌐 Payments/📜 any-payer.org.md>)
    || [🏳️🏧 Any Cash Machine](<../../../8 📜 Manifests/🌐 Payments/📜 atm.any-fintech.org.md>)
    |`✈️ Airlines` | [🏳️🛫 Any Airport](<../../../8 📜 Manifests/👥 any-nation.org/📜 airport.any-nation.org.md>)
    | | [🏳️💺 Any Airline](<../../../8 📜 Manifests/🌐 Businesses/📜 airline.any-business.org.md>)
    || [🌐💺 Any IGO Airlines](<../../../8 📜 Manifests/👥 any-igo.org/📜 airlines.any-igo.org.md>)
    || [🌐✈️ All Aviation Members](<../../../8 📜 Manifests/👥 any-igo.org/📜 aviation.any-igo.org.md>)
    | `🫱🏼‍🫲🏽 Non Profits` | [🌐 Emojis](<../../../8 📜 Manifests/👥 any-igo.org/📜 emojis.any-igo.org.md>)   
    || [🌐 Unicode Common Locale Data Repository (CLDR)](<../../../8 📜 Manifests/👥 any-igo.org/📜 locale.any-igo.org.md>)
    || [🌐 ISO, International Organization for Standardization](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>)
    || [🌐☎️ ITU - International Telecommunication Union](<../../../8 📜 Manifests/👥 any-igo.org/📜 telcos.any-igo.org.md>)
    || [🌐 Unicode](<../../../8 📜 Manifests/👥 any-igo.org/📜 unicode.any-igo.org.md>)
    | `🌐 Inter-gov Orgs`| [🌐🏥 World Health Organization](<../../../8 📜 Manifests/👥 any-igo.org/📜 health.any-igo.org.md>)
    || [🌐 Nation Members of Any IGO](<../../../8 📜 Manifests/👥 any-igo.org/📜 nations.any-igo.org.md>)
    | `🏳️ Any Nation`| [🏳️🏛️ Any Nation's Government](<../../../8 📜 Manifests/👥 any-nation.org/📜 any-nation.org.md>)
    || [🏳️🆔 Any Nation's Biometric Center](<../../../8 📜 Manifests/👥 any-nation.org/📜 biometrics.any-nation.org.md>)
    || [🏳️🏥 Any Nation's Health Services](<../../../8 📜 Manifests/👥 any-nation.org/📜 health.any-nation.org.md>)
    || [🏳️🏦 Any Nation's Tax Services](<../../../8 📜 Manifests/👥 any-nation.org/📜 taxes.any-nation.org.md>)
    |`🇺🇸 United States`| [🇺🇸 U.S. Government](<../../../8 📜 Manifests/👥 usa.gov/📜 usa.gov.md>)
    || [🇺🇸🏥 U.S. Department of Health & Human Services](<../../../8 📜 Manifests/🌐 Vaults/📜 hhs.gov.md>)
    || [🇺🇸🆔 U.S. Department of State](<../../../8 📜 Manifests/🌐 Vaults/📜 state.gov.md>)
    || [🇺🇸🏦 Federal Reserve of the United States](<../../../8 📜 Manifests/👥 usa.gov/📜 federalreserve.gov.md>)
    |`🇪🇺 European Union`| [🇪🇺 European Union](<../../../8 📜 Manifests/👥 europa.eu/📜 europa.eu/📜 europa.eu.md>)
    || [🇪🇺 European Commission](<../../../8 📜 Manifests/👥 europa.eu/📜 europa.eu/📜 ec.europa.eu.md>)
    || [🇪🇺🏦 European Central Bank](<../../../8 📜 Manifests/👥 europa.eu/📜 europa.eu/📜 ecb.europa.eu.md>)
    | `🌍 Other Nations`| [🇲🇹 Government of Malta](<../../../8 📜 Manifests/👥 Authorities/📜 gov.mt.md>)
    || [🇮🇹 Italian Government](<../../../8 📜 Manifests/👥 Authorities/📜 governo.it.md>) 
    | `🤲 Helper domains` | [🔥 Any Firewall](<../../../8 📜 Manifests/🌐 Backbone/📜 any-firewall.org.md>)
    || [🕸️ Any Graph](<../../../8 📜 Manifests/🌐 Backbone/📜 any-graph.org.md>)
    || [🕸️🇪🇺 Graph of European Union](<../../../8 📜 Manifests/🌐 Backbone/📜 graph.amazon.com.md>)
    || [🕸️☁️ Amazon Graph](<../../../8 📜 Manifests/🌐 Backbone/📜 graph.amazon.com.md>)
    || [👂 Any Listener](<../../../8 📜 Manifests/🌐 Backbone/📜 any-listener.org.md>)
    || [👂☁️ Amazon Listener](<../../../8 📜 Manifests/🌐 Backbone/📜 listener.amazon.com.md>)
    |`👱 Wallet domains`|  [🤵 Any Broker](<../../../8 📜 Manifests/🌐 Brokers/📜 any-broker.org.md>)
    || [📣 Any Wallet Notifier](<../../../8 📜 Manifests/🌐 Brokers/📜 any-notifier.org.md>)

    ---
    <br/>