# Comment mettre à jour les certificats du serveur OpenVPN ?

Ce tutoriel explique comment mettre à jour les certificats du serveur OpenVPN sur vos routeurs GL.iNet.

**Remarque** : ce processus nécessite la mise à jour du certificat Root CA, ce qui invalidera tous les certificats clients existants (intégrés dans les fichiers de configuration). Vous devez réexporter tous les fichiers de configuration pour que vos clients OpenVPN puissent se reconnecter au serveur.

1. Connectez-vous au panneau d'administration Web de votre routeur, puis accédez à **VPN** -> **OpenVPN Server**.

    Si votre serveur OpenVPN est en cours d'exécution, arrêtez le service.
    
2. Sous l'onglet Configuration, cliquez sur **Advanced Configuration** pour déplier les paramètres.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Recherchez **Server Root Certificate** et supprimez tout le contenu de la zone de texte.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Le **Server Certificate** et le **Server Key** associés seront également supprimés automatiquement, comme indiqué ci-dessous.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Laissez les trois zones vides, puis cliquez sur **Apply** en bas de la page. De nouveaux certificats seront automatiquement générés et rempliront les zones.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. Les certificats du serveur OpenVPN sont maintenant mis à jour. Cliquez sur **Export Client Configuration** en bas pour exporter de nouveaux fichiers de configuration permettant à vos appareils de se connecter.

---

Vous avez encore des questions ? Visitez notre [Forum Communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
