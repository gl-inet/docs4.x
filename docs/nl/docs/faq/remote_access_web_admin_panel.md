# Het webbeheerpaneel van een GL.iNet-router op afstand openen {#how-to-remotely-access-the-web-admin-panel-of-a-glinet-router}

Voor de volgende methoden moet je de router vooraf configureren terwijl je er fysiek bij bent.

## Method 1. GoodCloud {#method-1-goodcloud}

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} is een platform voor eenvoudige externe implementatie en beheer van verbonden apparaten. Koppel je GL.iNet-router aan GoodCloud om het webbeheerpaneel altijd en overal op afstand te openen en beheren.

Please refer to [this guide](../interface_guide/cloud.md){target="_blank"} for details.

## Method 2. VPN {#method-2-vpn}

Als je router een **openbaar IP-adres** heeft, kun je het webbeheerpaneel via een VPN-tunnel op afstand openen. Deze methode vereist geavanceerde configuratie en extra installatietijd.

1. Controleer of je router een openbaar IP-adres heeft. [Controleren of je een openbaar IP-adres hebt](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Set your router as a WireGuard Server. See [here](../interface_guide/wireguard_server.md){target="_blank"} for details.

3. Exporteer een configuratiebestand van je WireGuard Server voor later gebruik.

4. Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Server** en klik rechtsboven op **Options**. Schakel **Allow Remote Access to the LAN Subnet** in en klik op **Apply**.

5. Stel het apparaat waarmee je de router op afstand wilt openen als WireGuard Client in door het configuratiebestand handmatig te importeren.

    - Als je WireGuard Client een eindapparaat zoals een smartphone of laptop is, [installeer je de WireGuard-app](https://www.wireguard.com/install){target="_blank"}. Importeer daarna het bestand om een verbinding te starten.

    - Als je WireGuard Client een andere GL.iNet-router is, zoals een reisrouter, volg je [deze handleiding](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"} om het configuratiebestand te importeren en een verbinding te starten.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
