# De firmware van je router handmatig upgraden of downgraden (van v4.x naar v4.x) {#how-to-manually-upgrade-or-downgrade-your-router-firmware-from-v4x-to-v4x}

In deze handleiding lees je **hoe je de firmware van je router handmatig upgradet of downgradet (van v4.x naar v4.x)**. Voor het handmatig upgraden en downgraden van de routerfirmware gelden dezelfde stappen.

!!! Note "Over het upgraden en downgraden van de routerfirmware"

    **Upgraden:** GL.iNet-routers met firmwareversie 4.x bieden geen functie voor automatische updates.

    Wanneer een nieuwe firmwareversie beschikbaar is, verschijnt na aanmelding bij het webbeheerpaneel van de router de melding "Upgrade Reminder". Klik op **Upgrade** om de nieuwste firmwareversie in de lijst te installeren. Volg de onderstaande stappen als je handmatig naar een specifieke firmwareversie wilt upgraden.

    **Downgraden:** je kunt de routerfirmware downgraden om bepaalde problemen op te lossen.

## 1. Controleren of je router de nieuwste firmwareversie gebruikt (alleen voor upgraden) {#1-check-if-your-router-is-running-the-latest-firmware-version-only-for-upgrade}

1. Voer in een webbrowser de URL van het webbeheerpaneel van je router in (bijvoorbeeld 192.168.8.1) en meld je aan.
2. Selecteer in de linkerzijbalk **SYSTEM** > **Upgrade**.

## 2. Het firmwarebestand downloaden {#2-download-the-firmware-file}

1. Zoek in de zoekbalk van het [firmwaredownloadcentrum](https://dl.gl-inet.com/) naar je routermodel en selecteer het.
2. Selecteer op het tabblad **Stable** of een ander tabblad **DOWNLOAD FOR COMMON UPGRADE AND U-BOOT** naast de firmwareversie die je wilt downloaden.

## 3. De firmware uploaden {#3-upload-the-firmware}

De volgende instructies beschrijven hoe je firmware via het webbeheerpaneel van de router uploadt. (Wil je firmware via de mobiele GL.iNet-app uploaden, [download dan de app](https://www.gl-inet.com/app/) en configureer deze.)

1. Voer in een webbrowser de URL van het webbeheerpaneel van je router in (bijvoorbeeld 192.168.8.1) en meld je aan.
2. (Optioneel) Volg de onderstaande stappen als je een back-up van je huidige instellingen wilt maken.

    ??? "Een back-up van je huidige instellingen maken"

        a. Klik in de linkerzijbalk op **SYSTEM** > **Advanced Settings**.

        b. Klik op de koppeling of de knop **Go To LuCI** om de aanmeldpagina van LuCI te openen.

        c. Voer het beheerderswachtwoord in en klik op **Log in**.

        d. Klik op **System** > **Backup / Flash Firmware**.

        e. Klik onder **Backup** op **Generate archive**. Er wordt een bestand met je huidige instellingen naar je apparaat gedownload.

        **Dit bestand is alleen geschikt voor de firmwareversie die werd gebruikt toen de back-up werd gemaakt en niet voor andere firmwareversies.**

3. Klik in de linkerzijbalk op **SYSTEM** > **Upgrade**.
4. Klik op **Local Upgrade** en selecteer het bestand dat je eerder hebt gedownload.
5. Schakel **Keep Settings** in als je bij het upgraden je huidige instellingen wilt behouden, zoals het beheerderswachtwoord van je router. Schakel deze optie niet in wanneer je firmware downgradet.
6. Klik op **Install**.

**Opmerking:** schakel de router tijdens het upgraden niet uit. Nadat de upgrade is voltooid, verschijnt het aanmeldscherm van de router.

Herstel je routerinstellingen als deze tijdens de firmware-update verloren zijn gegaan.

Probeer de firmware via [U-boot](../faq/debrick.md) te upgraden als de bovenstaande methode niet werkt.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.

---
