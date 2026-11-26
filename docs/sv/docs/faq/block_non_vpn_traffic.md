# Hur skickar jag all data genom VPN? {#how-to-let-all-data-go-through-vpn}

Om du vill dirigera all nätverkstrafik på routern genom VPN och blockera alla internetanslutningar när VPN-anslutningen misslyckas följer du stegen nedan för att aktivera **VPN Kill Switch**.

**Obs!** Konfigurera först en VPN-klient på GL.iNet-routern innan du aktiverar VPN Kill Switch.

## För firmware v4.7 eller tidigare {#for-firmware-v47-or-earlier}

Logga in på routerns webbadministrationspanel, gå till **VPN** -> **VPN Dashboard** -> avsnittet **VPN Client** och klicka på **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Aktivera **Block Non-VPN Traffic** (kallas även Kill Switch i vissa firmwareversioner) och klicka sedan på **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Obs!** När Block Non-VPN Traffic/Kill Switch är aktiverat och VPN är inaktiverat eller frånkopplat hindras alla enheter som är anslutna till routern från att använda internet, för att förhindra DNS-läckor.

## För firmware v4.8 {#for-firmware-v48}

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

**All Other Traffic** är standardtunneln. Trafik som inte matchar någon av VPN-tunnlarna eller policyerna ovan, och trafik som omdirigeras hit vid VPN-redundansväxling, har normal internetåtkomst. Tunneln är aktiverad som standard. Om du inaktiverar den blockeras all sådan trafik, även trafik som annars skulle omdirigeras hit vid VPN-redundansväxling. Endast trafik som hanteras av de konfigurerade VPN-tunnlarna kan nå internet. Det ger samma skydd som **Enhanced Kill Switch**.

**Obs!** Inställningen **All Other Traffic** åsidosätter inte den separata Kill Switch-inställningen för varje tunnel.

## För firmware v4.9 och senare {#for-firmware-v49-and-above}

Från och med firmware v4.9 finns två typer av VPN Kill Switch, **Tunnel Kill Switch** och **Enhanced Kill Switch**.

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

Gå till **VPN** -> **VPN Dashboard** i routerns webbadministrationspanel.

Om du konfigurerar routern som VPN-klient aktiveras Kill Switch för VPN-tunneln som standard när VPN-anslutningen aktiveras.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Klicka på kugghjulsikonen bredvid tunnelns namn för att öppna **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Kill Switch för tunneln är aktiverad som standard.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Enhanced Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

Gå till **VPN** -> **VPN Dashboard** i routerns webbadministrationspanel. Klicka sedan på kugghjulsikonen uppe till höger.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

För trafikpolicyn finns alternativen **Allow Non-VPN Traffic** och **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic**: Aktiverat som standard. Trafik som inte matchar någon av VPN-tunnlarna eller policyerna ovan, och trafik som omdirigeras hit vid VPN-redundansväxling, har normal internetåtkomst.

- **Enhanced Kill Switch**: När alternativet är aktiverat måste alla enheter använda VPN för att komma åt internet. Trafik som inte matchar någon VPN-tunnel blockeras. Inställningen åsidosätter inte den separata Kill Switch-inställningen för varje tunnel.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
