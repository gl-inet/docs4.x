# Jak zaktualizować certyfikaty serwera OpenVPN?

W tym poradniku wyjaśniamy, jak zaktualizować certyfikaty serwera OpenVPN na routerach GL.iNet.

**Uwaga**: Ten proces wymaga zaktualizowania certyfikatu Root CA, co unieważni wszystkie istniejące certyfikaty klientów (osadzone w plikach konfiguracyjnych). Aby klienci OpenVPN mogli ponownie połączyć się z serwerem, musisz ponownie wyeksportować wszystkie pliki konfiguracyjne.

1. Zaloguj się do panelu administracyjnego routera i przejdź do **VPN** -> **OpenVPN Server**.

    Jeśli serwer OpenVPN jest uruchomiony, zatrzymaj usługę.
    
2. Na karcie **Configuration** kliknij **Advanced Configuration**, aby rozwinąć ustawienia.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Znajdź **Server Root Certificate** i usuń całą zawartość pola tekstowego.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Powiązane pola **Server Certificate** i **Server Key** również zostaną automatycznie wyczyszczone, jak pokazano poniżej.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Pozostaw wszystkie trzy pola puste i kliknij **Apply** na dole strony. Nowe certyfikaty zostaną wygenerowane automatycznie i uzupełnią te pola.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. Certyfikaty serwera OpenVPN są już zaktualizowane. Kliknij **Export Client Configuration** na dole strony, aby wyeksportować nowe pliki konfiguracyjne dla urządzeń, które będą się łączyć.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
