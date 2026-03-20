# Wie leite ich den gesamten Datenverkehr über ein VPN?

Wenn Sie möchten, dass der gesamte Netzwerkverkehr auf dem Router über das VPN geleitet wird und alle Internetverbindungen blockiert werden, wenn das VPN ausfällt, führen Sie bitte die folgenden Schritte aus, um den **VPN Kill Switch** zu aktivieren.

**Hinweis**: Richten Sie zuerst den VPN-Client auf Ihrem GL.iNet-Router ein, bevor Sie den VPN Kill Switch aktivieren.

## Für Firmware v4.7 oder früher

Melden Sie sich im Web-Admin-Panel Ihres Routers an, navigieren Sie zu **VPN** -> **VPN Dashboard** -> **VPN Client** und klicken Sie auf **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Aktivieren Sie **Block Non-VPN Traffic** (in einigen Firmware-Versionen auch Kill Switch genannt) und klicken Sie dann auf **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Hinweis:** Wenn **Block Non-VPN Traffic** / Kill Switch aktiviert ist und Ihr VPN deaktiviert oder getrennt wird, wird allen mit dem Router verbundenen Geräten der Internetzugriff verweigert, um DNS-Lecks zu verhindern.

## Für Firmware v4.8 oder neuer

In Firmware v4.8 wurde der VPN Kill Switch in zwei Modi aufgeteilt.

- **Tunnel Kill Switch**: Er ist standardmäßig aktiviert, wenn der entsprechende VPN-Tunnel aktiviert wird.

- **Erweiterter Kill Switch (im Richtlinienmodus)**: Er ist standardmäßig deaktiviert, damit der gesamte Datenverkehr, der nicht von den oben stehenden VPN-Tunneln und Richtlinien abgedeckt wird, weiterhin auf das Internet zugreifen kann. Kurz gesagt: Er erhält den normalen Internetzugang für Nicht-VPN-Datenverkehr aufrecht.

### Tunnel Kill Switch

Navigieren Sie im Web-Admin-Panel des Routers zu **VPN** -> **VPN Dashboard**.

Wenn Sie Ihren Router als VPN-Client eingerichtet haben, ist der Kill Switch für diesen VPN-Tunnel standardmäßig aktiviert, sobald das VPN aktiviert wird.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Globaler Modus)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Richtlinienmodus)</small>

Klicken Sie auf das Zahnradsymbol neben dem Tunnelnamen, um **Tunnel Options** zu öffnen.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Der Kill Switch für diesen Tunnel ist standardmäßig aktiviert.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Erweiterter Kill Switch

Diese Funktion ist im Richtlinienmodus verfügbar.

Navigieren Sie im Web-Admin-Panel des Routers zu **VPN** -> **VPN Dashboard**, wechseln Sie den VPN-Modus zu **Policy Mode** und suchen Sie dann unten nach dem Abschnitt **All Other Traffic**. Dieser Abschnitt kann je nach Firmware-Version leicht unterschiedlich aussehen.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** ist ein Standard-Tunnel, der den normalen Internetzugang für Datenverkehr sicherstellt, der nicht von den oben stehenden VPN-Tunneln und Richtlinien abgedeckt wird, oder für Datenverkehr, der per Failover von VPN-Verbindungen übernommen wurde. Dieser Tunnel ist standardmäßig aktiviert und schließt sich gegenseitig mit dem erweiterten Kill Switch aus.

**Hinweis**: Wenn Sie **All Other Traffic** deaktivieren, können Sie nur noch über VPN auf das Internet zugreifen. Jeder nicht zugeordnete Datenverkehr wird blockiert. Diese Einstellung setzt den individuellen Kill Switch für jeden Tunnel nicht außer Kraft.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.

