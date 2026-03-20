# Wie aktualisiere ich auf Firmware 4.x?

**Dieses Dokument ist veraltet und wird nicht mehr gepflegt. Klicken Sie [hier](../interface_guide/upgrade.md), um die aktuelle Upgrade-Anleitung aufzurufen.**

---

Befolgen Sie die folgenden Schritte, um Ihren Router von Firmware 3.x auf 4.x zu aktualisieren.

Hinweis: Behalten Sie beim Upgrade von v3.x auf v4.x bitte keine Einstellungen bei, da dies zu Instabilität führen kann. Sichern Sie vor dem Upgrade alle wichtigen Einstellungen.

GL-B1300 und GL-S1300 unterstützen die Mesh-Funktion in Firmware v4.x nicht.

---

## Methode 1: Lokales Upgrade

Sie können die Firmware über das Web-Admin-Panel aktualisieren.

1. Aktualisieren Sie die Firmware auf die neueste stabile 3.x-Version.

2. Laden Sie die 4.x-Firmware [hier](https://dl.gl-inet.com){target="_blank"} herunter. Achten Sie darauf, **die Version für common upgrade herunterzuladen**.

3. Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **Upgrade** -> **Local Upgrade**. Laden Sie die Firmware-Datei hoch, die Sie gerade heruntergeladen haben.

    **Hinweis:** Die 4.x-Firmware ist nicht mit der 3.x-Firmware kompatibel. Wenn Sie von einer 3.x-Firmware aktualisieren, behalten Sie die Einstellungen **NICHT** bei.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/gl-ax1800_upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow gl-90-desktop"}

## Methode 2: U-Boot-Upgrade

1. Laden Sie die 4.x-Firmware [hier](https://dl.gl-inet.com){target="_blank"} herunter. Achten Sie darauf, **die Version für U-Boot herunterzuladen**.

2. Folgen Sie dieser Anleitung zu [U-Boot](debrick.md), um die Firmware zu flashen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
