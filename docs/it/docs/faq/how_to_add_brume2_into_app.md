# Come aggiungere Brume 2 all'app mobile GL.iNet?

Puoi aggiungere Brume 2 (GL-MT2500/GL-MT2500A) all'app mobile GL.iNet anche se non dispone della funzione Wi-Fi. Puoi configurarlo sia come router principale sia come router secondario.

I metodi seguenti sono applicabili anche a Brume (GL-MV1000).

## Brume 2 come router secondario

**Topology**

Qui usiamo Slate AX (GL-AXT1800) come router principale e Brume 2 (GL-MT2500) come router secondario.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Accedi al pannello di amministrazione web di Brume 2, vai su **SYSTEM** -> **Security** -> **Open Ports on Router** e apri la porta **80**.

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    Per alcuni modelli meno recenti, vai su **Firewall** -> **Open Ports on Router** e apri la porta **80**.

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Accedi al router principale e annota il **WAN IP** di Brume 2.

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Collega un telefono al Wi-Fi del router principale.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

4. Avvia l'app GL.iNet e fai clic su **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

5. Fai quindi clic su **Initialized Devices**.

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.PNG){class="glboxshadow gl-50-desktop"}

6. Inserisci il WAN IP che hai trovato prima sul router principale.

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.PNG){class="glboxshadow gl-50-desktop"}

7. Inserisci la password di accesso di Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Ora il tuo Brume 2 comparirà nell'app mobile GL.iNet.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

## Brume 2 come router principale

**Topology**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Accedi al router secondario, che in questo caso è GL-AXT1800, e impostalo in modalità Access Point.

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Collega un telefono al Wi-Fi del router secondario.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

3. Avvia l'app GL.iNet e fai clic su **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

4. Seleziona il router principale.

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.PNG){class="glboxshadow gl-50-desktop"}

5. Fai clic su **Next**.

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.PNG){class="glboxshadow gl-50-desktop"}

6. Se sei ancora collegato al Wi-Fi del router secondario, attendi semplicemente. In caso contrario, ricollegati al Wi-Fi del router secondario.

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.PNG){class="glboxshadow gl-50-desktop"}

7. Inserisci la password di accesso di Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Ora il tuo Brume 2 comparirà nell'app mobile GL.iNet.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
