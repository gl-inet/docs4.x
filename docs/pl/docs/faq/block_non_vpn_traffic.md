# Jak skierować cały ruch przez VPN?

Jeśli chcesz, aby cały ruch sieciowy routera był kierowany przez VPN, a po awarii VPN wszystkie połączenia z Internetem zostały zablokowane, wykonaj poniższe kroki, aby włączyć **VPN Kill Switch**.

**Uwaga**: Przed włączeniem VPN Kill Switch najpierw skonfiguruj klient VPN na routerze GL.iNet.

## Dla firmware v4.7 lub starszego

Zaloguj się do panelu administracyjnego routera, przejdź do sekcji **VPN** -> **VPN Dashboard** -> **VPN Client**, a następnie kliknij **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Włącz **Block Non-VPN Traffic** (w niektórych wersjach firmware funkcja ta nazywa się również Kill Switch), a następnie kliknij **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Uwaga:** Gdy **Block Non-VPN Traffic** / Kill Switch jest włączony, a VPN zostanie wyłączony lub rozłączony, wszystkie urządzenia podłączone do routera utracą dostęp do Internetu, aby zapobiec wyciekom DNS.

## Dla firmware v4.8 lub nowszego

W firmware v4.8 VPN Kill Switch został podzielony na dwa tryby.

- **Tunnel Kill Switch**: jest domyślnie włączony po aktywowaniu odpowiedniego tunelu VPN.

- **Enhanced Kill Switch (in Policy Mode)**: jest domyślnie wyłączony, aby cały ruch nieobjęty powyższymi tunelami VPN i zasadami nadal miał dostęp do Internetu. Krótko mówiąc, utrzymuje normalny dostęp do Internetu dla ruchu spoza VPN.

### Kill Switch tunelu

W panelu administracyjnym routera przejdź do **VPN** -> **VPN Dashboard**.

Jeśli router jest skonfigurowany jako klient VPN, Kill Switch dla tego tunelu VPN jest domyślnie włączony po aktywacji VPN.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN tryb globalny)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN tryb polityk)</small>

Kliknij ikonę koła zębatego obok nazwy tunelu, aby otworzyć **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Kill Switch dla tego tunelu jest domyślnie włączony.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Rozszerzony Kill Switch

Ta funkcja jest dostępna w **Policy Mode** (trybie polityk).

W panelu administracyjnym routera przejdź do **VPN** -> **VPN Dashboard**, przełącz tryb VPN na **Policy Mode**, a następnie znajdź na dole sekcję **All Other Traffic**. Wygląd tej sekcji może się nieznacznie różnić w zależności od wersji firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** (cały pozostały ruch) to domyślny tunel, który zapewnia normalny dostęp do Internetu dla ruchu nieobjętego powyższymi tunelami VPN i zasadami oraz dla ruchu przełączonego awaryjnie z połączeń VPN. Ten tunel jest domyślnie włączony i wzajemnie wyklucza się z rozszerzonym Kill Switch.

**Uwaga**: Jeśli wyłączysz **All Other Traffic**, dostęp do Internetu będzie możliwy tylko przez VPN. Cały niepasujący ruch zostanie zablokowany. To ustawienie nie zastępuje indywidualnego Kill Switch dla każdego tunelu.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
