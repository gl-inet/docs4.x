# macOS kann nicht auf eine Samba-Freigabe schreiben

Wenn Sie ein mit exFAT formatiertes Speichergerät für eine Samba-Freigabe verwenden, können auf einigen macOS-Geräten beim Versuch, Dateien in die Freigabe zu schreiben, eine der folgenden Fehlermeldungen auftreten.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Versuchen Sie, dieses Problem mit den folgenden Methoden zu beheben.

1. **Berechtigungen der Samba-Freigabe prüfen.**

    Stellen Sie sicher, dass die Samba-Freigabe mit Schreibzugriff konfiguriert ist. Melden Sie sich am Web-Admin-Panel Ihres Routers an und prüfen Sie, ob für Ihr Benutzerkonto beim freigegebenen Ordner die Berechtigung "Read/Write" aktiviert ist.

2. **Verwenden Sie den Befehl `cp -X file-name`, um die Datei zu kopieren.**

    Da Finder bei Übertragungen automatisch erweiterte Attribute (z. B. Resource Forks, Metadaten) hinzufügt, die mit der Verarbeitung von exFAT-Speichern durch Samba in Konflikt geraten können, versuchen Sie bitte, die Datei mit dem Befehl **cp -X file-name** zu kopieren.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Oder verwenden Sie den Befehl **cp -rX folder-name**, um den Ordner zu kopieren.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Starten Sie Ihren Mac neu.**

    Klicken Sie auf das Apple-Menü und dann auf Restart. Wenn das Problem weiterhin besteht, fahren Sie den Mac herunter, trennen Sie alle externen Geräte, warten Sie 30 Sekunden und starten Sie ihn dann erneut.

4. **Benennen Sie die Datei um.**

    Klicken Sie mit der rechten Maustaste auf die Datei und dann auf Rename. Verwenden Sie einfache Namen und vermeiden Sie Sonderzeichen wie !@# oder Leerzeichen.

5. **Verbinden Sie das Speichergerät erneut.**

    Wenn Sie ein externes Laufwerk wie z. B. ein USB-Laufwerk verwenden, werfen Sie es zuerst aus, bevor Sie es abziehen, warten Sie 10 Sekunden und schließen Sie es dann wieder an. Sie können auch einen anderen USB-Port ausprobieren.

6. **Reparieren Sie Datenträgerfehler mit First Aid.**

    Beschädigte Datenträgerdaten können zu Schreibfehlern führen. Sie können das Festplattendienstprogramm von macOS verwenden, um Probleme zu beheben. 
    
    1. Öffnen Sie Finder -> Applications -> Utilities -> Disk Utility. 
    2. Wählen Sie in der linken Seitenleiste das Laufwerk bzw. Speichergerät (lokal oder extern) aus. 
    3. Klicken Sie auf First Aid -> Run. Warten Sie, bis der Vorgang abgeschlossen ist.

7. **Passen Sie das Dateisystem an oder formatieren Sie das Laufwerk.**

    Wenn Sie ein mit exFAT formatiertes Laufwerk verwenden, können unter macOS Kompatibilitätsprobleme mit Samba auftreten. Sie können die folgenden Methoden ausprobieren.
    
    - **In FAT32 formatieren** (für externe Laufwerke, plattformübergreifende Kompatibilität)
    
        1. Sichern Sie zuerst die Daten auf dem Laufwerk (durch das Formatieren werden alle Dateien gelöscht).
        2. Öffnen Sie Disk Utility -> Wählen Sie das Laufwerk aus -> Erase.
        3. Wählen Sie als Format "MS-DOS (FAT)" (FAT32) -> Klicken Sie auf Erase.

    - **In ext4 formatieren**
    
        !!! Note
        
            ext4 wird in erster Linie von Linux-Systemen unterstützt. Nach der Formatierung in ext4 ist das Speichergerät möglicherweise nicht mit Windows-Betriebssystemen kompatibel, was dazu führen kann, dass das Laufwerk auf Windows-Geräten nicht erkannt wird oder nicht beschrieben werden kann.
        
        1. Sichern Sie alle Daten auf dem Laufwerk, da bei der Formatierung alles gelöscht wird.
        2. Verwenden Sie ein Tool wie Disk Utility oder ein Linux-System, um das Laufwerk in ext4 zu formatieren.

8. **Aktualisieren Sie macOS und leeren Sie die Caches.**

    Veraltete Software oder beschädigte Caches können Konflikte verursachen. Gehen Sie zu System Settings -> General -> Software Update, installieren Sie die neueste Version und leeren Sie die System-Caches.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [Kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
