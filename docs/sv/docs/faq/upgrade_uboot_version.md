# Uppgradera U-Boot-versionen {#upgrade-u-boot-version}

## Varning {#warning}

**Det är mycket riskabelt att uppgradera U-Boot och det rekommenderas i allmänhet inte. Om uppgraderingen misslyckas slutar enheten att fungera och kan inte återställas. Gör detta endast när det är nödvändigt eller när GL.iNets support har instruerat dig att göra det**.

**Stäng INTE av strömmen under uppgraderingen. Det kan göra att uppgraderingen misslyckas och att enheten slutar fungera**.

## Förberedelser {#preparation}

- En dator med Ethernet-port. Förbered annars även en USB-till-Ethernet-adapter.
- En Ethernet-kabel.
- Ladda ned U-Boot-filen enligt anvisningarna från GL.iNets support. Kontrollera att du använder rätt U-Boot-fil. Om du inte vet hur du laddar ned U-Boot-filen kontaktar du oss via e-post på support@gl-inet.com.

## Uppgraderingssteg {#upgrade-steps}

Följ proceduren nedan för att öppna sidan för U-Boot-uppgradering.

1. Koppla från routerns strömförsörjning. Anslut datorn till routerns **Ethernet LAN port**. Alla andra portar **MÅSTE** vara **oanslutna**.

    !!! note

        På vissa modeller kan en viss LAN-port och WAN-porten byta funktion. Använd inte den LAN-porten. På GL-MT6000 (Flint 2) ska du till exempel inte använda LAN 1. Använd LAN 2, LAN 3 eller LAN 4 i stället.

2. Håll Reset-knappen ordentligt intryckt samtidigt som du slår på routern. Om routern saknar strömknapp startar den automatiskt när du ansluter strömmen.

    En lysdiod blinkar regelbundet några gånger. Släpp knappen när blinksekvensen ändras.

3. Ställ in datorns IP-adress manuellt på **192.168.1.2**. Följ guiden för ditt operativsystem nedan:

    ??? "Windows 7/Windows 10"

        1. Gå till **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Högerklicka på **Local Area Connection** -> **Properties**.

        3. Klicka på **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Ställ in **IP address** manuellt på `192.168.1.2`.

        5. Ställ in **Subnet mask** på `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/set_ip.jpg){class="glboxshadow"}

        6. Klicka på knappen **OK**.

    ??? "Windows 11"

        1. Öppna Settings.

        2. Klicka på **Network & Internet**.

        3. Klicka på fliken **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windwos11_ethernet.png){class="glboxshadow"}

        4. Klicka på knappen **Edit** i avsnittet "IP assignment".

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Välj alternativet **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Aktivera reglaget **IPv4**.

        7. Ställ in den statiska **IP address** på **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Ange **Subnet mask** som **255.255.255.0**.

        9. Klicka på knappen **Save**.

    ??? "macOS"

        1. Klicka på **Apple**-ikonen i det övre vänstra hörnet och välj **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_system_preferences.png){class="glboxshadow"}

        2. Klicka på **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_system_preferences_network.png){class="glboxshadow"}

        3. Klicka på **Ethernet** till vänster. Klicka sedan på listrutan bredvid **Configure IPv4** och välj **Manually**. Om du använder en USB-till-Ethernet-adapter kanske Ethernet inte visas. Anslutningen kan i stället visas med namnet på USB-till-Ethernet-adaptern.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_ip_manually_1.png){class="glboxshadow"}

        4. Ange `192.168.1.2` som **IPv4 Address**, `255.255.255.0` som **Subnet Mask** och `192.168.1.1` som **Router**. Klicka sedan på knappen Apply i det nedre högra hörnet.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_ip_manually_2.png){class="glboxshadow"}

4. **Använd Google Chrome eller Microsoft Edge för att öppna `http://192.168.1.1/uboot.html`**. Ange hela webbadressen så att en cachad rekommendation inte leder till fel adress.

    **Använd INTE Mozilla Firefox, eftersom det kan göra att routern slutar fungera.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/u-boot_update.png){class="glboxshadow" width="700"}

5. Klicka på knappen **Choose file** och välj U-Boot-filen som du laddade ned.

6. Klicka på knappen **Update U-Boot**. Stäng INTE av strömmen under uppgraderingen. Uppdateringen tar flera minuter.

7. Efter en lyckad uppdatering startas routern om. Du kan då återställa IP-inställningen från steg 3 och försöka öppna webbadministrationspanelen via **192.168.8.1**. Om webbadministrationspanelen öppnas normalt har routern startats om.

    **Obs!** Du kan behöva använda inkognitoläget eller radera webbläsarens cache och cookies för att öppna routern.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
