# Hur lägger jag till Brume 2 i GLiNet-mobilappen? {#how-to-add-brume-2-into-glinet-mobile-app}

Du kan lägga till Brume 2 (GL-MT2500/GL-MT2500A) i GLiNet-mobilappen även om den saknar Wi-Fi-funktion. Du kan konfigurera den som antingen primär eller sekundär router.

Följande metoder gäller även för Brume (GL-MV1000).

## Brume 2 som sekundär router {#brume-2-as-the-secondary-router}

**Topologi**

I det här exemplet är Slate AX (GL-AXT1800) den primära routern och Brume 2 (GL-MT2500) den sekundära routern.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Logga in på webbadministrationspanelen för Brume 2, gå till **SYSTEM** -> **Security** -> **Open Ports on Router** och öppna port **80**.

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    På vissa äldre modeller går du till **Firewall** -> **Open Ports on Router** och öppnar port **80**.

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Logga in på den primära routern och anteckna Brume 2-enhetens **WAN IP**.

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Anslut en telefon till den primära routerns Wi-Fi.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

4. Starta glinet-appen och klicka på **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

5. Klicka sedan på **Initialized Devices**.

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.png){class="glboxshadow gl-50-desktop"}

6. Ange WAN-IP-adressen som du tidigare hittade på den primära routern.

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.png){class="glboxshadow gl-50-desktop"}

7. Ange inloggningslösenordet för Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    Brume 2 visas nu i glinet-mobilappen.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

## Brume 2 som primär router {#brume-2-as-the-main-router}

**Topologi**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Logga in på den sekundära routern, som i det här exemplet är GL-AXT1800, och ställ in den på Access Point-läge.

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Anslut en telefon till den sekundära routerns Wi-Fi.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

3. Starta glinet-appen och klicka på **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

4. Välj den primära routern.

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.png){class="glboxshadow gl-50-desktop"}

5. Klicka på **Next**.

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.png){class="glboxshadow gl-50-desktop"}

6. Vänta om du fortfarande är ansluten till den sekundära routerns Wi-Fi. Anslut annars till den sekundära routerns Wi-Fi igen.

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.png){class="glboxshadow gl-50-desktop"}

7. Ange inloggningslösenordet för Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    Brume 2 visas nu i glinet-mobilappen.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
