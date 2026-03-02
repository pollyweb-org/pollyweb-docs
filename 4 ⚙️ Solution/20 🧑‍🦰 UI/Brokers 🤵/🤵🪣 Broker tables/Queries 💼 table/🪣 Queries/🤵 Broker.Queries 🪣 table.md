# 🤵 Broker.Queries 🪣 table

> About
* Part of the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>) helper

<br/>

## Lifecycle

![alt text](<🤵 Broker.Queries ⚙️ uml.png>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Queries
Item: Query
Key: Query, Consumer
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)


```yaml
Parents: 

    Chat: # Chat where the Query was sent

    Wallet: # Wallet owning the Chat
        Wallet.ID: Chat.Wallet

    Chatter: # Chat participant who sent the Query
        Chatter.Domain: Query.Consumer
        Chatter.Chat: Query.Chat

    Consumer: # Details about the consumer
        Domain: Query.Consumer
        Wallet: Chat.Wallet
```



<br/>

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`Queried`](<../🪣🔔 10 Queried/🤵 OnQueryQueried 🔔 handler.md>) [`Abrupt`](<../🪣🔔 15 Abrupt/🤵 OnQueryAbrupt 🔔 handler.md>) [`Informed`](<../🪣🔔 20 Informed/🤵 OnQueryInformed 🔔 handler.md>) [`Matched`](<../🪣🔔 30 Matched/🤵 OnQueryMatched 🔔 handler.md>) [`Trusted`](<../🪣🔔 40 Trusted/🤵 OnQueryTrusted 🔔 handler.md>) [`Selected`](<../🪣🔔 50 Selected/🤵 OnQuerySelected 🔔 handler.md>) [`Disclosed`](<../🪣🔔 70 Disclosed/🤵 OnQueryDisclosed 🔔 handler.md>) [`Shared`](<../🪣🔔 80 Shared/🤵 OnQueryShared 🔔 handler.md>)

```yaml
Handlers: 
    QUERIED              >> OnQueryQueried:   # Informed Schemas?
    QUERIED > ABRUPT     >> OnQueryAbrupt:    # Sends a FAIL
    QUERIED > INFORMED   >> OnQueryInformed:  # Matched Schemas?
    INFORMED > MATCHED   >> OnQueryMatched:   # Wallet trusted?
    MATCHED > TRUSTED    >> OnQueryTrusted:   # Asks to select
    TRUSTED > SELECTED   >> OnQuerySelected:  # Asks confirmation
    SELECTED > DISCLOSED >> OnQueryDisclosed: # Binds by Vaults
    SELECTED > SHARED    >> OnQueryShared:    # Tokens by Wallets
```


<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    AllOf: Chat, Query, Schemas, Consumer
    UUIDs: Chat, Query, Bind, Token
    Lists: Schemas, Matches, Trusts
    
    # Inputs
    Consumer.IsDomain:      # Consumer that requested the query
    Schemas.Each.IsSchema:  # List of Schemas queried
    Chat.STATE: ACTIVE      # Progress if the Chat is active
    
    # Outputs
    Matches.Each.Type.IsIn: BIND, TOKEN
    Trusts.Each.Type.IsIn: BIND, TOKEN
    Selected.Type.IsIn: BIND, TOKEN
    Vault.IsDomain:         # Vault where a Bind is stored
    Issuer.IsDomain:        # Issuer of a Token
```

Uses: [`.Each`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Each ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) 


<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <query-uuid>        # ID on the Query
```

From [`Query@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 📃 handler.md>)

```yaml
Chat: <chat-uuid>       # Chat where the Query was sent
Query: <query-uuid>     # Query to reply to the Consumer 
Consumer: any-host.dom  # Sender of the Query
Schemas:                # List of acceptable schemas
  - any-authority.dom/ANY-SCHEMA  # Requested Schema 1
```

From [`OnQueryInformed` 🔔 handler](<../🪣🔔 20 Informed/🤵 OnQueryInformed 🔔 handler.md>)

```yaml
Matches: # All Binds and Tokens matching the Schemas        
  - ID: <item-uuid>
    Type: TOKEN   # TOKEN or BIND
    Title: Any Token, by Any Issuer
    Domain: any-issuer.dom
    Key: <token-uuid>
    Schema: any-authority.dom/ANY-SCHEMA  
```

From [`OnQueryMatched` 🔔 handler](<../🪣🔔 30 Matched/🤵 OnQueryMatched 🔔 handler.md>)

```yaml
Trusted: # Only the Binds and Tokens mutually trusted
  - ID: <item-uuid>
    # ...
```

From [`OnQueryTrusted` 🔔 handler](<../🪣🔔 40 Trusted/🤵 OnQueryTrusted 🔔 handler.md>)

```yaml
Selected: # Only the trusted Bind or Token selected
    ID: <item-uuid>
    # ...
```

From [`OnQuerySelected` 🔔 handler](<../🪣🔔 50 Selected/🤵 OnQuerySelected 🔔 handler.md>), for [`OnQueryDisclosed` 🔔](<../🪣🔔 70 Disclosed/🤵 OnQueryDisclosed 🔔 handler.md>)

```yaml
Bind: <bind-uuid>       # Bind to be shared
Vault: any-vault.dom    # Vault where the Bind is stored
```

From [`OnQuerySelected` 🔔 handler](<../🪣🔔 50 Selected/🤵 OnQuerySelected 🔔 handler.md>), for [`OnQueryShared` 🔔](<../🪣🔔 80 Shared/🤵 OnQueryShared 🔔 handler.md>)

```yaml
Token: <token-uuid>     # Token to be shared
Issuer: any-issuer.dom  # Issuer of the Token
```