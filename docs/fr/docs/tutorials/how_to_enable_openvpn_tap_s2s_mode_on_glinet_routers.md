# Comment activer le mode OpenVPN TAP-S2S sur les routeurs GL.iNet ?

## Scénarios d'utilisation

Après avoir activé le mode TAP-S2S, l'appareil client OpenVPN peut accéder à distance à l'appareil serveur OpenVPN, et l'appareil serveur OpenVPN peut également accéder à distance à l'appareil client OpenVPN. En revanche, les règles VPN définies sur le client OpenVPN lui-même ne prennent plus effet une fois le mode TAP-S2S activé.

## TAP-S2S vs mode TUN

Topologie du réseau

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

Les modes TAP-S2S et TUN utilisent la même méthode de connexion physique, mais leur méthode de connexion logique est différente. Voici les différences :

1. Lorsque des appareils du côté LAN du GL-X3000 accèdent à l'interface de gestion du GL-MT6000, le mode TAP-S2S n'utilise pas d'IP virtuelle, contrairement au mode TUN.
2. Lorsque des appareils du côté LAN du GL-X3000 accèdent à l'interface de gestion du GL-X3000, le mode TAP-S2S utilise une IP virtuelle, contrairement au mode TUN.
3. Lorsqu'un appareil du côté LAN du GL-X3000 connaît l'adresse IP d'un appareil situé du côté LAN du GL-MT6000, le mode TAP-S2S autorise un accès à distance direct, alors qu'en mode TUN, l'accès direct n'est pas possible sans activer des paramètres supplémentaires.
4. En mode TAP-S2S, le GL-X3000 doit passer par le GL-MT6000 pour accéder à Internet, alors qu'en mode TUN, le GL-X3000 peut accéder directement à Internet. Par conséquent, en mode TAP-S2S, les règles VPN définies sur le GL-X3000 ne prennent pas effet et il faut suivre les règles VPN définies sur le GL-MT6000.

## Tutoriels

Commencez par utiliser un routeur (supposé être un GL-MT6000) disposant d'une IP publique pour activer **OpenVPN Server**, définissez le mode de l'appareil sur **TAP-S2S**, cliquez sur **Apply**, puis sur **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

Ensuite, utilisez un routeur (supposé être un GL-X3000) disposant d'une IP publique pour ouvrir le client OpenVPN, importez le fichier de configuration téléchargé à l'étape précédente, cliquez sur **Apply**, puis activez la fonction.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

À ce moment-là, l'adresse IP du routeur GL-X3000 change. Vous pouvez vous connecter au tableau de bord de gestion du GL-MT6000, ouvrir **Clients**, puis trouver la nouvelle adresse IP du GL-X3000.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Si le GL-MT6000 perd sa connexion réseau ou désactive le serveur OpenVPN, ou si le GL-X3000 désactive le client OpenVPN, l'adresse IP du GL-X3000 est rétablie.

Points à noter :

- Les deux appareils doivent être mis à niveau vers la version v4.5, sinon ils ne pourront pas se connecter ;
- TAP-S2S fonctionne uniquement avec le mode global ; il s'ajuste automatiquement lorsque OpenVPN est activé.
- Après avoir activé cette fonction, les fonctions suivantes ne peuvent pas être utilisées : serveur VPN, Adguard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping, etc.

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
