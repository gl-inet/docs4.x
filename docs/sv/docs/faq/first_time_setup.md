# Förstagångskonfiguration {#first-time-setup}

Förstagångskonfigurationen är mycket likartad för olika GL.iNet-routrar. De flesta modeller har en Wi-Fi-modul, men vissa saknar den.

Följande instruktioner är därför uppdelade i två fall beroende på om det finns en Wi-Fi-modul.

* [För modeller med Wi-Fi](#for-models-that-have-wi-fi)
* [För modeller utan Wi-Fi](#for-models-that-dont-have-wi-fi)

## För modeller med Wi-Fi {#for-models-that-have-wi-fi}

I följande steg används GL-MT3000 (Beryl AX) som exempel.

Förbered följande delar som ingår i förpackningen.

- En GL-MT3000-router (Beryl AX)
- En nätadapter
- En Ethernet-kabel

Titta på videoguiden eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. **Slå på routern**

    Anslut nätadapterns ena ände till routern och den andra till ett eluttag. Routern startar automatiskt.

    Vissa modeller (till exempel Slate AX) har en TF-kortplats. Om du behöver använda ett TF-kort sätter du i det innan du slår på routern. Byte av TF-kort under drift stöds inte.

2. **Anslut till routern**

    Anslut en enhet (t.ex. en smarttelefon, bärbar dator eller stationär dator) till routern med en Ethernet-kabel eller via Wi-Fi.

    * Anslut via Ethernet: Anslut enheten till routerns LAN-port med en Ethernet-kabel.

    * Anslut via Wi-Fi: Leta reda på Wi-Fi-nätverkets SSID och Wi-Fi-nyckel på etiketten på routerns undersida. Sök efter routerns SSID på enheten och ange sedan Wi-Fi-nyckeln.

        !!! tip

            1. QR-koden på etiketten på undersidan innehåller standarduppgifterna för Wi-Fi. Du kan ansluta snabbt genom att skanna den med en QR-kodläsare.
            2. Om Wi-Fi-nyckeln inte står på etiketten på vissa äldre modeller kan du prova "goodlife".

    När du har anslutit till Wi-Fi kanske du inte får internetåtkomst direkt. Följ nästa steg för att först konfigurera nätverket innan du ansluter till internet.

3. **Logga in på webbadministrationspanelen**

    Öppna en webbläsare (Chrome, Edge och Safari rekommenderas för bättre kompatibilitet) och gå till [http://192.168.8.1](http://192.168.8.1). GL.iNets inloggningssida öppnas. Om du inte kan öppna webbadministrationspanelen klickar du [här](cannot_access_web_admin_panel.md) för felsökningsanvisningar.

    Ange ett administratörslösenord och klicka sedan på **Next**.

    ![mt3000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_password.png){class="glboxshadow"}

    Konfigurera Wi-Fi. Om du ändrar Wi-Fi-uppgifterna måste du ansluta till det uppdaterade nätverket igen. Klicka sedan på **Next**.

    ![mt3000 set up wifi](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_set_up_wifi.png){class="glboxshadow"}

    Vänta tills routern har initierats.

    ![mt3000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_initializing.png){class="glboxshadow"}

    Därefter öppnas routerns webbadministrationspanel.

    ![mt3000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_panel.png){class="glboxshadow"}

4. **Anslut till internet**

    * [Anslut till internet med en Ethernet-kabel](../interface_guide/internet_ethernet.md)
    * [Anslut till internet via ett befintligt Wi-Fi-nätverk](../interface_guide/internet_repeater.md)
    * [Anslut till internet via internetdelning med USB](../interface_guide/internet_tethering.md)
    * [Anslut till internet via ett USB-modem](../interface_guide/internet_cellular.md)

## För modeller utan Wi-Fi {#for-models-that-dont-have-wi-fi}

I följande steg används GL-MT5000 (Brume 3) som exempel.

1. **Slå på routern**

    Anslut nätadapterns ena ände till routern och den andra till ett eluttag. Routern startar automatiskt.

2. **Anslut till routern**

    Anslut en enhet (t.ex. en bärbar eller stationär dator) till routerns LAN-port med en Ethernet-kabel.

3. **Logga in på webbadministrationspanelen**

    Öppna en webbläsare (Chrome, Edge och Safari rekommenderas för bättre kompatibilitet) och gå till [http://192.168.8.1](http://192.168.8.1). GL.iNets inloggningssida öppnas. Om du inte kan öppna webbadministrationspanelen klickar du [här](cannot_access_web_admin_panel.md) för felsökningsanvisningar.

    Ange ett administratörslösenord och klicka sedan på **Next**.

    ![mt5000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_password.png){class="glboxshadow"}

    Vänta tills routern har initierats.

    ![mt5000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_initializing.png){class="glboxshadow"}

    Därefter öppnas routerns webbadministrationspanel.

    ![mt5000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_panel.png){class="glboxshadow"}

4. **Anslut till internet**

    * [Anslut till internet med en Ethernet-kabel](../interface_guide/internet_ethernet.md)
    * [Anslut till internet via internetdelning med USB](../interface_guide/internet_tethering.md)
    * [Anslut till internet via ett USB-modem](../interface_guide/internet_cellular.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
