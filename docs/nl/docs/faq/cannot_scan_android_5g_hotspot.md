# Cannot Scan Android 5G Hotspot {#cannot-scan-android-5g-hotspot}

Connecting the GL.iNet router as a repeater to an Android phone's 5G hotspot is one of the common ways to access the Internet.

Als de router de 5G-hotspot van je Android-telefoon niet kan vinden, kan dit aan het wifi-kanaal liggen.

Sommige Android-telefoons stellen hun 5G-hotspot standaard in op een Amerikaans kanaal. Dit kan problemen geven als je GL.iNet-router niet in de VS is gekocht.

Volg de onderstaande stappen om de wifi-landcode van je GL.iNet-router in LuCI te wijzigen.

1. Meld je aan bij je GL.iNet-router en ga naar **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Meld je bij LuCI aan met hetzelfde beheerderswachtwoord.

2. Edit Wi-Fi settings.

    Ga naar **Network** -> **Wireless**, zoek 5G Wi-Fi en klik rechts op **Edit**.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. Select US as the country code.

    Klik op de pagina Wireless onder **Device Configuration** op het tabblad **Advanced Settings**. Selecteer US (United States) als landcode voor 5GHz-wifi.

    ![5gus](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. Click **Save & Apply** before logging out.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    Probeer daarna de 5G-hotspot van je Android-telefoon opnieuw te vinden.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
