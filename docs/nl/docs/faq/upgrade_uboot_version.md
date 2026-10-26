# Upgrade U-Boot Version {#upgrade-u-boot-version}

## Waarschuwing {#warning}

**Upgrading U-Boot is very dangerous and generally not recommended. Once it fails, your device will be bricked and there will be no way to restore it. Only do this when necessary or instructed by GL.iNet support**.

**Do NOT turn off the power during the upgrade process, otherwise it may cause the upgrade to fail and the device to be bricked**.

## Preparation {#preparation}

- Een computer met een Ethernetpoort. Gebruik anders een extra USB-Ethernetadapter.
- An Ethernet cable.
- Download het U-Boot-bestand volgens de instructies van GL.iNet-ondersteuning. Controleer of je het juiste bestand gebruikt. Neem via support@gl-inet.com contact met ons op als je niet weet hoe je het downloadt.

## Upgrade Steps {#upgrade-steps}

Volg de onderstaande procedure om de U-Boot-upgradepagina te openen.

1. Koppel de voeding van de router los. Verbind je computer met de **Ethernet LAN port** van de router. Alle andere poorten **MOETEN** ongebruikt blijven.

    !!! note

        Bij sommige modellen is een bepaalde LAN-poort uitwisselbaar met de WAN-poort. Gebruik deze LAN-poort niet. Gebruik op GL-MT6000 (Flint 2) bijvoorbeeld LAN 2, LAN 3 of LAN 4 in plaats van LAN 1.

2. Houd de Reset-knop stevig ingedrukt terwijl je de router inschakelt. Als de router geen aan-uitknop heeft, schakelt deze automatisch in wanneer je de voeding aansluit.

    De led knippert enkele keren in een vast patroon. Laat de knop los zodra het patroon verandert.

3. Stel het IP-adres van je computer handmatig in op **192.168.1.2**. Volg hieronder de stappen voor je besturingssysteem:

    ??? "Windows 7 / Windows 10"

        1. Go to **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Right click **Local Area Connection** -> **Properties**.

        3. Click **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Set the **IP address** to `192.168.1.2` manually.

        5. Set the **Subnet mask** to `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/set_ip.jpg){class="glboxshadow"}

        6. Click the **OK** button.

    ??? "Windows 11"

        1. Open Settings.

        2. Klik op **Network & Internet**.

        3. Klik op het tabblad **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windwos11_ethernet.png){class="glboxshadow"}

        4. Klik onder "IP assignment" op **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Select the **Manual** option.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Turn on the **IPv4 toggle** switch.

        7. Set the static **IP address** as **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Specify the **Subnet mask** as **255.255.255.0**.

        9. Click the **Save** button.

    ??? "macOS"

        1. Klik linksboven op het **Apple**-pictogram en selecteer **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_system_preferences.png){class="glboxshadow"}

        2. Click **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_system_preferences_network.png){class="glboxshadow"}

        3. Klik links op **Ethernet**, open de keuzelijst naast **Configure IPv4** en selecteer **Manually**. Bij een USB-Ethernetadapter kan de interface onder de naam van de adapter verschijnen.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_ip_manually_1.png){class="glboxshadow"}

        4. Stel **IPv4 Address** in op `192.168.1.2`, **Subnet Mask** op `255.255.255.0` en **Router** op `192.168.1.1`. Klik daarna rechtsonder op Apply.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_ip_manually_2.png){class="glboxshadow"}

4. **Open `http://192.168.1.1/uboot.html` met Google Chrome of Microsoft Edge**. Voer de volledige URL in om onjuiste suggesties uit de browsercache te voorkomen.

    **DO NOT use Mozilla Firefox, as it may brick your router.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/u-boot_update.png){class="glboxshadow" width="700"}

5. Klik op **Choose file** en selecteer het gedownloade U-Boot-bestand.

6. Klik op **Update U-Boot**. Schakel de voeding tijdens de upgrade NIET uit. De update duurt enkele minuten.

7. Na een geslaagde update start de router opnieuw op. Zet de IP-instelling uit stap 3 terug en open het webbeheerpaneel via **192.168.8.1**. Als dit normaal werkt, is de router opnieuw opgestart.

    **Opmerking:** mogelijk moet je de incognitomodus gebruiken of de browsercache en cookies verwijderen om de router te openen.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
