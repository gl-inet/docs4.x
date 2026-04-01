# Utiliser WinSCP pour accéder à vos fichiers partagés

Vous pouvez utiliser **WinSCP** pour accéder à vos fichiers partagés avec la fonction de partage de fichiers des routeurs **GL.iNet**.

Veuillez configurer vos liens **WebDAV** dans l'onglet de stockage réseau. Pour des détails de configuration, veuillez consulter la page [WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav).

## Configurer les liens dans WinSCP

Après avoir configuré WebDAV, vous pouvez revenir à la page **Share Folders** du stockage réseau.

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Faites un clic droit sur l'icône **"..."** et copiez le lien HTTPS.

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Lancez WinSCP et sélectionnez WebDAV, ainsi que le chiffrement TLS/SSL. Collez ensuite le lien dans le champ **Host name** ; le numéro de port passera automatiquement à 6008.

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Saisissez votre nom d'utilisateur et votre mot de passe, puis cliquez sur Save et Login ; le dossier partagé s'ouvrira.

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
