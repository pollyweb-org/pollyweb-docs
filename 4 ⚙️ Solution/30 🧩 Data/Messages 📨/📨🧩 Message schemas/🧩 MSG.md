
# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) `.MSG`

> Schema of a [domain Message 📨](<../📨 Message/📨 Message.md>)

<br/>

## Definition

> [🤝:](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /MSG

Blueprint: 
  Version: 1.0
  
  
  Format: 
    type: object
    required: [Header, Hash, Signature]
    properties:

      Header:
        type: object
        required: [From, To, Subject, Correlation, Timestamp, Selector]
        properties:

          From: 
            type: string
            format: hostname
            example: any-domain.dom

          To:
            type: string
            format: hostname
            example: any-domain.dom
            
          Subject:
            type: string
            example: CheckIn@Broker
            description: >
              Method to be called at the destination domain.
              Typically formatted as <method>@<role>.
              
          Correlation:
            type: string
            format: uuid
            example: 125a5c75-cb72-43d2-9695-37026dfcaa48
            description: Uniquely identifies the initial request.

          Timestamp:
            type: string
            format: utc.datetime
            example: 2024-09-21T12:34:00Z
            description: Date and time when the request was sent, in UTC.

          Selector:
            type: string
            example: pw1
            description: >
              DKIM selector used to locate the sender's public key in DNS.

          Schema:
            type: string
            default: pollyweb.org/MSG:1.0
            description: >
              Code schema to validate the content of the body.
              Defined as <domain>/<code-path>:<schema-version>.

      Body:
        type: object
        description: > 
          Main content of the message.

      Hash:
        type: string

      Signature:
        type: string
```        
