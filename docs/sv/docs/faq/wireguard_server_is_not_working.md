# Vad gör jag om WireGuard-servern inte fungerar korrekt? {#what-should-i-do-if-the-wireguard-server-is-not-working-properly}

Det finns flera möjliga orsaker till att WireGuard-servern på GL.iNet-routern inte fungerar korrekt.

Följ felsökningsstegen nedan för ditt specifika problem.

## Situation 1. WireGuard-servern startar men går inte att ansluta till {#situation-1-the-wireguard-server-is-starting-but-cant-be-connected}

??? "Följ dessa steg"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    Portvidarebefordran som har konfigurerats på den primära routern, som är ansluten till den sekundära routern (GL.iNet), kanske inte fungerar korrekt.
    Kontrollera portvidarebefordran genom att försöka vidarebefordra den primära routerns HTTPS-port till WireGuard-servern. Följ dessa steg:

    1. Vidarebefordra den primära routerns HTTPS-port till WireGuard-servern

        1. Logga in på den primära routerns administrationspanel.
        2. Öppna sidan för portvidarebefordran.
        3. Skapa en ny port och ge den namnet **HTTPS**.
        4. Ange följande information:
            * **External port/Internal port:** Ange **443**.
            * **Protocol:** Välj **All** eller **UDP/TCP**.
            * **Internal IP** (kan även visas som **Host IP**): Ange den sekundära routerns WAN-IP-adress eller välj den sekundära routern i listrutan om den är tillgänglig.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. Aktivera DDNS och fjärråtkomst via HTTPS (på GL.iNet-routern)

        1. Ange webbadressen till GL.iNet-routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
        2. Klicka på **Applications** > **Dynamic DNS** i det vänstra sidofältet.
        3. Aktivera **Enable DDNS** och markera rutan **I have read and agree to the Terms of Service & Privacy Policy**.
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Spara värdnamnet eftersom du behöver det senare och klicka sedan på **Apply**.
        5. Klicka på **System** > **Security** i det vänstra sidofältet.
        6. Aktivera **HTTPS Remote Access** under **Remote Access Control**.
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Klicka på **Apply**.

    3. Kontrollera om du kan öppna GL.iNet-routerns administrationspanel

        1. Anslut en annan enhet (t.ex. en bärbar dator eller mobil enhet) till ett annat Wi-Fi-nätverk eller mobilnätet.
        2. Ange värdnamnet som du sparade tidigare (abcd123.glddns.com) i webbläsarens adressfält.
        3. Klicka på **Advanced**.
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Klicka på **Proceed to abcd123.glddns.com(unsafe)**.
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Om inloggningssidan för GL.iNet-routern (den sekundära routern) visas fungerar portvidarebefordran som du konfigurerade på den primära routern korrekt.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Om inloggningssidan för GL.iNet-routern (den sekundära routern) inte visas fungerar portvidarebefordran inte korrekt. Konfigurera portvidarebefordran igen eller använd en router med fungerande portvidarebefordran som primär router.

## Situation 2. WireGuard-servern visar en ansluten klient men VPN-klienten kommer inte åt internet {#situation-2-the-wireguard-server-shows-connected-client-but-the-vpn-client-cannot-access-the-internet}

??? "Följ dessa steg"

    Följ stegen för varje möjlig orsak nedan och kontrollera om problemet har lösts. Om problemet har lösts kan du hoppa över resten av avsnittet.

    **Möjlig orsak 1: Din internetleverantör kanske inte kan slå upp GL.iNets DNS-servrar**

    Försök konfigurera DNS-serveradresserna manuellt genom att följa dessa steg:

    1. Ange webbadressen till GL.iNet-routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
    2. Klicka på **Network** > **DNS** i det vänstra sidofältet.
    3. Välj **Manual DNS** för **Mode**.
    4. Välj **Google Public DNS** för **DNS Server 1**.
    5. Klicka på **Apply**.

    **Möjlig orsak 2: Den primära routerns gateway-IP-adress är i konflikt med WireGuard-serverns IP-adress**

    Försök ändra IPv4-adressen genom att följa dessa steg:

    1. Ange webbadressen till GL.iNet-routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
    2. Klicka på **VPN** > **WireGuard Server** i det vänstra sidofältet.
    3. Ange en ny IP-adress (t.ex. 10.1.0.1/24) i fältet **IPv4 Address** på fliken **Configuration**.
    4. Klicka på **Apply**.

    **Möjlig orsak 3: Om både WireGuard-servern och WireGuard-klienten har konfigurerats på GL.iNet-routrar är deras LAN-IP-adresser i konflikt**

    Försök ändra LAN-IP-adressen på någon av routrarna genom att följa dessa steg:

    1. Logga in på administrationspanelen för någon av GL.iNet-routrarna (t.ex. 192.168.8.1) i en webbläsare.
    2. Klicka på **Network** > **LAN** i det vänstra sidofältet.
    3. Ange en ny LAN-IP-adress (t.ex. 192.168.10.1) i fältet **Router IP address**.
    4. Klicka på **Apply**.

    **Möjlig orsak 4: WireGuard-serverns IP-adress har uppdaterats men subnätet saknas**

    Lägg till ett subnät i WireGuard-serverns IP-adress genom att följa dessa steg:

    1. Ange webbadressen till GL.iNet-routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
    2. Klicka på **VPN** > **WireGuard Server** i det vänstra sidofältet.
    3. Lägg till **/24** efter **10.0.0.1** i fältet **IPv4 Address** på fliken **Configuration**.
    4. Klicka på **Apply**.

