# How to set up port forwarding on your primary router

If you are setting up a server (such as an [OpenVPN server](https://docs.gl-inet.com/router/en/4/tutorials/build_your_own_openvpn_home_server_with_two_glrouter/) or [WireGuard server](https://docs.gl-inet.com/router/en/4/tutorials/build_your_own_wireguard_home_server_with_two_glinet_routers/)) on your GL.iNet router and it is connected to a primary router, you will have to set up port forwarding on the primary router. This ensures the server to be accessible properly. (Note that if there are other routers between the primary router and the GL.iNet router, you will have set up port forwarding on all these preceding routers.)

The steps for setting up port forwarding vary depending on the brand and model of your router. Refer to the section appropriate to you below. 

## GL.iNet router as my primary router

If your primary router is a GL.iNet router, follow these steps to set up port forwarding on it. 

1. In a web browser, enter the URL to your router admin panel (e.g., 192.168.8.1) and sign in.
2. In the left sidebar, click **Network** > **Firewall**. 
3. In the **Port Forwards** tab, click **Add**. 
4. Enter the following information: 
    * **Name:** Enter any name for the rule.
    * **Protocol:** Keep it as-is. 
    * **External Zone:** Keep it as-is. 
    * **External Port:** Enter the port you are using. For example, the default ports are **1194** (for OpenVPN servers) and **51820** (for WireGuard servers).
    * **Internal Zone:** Keep it as-is. 
    * **Internal IP:** Select the router you want to forward your port to. 
    * **Internal Port:** Enter the port you are using. For example, the default ports are **1194** (for OpenVPN servers) and **51820** (for WireGuard servers).
5. Click **Apply**. 

## Other router brands as my primary router

!!! note "Make sure to enter the following information when setting up port forwarding:"

    Different router brands and models have different ways of naming the information you have to provide when you set up port forwarding. In general, make sure to enter the following information on the router's port forwarding screen:
    
    * **External port/Internal port:** Enter the port you are using. For example, the default ports are **1194** (for OpenVPN servers) and **51820** (for WireGuard servers).
    * **Protocol:** Choose **All** or **UDP/TCP**.
    * **Internal IP** (or shown as **Host IP**): Enter your secondary router's WAN IP address or select your secondary router from the dropdown if available. 

Here are the instructions for setting up port forwarding on certain router brands and models as your primary router:

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/)
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/)
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/)

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/)

### Eero 

[Refer to these instructions.](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding)

### Linksys

[Refer to these instructions.](https://www.tp-link.com/us/support/faq/1379/)

### Netgear 

[Refer to these instructions.](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router)

### TP-Link 

[Refer to these instructions.](https://www.tp-link.com/us/support/faq/1379/)

If you need assistance because your specific router brand or model is not listed above, contact your router manufacturer or the GL.iNet Support Team via email at [support@glinet.biz](mailto:support@glinet.biz).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.