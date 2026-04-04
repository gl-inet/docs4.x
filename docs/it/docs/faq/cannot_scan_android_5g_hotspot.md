# Impossibile rilevare l'hotspot 5G di Android

Collegare il router GL.iNet come repeater all'hotspot 5G di un telefono Android è uno dei modi più comuni per accedere a Internet.

Tuttavia, se non riesci a rilevare l'hotspot 5G del telefono Android, il problema potrebbe essere legato al country code Wi-Fi.

Alcuni telefoni Android impostano per impostazione predefinita l'hotspot 5G su un canale degli Stati Uniti. Se il router GL.iNet non è stato acquistato originariamente negli Stati Uniti, potresti riscontrare questo problema.

Puoi modificare il country code Wi-Fi del router GL.iNet nella pagina LuCI seguendo i passaggi riportati di seguito.

## Passaggio 1. Accedi a LuCI

Accedi al router GL.iNet, nella barra laterale sinistra scegli **SYSTEM -> Advanced Settings -> Go to LuCI**. Accedi a LuCI con la stessa password amministratore.

## Passaggio 2. Modifica le impostazioni Wi-Fi

Vai a **Network -> Wireless**, seleziona il Wi-Fi 5G e fai clic su modifica. Se stai usando GL-MT3000, vai su **Network -> MTK Wi-Fi**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

![mtkwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/mtkwifi.jpg){class="glboxshadow"}

## Passaggio 3. Seleziona US come country code

In **Device Configuration -> Advanced Settings**, seleziona US (United States) come country code per il Wi-Fi a 5 GHz.

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

Fai clic su **Save & Apply** prima di uscire.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

Quindi prova a rilevare di nuovo l'hotspot 5G del telefono Android.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
