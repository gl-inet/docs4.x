# How to let all data go through VPN? {#how-to-let-all-data-go-through-vpn}

Als je al het netwerkverkeer via de VPN wilt routeren en alle internetverbindingen wilt blokkeren wanneer de VPN uitvalt, volg je de onderstaande stappen om **VPN Kill Switch** in te schakelen.

**Note**: Set up VPN client on your GL.iNet router first before enabling VPN Kill Switch.

## For firmware v4.7 or earlier {#for-firmware-v47-or-earlier}

Log in to your router's web Admin Panel, navigate to **VPN** -> **VPN Dashboard** -> **VPN Client** section, and click **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Schakel **Block Non-VPN Traffic** in, in sommige firmwareversies Kill Switch genoemd, en klik op **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Opmerking:** als Block Non-VPN Traffic / Kill Switch is ingeschakeld en de VPN is uitgeschakeld of verbroken, wordt internettoegang voor alle verbonden apparaten geblokkeerd om DNS-lekken te voorkomen.

## Voor firmware v4.8 {#for-firmware-v48}

In firmware v4.8 is VPN Kill Switch opgesplitst in twee modi.

- **Tunnel Kill Switch**: standaard ingeschakeld wanneer de bijbehorende VPN-tunnel wordt geactiveerd.

- **Enhanced Kill Switch (in Policy Mode)**: standaard uitgeschakeld zodat verkeer dat niet onder de bovenstaande VPN-tunnels en beleidsregels valt internettoegang houdt.

### Tunnel Kill Switch {#tunnel-kill-switch}

On the router's web Admin Panel, navigate to **VPN** -> **VPN Dashboard**.

Als je de router als VPN-client instelt, wordt Kill Switch voor deze tunnel standaard ingeschakeld zodra de VPN wordt geactiveerd.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Global Mode)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Policy Mode)</small>

Klik op het tandwielpictogram naast de tunnelnaam om **Tunnel Options** te openen.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Kill Switch voor deze tunnel is standaard ingeschakeld.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Enhanced Kill Switch {#enhanced-kill-switch}

Deze functie is beschikbaar in de beleidsmodus.

Ga in het webbeheerpaneel naar **VPN** -> **VPN Dashboard**, stel de VPN-modus in op **Policy Mode** en zoek onderaan het gedeelte **All Other Traffic**. Dit gedeelte kan per firmwareversie iets verschillen.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** is de standaardtunnel. Deze biedt normale internettoegang voor verkeer dat niet overeenkomt met de bovenstaande VPN-tunnels of beleidsregels en voor verkeer dat door VPN-failover hierheen wordt geleid. De tunnel is standaard ingeschakeld. Schakel je deze uit, dan wordt al dit verkeer geblokkeerd, ook verkeer dat anders via VPN-failover zou worden omgeleid. Alleen verkeer dat via de ingestelde VPN-tunnels loopt kan dan het internet bereiken. Dit biedt dezelfde bescherming als **Enhanced Kill Switch**.

**Opmerking:** **All Other Traffic** overschrijft de Kill Switch van afzonderlijke tunnels niet.

## Voor firmware v4.9 en hoger {#for-firmware-v49-and-above}

Vanaf firmware v4.9 zijn er twee typen VPN Kill Switch: **Tunnel Kill Switch** en **Enhanced Kill Switch**.

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

On the router's web Admin Panel, navigate to **VPN** -> **VPN Dashboard**.

Als je de router als VPN-client instelt, wordt Kill Switch voor deze tunnel standaard ingeschakeld zodra de VPN wordt geactiveerd.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Klik op het tandwielpictogram naast de tunnelnaam om **Tunnel Options** te openen.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Kill Switch voor deze tunnel is standaard ingeschakeld.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Enhanced Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

Ga in het webbeheerpaneel van de router naar **VPN** -> **VPN Dashboard** en klik rechtsboven op het tandwielpictogram.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

Voor het verkeersbeleid zijn er twee opties: **Allow Non-VPN Traffic** en **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic**: Standaard ingeschakeld. Deze optie biedt normale internettoegang voor verkeer dat niet overeenkomt met bovenstaande VPN-tunnels of beleidsregels en voor verkeer dat door VPN-failover hierheen wordt geleid.

- **Enhanced Kill Switch**: Als deze optie is ingeschakeld, hebben alle apparaten via een VPN toegang tot internet. Verkeer dat niet overeenkomt met een VPN-tunnel wordt geblokkeerd. Deze instelling overschrijft de Kill Switch van afzonderlijke VPN-tunnels niet.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
