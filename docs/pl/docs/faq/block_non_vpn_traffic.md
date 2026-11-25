# Jak skierować cały ruch przez VPN? {#how-to-let-all-data-go-through-vpn}

Jeśli chcesz, aby cały ruch sieciowy routera był kierowany przez VPN, a po awarii VPN wszystkie połączenia z Internetem zostały zablokowane, wykonaj poniższe kroki, aby włączyć **VPN Kill Switch**.

**Uwaga**: Przed włączeniem VPN Kill Switch najpierw skonfiguruj klient VPN na routerze GL.iNet.

## Dla firmware v4.7 lub starszego {#for-firmware-v47-or-earlier}

Zaloguj się do panelu administracyjnego routera, przejdź do sekcji **VPN** -> **VPN Dashboard** -> **VPN Client**, a następnie kliknij **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Włącz **Block Non-VPN Traffic** (w niektórych wersjach firmware funkcja ta nazywa się również Kill Switch), a następnie kliknij **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Uwaga:** Gdy **Block Non-VPN Traffic** / Kill Switch jest włączony, a VPN zostanie wyłączony lub rozłączony, wszystkie urządzenia podłączone do routera utracą dostęp do Internetu, aby zapobiec wyciekom DNS.

## Dla firmware v4.8 {#for-firmware-v48}

W firmware v4.8 VPN Kill Switch został podzielony na dwa tryby.

- **Tunnel Kill Switch**: jest domyślnie włączony po aktywowaniu odpowiedniego tunelu VPN.

- **Enhanced Kill Switch (in Policy Mode)**: jest domyślnie wyłączony, aby cały ruch nieobjęty powyższymi tunelami VPN i zasadami nadal miał dostęp do Internetu. Krótko mówiąc, utrzymuje normalny dostęp do Internetu dla ruchu spoza VPN.

### Kill Switch tunelu {#tunnel-kill-switch}

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

### Rozszerzony Kill Switch {#enhanced-kill-switch}

Ta funkcja jest dostępna w **Policy Mode** (trybie polityk).

W panelu administracyjnym routera przejdź do **VPN** -> **VPN Dashboard**, przełącz tryb VPN na **Policy Mode**, a następnie znajdź na dole sekcję **All Other Traffic**. Wygląd tej sekcji może się nieznacznie różnić w zależności od wersji firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** to domyślny tunel, który zapewnia normalny dostęp do internetu ruchowi niedopasowanemu do żadnego z powyższych tuneli VPN ani reguł oraz ruchowi skierowanemu tutaj przez awaryjne przełączenie VPN. Tunel jest domyślnie włączony. Jego wyłączenie blokuje cały ten ruch, w tym ruch, który w razie awarii połączenia VPN zostałby tutaj przekierowany. Dostęp do internetu ma wtedy tylko ruch obsługiwany przez skonfigurowane tunele VPN, tak jak w przypadku **Enhanced Kill Switch**.

**Uwaga:** Ustawienie **All Other Traffic** nie zastępuje funkcji Kill Switch poszczególnych tuneli.

## Dla firmware v4.9 i nowszych {#for-firmware-v49-and-above}

W firmware v4.9 i nowszych wersjach są dostępne dwa rodzaje funkcji VPN Kill Switch: **Tunnel Kill Switch** i **Enhanced Kill Switch**.

### Kill Switch tunelu {#for-firmware-v49-and-above-tunnel-kill-switch}

W panelu administracyjnym routera przejdź do **VPN** -> **VPN Dashboard**.

Jeśli router jest skonfigurowany jako klient VPN, Kill Switch dla tego tunelu VPN jest domyślnie włączony po aktywacji VPN.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Kliknij ikonę koła zębatego obok nazwy tunelu, aby otworzyć **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Kill Switch dla tego tunelu jest domyślnie włączony.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Rozszerzony Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

W panelu administracyjnym routera przejdź do **VPN** -> **VPN Dashboard**, a następnie kliknij ikonę koła zębatego w prawym górnym rogu.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

Reguły ruchu można ustawić na dwa sposoby: **Allow Non-VPN Traffic** lub **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic**: Opcja jest domyślnie włączona. Zapewnia normalny dostęp do internetu ruchowi niedopasowanemu do żadnego z powyższych tuneli VPN ani reguł oraz ruchowi skierowanemu tutaj przez awaryjne przełączenie VPN.

- **Enhanced Kill Switch**: Po włączeniu tej opcji wszystkie urządzenia muszą korzystać z VPN, aby uzyskać dostęp do internetu. Ruch niedopasowany do żadnego tunelu VPN jest blokowany. To ustawienie nie zastępuje funkcji Kill Switch poszczególnych tuneli VPN.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
