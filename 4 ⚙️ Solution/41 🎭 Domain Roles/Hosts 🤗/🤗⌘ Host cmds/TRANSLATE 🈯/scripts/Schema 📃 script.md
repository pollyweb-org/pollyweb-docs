# 🈯 TRANSLATE SCHEMA 📃 script


## Script

```yaml
📃 .TRANSLATE-SCHEMA:

# Get the schema info
- SEND >> $schema:
    Header:
        To: $.Hosted.Graph
        Subject: Schema@Graph
    Body:
        Schema: $Schema

# Find a matching translation
- SELECT >> $translation:
    First: .Value
    From: $schema.Translations
    Where: .Key.Is($To)
    
# Prepare the response
- SET $return.Domain:
    Title: $schema.Title
    Description: $schema.Title
    Translation: $translation.Default(
        $schema.Title.Translate($To))

# Return the domain translation
- RETURN: $return
```