# Comment vérifier si vous avez une adresse IP publique

Une adresse IP publique, contrairement à une adresse IP privée, est un identifiant numérique unique attribué à vos appareils connectés à Internet. Vous aurez besoin d'une adresse IP publique si vous souhaitez héberger un site web, configurer un serveur VPN ou fournir des services en ligne. Votre fournisseur d'accès à Internet vous en attribue généralement une. 

Si vous n'êtes pas sûr d'avoir une adresse IP publique, suivez l'une de ces méthodes pour le vérifier. 

**Méthode 1 : contactez directement votre fournisseur d'accès à Internet**

**Méthode 2 : vérifiez votre adresse IP dans le panneau d'administration du routeur et sur Internet** 

1. Connectez-vous au panneau d'administration de votre routeur. 
    * Pour les routeurs GL.iNet, saisissez `192.168.8.1` dans un navigateur Web et connectez-vous.
    * Si vous avez plus d'un routeur dans votre installation, connectez-vous au panneau d'administration du routeur principal. 
2. Dans le panneau d'administration du routeur, repérez votre adresse IP WAN (par ex. 42.XXX.XX.)
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. Dans un navigateur Web, recherchez "what is my ip".
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Si les deux adresses IP correspondent, vous disposez d'une adresse IP publique. 
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Si vous n'avez pas d'adresse IP publique, vous pouvez envisager d'utiliser un outil d'accès à l'intranet depuis Internet. Il permet à votre site web, à votre serveur VPN ou à vos services d'être accessibles sur Internet, même si vous ne disposez pas d'adresse IP publique. 

---

Articles connexes

- [Configurer le serveur WireGuard sur un routeur GL.iNet](../interface_guide/wireguard_server.md)
- [Configurer le serveur OpenVPN sur un routeur GL.iNet](../interface_guide/openvpn_server.md)
- [Redirection de port](../interface_guide/port_forwarding.md)

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
