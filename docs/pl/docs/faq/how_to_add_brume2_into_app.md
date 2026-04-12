# Jak dodać Brume 2 do aplikacji mobilnej GL.iNet?

Możesz dodać Brume 2 (GL-MT2500/GL-MT2500A) do aplikacji mobilnej GL.iNet, nawet jeśli urządzenie nie obsługuje Wi-Fi. Możesz skonfigurować je jako router główny albo router dodatkowy.

Poniższe metody dotyczą również modelu Brume (GL-MV1000).

## Brume 2 jako router dodatkowy

**Topologia**

W tym przykładzie Slate AX (GL-AXT1800) jest routerem głównym, a Brume 2 (GL-MT2500) routerem dodatkowym.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Zaloguj się do panelu administracyjnego WWW Brume 2, przejdź do **SYSTEM** -> **Security** -> **Open Ports on Router** i otwórz port **80**.

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    W przypadku niektórych starszych modeli przejdź do **Firewall** -> **Open Ports on Router** i otwórz port **80**.

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Zaloguj się do routera głównego i zanotuj **WAN IP** urządzenia Brume 2.

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Połącz telefon z siecią Wi-Fi routera głównego.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

4. Uruchom aplikację GL.iNet i kliknij **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

5. Następnie kliknij **Initialized Devices**.

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.PNG){class="glboxshadow gl-50-desktop"}

6. Wpisz adres WAN IP odczytany wcześniej na routerze głównym.

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.PNG){class="glboxshadow gl-50-desktop"}

7. Wpisz hasło logowania do Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Teraz Brume 2 pojawi się w aplikacji mobilnej GL.iNet.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

## Brume 2 jako router główny

**Topologia**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Zaloguj się do routera dodatkowego, którym w tym przypadku jest GL-AXT1800, i ustaw go w trybie Access Point.

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Połącz telefon z siecią Wi-Fi routera dodatkowego.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"} 

3. Uruchom aplikację GL.iNet i kliknij **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

4. Wybierz router główny.

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.PNG){class="glboxshadow gl-50-desktop"}

5. Kliknij **Next**

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.PNG){class="glboxshadow gl-50-desktop"}

6. Jeśli nadal masz połączenie z Wi-Fi routera dodatkowego, po prostu poczekaj. Jeśli nie, połącz się z nim ponownie.

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.PNG){class="glboxshadow gl-50-desktop"}

7. Wpisz hasło logowania do Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Teraz Brume 2 pojawi się w aplikacji mobilnej GL.iNet.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
