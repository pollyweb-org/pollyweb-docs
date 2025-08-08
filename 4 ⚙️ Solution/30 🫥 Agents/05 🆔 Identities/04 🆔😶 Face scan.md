🆔 Identity face scans FAQ
===

![](<00 📎 Assets/🆔 Online.png>)

1. **How is face recognition secured with a selfie input?**

    NLWeb discourages face recognition via selfie inputs (except in supervised scenarios) because bad actors can inject a fake picture. 
    
    Instead, NLWeb recommends using liveness checks from a remote service exposed via a Web 2.0 browser (e.g., by using Amazon Rekognition Face Liveness or Azure AI Vision Face Liveness). 

    ---
    
1. **How is face recognition secured with remote liveness checks?**

    Services implementing liveness checks mitigate frauds and replay attacks even if the Wallet device is running a sophisticated forgery software, is being used by an AI bot, or has been compromised by an attacker. 
    
    Liveness checks are video-based checks supported by a remove Web 2.0 page that typically include the following features:
    - **Facial motion analysis**: Tracks real-time facial movements like blinking.
    - **Challenge-response**: Prompts users to perform actions, making it hard for fraudulent software to mimic.
    - **Presentation attacks detection**: Detects spoof attacks presented to the camera, such as printed 2D photos, 2D cut-out paper masks, and hi-res photos or videos on a digital screen.
    - **Bypass attacks detection**: Detects spoof attacks that bypass the camera, such as pre-recorded, synthetic, and deepfake videos directly injected into the video capture sub-system.
    - **3D mask attacks detection**: Detects spoof attacks that use 3D masks made of silicone, latex, plastic, cloth, and more.
    
    ---
    
1. **How to implement face liveness checks on AWS?**

    ![](<00 📎 Assets/🆔 Face Scan @AWS.png>)

    Identity domains rely on the following components for domain [📨 Messaging](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>):
    - 📨 **Inbox**: the combination of the Distributer plus the Endpoint;
    - 📮 **Async Post**: an async message outbound that signs messages.

    ---
    