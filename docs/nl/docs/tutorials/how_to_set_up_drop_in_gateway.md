# Drop-in Gateway instellen op een GL.iNet-router {#how-to-set-up-drop-in-gateway-on-a-glinet-router}

GL.iNet biedt de functie Drop-in Gateway, waarmee je functies aan je primaire router toevoegt die deze mogelijk niet heeft, zoals AdGuard Home, versleutelde DNS en VPN. Met deze functie kun je je primaire router gewoon blijven gebruiken en tegelijk van aanvullende functies profiteren.

Je kunt Drop-in Gateway inschakelen voor [al je apparaten](#enable-drop-in-gateway-for-all-devices) of voor [specifieke apparaten](#enable-drop-in-gateway-for-specific-devices) die met je primaire router zijn verbonden. Volg het gedeelte dat bij je configuratie past.

**Opmerking**: modellen met een firmwareversie ouder dan v4.5.0 ondersteunen alleen het inschakelen van Drop-in Gateway voor alle apparaten. Wanneer Drop-in Gateway is ingeschakeld, worden alle clientapparaten via de Drop-in Gateway met het netwerk verbonden. Al het verkeer van verbonden clients wordt dan eerst door deze router verwerkt.

---

## Drop-in Gateway inschakelen voor alle apparaten {#enable-drop-in-gateway-for-all-devices}

### 1. De GL.iNet-router verbinden met de hoofdrouter {#1-connect-glinet-router-to-the-main-router}

Verbind de WAN-poort van de GL.iNet-router met een ethernetkabel met de LAN-poort van de hoofdrouter.

### 2. Drop-in Gateway inschakelen {#2-enable-drop-in-gateway}

Je kunt Drop-in Gateway op twee manieren inschakelen: via het webbeheerpaneel van de router of via de mobiele GL.iNet-app.

??? "Via het webbeheerpaneel"

    1. Voer in een webbrowser `192.168.8.1` in.

    2. Voer je wachtwoord in en klik op **Login**.

    3. Klik in de linkerzijbalk op **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Schakel de optie naast **Enable Drop-in Gateway Mode** in.

    5. Selecteer **All devices are networked through drop-in gateway**.

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Klik op **Apply**.

??? "Via de mobiele GL.iNet-app"

    **Opmerking:** installeer de mobiele GL.iNet-app op je apparaat voordat je begint.

    1. Tik in het hoofdscherm van de app op het tabblad **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tik op **Enable**.

    3. Tik bij **Devices are networked via drop-in gateway** op **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Tik op **Done**.

### 3. De DHCP-server op de hoofdrouter uitschakelen {#3-disable-dhcp-server-on-the-main-router}

Meld je aan bij je primaire router om de DHCP-server uit te schakelen. Raadpleeg de instructies van de fabrikant van je router of neem contact op met hun ondersteuning.

### 4. AdGuard, DNS, VPN en andere functies instellen {#4-set-up-adguard-dns-vpn-and-other-features}

Volg deze handleidingen om de gewenste functies op je GL.iNet-router in te schakelen.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Versleutelde DNS](../interface_guide/dns.md){target="_blank"}
* [Ouderlijk toezicht](../interface_guide/parental_control.md){target="_blank"}
* [WireGuard-client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN-client](../interface_guide/openvpn_client.md){target="_blank"}

---

## Drop-in Gateway inschakelen voor specifieke apparaten {#enable-drop-in-gateway-for-specific-devices}

### 1. De GL.iNet-router verbinden met de hoofdrouter {#1-connect-glinet-router-to-the-main-router_1}

Verbind de WAN-poort van de GL.iNet-router met een ethernetkabel met de LAN-poort van de hoofdrouter.

### 2. Drop-in Gateway inschakelen {#2-enable-drop-in-gateway_1}

Je kunt Drop-in Gateway op twee manieren inschakelen: via het webbeheerpaneel van de router of via de mobiele GL.iNet-app.

??? "Via het webbeheerpaneel"

    1. Voer in een webbrowser `192.168.8.1` in.

    2. Voer je wachtwoord in en klik op **Login**.

    3. Klik in de linkerzijbalk op **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Schakel de optie naast **Enable Drop-in Gateway Mode** in.

    5. Selecteer **Some devices select their own networking gateway**.

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Klik op **Apply**.

    **Opmerking:** sluit dit tabblad NIET. In de volgende stap moet je het IP-adres invoeren dat op het scherm wordt weergegeven.

