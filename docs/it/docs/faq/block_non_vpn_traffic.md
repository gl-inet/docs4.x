# Come instradare tutti i dati attraverso la VPN? {#how-to-let-all-data-go-through-vpn}

Se vuoi instradare tutto il traffico di rete del router attraverso la VPN e bloccare tutte le connessioni Internet quando la VPN non è disponibile, segui i passaggi seguenti per abilitare il **VPN Kill Switch**.

**Nota**: prima di abilitare il VPN Kill Switch, configura prima un client VPN sul router GL.iNet.

## Per firmware v4.7 o precedenti {#for-firmware-v47-or-earlier}

Accedi al pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard** -> sezione **VPN Client** e fai clic su **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Attiva **Block Non-VPN Traffic** (chiamato anche Kill Switch in alcune versioni del firmware), quindi fai clic su **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Nota:** quando **Block Non-VPN Traffic / Kill Switch** è abilitato, se la VPN viene disabilitata o si disconnette, a tutti i dispositivi collegati al router verrà impedito l'accesso a Internet per evitare perdite DNS.

## Per il firmware v4.8 {#for-firmware-v48}

Nel firmware v4.8, il VPN Kill Switch è stato suddiviso in due modalità.

- **Tunnel Kill Switch**: è abilitato per impostazione predefinita quando il tunnel VPN corrispondente viene attivato.

- **Enhanced Kill Switch (in Policy Mode)**: è disabilitato per impostazione predefinita per garantire che tutto il traffico non coperto dai tunnel VPN e dalle policy sopra possa comunque accedere a Internet. In breve, mantiene il normale accesso a Internet per il traffico non VPN.

### Tunnel Kill Switch {#tunnel-kill-switch}

Nel pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard**.

Se configuri il router come client VPN, il Kill Switch per questo tunnel VPN è abilitato per impostazione predefinita una volta attivata la VPN.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Global Mode)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Policy Mode)</small>

Fai clic sull'icona a forma di ingranaggio accanto al nome del tunnel per accedere a **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Il Kill Switch per questo tunnel è abilitato per impostazione predefinita.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Enhanced Kill Switch {#enhanced-kill-switch}

Questa funzione è disponibile in **Policy Mode**.

Nel pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard**, passa la modalità VPN a **Policy Mode**, quindi individua in basso una sezione denominata **All Other Traffic**. Questa sezione può variare leggermente in base alla versione del firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** è il tunnel predefinito. Consente il normale accesso a Internet al traffico che non corrisponde ai tunnel VPN o ai criteri precedenti e al traffico reindirizzato qui dal failover VPN. Il tunnel è attivo per impostazione predefinita. Se lo disattivi, viene bloccato tutto questo traffico, incluso quello che altrimenti verrebbe reindirizzato dal failover di una connessione VPN. Solo il traffico gestito dai tunnel VPN configurati può quindi raggiungere Internet, con la stessa protezione di **Enhanced Kill Switch**.

**Nota:** L’impostazione **All Other Traffic** non sostituisce il Kill Switch di ciascun tunnel.

## Per il firmware v4.9 e versioni successive {#for-firmware-v49-and-above}

Il firmware v4.9 e le versioni successive offrono due tipi di Kill Switch VPN: **Tunnel Kill Switch** e **Enhanced Kill Switch**.

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

Nel pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard**.

Se configuri il router come client VPN, il Kill Switch per questo tunnel VPN è abilitato per impostazione predefinita una volta attivata la VPN.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Fai clic sull'icona a forma di ingranaggio accanto al nome del tunnel per accedere a **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Il Kill Switch per questo tunnel è abilitato per impostazione predefinita.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Enhanced Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

Nel pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard**, quindi fai clic sull’icona a forma di ingranaggio in alto a destra.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

Il controllo dei criteri del traffico offre due opzioni: **Allow Non-VPN Traffic** ed **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic**: È attiva per impostazione predefinita. Consente il normale accesso a Internet al traffico che non corrisponde ai tunnel VPN o ai criteri precedenti e al traffico reindirizzato qui dal failover VPN.

- **Enhanced Kill Switch**: Quando è attiva, obbliga tutti i dispositivi ad accedere a Internet tramite una VPN. Blocca il traffico che non corrisponde ad alcun tunnel VPN. Questa impostazione non sostituisce il Kill Switch di ciascun tunnel.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
