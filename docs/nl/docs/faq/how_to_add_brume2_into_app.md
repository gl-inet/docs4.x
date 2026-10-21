# How to add Brume 2 into GLiNet Mobile App? {#how-to-add-brume-2-into-glinet-mobile-app}

Je kunt Brume 2 (GL-MT2500/GL-MT2500A) aan de GLiNet Mobile App toevoegen, ook zonder wifi. Je kunt hem als primaire of secundaire router instellen.

De volgende methoden zijn ook van toepassing op Brume (GL-MV1000).

## Brume 2 als secundaire router {#brume-2-as-the-secondary-router}

**Topology**

In dit voorbeeld is Slate AX (GL-AXT1800) de primaire router en Brume 2 (GL-MT2500) de secundaire router.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Log in to your Brume 2 web Admin Panel, go to **SYSTEM** -> **Security** -> **Open Ports on Router**, open port **80**.

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    For some older models, go to **Firewall** -> **Open Ports on Router**, open port **80**.

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Meld je aan bij de primaire router en noteer het **WAN IP** van Brume 2.

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Verbind een telefoon met de wifi van je primaire router.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

4. Open de glinet-app en klik op **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

5. Then click **Initialized Devices**.

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.png){class="glboxshadow gl-50-desktop"}

6. Voer het WAN-IP in dat je op de primaire router hebt gevonden.

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.png){class="glboxshadow gl-50-desktop"}

7. Input the login password of Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    Brume 2 verschijnt nu in de glinet-app.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

## Brume 2 als primaire router {#brume-2-as-the-main-router}

**Topology**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Meld je aan bij de secundaire router, in dit voorbeeld GL-AXT1800, en stel deze in op Access Point-modus.

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Verbind een telefoon met de wifi van je secundaire router.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

3. Open de glinet-app en klik op **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

4. Select your main router.

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.png){class="glboxshadow gl-50-desktop"}

5. Click **Next**

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.png){class="glboxshadow gl-50-desktop"}

6. Wacht als je nog met de wifi van de secundaire router bent verbonden. Maak anders opnieuw verbinding met die wifi.

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.png){class="glboxshadow gl-50-desktop"}

7. Input the login password of Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    Brume 2 verschijnt nu in de glinet-app.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
