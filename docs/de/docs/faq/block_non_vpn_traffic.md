# Wie leite ich den gesamten Datenverkehr über ein VPN? {#how-to-let-all-data-go-through-vpn}

Wenn Sie möchten, dass der gesamte Netzwerkverkehr auf dem Router über das VPN geleitet wird und alle Internetverbindungen blockiert werden, wenn das VPN ausfällt, führen Sie bitte die folgenden Schritte aus, um den **VPN Kill Switch** zu aktivieren.

**Hinweis**: Richten Sie zuerst den VPN-Client auf Ihrem GL.iNet-Router ein, bevor Sie den VPN Kill Switch aktivieren.

## Für Firmware v4.7 oder früher {#for-firmware-v47-or-earlier}

Melden Sie sich im Web-Admin-Panel Ihres Routers an, navigieren Sie zu **VPN** -> **VPN Dashboard** -> **VPN Client** und klicken Sie auf **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Aktivieren Sie **Block Non-VPN Traffic** (in einigen Firmware-Versionen auch Kill Switch genannt) und klicken Sie dann auf **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Hinweis:** Wenn **Block Non-VPN Traffic** / Kill Switch aktiviert ist und Ihr VPN deaktiviert oder getrennt wird, wird allen mit dem Router verbundenen Geräten der Internetzugriff verweigert, um DNS-Lecks zu verhindern.

## Für Firmware v4.8 {#for-firmware-v48}

In Firmware v4.8 wurde der VPN Kill Switch in zwei Modi aufgeteilt.

- **Tunnel Kill Switch**: Er ist standardmäßig aktiviert, wenn der entsprechende VPN-Tunnel aktiviert wird.

- **Erweiterter Kill Switch (im Richtlinienmodus)**: Er ist standardmäßig deaktiviert, damit der gesamte Datenverkehr, der nicht von den oben stehenden VPN-Tunneln und Richtlinien abgedeckt wird, weiterhin auf das Internet zugreifen kann. Kurz gesagt: Er erhält den normalen Internetzugang für Nicht-VPN-Datenverkehr aufrecht.

### Tunnel Kill Switch {#tunnel-kill-switch}

Navigieren Sie im Web-Admin-Panel des Routers zu **VPN** -> **VPN Dashboard**.

Wenn Sie Ihren Router als VPN-Client eingerichtet haben, ist der Kill Switch für diesen VPN-Tunnel standardmäßig aktiviert, sobald das VPN aktiviert wird.

![global mode kill switch](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Globaler Modus)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Richtlinienmodus)</small>

Klicken Sie auf das Zahnradsymbol neben dem Tunnelnamen, um **Tunnel Options** zu öffnen.

![tunnel options 1](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Der Kill Switch für diesen Tunnel ist standardmäßig aktiviert.

![tunnel options 2](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Erweiterter Kill Switch {#enhanced-kill-switch}

Diese Funktion ist im Richtlinienmodus verfügbar.

Navigieren Sie im Web-Admin-Panel des Routers zu **VPN** -> **VPN Dashboard**, wechseln Sie den VPN-Modus zu **Policy Mode** und suchen Sie dann unten nach dem Abschnitt **All Other Traffic**. Dieser Abschnitt kann je nach Firmware-Version leicht unterschiedlich aussehen.

![all other traffic](https://static.gl-inet.com/docs/router/de/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** dient als Standardtunnel und ermöglicht den normalen Internetzugang für Datenverkehr, der keinem der oben genannten VPN-Tunnel und keiner der Richtlinien entspricht oder bei einem VPN-Failover hierher umgeleitet wird. Die Option ist standardmäßig aktiviert. Wenn Sie sie deaktivieren, wird dieser gesamte Datenverkehr blockiert, einschließlich des Datenverkehrs, der sonst bei einem VPN-Failover weitergeleitet würde. Damit gelangt nur Datenverkehr, der über einen konfigurierten VPN-Tunnel läuft, ins Internet. Der erweiterte Kill Switch bietet denselben Schutz.

**Hinweis**: Die Einstellung **All Other Traffic** setzt den Kill Switch eines einzelnen Tunnels nicht außer Kraft.

## Für Firmware v4.9 und höher {#for-firmware-v49-and-above}

Ab Firmware v4.9 stehen zwei Arten des VPN Kill Switch zur Verfügung, **Tunnel Kill Switch** und **Enhanced Kill Switch**.

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

Navigieren Sie im Web-Admin-Panel des Routers zu **VPN** -> **VPN Dashboard**.

Wenn Sie Ihren Router als VPN-Client eingerichtet haben, ist der Kill Switch für diesen VPN-Tunnel standardmäßig aktiviert, sobald Sie das VPN aktivieren.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Klicken Sie auf das Zahnradsymbol neben dem Tunnelnamen, um **Tunnel Options** zu öffnen.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Der Kill Switch für diesen Tunnel ist standardmäßig aktiviert.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Erweiterter Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

Navigieren Sie im Web-Admin-Panel des Routers zu **VPN** -> **VPN Dashboard** und klicken Sie oben rechts auf das Zahnradsymbol.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

Für die Datenverkehrsrichtlinie stehen die Optionen **Allow Non-VPN Traffic** und **Enhanced Kill Switch** zur Verfügung.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic** ist standardmäßig aktiviert. Diese Option ermöglicht den normalen Internetzugang für Datenverkehr, der keinem der oben genannten VPN-Tunnel und keiner der Richtlinien entspricht oder bei einem VPN-Failover hierher umgeleitet wird.

- **Enhanced Kill Switch** erzwingt bei Aktivierung den Internetzugang über ein VPN für alle Geräte. Datenverkehr, der keinem VPN-Tunnel entspricht, wird blockiert. Diese Einstellung setzt den für einzelne VPN-Tunnel konfigurierten Kill Switch nicht außer Kraft.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.

