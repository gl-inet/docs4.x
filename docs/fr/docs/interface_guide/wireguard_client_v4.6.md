# Configurer le client WireGuard sur les routeurs GL.iNet (firmware v4.6 et antérieur)

**Remarque** : ce guide s'applique au firmware v4.6 et aux versions antérieures. Pour les versions plus récentes, veuillez consulter [cette page](wireguard_client.md).

---

WireGuard® est un VPN extrêmement simple, rapide et moderne qui utilise une cryptographie de pointe. Il vise à être plus rapide, plus simple, plus léger et plus pratique qu'IPsec, tout en évitant sa complexité. Il offre également de meilleures performances qu'OpenVPN.

Si vous avez déjà souscrit un service WireGuard auprès d'un fournisseur mais que vous ne savez pas comment obtenir les fichiers de configuration, consultez [ce guide](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) ou contactez l'assistance de votre fournisseur.

Vous pouvez configurer le client WireGuard via le panneau d'administration web ou l'[application mobile](../faq/mobile_app.md).

- L'application mobile intègre plusieurs fournisseurs de services WireGuard, comme AzireVPN, Mullvad, OVPN, StrongVPN et PIA VPN.

- Le panneau d'administration web prend en charge moins de fournisseurs WireGuard (par ex. AzireVPN et Mullvad), mais propose des pages plus détaillées et plus intuitives.

Voici les étapes de configuration via le panneau d'administration web.

---

Connectez-vous au panneau d'administration web et accédez à **VPN** -> **WireGuard Client**.

Si vous disposez d'un abonnement **AzireVPN** ou **Mullvad**, vous pouvez vous connecter directement avec vos identifiants. Sinon, cliquez sur **Add Manually** pour téléverser les profils WireGuard manuellement.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Configurer AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} est un service VPN axé sur la confidentialité, qui fournit des tunnels sûrs, modernes et robustes comme WireGuard.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Saisissez **Username** et **Password**, puis cliquez sur **Save Credentials & Get Servers**. Le système générera des fichiers de configuration pour chaque serveur.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Accédez à VPN Dashboard pour activer la connexion.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Une fois connecté, vous verrez votre adresse IP utilisateur ainsi que le nombre d'octets envoyés/reçus.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Mettre à jour les serveurs

    AzireVPN peut mettre certains serveurs en maintenance ou les arrêter, ce qui peut provoquer des échecs de connexion. Vous pouvez cliquer sur **Update Servers** pour récupérer la liste des serveurs actuellement disponibles.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Modifier les identifiants

    Cliquez sur l'icône d'engrenage pour modifier les identifiants.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Configurer Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} est un service VPN qui aide à préserver la confidentialité de votre activité en ligne, de votre identité et de votre localisation.

Le firmware 4.x intègre le service Mullvad WireGuard.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Saisissez **Account**, puis cliquez sur **Save Credentials & Get Servers**.

    Le numéro de compte Mullvad est un nombre décimal à 16 chiffres compris entre `1000 0000 0000 0000` et `9999 9999 9999 9999`.

    Une boîte de dialogue s'affichera pour sélectionner un emplacement.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Le système générera ensuite les fichiers de configuration pour les serveurs de l'emplacement sélectionné.

    La **Public Key** est la clé publique WireGuard à envoyer au serveur Mullvad. Vous pouvez avoir jusqu'à cinq clés simultanément et les gérer sur la [page Mullvad](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Accédez à VPN Dashboard pour activer la connexion.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Une fois connecté, vous verrez votre adresse IP utilisateur ainsi que le nombre d'octets envoyés/reçus.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Mettre à jour les serveurs

    Mullvad peut mettre certains serveurs en maintenance ou les arrêter, ce qui peut provoquer des échecs de connexion. Vous pouvez cliquer sur **Update Servers** pour récupérer la liste des serveurs actuellement disponibles.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Modifier les identifiants

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Supprimer les informations du compte

    Si vous cliquez sur **Delete**, cela supprimera de votre routeur les identifiants du compte, la clé privée, la clé publique et les fichiers de configuration.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Supprimer

    Permet de supprimer tous les fichiers de configuration en un clic et propose également de supprimer la clé privée et la clé publique.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Configurer le client WireGuard

Depuis le firmware 4.0, les profils WireGuard peuvent être gérés par groupes.

1. Cliquez sur **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Le système créera un groupe.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Donnez au groupe un nom explicite, par exemple `azirevpn`. Vous pourrez ensuite téléverser des fichiers de configuration ou ajouter manuellement une configuration.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Téléverser des fichiers de configuration**

        Téléversez votre fichier de configuration WireGuard, puis cliquez sur **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration** : à utiliser si vous souhaitez coller la configuration WireGuard ou renseigner chaque champ.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Donnez un nom explicite et collez la configuration, puis cliquez sur **Apply** pour continuer.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Vous pouvez aussi ajouter la configuration en remplissant chaque champ, en cliquant sur **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Cliquez sur l'icône à trois points pour démarrer, modifier ou supprimer le profil.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Vérifiez l'état de la connexion sur la page [VPN Dashboard](vpn_dashboard_v4.7.md).

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® est une marque déposée de Jason A. Donenfeld.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
