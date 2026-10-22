# Logga in på routern via SSH {#ssh-log-in-to-the-router}

Secure Shell (SSH) är ett kryptografiskt nätverksprotokoll för säker användning av nätverkstjänster över ett osäkert nätverk. Det vanligaste användningsområdet är fjärrinloggning på datorsystem. Ibland behöver du grundläggande verktyg för att ansluta till en server via SSH. Den här guiden beskriver hur du loggar in på GL.iNet-routrar via SSH.

---

## För Windows-användare {#for-windows-user}

I Windows kan du öppna routerns terminal via bland annat Kommandotolken, PowerShell, Bitvise eller PuTTY.

### Använda Kommandotolken i Windows {#using-windows-cmd}

1. Öppna Kommandotolken

    Tryck på **Win** + **R** (Windows-tangenten + R) för att öppna dialogrutan Kör. Skriv **cmd** och tryck på Enter.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Ett svart kommandotolksfönster öppnas.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Logga in på routern

    Skriv `ssh root@192.168.8.1` i kommandotolken och tryck på Enter.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Obs!** `192.168.8.1` är routerns standard-IP-adress. Om du har ändrat den använder du din anpassade IP-adress.

    Ange sedan routerns administratörslösenord och tryck på Enter. **Av säkerhetsskäl visas inte lösenordet på skärmen**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Om lösenordet är korrekt loggas du in på routern.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Felsökning"

    1. **Fel: Connection timed out**

        Kontrollera att enheten, till exempel en bärbar dator, är ansluten till routern. Anslut igen till routerns Wi-Fi eller LAN-port och försök på nytt.

    2. **Fel: Permission denied**

        Kontrollera att du anger rätt administratörslösenord. Om du har glömt lösenordet återställer du routern genom att hålla RESET-knappen intryckt i 10 sekunder.

### Använda PowerShell {#using-powershell}

1. Öppna Windows PowerShell

    Klicka på sökikonen i aktivitetsfältet, skriv **PowerShell**, välj **Windows PowerShell** och **kör programmet som administratör**.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Logga in på routern

    Skriv `ssh root@192.168.8.1` i PowerShell-fönstret och tryck på Enter.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Obs!** `192.168.8.1` är routerns standard-IP-adress. Om du har ändrat den använder du din anpassade IP-adress.

    Systemet ber dig bekräfta anslutningen. Skriv `yes` och tryck på Enter.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Du uppmanas att ange routerns administratörslösenord. Ange rätt lösenord och tryck på Enter. **Av säkerhetsskäl visas inte lösenordet på skärmen**.

    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

    Du loggas sedan in på routerns terminal.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Felsökning"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Detta inträffar om routerns säkerhetsnyckel har ändrats, till exempel efter en fabriksåterställning eller firmwareuppdatering, eller om du tidigare har anslutit till en annan router så att verifieringen av värdnyckeln misslyckas.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Åtgärda problemet genom att öppna Utforskaren, gå till `C:\Users\Administrator\.ssh` och leta reda på filen **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Dubbelklicka på filen known_hosts och öppna den med Anteckningar.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Ta bort posten som hör till routerns IP-adress, till exempel 192.168.8.1, och spara filen. Stäng Utforskaren.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Gå tillbaka till PowerShell och anslut till routern igen med kommandot `ssh root@192.168.8.1`. Du uppmanas att bekräfta anslutningen. Skriv `yes`, tryck på Enter och ange sedan routerns inloggningslösenord. Därefter loggas du in på routerns terminal.

    2. **Vad gör jag om jag har ändrat routerns SSH-port?**

        Om du har ändrat routerns SSH-port anger du porten med parametern "-p" när du använder ssh-kommandot. Exempel:

        ``ssh -p [nytt portnummer] [användarnamn]@[routerns IP-adress]``

### Använda Bitvise {#using-bitvise}

Titta på videon för att logga in på routern via Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Använda PuTTY {#using-putty}

1. Hämta PuTTY

    Hämta den senaste versionen av PuTTY [här](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Installera PuTTY

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Starta PuTTY

    Klicka på **PuTTY** i Start-menyn.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    Följande konfigurationsfönster visas.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Ange `192.168.8.1` i Host Name (or IP address), behåll standardporten `22` och välj anslutningstypen `SSH`.

    Ange `Your Session` under saved sessions och välj `Save` för att spara inställningarna.

    Klicka sedan på `Open` längst ned.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    En säkerhetsvarning visas. Klicka på `Yes`.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Ange sedan administratörslösenordet. **Av säkerhetsskäl visas inte lösenordet på skärmen**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    När bilden ovan visas är du inloggad på routern via SSH.

---

## För Linux- och Mac-användare {#for-linuxmac-user}

Processen är i stort sett densamma i Linux och Mac OS. Nedan används Ubuntu som exempel.

### Använda Ubuntu {#using-ubuntu}

1. Starta Terminal.

    Starta Ubuntu. Dubbelklicka på Terminal-ikonen för att öppna Terminal.

    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Logga in på routern.

    Ange SSH-inloggningskommandot: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    Systemet ber dig bekräfta anslutningen. Skriv "yes" och tryck på Enter.

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Ange sedan routerns administratörslösenord. **Av säkerhetsskäl visas inte lösenordet på skärmen**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    När bilden ovan visas är du inloggad på routern.

??? "Felsökning"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Detta inträffar om routerns säkerhetsnyckel har ändrats, till exempel efter en fabriksåterställning eller firmwareuppdatering, eller om du tidigare har anslutit till en annan router så att verifieringen av värdnyckeln misslyckas.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Om detta inträffar kör du kommandot i den röda rutan ovan. Kopiera exakt det kommando som visas i terminalen.

        `ssh-keygen -f ~/.ssh/known_hosts -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Försök sedan ansluta igen.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**

        Det här felet kan visas när du ansluter. Det beror på en ändring i OpenSSH-paketet från version 8.8. Åtgärda det genom att öppna filen **~/.ssh/config** i en textredigerare, till exempel Nano eller Vim, och lägga till följande rader:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Ändra värdens IP-adress om routern inte använder standardadressen.

        Mer information om problemet finns [här](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
