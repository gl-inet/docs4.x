# Changer le port WAN en port LAN

Vous pouvez convertir le port WAN de votre routeur en port LAN. Cela est particulièrement utile lorsque vous utilisez le routeur en mode répéteur, où le port WAN n'est pas nécessaire. En changeant le port WAN en port LAN, vous obtenez un port LAN supplémentaire pour étendre la connectivité.

Suivez les étapes ci-dessous pour changer le port WAN en port LAN.

## Pour le firmware 4.7 et versions ultérieures

1. Laissez le port WAN déconnecté.

2. Connectez un appareil au routeur et accédez au panneau d'administration web du routeur.

3. Dans le panneau d'administration web, allez à la section **INTERNET** -> **Ethernet**, puis cliquez sur l'icône en forme d'engrenage en haut à droite.

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

	Vous serez redirigé vers la page **Port Management**, où l'état du port WAN est affiché comme utilisé pour le WAN.

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Cliquez sur **LAN** pour modifier les propriétés du port Ethernet, puis cliquez sur **Apply**.

	![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

	Dans la fenêtre d'avertissement qui s'affiche, cliquez sur **Apply** pour confirmer.
	
	![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

	**Remarque** : le Wi-Fi peut se déconnecter temporairement pendant ce processus. Reconnectez-vous au routeur une fois l'opération terminée.

5. De retour dans la section Ethernet, vous verrez que le port WAN est maintenant utilisé comme port LAN.

	![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

	Vous pouvez le repasser en WAN depuis la page **Port Management**, ou appuyer sur le bouton RESET pendant 4 secondes pour redémarrer l'interface WAN.

## Pour le firmware 4.6 et versions antérieures

1. Laissez le port WAN déconnecté.

2. Connectez un appareil au routeur et accédez au panneau d'administration web.

3. Dans le panneau d'administration web, allez à la section **INTERNET** -> **Ethernet**, où l'état du port WAN est affiché comme **Using as WAN**. Cliquez sur **Change to LAN**.

	![internet page](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Cliquez sur **Apply** pour confirmer.

	![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

	**Remarque** : le Wi-Fi peut se déconnecter temporairement pendant ce processus. Reconnectez-vous au routeur une fois l'opération terminée.

5. De retour dans la section Ethernet, l'état affiché devient `Using as LAN`.

	![using as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

	Vous pouvez simplement revenir au réglage précédent en répétant la procédure ci-dessus.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
