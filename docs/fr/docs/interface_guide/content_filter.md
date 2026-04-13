# Filtre de contenu

Le filtre de contenu est une fonctionnalité de sécurité en ligne intelligente basée sur la classification DPI. Il bloque automatiquement les sites web nuisibles et malveillants afin de garder votre réseau propre et sécurisé, et prend également en charge des règles personnalisées pour bloquer des applications, domaines ou adresses IP spécifiques.

## Modèles pris en charge

!!! note "Modèles pris en charge"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configuration rapide

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **Content Filter**.

Activez l’interrupteur dans l’angle supérieur droit, personnalisez le contenu à bloquer (comme les applications, domaines ou adresses IP), puis cliquez sur **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Cette page se compose de deux parties :

- **Blocked Apps List** : cette section comprend trois catégories présélectionnées : Gambling, Adult et Malware. Lorsqu’elles sont activées, tous les sites web, services ou applications liés à ces trois catégories sont bloqués.

    Vous pouvez également cliquer sur **Edit App** pour ajouter d’autres catégories selon vos besoins (par ex. Game, Social Media).

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    Dans la fenêtre contextuelle, sélectionnez les catégories à bloquer. Les trois catégories par défaut sont vides ; toutes les autres catégories comprennent une liste d’applications.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Cliquez sur une catégorie pour afficher et sélectionner les applications à bloquer, ou cliquez sur **Select All** en haut à droite pour bloquer toutes les applications de cette catégorie en une seule fois, puis cliquez sur **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

    Vous verrez ensuite les applications sélectionnées dans la liste **Blocked App List**.

- **Blocked Domain / IP List** : cette section vous permet de saisir manuellement des domaines spécifiques (par ex. `google.com`), des plages CIDR (par ex. `192.168.8.0/24`) ou des adresses IP (par ex. `192.168.10.10`) afin d’en bloquer l’accès. La liste prend en charge jusqu’à 10000 entrées.

    Saisissez les domaines ou adresses IP à bloquer, puis cliquez sur **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Test du filtre de contenu

Par exemple, nous avons sélectionné la catégorie **Game**, qui inclut Nintendo.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

Sur un ordinateur portable connecté à votre routeur, le site `nintendo.com` n’est plus accessible, alors qu’il l’était avant l’activation du filtre de contenu.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

Dans le panneau d’administration web du routeur, vous pouvez voir le nombre de requêtes d’accès qui ont été bloquées.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
