# Konfigurera en OpenVPN-server på GL.iNet-routrar {#how-to-set-up-openvpn-server-on-glinet-routers}

Den här guiden visar hur du konfigurerar en OpenVPN-server på GL.iNet-routrar. Med en VPN-server kan du upprätta en säker fjärranslutning till nätverket hemma eller på kontoret. På en GL.iNet-router kan du konfigurera en OpenVPN-server på några minuter.

!!! note "Kontrollera följande krav innan du börjar"

    **Offentlig IP-adress**

    En offentlig IP-adress krävs för att konfigurera en OpenVPN-server. Följ [den här länken](how_to_check_if_isp_assigns_you_a_public_ip_address.md) för att kontrollera om du har en.

    **Portvidarebefordran**

    Om GL.iNet-routern är ansluten bakom en primär router [konfigurerar du portvidarebefordran på den primära routern](how_to_set_up_port_forwarding.md).

## 1. Logga in på routern {#1-log-in-to-your-router}

Öppna en webbläsare och gå till routerns webbadministrationspanel (standard-IP: 192.168.8.1). Logga in med administratörslösenordet.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Aktivera Dynamic DNS (valfritt) {#2-enable-dynamic-dns-optional}

En OpenVPN-server kräver vanligtvis en **statisk offentlig IP-adress**, som ger andra enheter en fast slutpunkt för åtkomst till VPN-servern.

Om du i stället har en dynamisk offentlig IP-adress kan du behöva aktivera **Dynamic DNS (DDNS)** på GL.iNet-routern. Då kan anslutningen till OpenVPN-servern behållas även när den offentliga IP-adressen ändras dynamiskt.

Följ stegen nedan för att aktivera Dynamic DNS.

1. Gå till **APPLICATIONS** > **Dynamic DNS** i routerns webbadministrationspanel.
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Aktivera **Enable DDNS**, läs och godkänn **Terms of Service & Privacy Policy** och klicka sedan på **Apply**.
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Ladda ned konfigurationsfilen {#3-download-configuration-file}

1. Gå till **VPN** > **OpenVPN Server** i routerns webbadministrationspanel.
2. Klicka på **Generate Configuration**.
3. Behåll standardinställningarna och klicka sedan på **Export Client Configuration**.
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. Aktivera **Use DDNS Domain** i dialogrutan om du tidigare har konfigurerat **Dynamic DNS**.
5. Klicka på **Download** och spara filen.
6. Klicka på **Start** högst upp på sidan **OpenVPN Server**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Valfritt) Aktivera följande inställningar för åtkomst till VPN-serverns lokala nätverk:"

    För firmware v4.7 och tidigare:

    1. Klicka på **VPN** > **VPN Dashboard** i det vänstra sidofältet.
    2. Klicka på ikonen Options.
    3. Aktivera **Remote Access LAN**.
    4. Klicka på **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    För firmware v4.8 och senare:

    1. Klicka på **VPN** > **OpenVPN Server** i det vänstra sidofältet.
    2. Klicka på **Options** i det övre högra hörnet.
    3. Aktivera **Allow Remote Access the LAN Subnet**.
    4. Klicka på **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

## 4. Anslut till OpenVPN-servern {#4-connect-to-openvpn-server}

Du behöver en OpenVPN-klient för att ansluta till OpenVPN-servern. Konfigurera den med någon av följande metoder:

??? "Metod 1: En OpenVPN-klientapp från tredje part (använd metoden om du saknar en extra router som kan konfigureras som OpenVPN-klient)"

    I guiden används OpenVPN Connect, den officiella appen från OpenVPN Inc, som exempel.

    1. Anslut en annan enhet till ett annat Wi-Fi-nätverk (eller till mobilnätet om du använder en mobil enhet).
    2. Skicka konfigurationsfilen som du hämtade tidigare till enheten, till exempel via e-post, och ladda sedan ned filen på enheten.
    3. Ladda ned OpenVPN Connect för enhetens operativsystem:
        * [Windows](https://openvpn.net/client/)
        * [Mac](https://openvpn.net/client/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/client/)
    4. Läs villkoren i appen och välj sedan **Agree**.
    5. Välj **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Välj **Browse** och sedan konfigurationsfilen som du laddade ned tidigare.
    7. Välj **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Välj **Connect** > **OK** > **Allow**.

    Ordet "Connected" visas högst upp i VPN-profilen.
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Metod 2: En router som kan konfigureras som OpenVPN-klient"

    Du kan använda valfri router som stöder manuell konfiguration av en OpenVPN-klient. I guiden används GL.iNets reserouter [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) som exempel.

    1. Anslut en annan enhet till ett annat Wi-Fi-nätverk (eller till mobilnätet om du använder en mobil enhet).
    2. Ange webbadressen till routerns administrationspanel (t.ex. 192.168.8.1) i webbläsarens adressfält.
    3. Ange lösenordet och klicka sedan på **Login**.
    4. Klicka på **VPN** > **OpenVPN Client** i det vänstra sidofältet.
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Klicka på **Add Manually**.
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Ange ett namn i fältet och klicka sedan på bockikonen.
    7. Ladda upp konfigurationsfilen som du hämtade tidigare.
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Klicka på **Apply**.
    9. Klicka på ikonen med tre punkter och sedan på **Start**.
    10. Anslut en enhet till routern som kör OpenVPN-klienten.

## 5. Verifiera VPN-anslutningen {#5-verify-vpn-connection}

Öppna en webbläsare och sök efter din IP-adress och plats. Om de stämmer överens med VPN-serverns IP-adress och plats i stället för internetleverantörens har VPN-anslutningen upprättats.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
