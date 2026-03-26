# Se connecter à Internet via le partage de connexion USB

L'utilisation d'un câble USB pour partager le réseau de votre smartphone avec le routeur s'appelle le Tethering. Les modems host-less fonctionnent également en mode Tethering lors de la configuration du modem.

**Remarque :** certains opérateurs mobiles limitent le Tethering ou facturent des frais supplémentaires. Nous vous recommandons de vérifier ce point auprès de votre opérateur.

## Configuration

=== "iPhone"

    1. Connectez un iPhone au port USB du routeur à l'aide d'un câble USB. Une boîte de dialogue système s'affichera pour vous demander si vous faites confiance à l'appareil. Appuyez sur **Trust** pour continuer. 

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Accédez à **Settings** -> **Personal Hotspot** sur l'iPhone. Activez **Allow Others to Join**.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Connectez un ordinateur ou un autre téléphone au routeur, puis connectez-vous au panneau d'administration web de votre routeur, accédez à la section **INTERNET** -> **Tethering**, puis cliquez sur **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        Si vous devez définir des paramètres avancés tels que TTL, HL et MTU, cliquez sur **Advanced** pour les personnaliser, puis cliquez sur **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        La connexion démarre.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Une fois connecté, l'état du partage de connexion personnel (par exemple le nombre d'appareils connectés) apparaît dans la barre d'état en haut de l'écran du téléphone.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        Le panneau d'administration web affichera également l'état de la connexion Tethering.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Connectez un téléphone Android au port USB du routeur à l'aide d'un câble USB. Une boîte de dialogue système peut s'afficher pour demander les préférences USB. Sélectionnez **USB Tethering** ou **File Transfer** si demandé. 

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. Accédez aux **Settings** de votre téléphone -> **Network & Internet** -> **Personal Hotspot**. Activez **Personal Hotspot** ou **USB Tethering**.
    
        (La procédure d'activation du **USB Tethering** varie selon les marques. Vérifiez l'emplacement exact dans les paramètres de votre appareil et contactez l'assistance du fabricant si nécessaire.)

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Connectez un ordinateur ou un autre téléphone au routeur, puis connectez-vous au panneau d'administration web de votre routeur, accédez à la section **INTERNET** -> **Tethering**, puis cliquez sur **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        Si vous devez définir des paramètres avancés tels que TTL, HL et MTU, cliquez sur **Advanced** pour les personnaliser, puis cliquez sur **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        La connexion démarre.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Une fois connecté, l'état du point d'accès personnel (par exemple le nombre d'appareils connectés) apparaît dans la barre d'état en haut de l'écran du téléphone. 
    
        Le panneau d'administration web affichera également l'état de la connexion Tethering.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Pour la documentation officielle Android, consultez [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Avertissement

Lorsque l'accès à Internet n'est pas disponible, l'avertissement correspondant s'affiche : 

**"The interface is connected, but the Internet can't be accessed."**

Solutions : 

1. Vérifiez si le smartphone dispose d'un accès à Internet.

2. Accédez à la page [Multi-WAN](multi-wan.md) pour déterminer si vous pouvez accéder à Internet ou non.

## Dépannage

Si la connexion échoue, essayez les étapes de dépannage suivantes :
    
- Utilisez l'alimentation d'origine du routeur.
- Débranchez puis rebranchez le câble USB.
- Utilisez un autre câble USB. Assurez-vous qu'il prend en charge le transfert de données (pas seulement la charge).
- Désactivez puis réactivez **USB Tethering** plusieurs fois (pour les téléphones Android).
- Désactivez puis réactivez **Allow Others to Join** plusieurs fois (pour l'iPhone).
- Redémarrez votre smartphone et réessayez.

---

Articles connexes

- [Page Internet](internet.md)
- [Comment définir la priorité de chaque méthode d'accès à Internet ?](multi-wan.md)
- [Comment définir l'équilibrage de charge lorsque plusieurs méthodes d'accès à Internet sont utilisées en même temps ?](multi-wan.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
