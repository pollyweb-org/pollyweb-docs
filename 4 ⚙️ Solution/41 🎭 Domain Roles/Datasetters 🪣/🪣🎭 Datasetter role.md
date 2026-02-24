🪣🎭 Datasetter domain role
===

![](<.📎 Assets/🪣 Datasetter.png>)

1. **What is a Datasetter domain role in PollyWeb?**

    A Datasetter is an [🪢 Integrator](<../Integrators 🪢/🪢🎭 Integrator role.md>) domain that exposes a synchronous data API. 

    ---
    <br/>

1. **What are examples of possible data APIs?**

    Data APIs can be 
    * reference data (e.g., countries, flags, country calling codes), 
    * dynamic datasets (e.g., weather forecasts), 
    * or any type of data capable of being downloaded from an HTTPS endpoint.

    ---
    <br/>

1. **How do Datasets handle data API requests?**

    When using the PollyWeb SDK, Datasets can point the data APIs 
    * to static datasets (e.g., CSV files), 
    * to databases (e.g., PostgreSQL), 
    * or to custom-built handlers (e.g., Python).

    ---
    <br/>

1. **How can Hosts leverage Datasets on chats?**

    When using the PollyWeb SDK, Hosts can reference these APIs in workflow and schema-based CRUD dialogs by using PollyWeb locators. 
    
    * The PollyWeb SDK will pull the data schema from the Datasetter's Manifest, and map it to the CRUD schema of the Host. 
    * When chatting with users, the PollyWeb SDK invokes the Datasetter's end-point.

    ---
    <br/>

1. **How do Hosts reference a Datasets API?**

    Data APIs are referenced by `{column}@{domain}/{offer}` - e.g.:
    * `Code@standards.any-igo.dom/639-1` 
    * references the `Code` column 
    * in the `639-1` data API 
    * offered by the domain [`standards.any-igo.dom` 📜](<../../../8 📜 Manifests/👥 any-igo.dom/📜 standards.any-igo.dom.md>) .

    ---
    <br/>