# Specifieke clientapparaten blokkeren op een GL.iNet-router {#how-to-block-specific-client-devices-on-a-glinet-router}

In deze handleiding lees je hoe je specifieke clientapparaten op een GL.iNet-router blokkeert. Door clientapparaten te blokkeren, voorkom je onbevoegde toegang tot je netwerk. Dit helpt de beveiliging van je netwerk te verbeteren of de internettoegang van je gezin te beheren.

GL.iNet-routers blokkeren clientapparaten op basis van hun MAC-adres, een unieke identificatie van 12 tekens die aan afzonderlijke apparaten in een netwerk is toegewezen. Deze methode wordt ook MAC-adresfiltering genoemd.

Je kunt clientapparaten op je GL.iNet-router op twee manieren blokkeren: via het [webbeheerpaneel van de router](#block-client-devices-via-the-admin-panel) of de [mobiele GL.iNet-app](#block-client-devices-via-the-glinet-mobile-app).

## Clientapparaten blokkeren via het webbeheerpaneel {#block-client-devices-via-the-admin-panel}

### 1. Aanmelden bij het webbeheerpaneel {#1-sign-in-to-the-admin-panel}

Voer in een webbrowser `192.168.8.1` in. Voer je wachtwoord in en klik op **Login**.

### 2. Clientapparaten blokkeren {#2-block-client-devices}

Je kunt clientapparaten op twee manieren blokkeren, afhankelijk van of je hun MAC-adres hebt:

* Als je hun MAC-adres niet hebt: gebruik de [eerste methode](#method-1-block-devices-without-their-mac-addresses), waarmee je apparaten uit de lijsten kunt blokkeren.
* Als je hun MAC-adres hebt: gebruik de [tweede methode](#method-2-block-devices-with-their-mac-addresses).

#### Methode 1: apparaten blokkeren zonder hun MAC-adres {#method-1-block-devices-without-their-mac-addresses}

1. Klik in de linkerzijbalk op **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Schakel de optie naast het apparaat in.
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Als de apparaten die je wilt blokkeren niet in de lijsten staan, moet je ze blokkeren door [hun MAC-adres aan de blokkeerlijst toe te voegen](#method-2-block-devices-with-their-mac-addresses).

#### Methode 2: apparaten blokkeren met hun MAC-adres {#method-2-block-devices-with-their-mac-addresses}

Voor deze methode heb je het MAC-adres van het apparaat nodig. Raadpleeg hiervoor de instructies van de fabrikant van het apparaat.
Volg deze stappen zodra je het MAC-adres van het apparaat hebt:

1. Klik in de linkerzijbalk op **Clients**.
2. Klik bovenaan op **Blocklist**.
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Gebruik een van de volgende methoden om apparaten te blokkeren:
    - MAC-adressen afzonderlijk invoeren: voer ze in het lege veld in.
    - Een lijst met MAC-adressen importeren: klik op **Import Clients**. Importeer een bestand en klik op **Import**.
4. Klik op **Apply**.
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Clientapparaten blokkeren via de mobiele GL.iNet-app {#block-client-devices-via-the-glinet-mobile-app}

**Opmerking:** installeer en configureer de mobiele GL.iNet-app op je apparaat voordat je begint.

Je kunt clientapparaten op twee manieren blokkeren, afhankelijk van of je hun MAC-adres hebt:

* Als je hun MAC-adres niet hebt: gebruik de [eerste methode](#mobile-1), waarmee je apparaten uit de lijst kunt blokkeren.
* Als je hun MAC-adres hebt: gebruik de [tweede methode](#mobile-2).

### Methode 1: apparaten blokkeren zonder hun MAC-adres {#mobile-1}

1. Tik in het hoofdscherm van de app onder **Connected Clients** en **Offline Clients** op het apparaat dat je wilt blokkeren.
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. Schakel onder **Settings** de optie **Block** in.
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Als de apparaten die je wilt blokkeren niet in de lijsten staan, moet je ze blokkeren door [hun MAC-adres aan de blokkeerlijst toe te voegen](#mobile-2).

### Methode 2: apparaten blokkeren met hun MAC-adres {#mobile-2}

Voor deze methode heb je het MAC-adres nodig van het apparaat dat je wilt blokkeren. Raadpleeg hiervoor de instructies van de fabrikant.
Volg deze stappen zodra je het MAC-adres van het apparaat hebt:

1. Tik in het hoofdscherm van de app op het pictogram Settings > **Access Control**.
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Tik op **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Gebruik een van de volgende methoden om apparaten te blokkeren:
    - MAC-adressen afzonderlijk invoeren: tik op **Add MAC address**. Voer het MAC-adres in en tik op **Done**.
    - Een lijst met MAC-adressen importeren: tik op **Import Clients** > **Import Clients**. Tik op een bestand.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
