# Återställ routern med U-Boot {#using-uboot-to-unbrick-your-router}

Om routern har slutat fungera på grund av ett eget projekt eller installation av fel firmware kanske du inte längre kommer åt den. I så fall kan du installera om firmware med U-Boots felsäkra läge.

**Obs!** U-Boot-åtgärden tar bort routerns inställningar och installerade plugin-program.

---

## Förberedelser {#preparation}

Förbered en stationär eller bärbar dator med en Ethernet-port. Om datorn saknar Ethernet-port behöver du även en USB-till-Ethernet-adapter.

**Obs!** GL-E5800 (Mudi 7) stöder för närvarande inte installation av firmware via U-Boot.

## Återställningssteg {#unbrick-steps}

Titta på videoguiden eller följ proceduren nedan för att öppna U-Boot-webbgränssnittet och installera om firmware.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>Stegen för ominstallation av firmware med U-Boot är i stort sett desamma. Videon använder Mudi/Mudi V2 som exempel. Följ proceduren nedan för andra modeller.</small>

1. Ladda ned U-Boot-firmware [här](https://dl.gl-inet.com/){target="_blank"} till datorn.

    Vissa modeller har två firmwarevarianter. Ladda ned den firmware som är kompatibel med U-Boot.

2. Stäng av routern. Anslut en dator till routerns **Ethernet LAN port** och låt alla andra portar vara oanslutna.

    !!! note

        På vissa modeller kan en viss LAN-port ändras till WAN. Använd inte den LAN-porten för att installera firmware. På GL-MT6000 (Flint 2) ska du till exempel inte använda LAN 1. Använd LAN 2, LAN 3 eller LAN 4 i stället.

3. Håll Reset-knappen ordentligt intryckt och **slå samtidigt på routern**. Om routern saknar strömknapp startar den automatiskt när du ansluter strömmen.

    Vänta tills lysdioden har blinkat regelbundet flera gånger. Släpp Reset-knappen **när** blinkmönstret ändras.

    !!! note "Lysdiodernas blinkmönster efter enhetsmodell"

        **Obs!** Identiska routermodeller från olika produktionsserier kan ha olika lysdiodsfärger eller blinksekvenser. Det påverkar inte återställningen med U-Boot. Fokusera på förändringen av lysdiodens blinkstatus.

        - För **GL-MT6000 (Fortify)**: Den blå lysdioden blinkar 6 gånger och lyser sedan med fast vitt sken.

        - För **GL-MG1300 (Mango 2)**: Den blå lysdioden blinkar 7 gånger och lyser sedan med fast vitt sken.

        - För **GL-BE14000 (Flint 4), GL-BE10000 (Slate 7 Pro) och GL-BE3600 (Slate 7)**: När du har hållit Reset-knappen intryckt i cirka 5 sekunder visas en nedräkning på 5 sekunder på pekskärmen. Fortsätt att hålla Reset-knappen intryckt tills nästa uppmaning visas på skärmen, till exempel att du ska ställa in datorns IP-adress manuellt på 192.168.1.2 och öppna http://192.168.1.1 i webbläsaren. Fortsätt till steg 4 för fler instruktioner.

        - För **GL-MT3600BE (Beryl 7)**: Den blå lysdioden blinkar 7 gånger och lyser sedan med fast vitt sken.

        - För **GL-MT5000 (Brume 3)**: Power-lysdioden blinkar blått 7 gånger och lyser sedan med fast vitt sken.

        - För **GL-BE6500 (Flint 3e)**: Den blå lysdioden blinkar 6 gånger och lyser sedan med fast vitt sken.

        - För **GL-BE9300 (Flint 3)**: Den blå lysdioden blinkar 6 gånger och lyser sedan med fast vitt sken.

        - För **GL-X2000 (Spitz Plus)**: Internet-lysdioden blinkar 5 gånger och därefter lyser Wi-Fi-lysdioden med fast sken.

        - För **GL-B3000 (Marble)**: Den blå lysdioden blinkar 7 gånger och lyser sedan med fast vitt sken.

        - För **GL-MT6000 (Flint 2)**: Den blå lysdioden blinkar 6 gånger och lyser sedan med fast vitt sken.

        - För **GL-MT3000 (Beryl AX)**: Den blå lysdioden blinkar 6 gånger och lyser sedan med fast vitt sken.

        - För **GL-MT2500/GL-MT2500A (Brume 2)**: Power-lysdioden blinkar blått 5 gånger och lyser sedan med fast vitt sken.

        - För **GL-X3000 (Spitz AX)**: Internet-lysdioden blinkar 5 gånger och därefter lyser Wi-Fi-lysdioden med fast sken.

        - För **GL-XE3000 (Puli AX)**: Internet-lysdioden blinkar 5 gånger och därefter lyser Wi-Fi-lysdioden med fast sken.

        - För **GL-XE300 (Puli)**: LAN-lysdioden blinkar 5 gånger och därefter lyser Wi-Fi-lysdioden med fast sken.

        - För **GL-E750 (Mudi)**: Skärmen visar först "Booting", sedan "Reset Counting 1 to 4" och till sist "Please Open Web 192.168.1.1".

        - För **GL-X750 (Spitz)**: Internet-lysdioden blinkar 5 gånger och därefter lyser Wi-Fi-lysdioden med fast sken.

        - För **GL-AX1800 (Flint)**: Den blå lysdioden blinkar 5 gånger och lyser sedan med fast vitt sken.

        - För **GL-AXT1800 (Slate AX)**: Den blå lysdioden blinkar 5 gånger och lyser sedan med fast vitt sken.

        - För **GL-SFT1200 (Opal)**: Den blå lysdioden blinkar 5 gånger och lyser sedan med fast vitt sken.

        - För **GL-MT1300 (Beryl)**: Den blå lysdioden blinkar långsamt två gånger, blinkar sedan snabbare 5 gånger och lyser därefter med fast vitt sken.

        - För **GL-A1300 (Slate Plus)**: Lysdioden blinkar långsamt 5 gånger, lyser med fast sken en kort stund och blinkar sedan snabbt hela tiden.

        - För **GL-MT300N-V2 (Mango)** och **GL-AR300M (Shadow)**: Lysdioden blinkar 5 gånger.

        - För **GL-X300B (Collie)**: WAN-lysdioden blinkar 5 gånger och därefter lyser Wi-Fi-lysdioden med fast sken.

        - För **GL-AP1300 (Cirrus)**: Power-lysdioden blinkar långsamt 5 gånger, lyser med fast sken en kort stund och blinkar sedan snabbt hela tiden.

        - För **GL-B1300 (Convexa-B)** och **GL-S1300 (Convexa-S, EOL)**: Lysdioden blinkar 4 gånger.

            Power-lysdioden längst till vänster lyser hela tiden medan Wi-Fi-lysdioden längst till höger blinkar 4 gånger. Därefter lyser Mesh-lysdioden i mitten med fast sken.

            (På vissa äldre GL-B1300 lyser Power-lysdioden längst till vänster hela tiden, medan både lysdioden i mitten och lysdioden längst till höger blinkar 5 gånger samtidigt och sedan lyser med fast sken.)

        - För **GL-B2200 (Velica)**: De två lysdioderna lyser först blått, ändras sedan till vitt och blinkar 5 gånger och lyser därefter med fast blått sken.

        - För **GL-SF1200**: 5G-lysdioden blinkar 5 gånger och lyser sedan med fast sken.

        - För **GL-S200** blinkar den cyanblå lysdioden 5 gånger, lyser kort lila och lyser sedan med fast cyanblått sken.

        - För **GL-AR750 (Creta)** och **GL-AR750S-EXT (Slate)**: Lysdioden blinkar 5 gånger.

        - För **GL-USB150 (Microuter)**, **microuter-N300** och **GL-AR150 (White)**: Lysdioden blinkar 5 gånger.

        - För **GL-MV1000/GL-MV1000W (Brume)**: Ingen upprepad blinksignal visas. Power- och WAN-lysdioderna lyser hela tiden.

        - För **GL-MiFi**: Lysdioden blinkar 6 gånger.

        - För **GL-MT300N** och **GL-MT300A**: Lysdioden blinkar 3 gånger.

4. Ställ in datorns IP-adress manuellt på **192.168.1.2**. Följ guiden för ditt operativsystem nedan:

    ??? "Windows 7/Windows 10"

        1. Gå till **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.
        2. Högerklicka på **Local Area Connection** -> **Properties**.
        3. Klicka på **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.
        4. Ställ in **IP address** manuellt på `192.168.1.2`.
        5. Ställ in **Subnet mask** på `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/4/faq/debrick/set_ip.jpg){class="glboxshadow"}

        6. Klicka på knappen **OK**.

    ??? "Windows 11"

        1. Öppna Settings.
        2. Klicka på **Network & Internet**.
        3. Klicka på fliken **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. Klicka på knappen **Edit** i avsnittet "IP assignment".

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Välj alternativet **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Aktivera reglaget **IPv4**.
        7. Ställ in den statiska **IP address** på **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Ange **Subnet mask** som **255.255.255.0**.
        9. Klicka på knappen **Save**.

    ??? "macOS"

        1. Klicka på **Apple**-ikonen i det övre vänstra hörnet och välj **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_system_preferences.png){class="glboxshadow"}

        2. Klicka på **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        3. Klicka på **Ethernet** till vänster. Klicka sedan på listrutan bredvid **Configure IPv4** och välj **Manually**. Om du använder en USB-till-Ethernet-adapter kanske Ethernet inte visas. Anslutningen kan i stället visas med namnet på USB-till-Ethernet-adaptern.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        4. Ange `192.168.1.2` som **IPv4 Address**, `255.255.255.0` som **Subnet Mask** och `192.168.1.1` som **Router**. Klicka sedan på knappen Apply i det nedre högra hörnet.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Öppna **http://192.168.1.1** i webbläsaren. Detta är U-Boot-webbgränssnittet.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note

        - Om du inte kan öppna U-Boot-webbgränssnittet kontrollerar du om något VPN- eller proxyprogram körs. Inaktivera alla VPN- och proxyprogram, inklusive Tailscale och ZeroTier.

        - U-Boot-webbgränssnittet ovan kan skilja sig från det du ser, eftersom U-Boot-versionen varierar beroende på produktionsdatum. I vissa sällsynta fall rekommenderar vi att U-Boot-versionen uppgraderas. Följ guiden [här](upgrade_uboot_version.md).

6. Klicka på knappen **Choose file** för att leta reda på firmwarefilen. Klicka sedan på knappen **Update firmware**.

7. Vänta i cirka 3 minuter. Stäng inte av enheten under firmwareuppdateringen.

    Routern är klar när den blå lysdioden fortsätter att blinka. På vissa mobilroutermodeller är den klar när både Power- och Wi-Fi-lysdioderna lyser med fast sken.

8. Återställ IP-inställningarna från steg 4 och anslut datorn till routerns LAN eller Wi-Fi. Du kan sedan öppna routerns webbadministrationspanel via **192.168.8.1** igen.

    **Obs!** Du kan behöva använda inkognitoläget eller radera webbläsarens cache och cookies för att öppna routern.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
