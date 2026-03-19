# So konfigurieren Sie auf den Client-Geräten manuell eine statische IP-Adresse

=== "Windows 11"

    Unter Windows 11 können Sie in der App **Settings** für drahtlose und kabelgebundene Adapter eine statische IP-Adresskonfiguration festlegen.

    **Statische IP-Adresse für einen Wi-Fi-Adapter festlegen**

    Gehen Sie wie folgt vor, um einem Wi-Fi-Adapter eine statische IP-Adresskonfiguration zuzuweisen:

    1. Öffnen Sie unter Windows 11 **Settings** -> **Network & Internet** -> die Registerkarte **Wi-Fi** -> wählen Sie die aktuelle Netzwerkverbindung aus.

    2. Klicken Sie im Abschnitt „IP settings“ auf die Schaltfläche **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. Führen Sie zum Einrichten die folgenden Schritte aus:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Wählen Sie die Option **Manual** aus und schalten Sie den Schalter **IPv4** ein.

        - Legen Sie eine statische IP-Adresse für Windows 11 fest, zum Beispiel 10.1.4.119.

        - Geben Sie eine Subnetzmaske an, zum Beispiel 255.255.255.0.

        - Geben Sie eine Default-Gateway-Adresse an.

        - Geben Sie eine Preferred-DNS-Adresse an (erforderlich).

        - (Optional) Geben Sie eine „Alternate DNS“-Adresse an.

        - Verwenden Sie das Dropdown-Menü „DNS over HTTPS“ und wählen Sie für die bevorzugten und alternativen Adressen die Option **Off**. Sie können DoH aber auch mit diesen Optionen aktivieren:

            - **Off**: Überträgt den gesamten DNS-Datenverkehr unverschlüsselt.

            - **On (automatic template)**: Überträgt den gesamten DNS-Datenverkehr verschlüsselt.

            - **On (manual template)**: Ermöglicht es Ihnen, ein bestimmtes Template anzugeben. Dies ist nur erforderlich, wenn der DNS-Dienst nicht automatisch funktioniert oder ein Template verwendet werden muss, das wie erwartet funktioniert.

        - Schalten Sie den Schalter „Fallback to plaintext“ aus (wenn Sie DoH aktivieren).

            - Kurztipp: Wenn Sie diese Funktion aktivieren, verschlüsselt das System den DNS-Datenverkehr, erlaubt aber, dass Anfragen ohne Verschlüsselung gesendet werden.

    4. Klicken Sie auf die Schaltfläche **Save**.

        Sobald Sie die Schritte abgeschlossen haben, wird die statische Netzwerkkonfiguration auf den Computer angewendet. Sie können die neuen Einstellungen testen, indem Sie einen Webbrowser öffnen und eine Website aufrufen.


    ## **Statische IP-Adresse für einen Ethernet-Adapter festlegen**

    Gehen Sie wie folgt vor, um einem Ethernet-Adapter (kabelgebunden) unter Windows 11 eine statische IP-Adresse zuzuweisen:

    1. Öffnen Sie **Settings** -> **Network & Internet** -> die Registerkarte **Ethernet**.

    2. Klicken Sie im Abschnitt „IP settings“ auf die Schaltfläche **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. Führen Sie zum Einrichten die folgenden Schritte aus:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Wählen Sie die Option **Manual** aus.

        - Schalten Sie den Schalter **IPv4** ein.

        - Legen Sie eine statische IP-Adresse für Windows 11 fest, zum Beispiel 10.1.4.119.

        - Geben Sie eine Subnetzmaske an, zum Beispiel 255.255.255.0.

        - Geben Sie eine Default-Gateway-Adresse an.

        - Geben Sie eine Preferred-DNS-Adresse an (erforderlich).

        - (Optional) Geben Sie eine „Alternate DNS“-Adresse an.

        - Verwenden Sie das Dropdown-Menü „DNS over HTTPS“ und wählen Sie für die bevorzugten und alternativen Adressen die Option **Off**. Sie können DoH aber auch mit diesen Optionen aktivieren:

            * **Off**: Überträgt den gesamten DNS-Datenverkehr unverschlüsselt.

            * **On (automatic template)**: Überträgt den gesamten DNS-Datenverkehr verschlüsselt.

            * **On (manual template)**: Ermöglicht es Ihnen, ein bestimmtes Template anzugeben. Dies ist nur erforderlich, wenn der DNS-Dienst nicht automatisch funktioniert oder ein Template verwendet werden muss, das wie erwartet funktioniert.

        - Schalten Sie den Schalter „Fallback to plaintext“ aus (wenn Sie DoH aktivieren).

    4. Klicken Sie auf die Schaltfläche **Save**.

        Nachdem Sie die Schritte abgeschlossen haben, können Sie Ihre Einstellungen testen, indem Sie in Ihrem Webbrowser eine Website öffnen.


