# Filtro contenuti

Content Filter è una funzione intelligente di sicurezza online basata sulla classificazione DPI. Blocca automaticamente siti web dannosi o malevoli per mantenere la rete pulita e sicura e supporta anche regole personalizzate per bloccare app, domini o indirizzi IP specifici.

**Nota**:

1. Il Filtro contenuti non ha effetto quando il router è in modalità Drop-in Gateway.
2. Content Filter non può funzionare con Network Acceleration. L'abilitazione di Content Filter disattiva automaticamente Network Acceleration per garantire prestazioni stabili.

## Modelli supportati

!!! note "Modelli supportati"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Nota: i modelli contrassegnati con ※ supportano Content Filter a partire dal firmware v4.9.

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **Content Filter**.

Attiva l'interruttore nell'angolo superiore destro, personalizza i contenuti da bloccare, come app, domini o indirizzi IP, quindi fai clic su **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Questa pagina è composta da due parti:

- **Blocked Apps List**: questa sezione include tre categorie preselezionate: Gambling, Adult e Malware. Quando sono abilitate, tutti i siti web, i servizi o le app correlati a queste tre categorie verranno bloccati.

    Puoi anche fare clic su **Edit App** per aggiungere altre categorie, ad esempio Game o Social Media, secondo necessità.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    Nella finestra pop-up, seleziona le categorie che vuoi bloccare. Le tre categorie predefinite sono vuote; tutte le altre categorie includono un elenco di app.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Fai clic su una categoria per visualizzare e selezionare le app che vuoi bloccare, oppure fai clic su **Select All** in alto a destra per bloccare in una sola volta tutte le app di quella categoria, quindi fai clic su **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    Vedrai quindi le app selezionate in Blocked App List.

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

- **Blocked Domain / IP List**: questa sezione consente di inserire manualmente domini specifici, ad esempio `google.com`, intervalli CIDR, ad esempio `192.168.8.0/24`, oppure indirizzi IP, ad esempio `192.168.10.10`, per bloccarne l'accesso. L'elenco supporta fino a 10000 voci.

    Inserisci i domini o gli indirizzi IP che vuoi bloccare, quindi fai clic su **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Test del filtro contenuti

Ad esempio, abbiamo selezionato la categoria **Game**, che include Nintendo.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

Su un laptop collegato al router, il sito `nintendo.com` non è più accessibile, mentre prima dell'abilitazione di Content Filter era raggiungibile.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

Nel pannello di amministrazione web del router puoi vedere il numero di richieste di accesso che sono state bloccate.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
