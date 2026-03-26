# MAC Address

Ce guide s'applique au firmware v4.5 et aux versions antérieures.

La page MAC Address s'appelait auparavant MAC Clone et a été renommée MAC Address à partir de la v4.2.

Depuis la v4.6, les paramètres d'adresse MAC des interfaces Ethernet et Repeater ont été déplacés respectivement vers [Port Ethernet](ethernet_port.md) et [Repeater](internet_repeater.md).

---

Dans la partie gauche du panneau d'administration web, accédez à **NETWORK** -> **MAC Address**.

Vous pouvez y trouver l'adresse MAC par défaut du routeur, cloner l'adresse MAC d'un client, saisir manuellement une adresse MAC ou générer une adresse MAC aléatoire.

Si l'appareil prend en charge la configuration de plusieurs ports Ethernet utilisables comme ports WAN, vous pouvez définir séparément l'adresse MAC de chaque port. Notez que le réglage de l'adresse MAC n'est valable que lorsque le port Ethernet est utilisé comme port WAN.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* Adresse MAC d'usine par défaut.

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Cloner l'adresse MAC d'un client.

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Remarque :** de nombreux appareils récents utilisent désormais une adresse MAC aléatoire différente pour se connecter à différents réseaux Wi‑Fi. L'adresse MAC affichée ici peut donc ne pas correspondre à l'adresse MAC réelle de l'appareil de l'utilisateur. Selon les appareils, cette adresse MAC aléatoire peut aussi être appelée Private Wi‑Fi Address ou random hardware address.

* Saisir manuellement une adresse MAC ou générer une adresse MAC aléatoire.

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Scénarios d'utilisation

Lorsque vous vous connectez à un hotspot public, utilisez une adresse MAC aléatoire si vous ne voulez pas que le hotspot connaisse votre véritable adresse MAC ou limite votre accès à Internet en fonction de celle-ci. Veuillez consulter ce guide : [Se connecter à un hotspot avec un portail captif](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
