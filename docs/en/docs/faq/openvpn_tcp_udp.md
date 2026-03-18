# OpenVPN, TCP vs UDP

GL.iNet router's OpenVPN Server supports both TCP and UDP protocols. What's the difference?

TCP is more reliable but slower in speed. UDP is faster but less reliable.

If you need low-latency and continuous data transmission for an application to work properly, UDP is a better choice. Otherwise, TCP is a reliable protocol for transferring data without loss during transmission. 

UDP is more suitable for gaming, streaming, or using VoIP services. TCP is more suitable for emailing, web browsing, and file transfer.

We recommend trying the UDP protocol first and only switching to TCP if you experience connection instability, packet loss, or other reliability-related issues.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
