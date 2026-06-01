# ACL

> La fonctionnalité ACL a été introduite dans le firmware v4.9.

ACL, abréviation de Access Control List, vous permet de créer des règles pour gérer le trafic réseau en fonction des protocoles de connexion, des adresses des appareils et des ports. Elle contrôle si l'accès réseau est autorisé ou bloqué. Si plusieurs règles ACL entrent en conflit, le système applique celle qui a la priorité la plus élevée.

ACL fonctionne différemment de Port Forwarding : ACL autorise ou bloque principalement l'accès réseau à des fins de sécurité, tandis que Port Forwarding redirige le trafic externe vers des appareils spécifiques de votre réseau local afin de permettre l'accès à distance à des services locaux.

---

Dans le panneau d'administration web, accédez à **SECURITY** -> **ACL**.

Cliquez sur le bouton **Add Rule** à droite.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Créez votre règle ACL dans la fenêtre contextuelle, puis cliquez sur **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name** : saisissez un nom personnalisé pour la règle.

- **Protocol** : précisez le type de trafic réseau concerné par cette règle. Sélectionnez un protocole parmi `Any`, `TCP`, `UDP`, `TCP+UDP` et `ICMP`.

- **IP Type** : définit le format d'adresse IP du trafic réseau. Sélectionnez le type parmi `IPv4 & IPv6`, `IPv4` et `IPv6`.

- **Source Zone** : sélectionnez la zone réseau d'où provient le trafic. Options disponibles : `LAN`, `Guest`, `IoT` et `WAN`.

- **Source Address** : (facultatif) Limitez la règle à des appareils ou adresses IP sources spécifiques. Vous pouvez sélectionner une adresse source dans la liste déroulante.

- **Destination Zone** : indique où se dirige le trafic réseau. Sélectionnez la zone réseau de destination. Options disponibles : `LAN`, `Guest`, `IoT` et `WAN`.

- **Destination Address** : (facultatif) Limitez la règle à des appareils ou adresses IP de destination spécifiques. Vous pouvez sélectionner une adresse de destination dans la liste déroulante.

- **Action** : choisissez si le trafic réseau correspondant à cette règle doit être `Accept` ou `Block`.

- **Enable** : activez ou désactivez cette règle.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.