# 🚀📨 Synchronous Requests

> Part of [domain Message 📨](<../📨 Message/📨 Message.md>)

> Implemented by [👥⏩👥 Request Sync 🚀](<../../../40 👥 Domains/👥⏩ Domain flows/Send Sync 👥🚀👥 /👥 Sync Request ⏩ flow.md>)

<br/> 

1. **What are Synchronous Requests?**

    [Domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) send requests and wait for the immediate response over an HTTPS request.

    ---
    <br/>


1. **How do sender domains prevent man-in-the-middle attacks?**

    By using HTTPS POST requests, sender domains ensure outbound messages are encrypted, and rely on trusted Certificate Authorities (CAs) to validate the TLS certificate of the receiver. 
    - By using a well-known URL prefix plus the receiver’s domain, sender domains rely only on DNS for network discovery.

    ---
    <br/>



1. **Can messages be compressed?** 

    HTTPS already handles compression:
    - `HTTP/2` and `HTTP/3` compress the header;
    - `Accept-Encoding` with `br, gzip` compresses the body. 

    ---
    <br/>

1. **With HTTPS compression, how is BREACH prevented?** 

    BREACH is a category of vulnerabilities where, to be vulnerable, a web application must:     
    * be served from a server that uses HTTP-level compression,
    * reflect user-input in HTTP response bodies,
    * and reflect a secret (such as a CSRF token) in HTTP response bodies.
  
    Additionally, while not strictly a requirement, the attack is helped greatly by responses that remain mostly the same (modulo the attacker's guess). 
    * This is because the difference in size of the responses measured by the attacker can be quite small. 
    * Any noise in the side-channel makes the attack more difficult (though not impossible). 

    BREACH was assessed for NLWeb, and it was determined that the protocol is not exposed to these specific risks.

    ---
    <br/>

