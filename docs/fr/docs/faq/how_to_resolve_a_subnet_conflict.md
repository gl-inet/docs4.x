# Comment résoudre un conflit de sous-réseau LAN ?

Lorsque vous branchez un câble Ethernet entre votre routeur domestique et le port WAN du routeur GL.iNet, il se peut que vous voyiez parfois ce message :

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Cela se produit parce que votre routeur domestique utilise la même adresse IP LAN que le routeur GL.iNet ; on parle alors de conflit LAN.

Suivez les étapes ci-dessous pour modifier le sous-réseau LAN.

## 1. Modifier le sous-réseau LAN

Veuillez cliquer sur le lien **Change LAN Subnet** ; vous serez redirigé vers la page de configuration **LAN**.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Remplacez le nombre après le deuxième point (qui est **8** par défaut) par un autre nombre. Par exemple, 192.168.10.1, puis cliquez sur **Apply**.

Après la modification, attendez quelques secondes. La page sera actualisée et redirigée automatiquement vers la nouvelle adresse IP **192.168.10.1**. Vous verrez alors que l'avertissement de conflit de sous-réseau a disparu.

Si la page n'est pas redirigée, passez à l'étape suivante.

## 2. Se connecter avec la nouvelle IP LAN

Saisissez manuellement l'adresse IP LAN modifiée dans la barre d'adresse, puis appuyez sur Entrée.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Connectez-vous avec votre mot de passe administrateur et l'avertissement de conflit de sous-réseau disparaîtra.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
