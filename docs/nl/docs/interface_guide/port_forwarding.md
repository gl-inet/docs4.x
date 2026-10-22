# Port Forwarding {#port-forwarding}

**Opmerking**: deze handleiding geldt voor firmware v4.6 en hoger. Raadpleeg voor eerdere versies [Firewall](firewall.md).

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **Port Forwarding** of, vanaf firmware v4.9, **SECURITY** -> **Port Forwarding**.

Op deze pagina kun je firewallregels configureren, waaronder DMZ en port forwarding.

## DMZ {#dmz}

Met DMZ kun je één computer vanaf internet bereikbaar maken. Alle inkomende pakketten worden naar deze computer doorgestuurd.

Schakel **Enable DMZ** in. Selecteer het interne IP-adres van het hostapparaat dat alle inkomende pakketten ontvangt.

Je kunt de prioriteit van DMZ instellen. Als de DMZ-prioriteit hoger is dan die van de regels voor port forwarding, worden alle regels ongeldig. Anders worden verzoeken alleen naar het DMZ Host-apparaat doorgestuurd als voor de gebruikte poort geen regel bestaat.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding {#port-forwarding_1}

Met Port Forwarding kunnen externe computers verbinding maken met een lokale computer of server achter de firewall in het LAN, zoals web- of FTP-servers.

Klik in het gedeelte Port Forwarding op **Add** om port forwarding in te stellen.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

Voeg in het pop-upvenster een nieuwe regel voor port forwarding toe en klik op **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

- **Protocol:** kies voor deze regel `TCP`, `UDP` of `TCP and UDP`.

- **External Zone:** de opties zijn `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN` en `Guest`.

- **External Port:** de externe poortnummers. Voer één poort van 1 tot 65535 in of een bereik door het eerste en laatste nummer met een koppelteken te verbinden, zoals 501-510.

- **Internal Zone:** de opties zijn `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server` en `WAN`.

- **Internal IP:** het IP-adres dat de router aan het apparaat heeft toegewezen dat op afstand toegankelijk moet zijn.

- **Internal Port:** het interne poortnummer van het apparaat. Gebruik één poort als bij **External Port** één poort is ingesteld en het overeenkomstige bereik als daar een bereik is ingesteld. Laat dit leeg als het gelijk is aan de externe poort.

- **Description:** stel een aangepaste naam of optionele beschrijving voor de regel in.

- **Enable:** schakel deze regel in of uit.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
