🤝: nlweb.org/MANIFEST/CODE

Path: /TYPES

Schema: 
  Format: 
    properties: 

      Code:
        type: string
        example: nlweb.org/QR
        description: >
          Reference to a data type defined by the manifest of an authority.
          It's composed by the authority's domain and code path.
          For example, for [nlweb.org/QR]:
          - the manifest is at http://nlweb.org.com/manifest;
          - the schema definition is at 'Path:/QR' inside the manifest.
          Note: the manifest may delegate the definition to sub manifests.

      Domain:
        type: string
        format: hostname  
        example: any-domain.com
        description: An internet domain name.

      Key:
        type: string
        description: Public Key, from a a key pair.

      Rank:
        type: integer
        minimum: 1
        maximum: 5
        description: Star rank.

      Schema: 
        type: string
        example: nlweb.org/QR:3.11
        description: >
          Reference to the schema of data type defined by the manifest of an authority.
          It's composed by the authority's domain, code path, and an optional version.
          For example, for [nlweb.org/QR:3.11]:
          - the manifest is at http://nlweb.org.com/manifest;
          - the schema definition is at 'Path:/QR' inside the manifest;
          - the version of the schema is 3.11 (if omitted, defaults to 1.0).
          For example, for [nlweb.org/QR]:
          - the version of the schema is 1.0 (the default).
          Note: the manifest may delegate the definition to sub manifests.

      Timestamp:
        type: string
        format: utc.datetime
        example: '2098-12-10T13:45:00.000Z'
        description: Date time in UTC format.

      UUID:
        type: string
        format: uuid
        example: 28ff57b4-76f6-4944-a710-a71f9d667cee
        description: Universal unique identifier.