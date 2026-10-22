# Det går inte att hitta en Android-telefons 5G-hotspot {#cannot-scan-android-5g-hotspot}

Ett vanligt sätt att ansluta till internet är att ansluta GL.iNet-routern som repeater till en Android-telefons 5G-hotspot.

Om det inte går att hitta Android-telefonens 5G-hotspot kan problemet bero på Wi-Fi-kanalen.

Vissa Android-telefoner använder som standard en amerikansk kanal för sin 5G-hotspot. Det kan orsaka problemet om GL.iNet-routern inte ursprungligen köptes i USA.

Du kan ändra GL.iNet-routerns landskod för Wi-Fi i LuCI-gränssnittet genom att följa stegen nedan.

1. Logga in på GL.iNet-routern och gå till **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Logga in på LuCI med samma administratörslösenord.

2. Redigera Wi-Fi-inställningarna.

    Gå till **Network** -> **Wireless**, leta reda på 5G Wi-Fi och klicka på **Edit** till höger.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. Välj USA som landskod.

    På sidan Wireless klickar du på fliken **Advanced Settings** under **Device Configuration**. Välj US (United States) som landskod för 5GHz Wi-Fi.

    ![5gus](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. Klicka på **Save & Apply** innan du loggar ut.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    Försök sedan hitta Android-telefonens 5G-hotspot igen.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
