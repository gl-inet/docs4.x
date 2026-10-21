# Cannot connect to an obfuscated WireGuard server {#cannot-connect-to-an-obfuscated-wireguard-server}

VPN-obfuscatie laat VPN-verkeer op normaal internetverkeer lijken. Sommige GL.iNet-routers ondersteunen AmneziaWG, waarmee je een WireGuard-server met verkeersobfuscatie kunt instellen.

Volg de onderstaande stappen als je geen verbinding met een verborgen WireGuard-server kunt maken.

1. **Ensure the WireGuard configuration imported to each client is dedicated.**

    Each client requires an exclusive peer configuration file. Sharing one configuration across multiple clients will result in connection failures.

    If necessary, navigate to **VPN** -> **WireGuard Server** -> **Profiles** to view your exported profiles.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Ensure that the obfuscated parameters can be verified by the client.**

    AmneziaWG is achterwaarts compatibel. Als je WireGuard-server alleen AmneziaWG v1.0 ondersteunt, slaagt de verificatie van het configuratiebestand ook bij import in een client met v2.0.

    Als het configuratiebestand obfuscatieparameters van AmneziaWG v2.0 bevat, moet de WireGuard-client v2.0 ondersteunen. Anders kan de parameterverificatie mislukken.

    !!! tip "How to identify the AmneziaWG version?"

        **V1.0**: No S3-S4 parameters; H1-H4 are fixed single integers.

        **V2.0**: het is V2.0 als aan een van de onderstaande voorwaarden wordt voldaan:

        - Includes S3-S4 parameters
        - H1-H4 are set as numeric ranges
        - Includes customized I1-I5 parameters.

        > Opmerking: I1-I5 worden niet automatisch gegenereerd. Je kunt ze handmatig als extra regels toevoegen om AmneziaWG-verkeer op protocollen zoals QUIC of WebRTC te laten lijken.

    Als je WireGuard-client een GL.iNet-router is, controleer je de AmneziaWG-versie met een van de volgende methoden.

    ??? note "Check via Router Web Admin Panel"

        1. Log in to your router's web Admin Panel.

        2. Ga naar **VPN** -> **WireGuard Server** -> **Configuration** en controleer de obfuscatieparameters. Als **S3-S4** en **H1–H4** als variabele bereiken in plaats van vaste waarden zijn ingesteld, gebruikt de router AmneziaWG 2.0.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            Otherwise, it uses AmneziaWG 1.0, as shown below.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Check via SSH Command"

        1. Log in to your router via SSH.

        2. Voer `opkg list|grep awg` uit en controleer het achtervoegsel van **kmod-amneziawg**. Als dit **2.0** is, ondersteunt de router AmneziaWG 2.0.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            Otherwise, it runs AmneziaWG 1.0, as shown below.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Adjust obfuscation parameters.**

    Als je [obfuscatieparameters](amneziawg_obfuscation.md#parameter-overview) zoals Jc, Jmin en Jmax handmatig hebt ingesteld, kunnen onjuiste waarden een mislukte handshake veroorzaken.

    Wijzig de obfuscatieparameters en maak opnieuw verbinding om niet-overeenkomende parameters uit te sluiten. Je kunt ook de standaardinstellingen herstellen om te testen.

4. **Test connection with the official AmneziaWG App.**

    Voer een vergelijkende test uit: installeer de officiële Amnezia WG-app, importeer het oorspronkelijke door de server geëxporteerde configuratiebestand en probeer verbinding te maken.

    - Als de officiële app verbinding maakt, is het configuratiebestand geldig. Controleer de netwerkverbinding van het oorspronkelijke clientapparaat of neem contact op met ondersteuning.

    - Als de verbinding nog steeds mislukt, ligt het probleem bij de serverconfiguratie van de router. Controleer de serverinstellingen en obfuscatieparameters.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
