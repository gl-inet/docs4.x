# Come instradare tutti i dati attraverso la VPN?

Se vuoi instradare tutto il traffico di rete del router attraverso la VPN e bloccare tutte le connessioni Internet quando la VPN non è disponibile, segui i passaggi seguenti per abilitare il **VPN Kill Switch**.

**Nota**: prima di abilitare il VPN Kill Switch, configura prima un client VPN sul router GL.iNet.

## Per firmware v4.7 o precedenti

Accedi al pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard** -> sezione **VPN Client** e fai clic su **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Attiva **Block Non-VPN Traffic** (chiamato anche Kill Switch in alcune versioni del firmware), quindi fai clic su **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Nota:** quando **Block Non-VPN Traffic / Kill Switch** è abilitato, se la VPN viene disabilitata o si disconnette, a tutti i dispositivi collegati al router verrà impedito l'accesso a Internet per evitare perdite DNS.

## Per firmware v4.8 o successivi

Nel firmware v4.8, il VPN Kill Switch è stato suddiviso in due modalità.

- **Tunnel Kill Switch**: è abilitato per impostazione predefinita quando il tunnel VPN corrispondente viene attivato.

- **Enhanced Kill Switch (in Policy Mode)**: è disabilitato per impostazione predefinita per garantire che tutto il traffico non coperto dai tunnel VPN e dalle policy sopra possa comunque accedere a Internet. In breve, mantiene il normale accesso a Internet per il traffico non VPN.

### Tunnel Kill Switch

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

### Enhanced Kill Switch

Questa funzione è disponibile in **Policy Mode**.

Nel pannello di amministrazione web del router, vai a **VPN** -> **VPN Dashboard**, passa la modalità VPN a **Policy Mode**, quindi individua in basso una sezione denominata **All Other Traffic**. Questa sezione può variare leggermente in base alla versione del firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** è un tunnel predefinito che garantisce il normale accesso a Internet per il traffico non coperto dai tunnel VPN e dalle policy sopra, oppure per il traffico che ha eseguito il failover da connessioni VPN. Questo tunnel è abilitato per impostazione predefinita ed è mutuamente esclusivo rispetto a Enhanced Kill Switch.

**Nota**: se disabiliti **All Other Traffic**, potrai accedere a Internet solo tramite VPN. Tutto il traffico non corrispondente verrà bloccato. Questa impostazione non sostituisce il Kill Switch individuale di ciascun tunnel.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
