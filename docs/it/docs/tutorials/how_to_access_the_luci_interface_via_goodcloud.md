# Come accedere all'interfaccia LuCI tramite GoodCloud

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} supera i limiti geografici e offre un modo pratico per la gestione remota del router. Tramite GoodCloud puoi accedere all'interfaccia LuCI del router in qualsiasi momento e ovunque, eseguire varie impostazioni sul router e gestire facilmente la rete.

## Preparazione

- Hardware: un router GL.iNet gia' configurato per l'accesso a Internet e funzionante correttamente.
- Ambiente di rete: la rete a cui il router e' connesso deve essere stabile e avere normale accesso a Internet.
- Associazione del dispositivo: devi [associare il router GL.iNet al tuo account GoodCloud](../interface_guide/cloud.md/#setup-your-goodcloud-account). Se non hai un account GoodCloud, [registrane](https://www.goodcloud.xyz/){target="_blank"} uno.

## Passaggi per accedere all'interfaccia LuCI tramite GoodCloud

### Per firmware versione 4.7 o successiva

Dalla versione v4.7, gli utenti possono accedere direttamente alla pagina LuCI dalla piattaforma GoodCloud senza passare dal pannello di amministrazione web del router.

1. Accedi al tuo account GoodCloud [qui](https://www.goodcloud.xyz/){target="_blank"}.

2. Sul lato sinistro vai su **Devices** -> **Bound Devices**. Fai clic sul nome del dispositivo a cui vuoi accedere e vedrai le icone di Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    Nella finestra pop-up verra' mostrata la porta 80. Cambia la porta in **8080** e fai clic su Apply.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Verrai reindirizzato alla pagina di login di LuCI. Inserisci la password amministratore per accedere.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. Hai effettuato correttamente l'accesso a LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### Per firmware versione 4.6 o precedente

1. Accedi al tuo account GoodCloud [qui](https://www.goodcloud.xyz/){target="_blank"}.

2. Sul lato sinistro vai su **Devices** -> **Bound Devices**. Fai clic sul nome del dispositivo a cui vuoi accedere e vedrai le icone di Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    Nella finestra pop-up verra' mostrata la porta 80; fai clic su Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Verrai quindi reindirizzato alla pagina di login del pannello di amministrazione GL.iNet. Inserisci la password amministratore per accedere.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. Dopo il login, sul lato sinistro vai su SYSTEM -> Advanced Settings e fai clic sul collegamento per andare all'interfaccia LuCI.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Verrai reindirizzato alla pagina di login di LuCI. Inserisci la stessa password amministratore per accedere.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. Hai effettuato correttamente l'accesso a LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
