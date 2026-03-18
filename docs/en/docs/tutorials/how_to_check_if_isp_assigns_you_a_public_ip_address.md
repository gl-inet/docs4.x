# How to check if you have a public IP address

A public address, as opposed to a private IP address, is a unqiue numerical identifier assigned to your devices connected to the internet. You will need a public IP address if you want to host a website, set up a VPN server, or provide any online services. Your internet service provider typically provides you with one. 

If you are not sure whether you have a public IP address, follow one of these methods to check. 

**Method 1: Contact your internet service provider directly**

**Method 2: Check your IP address in your router admin panel and on the internet** 

1. Log in to your router's admin panel. 
    * For GL.iNet routers, enter `192.168.8.1` into a web browser and sign in.
    * If you have more than one router in your setup, log in to the primary router's admin panel. 
2. In the router admin panel, locate your WAN IP address (e.g., 42.XXX.XX.)
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. In a web browser, search "what is my ip."
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

If the two IP addresses match, you have a public IP address. 
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

If you do not have a public IP address, you may consider using an intranet penetration tool. It allows your website, VPN server, or services to be accessible on the internet, even if you do not have a public IP address. 

---

Related Articles

- [Set Up WireGuard Server on GL.iNet Router](../interface_guide/wireguard_server.md)
- [Set Up OpenVPN Server on GL.iNet Router](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
