# DPI Engine

DPI (Deep Packet Inspection) è una tecnologia fondamentale per la gestione intelligente della rete. A differenza dei router tradizionali, che identificano solo gli indirizzi di origine e destinazione, DPI analizza in profondità il payload dei pacchetti e riconosce con precisione applicazioni e siti web tramite una libreria di firme, consentendo una classificazione e un controllo del traffico più granulari.

Il DPI Engine di GL.iNet viene eseguito localmente sul router per offrire una gestione intelligente della rete con piena tutela della privacy. Fornisce accesso completo a statistiche del traffico, filtro contenuti e QoS per un controllo approfondito del traffico.

Integrato con [Netify](https://www.netify.ai/){target="_blank"}, il DPI di GL.iNet adotta un plug-in embedded leggero per una distribuzione efficiente. Grazie al database di firme aggiornato online da Netify, consente una gestione affidabile, rendendo il controllo della rete più preciso ed efficiente.

**Nota**:

1. Le funzioni DPI non hanno effetto quando il router è in modalità Drop-in Gateway.

2. Quando DPI è abilitato, Network Acceleration viene disattivato automaticamente per garantire un funzionamento stabile.

## Modelli supportati

!!! note "Modelli supportati"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configurazione rapida

Nel pannello di amministrazione web, dal menu laterale sinistro vai su **FLOW CONTROL** -> **DPI Engine** e fai clic su **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

Nella finestra pop-up, leggi e accetta **Terms of Service & Privacy Policy**, quindi fai clic su **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Attendi mentre il router esegue le operazioni di sistema. Network Acceleration verrà disattivato e Data Statistics e Content Filter verranno abilitati.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Una volta completata l'attivazione, fai clic su **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Verrai indirizzato al **DPI Engine Version Center**, dove potrai visualizzare la versione del programma DPI e la versione del database.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Nota**: questa pagina mostra solo gli indicatori di stato principali del sistema. L'elaborazione del traffico inizierà quando verranno abilitate le relative funzioni.

## Aggiornamento del database

Se è disponibile una versione più recente del database, fai semplicemente clic su **Upgrade** per aggiornarlo.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
