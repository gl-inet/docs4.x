# Why do I get a message from DDNS test?

When you run the DDNS test on the Dynamic DNS page, you may get a message as shown below.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

It is not a **Warning** or an **Error** message, but a reminder indicating your router's network status.

This result typically reflects the router's network position. For example, if your GL.iNet router is configured as a secondary router in your home network, this message will appear. 

It will not disappear even if you've set up port forwarding on your primary router — this simply indicates the router is behind NAT.

If you need to expose services through NAT (e.g., for remote access), additional settings are required.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.