# Dynamic DNS {#dynamic-dns}

Dynamic Domain Name Service (Dynamic DNS of DDNS) koppelt een domeinnaam aan het dynamische IP-adres van een netwerkapparaat. Met Dynamic DNS heb je op afstand toegang tot je router. Hiervoor is een openbaar internet-IP-adres vereist.

## DDNS inschakelen {#enable-ddns}

Ga links in het webbeheerpaneel naar **APPLICATIONS** -> **Dynamic DNS**.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Schakel **Enable DDNS** in, ga akkoord met **Terms of Services & Privacy Policy** en klik op **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Klik rechtsonder op **Security Settings**.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

Controleer in het pop-upvenster of het gewenste protocol voor externe toegang is ingeschakeld. Ga anders naar SYSTEM -> Security -> Remote Access Control om het in te schakelen.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Schakel het gewenste protocol voor externe toegang in en klik op **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Het synchroniseren van records tussen DNS-servers kan maximaal 10 minuten duren. Daardoor is toegang via de DDNS-domeinnaam mogelijk niet direct beschikbaar na inschakeling of nadat je openbare IP-adres is gewijzigd.

**Opmerking**: als je DDNS en VPN Client tegelijk inschakelt, controleer je of **Services From GL.iNet Use VPN** is uitgeschakeld. Deze functie staat onder [VPN Client Options](vpn_dashboard_v4.8.md#tunnel-options) in VPN Dashboard.

## Controleren of DDNS werkt {#check-if-ddns-works}

Je kunt met het DDNS-testhulpmiddel of handmatig met opdrachten controleren of DDNS werkt.

=== "Het DDNS-testhulpmiddel gebruiken"

    Klik op de pagina Dynamic DNS op **DDNS Test**.

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Controleer of het IP-adres van de DDNS-domeinomzetting overeenkomt met het WAN-IP-adres van de router.

    Als dit niet het geval is, verschijnt bovenaan een gele melding dat de router zich mogelijk achter NAT bevindt en dat je port forwarding op de upstream router moet instellen.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Opdrachten gebruiken"

    1. Gebruik de opdracht `nslookup` om de koppeling tussen de domeinnaam en het IP-adres op te vragen, zoals hieronder.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup.png){class="glboxshadow" width="600"}

        **Tips:**

        - Vervang "xxxxxxx.glddns.com" in de bovenstaande afbeelding door je Host Name.

        - "8.8.8.8" in de bovenstaande afbeelding is Google DNS. Gebruik dit adres of vervang het door een andere DNS en druk op Enter.

    2. Bepaal aan de hand van het resultaat of je DDNS-domein aan een openbaar IP-adres is gekoppeld.

        - Als je een openbaar IP-adres ontvangt, zoals "183.178.10.100" in de bovenstaande afbeelding, is je DDNS-domein met succes aan een openbaar IP-adres gekoppeld.

        - Als je de melding "server can't find xxxxxxx.glddns.com" ontvangt, is de domeinomzetting mogelijk mislukt en is je DDNS-domein niet aan een openbaar IP-adres gekoppeld. Ga naar de volgende stap om dit te controleren.

    3. Meld je aan bij het webbeheerpaneel van je router en ga naar **INTERNET**. Zoek het WAN-IP-adres van de router in de actieve interface. Vergelijk dit adres met het bovenstaande openbare IP-adres. Als ze gelijk zijn, werkt DDNS.

## Externe toegang via HTTPS {#https-remote-access}

!!! Note

    1. Voor externe toegang via HTTPS is een **Public IP**-adres vereist.

        Klik [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) om te controleren of je internetprovider je een openbaar IP-adres toewijst.

    2. Als je router zich achter NAT bevindt, configureer je port forwarding met poort **443** op de upstream router voor HTTPS-toegang.

Volg de onderstaande stappen om externe HTTPS-toegang voor je router in te schakelen.

1. Schakel op de pagina Dynamic DNS **Enable DDNS** in, ga akkoord met **Terms of Services & Privacy Policy** en klik op **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Ga in het webbeheerpaneel naar SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Schakel **HTTPS Remote Access** in en klik op **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Na inschakeling kun je het beheerpaneel van de router overal via de DDNS-hostnaam en **HTTPS** openen, bijvoorbeeld `https://xxxxxxx.glddns.com`.

Als port forwarding is geconfigureerd, gebruik je `https://xxxxxxx.glddns.com:external_port`, waarbij je external_port door het werkelijke poortnummer vervangt.

**Opmerking**: deze functie gebruikt zelfondertekende certificaten. Browsers tonen daarom **Your connection is not private** wanneer je het beheerpaneel van de router via de DDNS-hostnaam en **HTTPS** opent. Hieronder wordt poort 8001 als voorbeeld gebruikt.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Klik onderaan op **Advanced** om door te gaan met externe HTTPS-toegang.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Klik vervolgens op **Proceed to xxxxxxx.glddns.com** om door te gaan.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Je kunt het webbeheerpaneel nu via de DDNS-hostnaam en HTTPS openen.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## Externe toegang via SSH {#ssh-remote-access}

!!! Note

    1. Voor externe toegang via SSH is een **Public IP**-adres vereist.

        Klik [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) om te controleren of je internetprovider je een openbaar IP-adres toewijst.

    2. Als je router zich achter NAT bevindt, configureer je port forwarding met poort **22** op de upstream router voor SSH-toegang.

Volg de onderstaande stappen om externe SSH-toegang voor je router in te schakelen.

1. Schakel op de pagina Dynamic DNS **Enable DDNS** in, ga akkoord met **Terms of Services & Privacy Policy** en klik op **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Ga in het webbeheerpaneel naar SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Schakel **SSH Remote Access** in en klik op **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Na inschakeling kun je de terminal van de router op afstand via de DDNS-hostnaam en **SSH** openen, bijvoorbeeld `ssh root@xxxxxxx.glddns.com`.

Als port forwarding is geconfigureerd, gebruik je `ssh -p external_port root@xxxxxxx.glddns.com`, waarbij je external_port door het werkelijke poortnummer vervangt.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
