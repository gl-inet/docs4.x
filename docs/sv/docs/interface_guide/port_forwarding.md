# Port Forwarding {#port-forwarding}

**Obs!** Guiden gäller firmware v4.6 och senare. För tidigare versioner, se [Firewall](firewall.md).

---

Öppna **NETWORK** -> **Port Forwarding**, eller **SECURITY** -> **Port Forwarding** i firmware v4.9 och senare.

På sidan konfigurerar du brandväggsregler för DMZ och portvidarebefordran.

## DMZ {#dmz}

Med DMZ kan du exponera en dator mot internet så att alla inkommande paket omdirigeras till den.

Aktivera **Enable DMZ** och välj den interna IP-adressen som ska ta emot alla inkommande paket.

Du kan ange DMZ-prioritet. Om den är högre än portvidarebefordringsreglerna ogiltigförklaras reglerna. Annars används DMZ Host endast när porten saknar motsvarande regel.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding {#port-forwarding_1}

Port Forwarding lets remote computers connect to a local computer or server behind the router's firewall in the LAN (such as web servers, FTP servers, etc).

Klicka på **Add** i avsnittet Port Forwarding.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

Lägg till en regel i popup-fönstret och klicka på **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

- **Protocol:** Choose `TCP`, `UDP`, or both `TCP and UDP` for this rule.

- **External Zone:** Välj `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN` eller `Guest`.

- **External Port:** Ange en port från 1 till 65535 eller ett intervall med bindestreck, till exempel 501-510.

- **Internal Zone:** Välj `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server` eller `WAN`.

- **Internal IP:** IP-adressen som routern tilldelar enheten som ska fjärranslutas.

- **Internal Port:** Enhetens interna port eller motsvarande intervall. Lämna tomt om det är samma som External Port.

- **Description:** Set a custom name or add a description for this rule (optional).

- **Enable:** Toggle to enable or disable this rule.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
