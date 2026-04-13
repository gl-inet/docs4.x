# Wsparcie techniczne przez GoodCloud

Czasami konieczne jest udostępnienie urządzenia przez GoodCloud, aby uzyskać wsparcie techniczne od GL.iNet. Ten przewodnik pokazuje, jak udostępnić urządzenie zespołowi wsparcia technicznego GL.iNet.

## Włącz GoodCloud i zdalny dostęp

Przed udostępnieniem urządzenia zespołowi wsparcia technicznego GL.iNet upewnij się, że router ma dodatkowe połączenie z internetem zapewniające stabilność. Skonfiguruj połączenie Ethernet lub Repeater jako zapasowe połączenie failover i sprawdź, czy działa prawidłowo.

Następnie zaloguj się do panelu administracyjnego WWW routera, aby włączyć GoodCloud i zdalny dostęp.

- **Dla wersji firmware 4.7.x lub nowszej**

    Przejdź do **CLOUD SERVICES** -> **GoodCloud**, kliknij **Get Started** i zaloguj się do swojego konta Cloud w prawym górnym rogu. Jeśli nie masz konta, najpierw je zarejestruj.

    ![get started log in](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/get_started_v4.7.x.png){class="glboxshadow"}
    
    Po zalogowaniu urządzenie zostanie automatycznie powiązane z Twoim kontem Cloud. 
    
    Przejdź na stronę **GoodCloud**, włącz **Remote SSH** oraz **Remote Web Access**, a następnie kliknij **Apply**.

    ![enable remote access 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.7.x.png){class="glboxshadow"}

- **Dla wersji firmware 4.6.x lub starszej**

    Przejdź do **APPLICATIONS** -> **GoodCloud**, włącz **GoodCloud**, **Remote SSH** i **Remote Web Access**, zaznacz **Terms of Service & Privacy Policy**, a następnie kliknij **Apply**.

    ![enable GoodCloud 4.6](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.6.x.png){class="glboxshadow"}

## Zaloguj się do konta Cloud i powiąż urządzenie

Jeśli router działa z firmware v4.7 lub nowszym, możesz zarejestrować konto w panelu administracyjnym WWW routera i zalogować się bezpośrednio. Po zalogowaniu bieżące urządzenie zostanie automatycznie powiązane z Twoim kontem Cloud. 

Jeśli router działa z firmware v4.6 lub starszym, wykonaj poniższe kroki, aby zalogować się do konta i powiązać urządzenie.

1. Otwórz [GoodCloud](https://www.goodcloud.xyz){target="_blank"} i zaloguj się do swojego konta. Jeśli nie masz konta, najpierw je zarejestruj.

2. Powiąż urządzenie z GoodCloud. Skorzystaj z [tego linku](../interface_guide/cloud.md#add-device-in-your-account).

## Udostępnij urządzenie zespołowi wsparcia technicznego GL.iNet

1. Otwórz [GoodCloud](https://www.goodcloud.xyz){target="_blank"} i zaloguj się.

2. Przejdź do **Devices** -> **Bound Devices** i kliknij urządzenie, które chcesz udostępnić. 

    ![bound devices](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/bound_devices.png){class="glboxshadow"}

3. Zostaniesz przeniesiony na stronę szczegółów urządzenia. Kliknij kartę **SHARE** i **Share Device**, jak pokazano poniżej. 

    ![share device](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device.png){class="glboxshadow"}

    Następnie udostępnij urządzenie zespołowi wsparcia technicznego GL.iNet. Aby lepiej zabezpieczyć sieć prywatną, włącz **Auto Expire Sharing** i ustaw wygaśnięcie po 7 dniach. Następnie kliknij **Confirm**.

    ![share device with GL.iNet support](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device_confirm.png){class="glboxshadow"}

**Oświadczenie o ochronie prywatności**

1. Urządzenia udostępnione zespołowi wsparcia technicznego GL.iNet są wykorzystywane WYŁĄCZNIE do celów diagnostycznych. Zespół wsparcia GL.iNet nie będzie przechowywać, tworzyć kopii zapasowych ani uzyskiwać dostępu do Twoich prywatnych informacji.

2. Aby zwiększyć bezpieczeństwo hasła, zalecamy zmianę hasła logowania do panelu administracyjnego WWW na tymczasowe przed udostępnieniem urządzenia zespołowi wsparcia GL.iNet. Po zakończeniu diagnostyki możesz przywrócić swoje zwykłe hasło.

## Przekaż informacje zespołowi wsparcia technicznego GL.iNet

Po udostępnieniu urządzenia przekaż odpowiedniemu pracownikowi wsparcia technicznego GL.iNet przez e-mail lub prywatną wiadomość na forum **adres MAC** routera oraz **hasło administratora**, aby umożliwić zdalną diagnostykę. 

**Nie wysyłaj tych informacji jednocześnie e-mailem i prywatną wiadomością.**

- **przez e-mail**: Wyślij te informacje do odpowiedniego pracownika wsparcia technicznego GL.iNet na adres [support@gl-inet.com](mailto:support@gl-inet.com).

- **przez prywatną wiadomość na oficjalnym forum**: Wyślij PM (prywatną wiadomość) do odpowiedniego pracownika wsparcia technicznego GL.iNet na [oficjalnym forum](https://forum.gl-inet.com){target="_blank"}. 

    Oto kroki wysłania prywatnej wiadomości na forum.

    1. Przejdź do [oficjalnego forum](https://forum.gl-inet.com){target="_blank"}.
    2. Kliknij nazwę użytkownika pracownika wsparcia GL.iNet, z którym się kontaktujesz.
    3. Kliknij przycisk **Message**, aby wysłać prywatną wiadomość.

        ![Jak wysłać prywatną wiadomość](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/PM_via_forum.gif){class="glboxshadow"}

Czasami nowi użytkownicy mogą nie mieć możliwości wysłania prywatnej wiadomości do zespołu wsparcia technicznego GL.iNet. W takim przypadku możesz odpowiedzieć w tym samym wątku, w którym prowadzisz rozmowę, i poprosić pracownika wsparcia technicznego, aby najpierw wysłał Ci prywatną wiadomość.

Prosimy, aby **NIE** udostępniać publicznie danych urządzenia; przekazuj je wyłącznie zespołowi wsparcia technicznego GL.iNet przez PM.

Po rozwiązaniu problemu anuluj udostępnianie i zmień hasło administratora routera.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
