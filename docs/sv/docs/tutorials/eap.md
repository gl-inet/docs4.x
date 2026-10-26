# Anslut GL.iNet-routrar till ett EAP-nätverk {#connect-glinet-routers-to-an-eap-network}

Vissa GL.iNet-routrar kan ansluta till EAP-Wi-Fi-nätverk (Extensible Authentication Protocol). EAP används ofta med **802.1X-autentisering** i **WPA2‑Enterprise/WPA3‑Enterprise**, till exempel i det globala utbildnings- och forskningsnätverket **eduroam**.

Du kan ansluta via GL.iNets webbadministrationspanel eller LuCI.

## Modeller som stöds {#supported-models}

??? "Modeller som stöds"
    - GL-MG1300 (Mango 2)
    - <u>GL-BE14000 (Flint 4)</u><sup>1</sup>
    - <u>GL-BE10000 (Slate 7 Pro)</u><sup>1</sup>
    - <u>GL-MT3600BE (Beryl 7)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - <u>GL-BE3600 (Slate 7)</u><sup>1</sup>
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>

    ---

    **Fotnot:**

    1. Vid anslutning till WPA/WPA2/WPA3-Enterprise stöder GL-BE10000 (Slate 7 Pro), GL-MT3600BE (Beryl 7) och GL-BE3600 (Slate 7) endast PEAP-autentiserade nätverk. Andra EAP-metoder, exempelvis EAP-TLS, EAP-TTLS och EAP-MD5, stöds inte.

    2. GL-MT6000 (Fortify), GL-MT6000 (Flint 2) och GL-MT3000 (Beryl AX) stöder inte EAP-nätverk med standardfirmware. GL.iNet tillhandahåller OpenWrt 24-firmware med EAP-stöd. Sök efter modellen i [Download Center](https://dl.gl-inet.com/){target="_blank"} och se fliken OPENWRT 24.

    3. GL-SFT1200 (Opal) stöder EAP-nätverk från firmware v4.8.

??? "Modeller som inte stöds"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Anslut via webbadministrationspanelen {#connect-via-web-admin-panel}

1. Gå till **INTERNET** -> avsnittet **Repeater** och klicka på **Connect**. Välj EAP-nätverkets SSID i sökresultatet eller klicka på **Join Other Network**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Ange **SSID**.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Välj WPA/WPA2/WPA3 Enterprise vid **Security**.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Ange **Username** och **Password** och klicka på **Apply**.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Anslut via LuCI {#connect-via-luci}

Webbadministrationspanelen stöder bara ett begränsat antal EAP-typer. Prova LuCI om anslutningen misslyckas. Följande steg är vägledande; utgå från enhetens faktiska LuCI-sidor.

1. Gå till **SYSTEM** -> **Advanced Settings**, installera LuCI och klicka på **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Logga in i LuCI med samma administratörslösenord och gå till Network -> Wireless.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Klicka på **Scan** i avsnittet 2.4G eller 5G.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Anslut till önskat nätverk.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Felsökning {#troubleshooting}

Webbadministrationspanelen kan misslyckas om EAP-nätverket kräver ytterligare parametrar som EAP-typ, matchning av domänsuffix, identitet eller anonym identitet.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

1. Hämta i förväg nätverkets EAP-typ (PEAP, TTLS eller TLS), autentiseringsdomän, fullständiga identitet, eventuell anonym identitet, inre autentiseringstyp (MSCHAPv2 eller PAP) och eventuellt CA-certifikat i .crt-format.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Avbryt först en misslyckad WebGUI-anslutning och gå sedan till **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Logga in med administratörslösenordet.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Gå till Network -> Wireless i LuCI. Klicka på **Scan** i 5G- eller 2.4G-avsnittet, välj EAP-nätverket och klicka på **Join Network**. Ange **WPA passphrase** på sidan "Joining Network" och klicka på **Submit**.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

4. Öppna **Interface Configuration** -> **Wireless Security** och ange parametrarna för nätverket. Klicka inte på Save ännu.

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. Öppna fliken **Advanced Settings**, ange ett gränssnittsnamn som **wlan0** och klicka på **Save**.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. Klicka på **Save & Apply** på Wireless-sidan. Routern ansluter till EAP-nätverket.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

7. Verifiera anslutningen.

    ??? "Kontrollera anslutningen i WebGUI"

        Repeaterikonen tänds när anslutningen har upprättats.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Obs!** LuCI-konfigurationen synkroniseras inte med WebGUI. Därför visas inte repeatergränssnittets IP-adress, gateway och övriga detaljer där, och repeateravsnittet kan vara tomt trots en fungerande anslutning.

    ??? "Kontrollera anslutningen via SSH"

        1. Logga in på routern via [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"}.

        2. Ange **ifconfig** och tryck på Enter. Kontrollera sedan gränssnittet **wlan0**.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
