# Så konfigurerar du Drop-in Gateway på en GL.iNet-router {#how-to-set-up-drop-in-gateway-on-a-glinet-router}

GL.iNets funktion Drop-in Gateway utökar funktionerna hos din primära router med sådant som den kanske saknar, till exempel AdGuard Home, krypterad DNS och VPN. Du kan fortsätta använda den primära routern som vanligt och samtidigt få tillgång till de extra funktionerna.

Du kan aktivera Drop-in Gateway för [alla enheter](#enable-drop-in-gateway-for-all-devices) eller [vissa enheter](#enable-drop-in-gateway-for-specific-devices) som är anslutna till den primära routern. Följ avsnittet som gäller för din konfiguration.

**Obs!** Modeller med firmwareversioner äldre än v4.5.0 stöder endast Drop-in Gateway för alla enheter. När Drop-in Gateway är aktiverat ansluts alla klientenheter via denna gateway, vilket innebär att all trafik från de anslutna klienterna först behandlas av GL.iNet-routern.

---

## Aktivera Drop-in Gateway för alla enheter {#enable-drop-in-gateway-for-all-devices}

### 1. Anslut GL.iNet-routern till den primära routern {#1-connect-glinet-router-to-the-main-router}

Anslut GL.iNet-routerns WAN-port till den primära routerns LAN-port med en Ethernet-kabel.

### 2. Aktivera Drop-in Gateway {#2-enable-drop-in-gateway}

Du kan aktivera Drop-in Gateway via routerns webbadministrationspanel eller GL.iNet-mobilappen.

??? "Via webbadministrationspanelen"

    1. Ange `192.168.8.1` i en webbläsare.

    2. Ange lösenordet och klicka på **Login**.

    3. Klicka på **Network** > **Drop-in Gateway** i det vänstra sidofältet.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Aktivera reglaget bredvid **Enable Drop-in Gateway Mode**.

    5. Välj **All devices are networked through drop-in gateway**.

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Klicka på **Apply**.

??? "Via GL.iNet-mobilappen"

    **Obs!** Installera GL.iNet-mobilappen på enheten innan du börjar.

    1. Tryck på fliken **System** > **Drop-in Gateway** på appens huvudskärm.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tryck på **Enable**.

    3. Tryck på **All** för **Devices are networked via drop-in gateway**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Tryck på **Done**.

### 3. Inaktivera DHCP-servern på den primära routern {#3-disable-dhcp-server-on-the-main-router}

Logga in på den primära routern och inaktivera DHCP-servern. Se anvisningarna från routertillverkaren eller kontakta tillverkarens support.

### 4. Konfigurera AdGuard, DNS, VPN och andra funktioner {#4-set-up-adguard-dns-vpn-and-other-features}

Följ dessa guider för att aktivera funktionerna som du vill använda på GL.iNet-routern.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Krypterad DNS](../interface_guide/dns.md){target="_blank"}
* [Föräldrakontroll](../interface_guide/parental_control.md){target="_blank"}
* [WireGuard-klient](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN-klient](../interface_guide/openvpn_client.md){target="_blank"}

---

## Aktivera Drop-in Gateway för vissa enheter {#enable-drop-in-gateway-for-specific-devices}

### 1. Anslut GL.iNet-routern till den primära routern {#1-connect-glinet-router-to-the-main-router_1}

Anslut GL.iNet-routerns WAN-port till den primära routerns LAN-port med en Ethernet-kabel.

### 2. Aktivera Drop-in Gateway {#2-enable-drop-in-gateway_1}

Du kan aktivera Drop-in Gateway via routerns webbadministrationspanel eller GL.iNet-mobilappen.

??? "Via webbadministrationspanelen"

    1. Ange `192.168.8.1` i en webbläsare.

    2. Ange lösenordet och klicka på **Login**.

    3. Klicka på **Network** > **Drop-in Gateway** i det vänstra sidofältet.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Aktivera reglaget bredvid **Enable Drop-in Gateway Mode**.

    5. Välj **Some devices select their own networking gateway**.

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Klicka på **Apply**.

    **Obs!** Stäng INTE den här fliken. Du behöver ange IP-adressen som visas på skärmen i nästa steg.

