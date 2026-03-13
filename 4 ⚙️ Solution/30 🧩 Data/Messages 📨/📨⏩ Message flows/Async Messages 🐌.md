# 🐌📨 Async Messages

> Part of [domain Message 📨](<../📨 Message/📨 Message.md>)

> Implemented by [👥⏩👥 Send Async 🐌](<../../../40 👥 Domains/👥⏩ Domain flows/Send Async 👥🐌👥/👥 Async Message ⏩ flow.md>)

<br/> 

1. **What are asynchronous messages?**

    [Domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) send fire-and-forget messages and events. 
    * Any eventual answer, if expected, will arrive via another asynchronous message.

    ---
    <br/>

1. **How do receiver domains reply to incoming messages?**

    PollyWeb advocates for communications to be asynchronous by default to minimize wait times in HTTPS communications and reduce the serverless compute cost of sending outbound messages. 
    
    - Thus, the receiver is expected to store the envelope in a resilient queue and immediately return a successful HTTPS 200 response. 
    
    - The receiver then processes the incoming envelopes [asynchronously](<Async Messages 🐌.md>) by consuming them from the queue - it discards invalid envelopes, and replies to valid ones by sending a new envelope to the sender.

    ---
    <br/>


1. **How can senders know if receivers discarded messages?**

    When discarding an invalid message, receiver domains send feedback to the sender with the original correlation ID. 
    
    * Sender domains define their [Buffer ⏳ helper domain](<../../../45 🤲 Helper domains/Buffers ⏳/⏳ Buffer/⏳🤲 Buffer helper.md>) in the `Identity` section of their [domain Manifest 📜](<../../Manifests 📜/📜 Manifest/📜 Manifest.md>).
       * If the `Feedback` property is not defined, then no feedback is given.
       * Domains get of the [Buffer ⏳ helper domain](<../../../45 🤲 Helper domains/Buffers ⏳/⏳ Buffer/⏳🤲 Buffer helper.md>) by calling the [About@Graph 🚀 request](<../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>).
  
        ```yaml
        🤝: pollyweb.org/MANIFEST/ABOUT
        About:
          Domain: any-sender.dom
          Feedback: any-buffer.dom
        ```

    * The feedback is sent via a [Buffer ⏳ helper domain](<../../../45 🤲 Helper domains/Buffers ⏳/⏳ Buffer/⏳🤲 Buffer helper.md>) defined by the sender's domain, using the [Feedback@Buffer 🐌 API message](<../../../45 🤲 Helper domains/Buffers ⏳/⏳📨 Buffer msgs/👥🐌⏳ Feedback.md>). 
        ```yaml
        Header:
            Schema: pollyweb.org/MSG:1.0
            From: any-receiver.dom
            To: any-buffer.dom
            Subject: Feedback@Buffer
        Body:
            Correlation: <correlation-uuid>
            Status: Discarded
            Reason: Invalid DKIM signature.
        ```

    ---
    <br/>