=== "macOS"

    So legen Sie in macOS eine statische IP-Adresse fest:

    Wenn Sie ein MacBook besitzen, möchten Sie möglicherweise einen neuen Netzwerkstandort erstellen. So können Sie die statische IP-Adresse nur für bestimmte Netzwerke und nicht für andere verwenden.

    Wählen Sie im Apple-Menü **System Preferences**.

    Wählen Sie **Network**. Das unten gezeigte Fenster wird angezeigt.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    Wählen Sie in der Seitenleiste eine aktive Netzwerkschnittstelle aus. In diesem Beispiel bin ich mit einem drahtlosen Netzwerk verbunden, daher wähle ich **Wi-Fi** aus.

    Notieren Sie sich die aktuelle IP-Adresse, die Ihrem Mac zugewiesen ist. Sie müssen gleich eine neue IP-Adresse aus dem aufgeführten privaten IP-Adressbereich auswählen.

    Klicken Sie auf **Advanced**.

    Wählen Sie **TCP/IP**. Das unten gezeigte Fenster wird angezeigt.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    Wählen Sie im Menü **Configure IPv4** die Option **Manually**.

    Geben Sie im Feld **IPv4 Address** eine statische IP-Adresse ein. Welche Zahl sollten Sie eingeben? Eine Möglichkeit ist, Ihre aktuelle IP-Adresse zu übernehmen und den letzten Teil der Nummer zu ändern. In diesem Beispiel hätte ich jede Adresse zwischen 192.168.7.0 und 192.168.7.255 wählen können, solange diese Adresse noch keinem anderen Gerät zugewiesen war.

    Klicken Sie auf **OK** -> **Apply**.


=== "Android"

    Die Schritte unterscheiden sich je nach Android-Version. Diese Dokumentation basiert auf Android 11.

    1. Gehen Sie zu **Settings** -> wählen Sie **Network & Internet**, dann **Wi-Fi** -> tippen Sie auf das aktuell verbundene Netzwerk, um das Einstellungsmenü zu öffnen.

    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. Um eine statische IP-Adresse festzulegen, gehen Sie wie folgt vor:

    - Wählen Sie oben rechts das Stiftsymbol aus, um auf die Netzwerkeinstellungen zuzugreifen.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Wählen Sie **Advanced Options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Wählen Sie **IP Settings**.

    - Ändern Sie die Einstellung von **DHCP** auf **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Wenn Sie statische IP-Adressen in Heimnetzwerken und anderen privaten Netzwerken verwenden, sollten diese aus den folgenden Standardbereichen für private IP-Adressen gewählt werden:

      10.0.0.0 bis 10.255.255.255,
      172.16.0.0 bis 172.31.255.255,
      192.168.0.0 bis 192.168.255.255

    - Geben Sie nun die IP-Adresse ein.
        - Dieser Schritt ist für jedes Netzwerk spezifisch, z. B. 192.168.1.128.

    - Das Gateway sollte anhand der IP-Adresse automatisch ausgefüllt werden. Falls nicht, kopieren Sie die IP-Adresse und ersetzen Sie die letzte Zahl durch eine 1.
        - Beispiel auf Basis des vorherigen Beispiels: 192.168.1.1

    3. Tippen Sie auf **Save** und lassen Sie das Netzwerk die Verbindung erneut herstellen.

=== "iOS"

    Wenn Sie statische IP-Adressen in Heimnetzwerken und anderen privaten Netzwerken verwenden, sollten diese aus den folgenden Standardbereichen für private IP-Adressen gewählt werden:

    10.0.0.0 bis 10.255.255.255
    172.16.0.0 bis 172.31.255.255
    192.168.0.0 bis 192.168.255.255

    Gehen Sie wie folgt vor, um eine statische IP-Adresse festzulegen:

    - Tippen Sie auf das Symbol **Settings**.

    - Gehen Sie zu **Wi-Fi**.

    - Tippen Sie neben dem Namen des Wi-Fi-Netzwerks auf das blaue Informationssymbol (i).
         - Wenn Sie eine Version älter als iOS 7 verwenden, kann dies ein blauer Pfeil sein.

    - Wechseln Sie zum Reiter **Static**, wie unten dargestellt.

    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - Tippen Sie auf das Feld **IP Address**.

    - Geben Sie die statische IP-Adresse ein, die Sie auf Ihrem iPhone/iPad verwenden möchten.

    - Tippen Sie auf das Feld **Router**.

    - Geben Sie die IP-Adresse des Routers ein.

    - Tippen Sie auf **Subnet Mask** und geben Sie Ihre Informationen ein.

        - In der Regel ist dies 225.225.0.0.

    - Tippen Sie oben links auf die Schaltfläche **Wi-Fi**, um die Einstellungen zu speichern.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
