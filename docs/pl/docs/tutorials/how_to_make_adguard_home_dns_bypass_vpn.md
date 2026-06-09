# Jak sprawić, aby DNS AdGuard Home omijał tunel VPN

Zazwyczaj VPN i AdGuard Home mogą działać jednocześnie na routerach GL.iNet. Problemy nie występują, gdy AdGuard Home nie jest skonfigurowany do obsługi zapytań DNS.

Jeśli jednak skonfigurujesz AdGuard Home do zarządzania całym ruchem DNS i przekazywania zapytań do **publicznych serwerów DNS nadrzędnych**, włączenie VPN spowoduje błędy w rozwiązywaniu nazw DNS.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home włączony i obsługuje zapytania DNS)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(Ustawienia DNS nadrzędnych AdGuard Home)</small>

Domyślnie cały ruch wychodzący jest kierowany przez tunel VPN. Wymusza to, że ruch DNS AdGuard Home do serwerów nadrzędnych przechodzi przez VPN, który nie może dotrzeć do Twoich publicznych serwerów DNS nadrzędnych. W rezultacie wszyscy podłączeni klienci nie będą mogli rozwiązywać nazw domen.

Aby AdGuard Home działał poprawnie, gdy VPN jest aktywny, możesz dodać trasę statyczną w LuCI, która przekieruje ruch DNS do serwerów nadrzędnych na zwykłą bramę WAN i ominie tunel VPN. Postępuj zgodnie z poniższymi krokami.

1. Zaloguj się do panelu administracyjnego routera przez przeglądarkę i przejdź do **SYSTEM** -> **Advanced Settings** ->** Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Zaloguj się przy użyciu tego samego hasła administratora.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. W LuCI przejdź do **Network** -> **Routing**, a następnie kliknij **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Utwórz nową trasę statyczną dla adresów swoich serwerów DNS nadrzędnych.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interfejs: Wybierz fizyczny interfejs WAN **wan**.
    
    - Typ trasy: Pozostaw wartość domyślną.
    
    - Cel: `[Your Public Upstream DNS Server]/32`
    
        Możesz użyć polecenia `nslookup`, aby sprawdzić rzeczywisty adres IP swojego publicznego serwera DNS nadrzędnego.
    
    - Brama: `[Your WAN Upstream Gateway IP]`
    
        Zazwyczaj jest to adres IP modemu lub bramy dostawcy internetu, na przykład `192.168.0.1`. Znajdziesz go na stronie stanu połączenia internetowego routera.

    Ta trasa zapewnia, że zapytania DNS AdGuard Home do serwerów nadrzędnych omijają tunel VPN i przechodzą bezpośrednio przez połączenie WAN.

4. Zapisz i zastosuj ustawienia. AdGuard Home wznowi normalne rozwiązywanie nazw DNS.

5. Przetestuj serwery DNS nadrzędne.

    Możesz zweryfikować swoje serwery DNS nadrzędne bezpośrednio w interfejsie AdGuard Home.
    
    W panelu administracyjnym routera przejdź do **APPLICATIONS** -> **AdGuard Home**, a następnie kliknij **Settings Page**, aby otworzyć panel AdGuard Home.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    W panelu AdGuard Home przejdź do **Settings** -> **DNS settings** -> **Upstream DNS servers** i kliknij **Test upstreams**. Wyniki pojawią się po prawej stronie.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Wskazówka**: Jeśli masz więcej niż jeden serwer DNS i są one mieszanką adresów IP i nazw domen, możesz rozdzielić DNS AdGuard od DNS VPN, co może być łatwiejsze niż użycie trasy statycznej. 

Zaloguj się przez SSH do routera GL.iNet i uruchom następujące polecenia, aby wymusić, że AdGuard Home będzie wysyłać zapytania DNS tylko przez WAN.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
