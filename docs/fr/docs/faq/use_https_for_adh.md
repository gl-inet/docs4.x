# Accéder au routeur GL.iNet et à AdGuard Home via HTTPS

Si vous souhaitez utiliser HTTPS pour accéder au routeur GL.iNet et à AdGuard Home, suivez les étapes ci-dessous.

## 1. Mettre à jour le certificat et la clé sur le routeur GL.iNet

Commencez par obtenir un certificat SSL ou utilisez un certificat SSL auto-signé.

Ensuite, connectez-vous en SSH à votre routeur GL.iNet ou utilisez WinSCP pour y téléverser le certificat et la clé mis à jour. Les chemins sont les suivants :

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Activer AdGuard Home

Connectez-vous au panneau d'administration web GL.iNet, puis allez dans **APPLICATIONS** -> **AdGuard Home** et activez AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Cliquez ensuite sur **Settings Page** en haut de cette page ; vous serez redirigé vers la page de paramètres d'AdGuard Home.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Modifier les paramètres de chiffrement

Dans la page de paramètres d'AdGuard Home, allez dans Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Cochez la case **Enable Encryption** en haut à gauche, puis saisissez **3001** pour le port HTTPS.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Ajoutez les chemins du certificat et de la clé mis à jour, puis cliquez sur **Save**.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Vous pourrez ensuite accéder en HTTPS à **192.168.8.1** ou **192.168.8.1:3001**.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
