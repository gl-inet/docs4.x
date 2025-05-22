# Why do I get a message from DDNS test?

When you run the DDNS test on the Dynamic DNS page, you may get a message as shown below.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

It is not a **Warning** or an **Error** message, but a reminder.

This result indicates the router’s network position. If your GL.iNet router is configured as a secondary router in your home network, this message will appear.

This message will not disappear even if you have configured port forwarding on your primary router. It simply reminds you that the router is behind NAT. 

If you need to expose services through the NAT (e.g., remote access), additional settings are required.

If you see the following message, it may indicate you are using a cellular network, where DDNS setup is not available.

![ddnsfail](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnsfail.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.