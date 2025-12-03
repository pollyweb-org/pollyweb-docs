# 🪵 Logger 🤲 helper

1. **What is a Logger?**

    A [Logger 🪵 helper domain](<🪵 Logger 🤲 helper.md>)
    * is a [Helper 🤲 domain](<../../$ Helpers 🤲/🤲 Helper/🤲👥 Helper domain.md>)
    * that receives log messages 
    * from other [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    ---
    <br/>

1. **What inbound messages are accepted by a Logger?**

    |[Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Purpose
    |-|-
    |[🚀 `Start`](<../🪵📨 Logger msgs/Start 👥🚀🪵/🪵 Start 🚀 call.md>) | Registers a log thread
    |[🐌 `Log`](<../🪵📨 Logger msgs/Log 👥🐌🪵/🪵 Log 🐌 msg.md>) | Logs into a thread
    |[🚀 `Export`](<../🪵📨 Logger msgs/Export 👥🚀🪵/🪵 Export 🚀 call.md>)| Exports log entries
    
    ---
    <br/>