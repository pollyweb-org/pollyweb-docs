# 🧑‍💻🛠️ Hoster helper FAQ

1. **What is a Hoster?**

    A [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) is 
    * any [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)
    * that host the infrastructure of other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
    * and allow their owners to manage them with a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>

1. **What roles do Hosters typically implement?**

    | [Role 🎭](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | Purpose
    |-|-
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | To have [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) with users.
    | [🗄️ Vault](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | To store the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) settings.
    | [🎴 Issuer](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | To issue [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) ownership [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).
    | [🪢 Integrator](<../12 💬 Chats/06 🪢🎭 Integrator role.md>) | To manifest the hosting service to  [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | To sell the usage plans via a [Biller 💳 helper domain](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>).
    

    ---
    <br/>

2. **What domain Helpers do Hosters typically leverage?**

    | [Helper 🛠️](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)  | Purpose 
    |-|-
    | [💳 Biller](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | To manage usage and subscription plans.
    | [🏦 Collector](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | To collect usage and subscription payments.
    
    ---
    <br/>

3. **What is required from domain owners?**

    | Requirement | Purpose
    |-|-
    | [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | To authenticate and [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with the [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>).
    | [Payer 💳 agent](<../../30 🫥 Agents/04 💳 Payers/04 💳🫥 Payer agent.md>) | To pay for usage and subscription plans.
    | [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | To authenticate the domain user.
    | [Folder 🗂️ editor](<../../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>) | To manage the settings of the hosted [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    ---
    <br/>

4. **How can a domain admin user leverage a [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>)?**

    |#| Category | Step
    |-|-|-
    |1| `Find` | Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), <br/>the admin user [finds 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) a [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>) <br/>and starts a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with the [Hoster's Host 🤗 role](<../12 💬 Chats/04 🤗🎭 Host role.md>).
    |2| `Bind`| On the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>), <br/>the user [Binds 🔗](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) to the [Hoster's Vault 🗄️ role](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), <br/>and creates a new [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).
    |3| `Clone`| On a workstation terminal, <br/>the user [scans ✨](<../11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the terminal QR code <br/>to link the terminal to the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>and download the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) settings.
    |4| `Edit`| On a code editor (e.g., Visual Studio Code)<br/>the user configures the logic webhooks <br/>and the public [domain 📜 Manifest](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).
    |5| `Sync`| On the workstation terminal, <br/>the user synchronizes the changes <br/>with the [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>).
    |6| `Test`| From the workstation terminal, <br/>the user opens [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) for manual testing.

    ---
    <br/>


5. **What does the Wallet Chat looks like?**

    | Service | Prompt  | User 
    | - | - | - 
    | [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) | 😃 Hi! What do you need? <br/>- [ Create ] a domain <br/>- [ Something else ] | > Create
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No]<br/>- domain admin 🧩 | > Yes 
    | [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) | 😃 Name for the domain? | `my-domain`
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save token? [Yes, No] <br/>- domain owner 🎫 <br/>- of my-domain
    | [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) | ✅ Done!
    
    ---
    <br/>

6. **What commands are supported on the terminal CLI?**

    The terminal Command Line Interface (CLI) supports the following commands.

    |🧑‍💻 Command | Description
    |-|-
    |`clone <name>` | Generates a [QR Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>)<br> for the user to scan with the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>to clone the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to a local folder<br/>- e.g., `my-hoster clone my-domain`
    |`sync` | Sends the changes with the [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>) <br/>- e.g., `my-hoster sync`
    |`chat <env>`| Opens a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with an environment<br/>on the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>- e.g., `my-hoster chat local`
    <!--|`test <env>`| Runs test scripts on an environment<br/>- e.g., `my-hoster test local`-->

    ---
    <br/>

7. **What does a terminal CLI interaction looks like?**

    |🧑‍💻 Command | 🖥️ Display |  Workstation
    |-|-|-
    |`$ clone my-domain` | ⏳ Scan the QR code... | [✨ scan](<../11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    || ✅ Domain cloned to folder
    |`code .` | &lt;opens visual studio code&gt;| 🧑‍💻 implement
    |`$ sync` | ✅ Changes synchronized.
    |`$ chat dev` | ⏳ Chat on your Wallet... | [💬 chat](<../12 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    |`$ chat prod` | ⏳ Chat on your Wallet... | [💬 chat](<../12 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    <!--|`$ test dev` | ✅ Tested successfully. | 🥳 celebrate-->
    
    

    ---
    <br/>



5. **What happens when the Wallet scans the QR?**

    | Service | Prompt  | User 
    | - | - | - 
    | [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) | ℹ️ Cloning request:<br/>- domain: my-domain<br/>- from: London, UK
    | [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) | 😃 Authorize? [Yes, No]<br/>- [ I don't recognize it ] | > Yes
    | [🧑‍💻 Hoster](<05 🧑‍💻🛠️ Hoster helper.md>) | ✅ Authorized!
    
    ---
    <br/>

6. **What domain files are cloned locally?**

    | File | Format | Purpose
    |-|-|-
    | 📥 Inbound | YAML | Message inbound configuration.
    | 📤 Outbound | YAML | Message outbound configuration.
    | [🛠️ Helpers](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)  | YAML | Required [Helper 🛠️ domains](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>).
    | [📜 Manifest](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) | YAML | Public information about the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).
    | 🔆 [Locators](<../11 🔆 Locators/01 🔆 Locator.md>) | YAML | Mapping of [Locators 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) to [Talkers 😃](<../33 😃 Talkers/01 😃 Talker.md>)
    | 😃 [Talkers](<../33 😃 Talkers/01 😃 Talker.md>) | Folder | Tree of [💬 Chat](<../12 💬 Chats/01 💬 Chat.md>) scripts by [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>)


    ---
    <br/>

7. **What does the Inbound file look like?**

    The `📥 Inbound.yaml` file tells the [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>) which [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to forward, and where to.
    
    * For [💬 Chats](<../12 💬 Chats/01 💬 Chat.md>) started from the workstation's terminal, the CLI will open a proxy connection to receive the messages from the [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>) and forward them to the target until the [💬 Chat](<../12 💬 Chats/01 💬 Chat.md>) ends, allowing a local web-server at http://localhost to be running as a target.
  
    * [💬 Chats](<../12 💬 Chats/01 💬 Chat.md>) starting with any other way will communicate only via the Internet, and will require the target to expose the WebHook endpoint as HTTPS.

    ```yaml
    🤝: nlweb.org/HOSTER/INBOUND

    Roles: # what messages to forward to the WebHook.
        - Host
        - Vault
        - Issuer
        - Seller
    
    Hook: # where to forward messages to.

        Targets: # test environments.
            dev: http://localhost:7070
            prod: https://my-domain.com/nlweb/prod/inbox
    
        Default: prod # handle live requests.
    ```

    ---
    <br/>

1. **What does the Outbound file look like?**

    The `📤 Outbound.yaml` is generated by the [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>) to tell the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) where to proxy messages to.

    * The [Hoster 🧑‍💻 domain](<05 🧑‍💻🛠️ Hoster helper.md>) proxy receives unsigned [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) from the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>), signs them with the [DKIM 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) private key, and forwards them downstream without ever disclosing the private key.


    ```yaml
    🤝: nlweb.org/HOSTER/OUTBOUND

    Proxy: https://{uuid}.proxies.any-hoster.com
    ```

    ---
    <br/>


2. **What does the Helpers file look like?**

    ```yaml
    🤝: nlweb.org/HOSTER/HELPERS

    Listeners: # to send Manifest 📜 updates.
        - listeners.nlweb.org
        - any-listener.org

    Graphs: # to verify Trust 👍 chains.
        - any-graph.org
    ```

    ---
    <br/>

3. **How to break the Manifest file when too big?**

    To break a [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) file, replace it with a folder of the same name, then create the following structure.

    ```yaml
    📜 Manifest/ # folder instead of a file.
    ├─ 📜 Manifest.yaml # identity section 👥
    │
    ├─ {Codes}/ # tree of schema codes 🧩
    │  └─ GROUP-A/
    │     ├─ 🧩 CODE-A1.yaml
    │     └─ 🧩 CODE-A2.yaml
    │
    ├─ {Flows}/ # tree of flows   
    │  └─ ✏️ FLOW-1.yaml
    │
    ├─ {Services}/ # tree of API integrations 🪢
    │  └─ GROUP-S/
    │     ├─ 🪢 INTEGRATION-1.yaml
    │     └─ 🪢 INTEGRATION-2.yaml
    │
    └─ {Trusts} # tree of trusts 👍
       └─ GROUP-B/
          ├─ GROUP-C/
          │  └─ 👍 TRUST-BC1.yaml
          └─ 👍 TRUST-B1.yaml
    ```

    ---
    <br/>


1. **What does the Locators file looks like?**

    The `🔆 Locators.yaml` file contains the mapping of [Locator 🔆 resources](<../11 🔆 Locators/01 🔆 Locator.md>) to [Talkers 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    * Note: only the `resource` part of each [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) is required.

    ```yaml
    🤝: nlweb.org/HOSTER/LOCATORS

    Locators:
        _default: # if no Host Locator is provided.
            Talker: talker-1
        resource-1:
            Talker: talker-1
        resource-2:
            Talker: talker-2
    ```  


    The [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) files reside under the `Talkers/` folder.

    ```yaml
    😃 Talkers/ # Tree of talkers
    ├─ 😃 talker-1.yaml
    └─ 😃 talker-2.yaml
    ```
    
    ---
    <br/>