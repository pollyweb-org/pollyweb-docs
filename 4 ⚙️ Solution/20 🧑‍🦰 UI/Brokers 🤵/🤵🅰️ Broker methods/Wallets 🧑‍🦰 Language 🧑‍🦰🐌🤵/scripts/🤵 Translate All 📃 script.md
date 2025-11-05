
```yaml

# Group the domains
- DISTINCT >> $domains:
    $wallet.Chats.Host
    $wallet.Binds.Vault
    $wallet.Tokens.Issuer

# Group the schemas
- DISTINCT >> $schemas:
    $wallet.Tokens.Schema

# Translate domains and schemas
- SEND >> $translated:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Language: $.Msg.Language
        Domains: $domains
        Schemas: $schemas

# Return the translations
- RETURN:
    $translated
```