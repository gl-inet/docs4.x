# Le modem USB ne fonctionne pas correctement sur un routeur GL.iNet

Certains routeurs GL.iNet disposent de ports USB. Les utilisateurs peuvent brancher un modem USB sur le port USB pour configurer l'accès à Internet, et même mettre en place des scénarios Multi-WAN s'il est combiné à d'autres accès Internet.

Cependant, il peut arriver que certains modems USB (comme le ZTE F50 Mobile Wi-Fi Hotspot) ne puissent pas être utilisés normalement sur le routeur, ce qui provoque des coupures fréquentes du réseau.

Cela peut être dû à un problème de compatibilité entre le port USB du routeur (généralement USB 3.0) et le Wi-Fi 2,4 GHz, ce qui entraîne des déconnexions répétées du modem USB et empêche un accès Internet normal.

Pour résoudre ce problème, vous pouvez changer la spécification du port USB de l'USB 3.0 vers l'USB 2.0.

Accédez au panneau d'administration de votre routeur GL.iNet, puis allez dans **SYSTEM -> Overview -> External Storage**.

Vous verrez une option nommée USB Protocol Switch.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Basculez-la sur USB 2.0 ; une invite s'affichera comme ci-dessous. Cliquez sur Switch pour continuer.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Lorsque le protocole USB s'affiche en USB 2.0, cela signifie que le changement a été effectué avec succès.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Après cela, veuillez vérifier si la connexion Internet s'est améliorée.

---

Articles connexes

- [Compatible Modems](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
