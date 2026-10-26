# Hur skickar jag all data genom VPN? {#how-to-let-all-data-go-through-vpn}

Om du vill dirigera all nätverkstrafik på routern genom VPN och blockera alla internetanslutningar när VPN-anslutningen misslyckas följer du stegen nedan för att aktivera **VPN Kill Switch**.

**Obs!** Konfigurera först en VPN-klient på GL.iNet-routern innan du aktiverar VPN Kill Switch.

## För firmware v4.7 eller tidigare {#for-firmware-v47-or-earlier}

Logga in på routerns webbadministrationspanel, gå till **VPN** -> **VPN Dashboard** -> avsnittet **VPN Client** och klicka på **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Aktivera **Block Non-VPN Traffic** (kallas även Kill Switch i vissa firmwareversioner) och klicka sedan på **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Obs!** När Block Non-VPN Traffic/Kill Switch är aktiverat och VPN är inaktiverat eller frånkopplat hindras alla enheter som är anslutna till routern från att använda internet, för att förhindra DNS-läckor.

## För firmware v4.8 eller senare {#for-firmware-v48-or-later}

I firmware v4.8 har VPN Kill Switch delats upp i två lägen.

- **Tunnel Kill Switch**: Aktiveras som standard när motsvarande VPN-tunnel aktiveras.

- **Enhanced Kill Switch (in Policy Mode)**: Är inaktiverad som standard, så att all trafik som inte omfattas av VPN-tunnlarna och policyerna ovan fortfarande kan nå internet. Trafik utan VPN behåller alltså normal internetåtkomst.

### Tunnel Kill Switch {#tunnel-kill-switch}

Gå till **VPN** -> **VPN Dashboard** i routerns webbadministrationspanel.

Om du konfigurerar routern som VPN-klient aktiveras Kill Switch för VPN-tunneln som standard när VPN-anslutningen aktiveras.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Global Mode)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Policy Mode)</small>

Klicka på kugghjulsikonen bredvid tunnelns namn för att öppna **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Kill Switch för tunneln är aktiverad som standard.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Enhanced Kill Switch {#enhanced-kill-switch}

Funktionen är tillgänglig i Policy Mode.

Gå till **VPN** -> **VPN Dashboard** i routerns webbadministrationspanel, ändra VPN-läget till **Policy Mode** och leta sedan reda på avsnittet **All Other Traffic** längst ned. Avsnittet kan se något annorlunda ut beroende på firmwareversion.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

All Other Traffic är en standardtunnel som ger normal internetåtkomst för trafik som inte omfattas av VPN-tunnlarna och policyerna ovan, eller för trafik som har redundansväxlat från VPN-anslutningar. Tunneln är aktiverad som standard och kan inte vara aktiverad samtidigt som Enhanced Kill Switch.

**Obs!** Om du inaktiverar All Other Traffic kan du endast komma åt internet via VPN. All trafik som inte matchar blockeras. Inställningen åsidosätter inte varje tunnels separata Kill Switch.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
