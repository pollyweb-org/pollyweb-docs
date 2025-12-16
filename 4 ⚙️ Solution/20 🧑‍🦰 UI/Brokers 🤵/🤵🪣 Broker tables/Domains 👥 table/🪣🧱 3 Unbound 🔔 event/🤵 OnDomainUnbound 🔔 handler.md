# 🤵 OnDomainUnbound 📃 handler

<br/>

## Diagram

![alt text](<🤵 OnDomainUnbound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnDomainUnbound:

# Remove all Binds for the Domain
- PARALLEL $Domain.Binds >> $bind:
    - SAVE $bind:
        STATE: REMOVED

# Reset the Domain
- SAVE $Domain:
    STATE: 
```