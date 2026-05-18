# Impossibile rilevare l'hotspot 5G di Android

Collegare il router GL.iNet come repeater all'hotspot 5G di un telefono Android è uno dei modi più comuni per accedere a Internet.

Tuttavia, se non riesci a rilevare l'hotspot 5G del telefono Android, il problema potrebbe essere legato al canale Wi-Fi.

Alcuni telefoni Android impostano per impostazione predefinita l'hotspot 5G su un canale degli Stati Uniti. Se il router GL.iNet non è stato acquistato originariamente negli Stati Uniti, potresti riscontrare questo problema.

Puoi modificare il country code Wi-Fi del router GL.iNet nell'interfaccia LuCI seguendo i passaggi riportati di seguito.

1. Accedi al router GL.iNet e vai su **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Accedi a LuCI con la stessa password amministratore.

2. Modifica le impostazioni Wi-Fi.

    Vai su **Network** -> **Wireless**, individua il Wi-Fi 5G e fai clic su **Edit** sulla destra.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

3. Seleziona US come country code.

    Nella pagina Wireless, fai clic sulla scheda **Advanced Settings** in **Device Configuration**. Seleziona US (United States) come country code per il Wi-Fi a 5 GHz.

    ![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

4. Fai clic su **Save & Apply** prima di uscire.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

    Quindi prova a rilevare di nuovo l'hotspot 5G del telefono Android.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