??? "Via de mobiele GL.iNet-app"

    **Opmerking:** installeer de mobiele GL.iNet-app op je apparaat voordat je begint.

    1. Tik in het hoofdscherm van de app op het tabblad **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tik op **Enable**.

    3. Tik bij **Devices are networked via drop-in gateway** op **part**.

        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Tik op **Done**.

    **Opmerking:** sluit dit tabblad NIET. In de volgende stap moet je het IP-adres invoeren dat op het scherm wordt weergegeven.

### 3. De gateway en DNS instellen op een specifiek apparaat {#3-set-gateway-and-dns-on-specific-device}

??? "Windows"

    1. Verbind je apparaat met de hoofdrouter.
    2. Open in Windows **Settings** > **Network & Internet**.
    3. Volg op basis van je verbindingsmethode deze stappen:
        * Ethernet: klik op **Ethernet**.
        * Wi-Fi: klik op **Wi-Fi** en vervolgens op de naam van het Wi-Fi-netwerk.
    4. Kopieer het IPv4-adres. Klik naast **IP assignment** op **Edit**.
    5. Klik op **Manual**.
    6. Schakel **IPv4** in.
    7. Voer de volgende gegevens in:
        * **IP address:** plak het IP-adres dat je in stap 4 hebt gekopieerd.
        * **Subnet mask:** voer **255.255.255.0** in.
        * **Gateway:** voer het IP-adres in dat op de pagina **Drop-in Gateway** wordt weergegeven.
        * **Preferred DNS:** voer het IP-adres in dat op de pagina **Drop-in Gateway** wordt weergegeven.
    8. Klik op **Save**.

??? "Android"
    1. Verbind je apparaat met de hoofdrouter.
    2. Open op je Android-apparaat **Settings**.
    3. Tik op **Connections** > **Wi-Fi**.
    4. Tik naast het netwerk waarmee je bent verbonden op het pictogram **Settings**.
    5. Tik op **View more**.
    6. Tik op **IP settings** > **Static**.
    7. Voer bij **Gateway** en **DNS 1** het IP-adres in dat op het scherm **Drop-in Gateway** wordt weergegeven.
    8. Tik op **Save**.

??? "iOS"
    1. Verbind je apparaat met de hoofdrouter.
    2. Open op je iOS-apparaat **Settings**.
    3. Tik op **Wi-Fi**.
    4. Tik op het Wi-Fi-netwerk waarmee je bent verbonden.
    5. Noteer onder **IPv4 Address** de waarden **IP Address** en **Subnet Mask**.
    6. Tik op **Configure IP** > **Manual**.
    7. Voer de volgende gegevens in:
        * **IP Address:** voer het IP Address in dat je in stap 5 hebt genoteerd.
        * **Subnet Mask:** voer de Subnet Mask in die je in stap 5 hebt genoteerd.
        * **Router:** voer het IP-adres in dat op het scherm **Drop-in Gateway** wordt weergegeven.
    8. Tik op **Save**.
    9. Tik op **Configure DNS** en vervolgens op **Manual**.
    10. Tik op **Add Server** en voer het IP-adres in dat op het scherm **Drop-in Gateway** wordt weergegeven.
    11. Tik op **Save**.

??? "Mac"
    1. Verbind je apparaat met de hoofdrouter.
    2. Klik op je Mac op het Apple-pictogram > **System Settings**.
    3. Klik in de linkerzijbalk op **Network**.
    4. Klik naast het netwerk waarmee je bent verbonden op **Details**.
    5. Klik op **TCP/IP**.
    6. Noteer **IP Address** en **Subnet Mask**.
    7. Klik naast **Configure IPv4** op **Manually**.
    8. Voer de volgende gegevens in:
        * **IP address:** voer het IP Address in dat je in stap 6 hebt genoteerd.
        * **Subnet mask:** voer de Subnet Mask in die je in stap 6 hebt genoteerd.
        * **Router:** voer het IP-adres in dat op de pagina **Drop-in Gateway** wordt weergegeven.
    9. Klik op **OK** > **OK**.

### 4. AdGuard, DNS, VPN en andere functies instellen {#4-set-up-adguard-dns-vpn-and-other-features_1}

Volg deze handleidingen om de gewenste functies op je GL.iNet-router in te schakelen.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Versleutelde DNS](../interface_guide/dns.md){target="_blank"}
* [Ouderlijk toezicht](../interface_guide/parental_control.md){target="_blank"}
* [WireGuard-client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN-client](../interface_guide/openvpn_client.md){target="_blank"}

---

Gerelateerd artikel:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
