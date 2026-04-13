# System Overview

Sul lato sinistro del pannello di amministrazione web, vai su **SYSTEM** -> **Overview**.

La pagina Overview mostra lo stato di alcuni componenti hardware e supporta alcuni controlli semplici, inclusi i seguenti:

- Stato di CPU, memoria, flash e dispositivi di archiviazione esterni.
- Stato di componenti hardware come ventola, batteria e cosi' via.
- Controllo di LED e ventola.
- Informazioni sul dispositivo.

Ecco un esempio con GL-MT3000.

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## Carico medio della CPU

Per la maggior parte dei modelli senza ventola, il carico medio della CPU viene visualizzato come segue.

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

Per alcuni modelli con ventola integrata, il carico medio della CPU viene visualizzato come segue.

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Passa il mouse sul grafico per mostrare i valori specifici.

Fai clic sulla temperatura a destra per passare da Celsius a Fahrenheit.

Fai clic sull'icona della ventola nell'angolo in alto a destra per entrare in Fan Settings.

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Modelli con ventola integrata"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Utilizzo della memoria

Passa il mouse sul grafico per mostrare i valori specifici.

**Nota**: la memoria mostrata qui e' la memoria disponibile per il sistema Linux. La memoria totale qui sara' inferiore alla memoria fisica perche' una parte viene allocata al sottosistema Wi-Fi o ad altre aree di boot.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

Facendo clic sull'icona dell'ingranaggio andrai alla sezione [Scheduled Tasks](scheduled_tasks.md) del LED.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

Mostra la memoria flash totale, incluse la parte usata dal sistema, quella usata dalle app e quella ancora disponibile.

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## Informazioni sul dispositivo

Questa sezione mostra le informazioni di base del dispositivo.

Device ID, MAC del dispositivo e S/N del dispositivo sono stati aggiunti dal firmware v4.7 e versioni successive.

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## Archiviazione esterna

Questa sezione, disponibile dalla v4.5, mostra la capacita' totale e disponibile del disco USB.

Alcuni modelli con firmware v4.7 e successivi supportano il cambio del protocollo USB.

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
