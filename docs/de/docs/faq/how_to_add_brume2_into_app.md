# Wie fügt man Brume 2 zur GLiNet Mobile App hinzu?

Sie können Ihre Brume 2 (GL-MT2500/GL-MT2500A) zur GLiNet Mobile App hinzufügen, auch wenn sie keine WLAN-Funktion hat. Sie können sie entweder als Hauptrouter oder als sekundären Router einrichten.

Die folgenden Methoden gelten auch für Brume (GL-MV1000).

## Brume 2 als sekundärer Router

**Topologie**

Hier verwenden wir Slate AX (GL-AXT1800) als Hauptrouter und Brume 2 (GL-MT2500) als sekundären Router.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Melden Sie sich im Web-Admin-Panel Ihrer Brume 2 an, gehen Sie zu **SYSTEM** -> **Security** -> **Open Ports on Router** und öffnen Sie Port **80**.

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    Bei einigen älteren Modellen gehen Sie zu **Firewall** -> **Open Ports on Router** und öffnen Sie Port **80**.

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Melden Sie sich am Hauptrouter an und notieren Sie die **WAN IP** der Brume 2.

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Verbinden Sie ein Smartphone mit dem WLAN Ihres Hauptrouters.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

4. Starten Sie die GLiNet App und tippen Sie auf **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

5. Tippen Sie dann auf **Initialized Devices**.

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.PNG){class="glboxshadow gl-50-desktop"}

6. Geben Sie die WAN IP ein, die Sie zuvor im Hauptrouter gefunden haben.

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.PNG){class="glboxshadow gl-50-desktop"}

7. Geben Sie das Anmeldepasswort der Brume 2 ein.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Nun wird Ihre Brume 2 in der GLiNet Mobile App angezeigt.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

## Brume 2 als Hauptrouter

**Topologie**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Melden Sie sich an Ihrem sekundären Router an, in diesem Fall dem GL-AXT1800, und setzen Sie ihn in den Access Point-Modus.

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Verbinden Sie ein Smartphone mit dem WLAN Ihres sekundären Routers.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"} 

3. Starten Sie die GLiNet App und tippen Sie auf **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

4. Wählen Sie Ihren Hauptrouter aus.

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.PNG){class="glboxshadow gl-50-desktop"}

5. Tippen Sie auf **Next**.

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.PNG){class="glboxshadow gl-50-desktop"}

6. Wenn Sie noch mit dem WLAN des sekundären Routers verbunden sind, warten Sie einfach. Falls nicht, verbinden Sie sich erneut mit dem WLAN des sekundären Routers.

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.PNG){class="glboxshadow gl-50-desktop"}

7. Geben Sie das Anmeldepasswort der Brume 2 ein.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Nun wird Ihre Brume 2 in der GLiNet Mobile App angezeigt.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.

