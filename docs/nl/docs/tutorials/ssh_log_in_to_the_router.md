# Via SSH aanmelden bij de router {#ssh-log-in-to-the-router}

Secure Shell (SSH) is een cryptografisch netwerkprotocol waarmee netwerkservices veilig via een onbeveiligd netwerk kunnen worden uitgevoerd. Een bekend toepassingsvoorbeeld is dat gebruikers zich op afstand bij computersystemen aanmelden. Soms heb je basishulpprogramma's nodig om via SSH verbinding te maken met de server. In deze handleiding lees je hoe je je via SSH aanmeldt bij GL.iNet-routers.

---

## Voor Windows-gebruikers {#for-windows-user}

Je kunt in Windows op verschillende manieren de terminal van de router openen, waaronder via Windows-opdrachtprompt, PowerShell, Bitvise of PuTTY.

### Windows-opdrachtprompt gebruiken {#using-windows-cmd}

1. Open de opdrachtprompt.

    Druk op **Win** + **R** (Windows-toets + R) om het venster Uitvoeren te openen. Typ **cmd** en druk op Enter.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Er wordt een zwart opdrachtpromptvenster geopend.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Meld je aan bij de router.

    Typ `ssh root@192.168.8.1` in het opdrachtpromptvenster en druk op Enter.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Opmerking**: 192.168.8.1 is het standaard-IP-adres van de router. Gebruik je aangepaste IP-adres als je dit eerder hebt gewijzigd.

    Typ vervolgens het beheerderswachtwoord van je router en druk op Enter. **Uit veiligheidsoverwegingen wordt het wachtwoord niet op het scherm weergegeven**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Als het wachtwoord juist is, word je bij je router aangemeld.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Problemen oplossen"

    1. **Fout: Connection timed out**

        Zorg dat je apparaat, bijvoorbeeld je laptop, met de router is verbonden. Maak opnieuw verbinding met het Wi-Fi-netwerk of de LAN-poort van de router en probeer het opnieuw.

    2. **Fout: Permission denied**

        Controleer of je het juiste beheerderswachtwoord invoert. Als je het wachtwoord bent vergeten, stel je de router opnieuw in door de RESET-knop 10 seconden ingedrukt te houden.

### PowerShell gebruiken {#using-powershell}

1. Open Windows PowerShell.

    Klik op het zoekpictogram op de taakbalk, typ **PowerShell**, selecteer **Windows PowerShell** en **voer dit uit als beheerder**.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Meld je aan bij de router.

    Typ `ssh root@192.168.8.1` in het PowerShell-venster en druk op Enter.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Opmerking**: 192.168.8.1 is het standaard-IP-adres van de router. Gebruik je aangepaste IP-adres als je dit eerder hebt gewijzigd.

    Het systeem vraagt je om de verbinding te bevestigen. Typ `yes` en druk op Enter.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Je wordt gevraagd het beheerderswachtwoord van de router in te voeren. Voer het juiste beheerderswachtwoord in en druk op Enter. **Uit veiligheidsoverwegingen wordt het wachtwoord niet op het scherm weergegeven**.

    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

    Je wordt vervolgens bij de terminal van je router aangemeld.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Problemen oplossen"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Dit gebeurt als de beveiligingssleutel van de router is gewijzigd, bijvoorbeeld na het herstellen van de fabrieksinstellingen of een firmware-update. Het kan ook gebeuren als je eerder verbinding hebt gemaakt met een andere router, waardoor de controle van de hostsleutel mislukt.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Open Verkenner, ga naar `C:\Users\Administrator\.ssh` en zoek het bestand **known_hosts** om dit op te lossen.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Dubbelklik op het bestand known_hosts en open het met Kladblok.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Verwijder de vermelding voor het IP-adres van de router, bijvoorbeeld 192.168.8.1, en sla het bestand op. Sluit Verkenner.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Gebruik in PowerShell opnieuw de opdracht `ssh root@192.168.8.1` om verbinding te maken met de router. Je wordt gevraagd de verbinding te bevestigen. Typ `yes`, druk op Enter en voer vervolgens het aanmeldwachtwoord van de router in. Je wordt nu bij de terminal van je router aangemeld.

    2. **Wat moet ik doen als ik de SSH-poort van de router heb gewijzigd?**

        Als je de SSH-poort van de router hebt gewijzigd, geef je de poort bij de ssh-opdracht op met de parameter "-p". Bijvoorbeeld:

        ``ssh -p [new port number] [username]@[router IP address]``

### Bitvise gebruiken {#using-bitvise}

Bekijk deze video om je via Bitvise bij je router aan te melden.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### PuTTY gebruiken {#using-putty}

1. Download PuTTY.

    Download [hier](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"} de nieuwste versie van PuTTY.

2. Installeer PuTTY.

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Start PuTTY.

    Klik in het menu Start op **PuTTY**.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    Het volgende configuratievenster wordt weergegeven.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Voer bij Host Name (or IP address) `192.168.8.1` in, behoud voor Port de standaardwaarde `22` en selecteer `SSH` als verbindingstype.

    Voer bij saved sessions `Your Session` in en klik op `Save` om de instellingen op te slaan.

    Klik vervolgens onderaan op `Open`.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    Er verschijnt een beveiligingswaarschuwing zoals hieronder. Klik op `Yes`.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Voer vervolgens je beheerderswachtwoord in. **Uit veiligheidsoverwegingen wordt het wachtwoord niet op het scherm weergegeven**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    Wanneer het bovenstaande scherm verschijnt, ben je via SSH bij de router aangemeld.

---

## Voor Linux-/Mac-gebruikers {#for-linuxmac-user}

Het proces is in Linux en Mac OS doorgaans hetzelfde. Hieronder gebruiken we Ubuntu als voorbeeld.

### Ubuntu gebruiken {#using-ubuntu}

1. Start Terminal.

    Start Ubuntu. Dubbelklik op het pictogram Terminal om Terminal te openen.

    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Meld je aan bij de router.

    Voer de SSH-aanmeldopdracht in: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    Het systeem vraagt je om de verbinding te bevestigen. Typ "yes" en druk op Enter.

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Voer vervolgens het beheerderswachtwoord van je router in. **Uit veiligheidsoverwegingen wordt het wachtwoord niet op het scherm weergegeven**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    Wanneer het bovenstaande scherm verschijnt, ben je bij de router aangemeld.

??? "Problemen oplossen"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Dit gebeurt als de beveiligingssleutel van de router is gewijzigd, bijvoorbeeld na het herstellen van de fabrieksinstellingen of een firmware-update. Het kan ook gebeuren als je eerder verbinding hebt gemaakt met een andere router, waardoor de controle van de hostsleutel mislukt.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Voer in dit geval de opdracht uit die hierboven in het rode kader staat. Kopieer de exacte opdracht die in je terminal wordt weergegeven.

        `ssh-keygen -f ~/.ssh/known_hosts -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Probeer vervolgens opnieuw verbinding te maken.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**

        Deze fout kan optreden wanneer je verbinding maakt. De fout wordt veroorzaakt door een wijziging in het Openssh-pakket vanaf versie 8.8. Open het bestand **~/.ssh/config** met een teksteditor, zoals Nano of Vim, en voeg de volgende regels toe:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Wijzig het host-IP-adres als dit niet meer het standaardadres is.

        Raadpleeg [deze discussie](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"} voor meer informatie over dit probleem.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
