# Jak włączyć tryb OpenVPN TAP-S2S na routerach GL.iNet?

## Scenariusze użycia

Po włączeniu trybu TAP-S2S urządzenie klienta OpenVPN może zdalnie uzyskać dostęp do urządzenia serwera OpenVPN, a urządzenie serwera OpenVPN może również zdalnie uzyskać dostęp do urządzenia klienta OpenVPN. Wadą jest jednak to, że reguły VPN ustawione przez samego klienta OpenVPN nie będą obowiązywać po włączeniu trybu TAP-S2S.

## TAP-S2S vs tryb TUN

Topologia sieci

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

Tryby TAP-S2S i TUN mają tę samą metodę połączenia fizycznego, ale ich metody połączenia logicznego są różne. Oto różnice:

1. Gdy urządzenia po stronie LAN GL-X3000 uzyskują dostęp do backendu zarządzania GL-MT6000, tryb TAP-S2S nie używa wirtualnego adresu IP, ale tryb TUN używa.
2. Gdy urządzenia po stronie LAN GL-X3000 uzyskują dostęp do backendu zarządzania GL-X3000, tryb TAP-S2S używa wirtualnego adresu IP, ale tryb TUN nie.
3. Gdy urządzenie po stronie LAN GL-X3000 zna adres IP urządzenia po stronie LAN GL-MT6000, tryb TAP-S2S umożliwia bezpośredni zdalny dostęp, ale tryb TUN nie może uzyskać dostępu bezpośrednio bez włączenia dodatkowych ustawień.
4. W trybie TAP-S2S GL-X3000 musi przechodzić przez GL-MT6000, aby uzyskać dostęp do internetu, podczas gdy w trybie TUN GL-X3000 może bezpośrednio uzyskać dostęp do internetu. Dlatego w trybie TAP-S2S reguły VPN ustawione przez GL-X3000 nie obowiązują i należy stosować reguły VPN ustawione przez GL-MT6000.

## Przewodnik

Najpierw użyj routera (zakładany jako GL-MT6000) z publicznym adresem IP, aby otworzyć serwer OpenVPN, ustaw tryb urządzenia na **TAP-S2S**, kliknij Apply, a następnie kliknij **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

Dodatkowo użyj routera (zakładany jako GL-X3000) z publicznym adresem IP, aby otworzyć klienta OpenVPN, zaimportuj plik konfiguracyjny pobrany w powyższych krokach, kliknij **Apply**, a następnie włącz funkcję.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

W tym momencie adres IP routera GL-X3000 się zmieni. Możesz zalogować się do panelu zarządzania GL-MT6000, otworzyć **Clients** i znaleźć nowy adres IP GL-X3000.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Jeśli GL-MT6000 straci połączenie sieciowe lub wyłączy serwer OpenVPN, lub GL-X3000 wyłączy klienta OpenVPN, adres IP GL-X3000 zostanie przywrócony.

Uwagi:

- Oba urządzenia muszą być zaktualizowane do wersji v4.5, w przeciwnym razie nie będą mogły się połączyć;
- TAP-S2S działa tylko z trybem globalnym VPN, dostosowuje się automatycznie po włączeniu OpenVPN.
- Po włączeniu tej funkcji nie można używać następujących funkcji: serwer VPN, Adguard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping itp.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