## Situation 3. WireGuard-servern körs men VPN-klienten kan inte ansluta till den {#situation-3-the-wireguard-server-is-running-but-vpn-client-cannot-connect-to-it}

??? "Följ dessa steg"

    Följ stegen för varje möjlig orsak nedan och kontrollera om problemet har lösts. Om problemet har lösts kan du hoppa över resten av avsnittet.

    **Möjlig orsak 1: Portvidarebefordran som har konfigurerats på den primära routern kanske inte fungerar korrekt**

    Kontrollera portvidarebefordran genom att försöka vidarebefordra HTTPS-porten till WireGuard-servern enligt lösningsstegen i situation 1.

    **Möjlig orsak 2: Du kanske inte har en offentlig IP-adress**

    Kontrollera det genom att följa [den här sidan](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    **Möjlig orsak 3: Om både WireGuard-servern och WireGuard-klienten har konfigurerats på GL.iNet-routrar är deras LAN-IP-adresser i konflikt**

    Ändra LAN-IP-adressen på någon av routrarna genom att följa dessa steg:

    1. Logga in på administrationspanelen för någon av GL.iNet-routrarna (t.ex. 192.168.8.1) i en webbläsare.
    2. Klicka på **Network** > **LAN** i det vänstra sidofältet.
    3. Ange en ny LAN-IP-adress (t.ex. 192.168.10.1) i fältet **Router IP address**.
    4. Klicka på **Apply**.

    **Möjlig orsak 4: Enheten som används för att ansluta till WireGuard-servern är ansluten till dess Wi-Fi-nätverk eller LAN-port**

    Anslut enheten till ett annat Wi-Fi-nätverk eller mobilnätet.

    **Möjlig orsak 5: Vissa rader kan saknas i konfigurationsfilen som du laddade upp till klientenheten**

    Ladda upp konfigurationsinformationen igen.

## Situation 4. WireGuard-servern är ansluten men anslutningen är instabil {#situation-4-the-wireguard-server-is-connected-but-the-connection-is-not-stable}

??? "Följ dessa steg"

    Följ stegen nedan för att lösa problemet. Kontrollera efter varje steg om problemet har lösts. Om problemet har lösts kan du hoppa över återstående steg.

    1. Ändra MTU från **1420** till ett lägre värde (t.ex. 1380) på VPN-klientenheten.
    2. Aktivera funktionen för VPN-genomströmning på den primära routern om den finns.
    3. Försök konfigurera DNS-servrar manuellt på GL.iNet-routern genom att följa dessa steg:
        1. Ange webbadressen till GL.iNet-routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
        2. Klicka på **Network** > **DNS** i det vänstra sidofältet.
        3. Välj **Manual DNS** för Mode.
        4. Välj **Google Public DNS** för **DNS Server 1**.
        5. Klicka på **Apply**.

## Situation 5. WireGuard-servern slutade plötsligt att fungera {#situation-5-the-wireguard-server-suddenly-stopped-working}

??? "Följ dessa steg"

    Följ stegen för varje möjlig orsak nedan och kontrollera om problemet har lösts. Om problemet har lösts kan du hoppa över resten av avsnittet.

    **Möjlig orsak 1: Det kan vara strömavbrott där WireGuard-servern är installerad**

    Kontrollera om WireGuard-servern fortfarande är ansluten genom att följa lösningsstegen i situation 1 eller via [GoodCloud](../interface_guide/cloud.md) (om routern tidigare har anslutits till tjänsten).

    **Möjlig orsak 2: Dynamic DNS (DDNS) har inte aktiverats**

    Om du har en dynamisk IP-adress, vilket är mest sannolikt, måste du aktivera DDNS. [Aktivera DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) och följ sedan återstående steg för att konfigurera WireGuard-servern igen.

    **Möjlig orsak 3: Portvidarebefordran slutade fungera av okänd anledning**

    [Konfigurera portvidarebefordran](../tutorials/how_to_set_up_port_forwarding.md) igen med en annan port.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