??? "Via GL.iNet-mobilappen"

    **Obs!** Installera GL.iNet-mobilappen på enheten innan du börjar.

    1. Tryck på fliken **System** > **Drop-in Gateway** på appens huvudskärm.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tryck på **Enable**.

    3. Tryck på **part** för **Devices are networked via drop-in gateway**.

        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Tryck på **Done**.

    **Obs!** Stäng INTE den här fliken. Du behöver ange IP-adressen som visas på skärmen i nästa steg.

### 3. Ange gateway och DNS på den aktuella enheten {#3-set-gateway-and-dns-on-specific-device}

??? "Windows"

    1. Anslut enheten till den primära routern.
    2. Öppna **Settings** > **Network & Internet** i Windows.
    3. Följ stegen för din anslutningsmetod:
        * Ethernet: Klicka på **Ethernet**.
        * Wi-Fi: Klicka på **Wi-Fi** och sedan på Wi-Fi-nätverkets namn.
    4. Kopiera IPv4-adressen. Klicka på **Edit** bredvid **IP assignment**.
    5. Klicka på **Manual**.
    6. Aktivera **IPv4**.
    7. Ange följande information:
        * **IP address:** Klistra in IP-adressen som du kopierade i steg 4.
        * **Subnet mask:** Ange **255.255.255.0**.
        * **Gateway:** Ange IP-adressen som visas på sidan **Drop-in Gateway**.
        * **Preferred DNS:** Ange IP-adressen som visas på sidan **Drop-in Gateway**.
    8. Klicka på **Save**.

??? "Android"
    1. Anslut enheten till den primära routern.
    2. Öppna **Settings** på Android-enheten.
    3. Tryck på **Connections** > **Wi-Fi**.
    4. Tryck på ikonen **Settings** bredvid nätverket som du är ansluten till.
    5. Tryck på **View more**.
    6. Tryck på **IP settings** > **Static**.
    7. Ange IP-adressen som visas på skärmen **Drop-in Gateway** för **Gateway** och **DNS 1**.
    8. Tryck på **Save**.

??? "iOS"
    1. Anslut enheten till den primära routern.
    2. Öppna **Settings** på iOS-enheten.
    3. Tryck på **Wi-Fi**.
    4. Tryck på Wi-Fi-nätverket som du är ansluten till.
    5. Anteckna **IP Address** och **Subnet Mask** under **IPv4 Address**.
    6. Tryck på **Configure IP** > **Manual**.
    7. Ange följande information:
        * **IP Address:** Ange IP-adressen som du antecknade i steg 5.
        * **Subnet Mask:** Ange nätmasken som du antecknade i steg 5.
        * **Router:** Ange IP-adressen som visas på skärmen **Drop-in Gateway**.
    8. Tryck på **Save**.
    9. Tryck på **Configure DNS** och sedan på **Manual**.
    10. Tryck på **Add Server** och ange IP-adressen som visas på skärmen **Drop-in Gateway**.
    11. Tryck på **Save**.

??? "Mac"
    1. Anslut enheten till den primära routern.
    2. Klicka på Apple-ikonen > **System Settings** på din Mac.
    3. Klicka på **Network** i det vänstra sidofältet.
    4. Klicka på **Details** bredvid nätverket som du är ansluten till.
    5. Klicka på **TCP/IP**.
    6. Anteckna **IP Address** och **Subnet Mask**.
    7. Klicka på **Manually** bredvid **Configure IPv4**.
    8. Ange följande information:
        * **IP address:** Ange IP-adressen som du antecknade i steg 6.
        * **Subnet mask:** Ange nätmasken som du antecknade i steg 6.
        * **Router:** Ange IP-adressen som visas på sidan **Drop-in Gateway**.
    9. Klicka på **OK** > **OK**.

### 4. Konfigurera AdGuard, DNS, VPN och andra funktioner {#4-set-up-adguard-dns-vpn-and-other-features_1}

Följ dessa guider för att aktivera funktionerna som du vill använda på GL.iNet-routern.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Krypterad DNS](../interface_guide/dns.md){target="_blank"}
* [Föräldrakontroll](../interface_guide/parental_control.md){target="_blank"}
* [WireGuard-klient](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN-klient](../interface_guide/openvpn_client.md){target="_blank"}

---

Relaterad artikel:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
