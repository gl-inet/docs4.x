# How to set up port forwarding on your primary router

If you are setting up a server (such as an [OpenVPN server](how_to_set_up_openvpn_server.md) or [WireGuard server](build_your_own_wireguard_home_server_with_two_glinet_routers.md)) your GL.iNet router and it is connected to a primary router, you will have to set up port forwarding on the primary router. This ensures the server to be accessible properly.

Note that if there are other routers between the primary router and the GL.iNet router, you have to set up port forwarding on all these preceding routers.

## Preparation

Before configuring port forwarding, we recommend **reserving a static IP address** for the GL.iNet router on your primary router. This ensures the GL.iNet router is always assigned a fixed IP address. 

Otherwise, if the primary router or GL.iNet router restarts, the primary router may assign a new IP address to the GL.iNet router, causing the port forwarding rule to fail. 

Next, set up port forwarding on your primary router for the GL.iNet router. 

The steps for configuring port forwarding vary by router brand and model. Refer to the appropriate section below.

## Using a GL.iNet Router as Your Primary Router

Please refer to [this link](../interface_guide/port_forwarding.md){target="_blank"}.

## Using Another Router Brand as Your Primary Router

!!! note "Make sure to enter the following information when setting up port forwarding"

    When configuring port forwarding, ensure the following information is provided. Note that terminology may vary across router brands and models.
    
    * **External port/Internal port:** Enter the port you are using. For example, the default ports are **1194** (for OpenVPN servers) and **51820** (for WireGuard servers).
    * **Protocol:** Choose **All** or **UDP/TCP**.
    * **Internal IP** (or shown as **Host IP**): Enter your secondary router's WAN IP address or select your secondary router from the dropdown if available. 

Here are step-by-step instructions for setting up port forwarding on common primary router brands and models. 

If your primary router brand or model is not listed below, refer to your router's documentation or contact their support team for further assistance.

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link 

* [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero 

Refer to [this link](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys

Refer to [this link](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear 

Refer to [this link](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.