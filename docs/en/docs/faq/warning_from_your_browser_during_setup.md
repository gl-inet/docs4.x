# Warning from your browser: Your Connection is not Private

You may encounter this browser alert if this is your first time setting up your GL.iNet router: Your Connection is not Private.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

This is a standard security warning issued by the browser when it detects a website without a trusted SSL/TLS certificate.

Browsers are typically designed to trust certificates issued by third-party certificate authorities (CAs). However, GL.iNet routers use self-signed certificates, which are not issued by CAs. Therefore, browsers flag them as insecure and display this warning.

## Is it safe to browse 192.168.8.1?

We prioritize your network security. During the initial setup, you do not need an internet connection, as the process is entirely local.

When connecting to the GL.iNet router's Wi-Fi during setup, you may see **"Connected, No internet"**. This is expected, as the router operates in a standalone local network during configuration.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

Similarly, the IP **192.168.8.1** is a private local IP address assigned to the router itself. It is used to access the device's local admin panel, not a public website. 

Since the connection is purely local and no internet access is required during setup, there is **no risk of privacy leakage**. This ensures a secure, isolated environment for configuring your router.

## Why do I still get a warning?

Browsers usually do not distinguish between a preset setup IP address and normal websites; they treat all IP addresses as websites and expect HTTPS connections to be secured by SSL/TLS certificates. 

GL.iNet routers do use SSL/TLS certificates, but they are self-signed and not issued by third-party certificate authorities (CAs). Although accessing this IP is secure (as it is on a private local network), it is still considered "insecure" by the browser, which is why an alert is issued.

## What can I do with this warning?

Please click **Advanced** and **Continue to 192.168.8.1** 

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Then you will re-direct to the web Admin Panel.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Can I add an SSL certificate in the router?

Yes, you can add your SSL certificate in the GLiNet routers.

[How to add a SSL certificate](../faq/use_https_for_adh.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
