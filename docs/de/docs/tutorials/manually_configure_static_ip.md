# So konfigurieren Sie auf den Client-Geräten manuell eine statische IP-Adresse {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    Unter Windows 11 können Sie für drahtlose und kabelgebundene Adapter eine statische IP-Adresse festlegen.

    **Statische IP-Adresse für einen Wi-Fi-Adapter festlegen**

    1. Öffnen Sie auf einem Windows-11-PC **Settings** -> **Network & internet** -> **Wi-Fi** und wählen Sie die aktuelle Wi-Fi-Verbindung aus.

    2. Suchen Sie **IP assignment** und klicken Sie auf die Schaltfläche **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. Wählen Sie im Pop-up-Fenster **Manual** aus und aktivieren Sie **IPv4**.

        ![Manuelle IP-Konfiguration](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Bearbeiten Sie die IP-Einstellungen wie folgt.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Legen Sie eine statische IP-Adresse fest, zum Beispiel `10.1.4.119`.

        - Subnet mask: Geben Sie eine Subnetzmaske an, zum Beispiel `255.255.255.0`.

        - Gateway: Geben Sie die Gateway-Adresse ein, üblicherweise die LAN-IP-Adresse Ihres Routers im selben Subnetz. Wenn Ihre IP-Adresse beispielsweise `10.1.4.119` lautet, ist das Gateway in der Regel `10.1.4.1`.

        - Preferred DNS: Geben Sie eine bevorzugte DNS-Adresse an (erforderlich). Sie können einen öffentlichen DNS-Server wie den DNS-Server `8.8.8.8` von Google verwenden.

        - Alternate DNS: Geben Sie eine alternative DNS-Adresse an (optional).

        - DNS over HTTPS: Wählen Sie "Off". Es gibt drei Optionen:

            - Off: Überträgt den gesamten DNS-Datenverkehr unverschlüsselt.

            - On (automatic template): Überträgt den gesamten DNS-Datenverkehr verschlüsselt.

            - On (manual template): Ermöglicht es Ihnen, ein bestimmtes Template anzugeben. Dies ist nur erforderlich, wenn der DNS-Dienst nicht automatisch funktioniert oder ein Template verwendet werden muss, das wie erwartet funktioniert.

        - Schalten Sie den Schalter "Fallback to plaintext" aus, wenn Sie DNS over HTTPS aktivieren.

            **Hinweis**: Wenn Sie diese Funktion aktivieren, verschlüsselt das System den DNS-Datenverkehr, erlaubt aber, dass Anfragen ohne Verschlüsselung gesendet werden.

    5. Klicken Sie auf **Save**, um die Einstellungen anzuwenden.

        Sobald Sie die Schritte abgeschlossen haben, wird die statische Netzwerkkonfiguration auf den Computer angewendet. Sie können die neuen Einstellungen testen, indem Sie einen Webbrowser öffnen und eine Website aufrufen.

    ---

    **Statische IP-Adresse für einen Ethernet-Adapter festlegen**

    1. Öffnen Sie auf einem Windows-11-PC **Settings** -> **Network & internet** -> **Ethernet**.

    2. Suchen Sie **IP assignment** und klicken Sie auf die Schaltfläche **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. Wählen Sie im Pop-up-Fenster **Manual** aus und aktivieren Sie **IPv4**.

        ![Manuelle IP-Konfiguration](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Bearbeiten Sie die IP-Einstellungen wie folgt.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Legen Sie eine statische IP-Adresse fest, zum Beispiel `10.1.4.119`.

        - Subnet mask: Geben Sie eine Subnetzmaske an, zum Beispiel `255.255.255.0`.

        - Gateway: Geben Sie die Gateway-Adresse ein, üblicherweise die LAN-IP-Adresse Ihres Routers im selben Subnetz. Wenn Ihre IP-Adresse beispielsweise `10.1.4.119` lautet, ist das Gateway in der Regel `10.1.4.1`.

        - Preferred DNS: Geben Sie eine bevorzugte DNS-Adresse an (erforderlich). Sie können einen öffentlichen DNS-Server wie den DNS-Server `8.8.8.8` von Google verwenden.

        - Alternate DNS: Geben Sie eine alternative DNS-Adresse an (optional).

        - DNS over HTTPS: Wählen Sie "Off". Es gibt drei Optionen:

            - Off: Überträgt den gesamten DNS-Datenverkehr unverschlüsselt.

            - On (automatic template): Überträgt den gesamten DNS-Datenverkehr verschlüsselt.

            - On (manual template): Ermöglicht es Ihnen, ein bestimmtes Template anzugeben. Dies ist nur erforderlich, wenn der DNS-Dienst nicht automatisch funktioniert oder ein Template verwendet werden muss, das wie erwartet funktioniert.

        - Schalten Sie den Schalter "Fallback to plaintext" aus, wenn Sie DNS over HTTPS aktivieren.

            **Hinweis**: Wenn Sie diese Funktion aktivieren, verschlüsselt das System den DNS-Datenverkehr, erlaubt aber, dass Anfragen ohne Verschlüsselung gesendet werden.

    5. Klicken Sie auf **Save**, um die Einstellungen anzuwenden.

        Sobald Sie die Schritte abgeschlossen haben, wird die statische Netzwerkkonfiguration auf den Computer angewendet. Sie können die neuen Einstellungen testen, indem Sie einen Webbrowser öffnen und eine Website aufrufen.

=== "macOS"

    So legen Sie in macOS eine statische IP-Adresse fest.

    Wählen Sie im Apple-Menü **System Preferences**.

    Wählen Sie **Network**. Die folgende Seite wird angezeigt. Wählen Sie in der Seitenleiste eine aktive Netzwerkschnittstelle aus, zum Beispiel **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Notieren Sie sich die aktuelle IP-Adresse, die Ihrem Mac zugewiesen ist. Sie müssen eine neue IP-Adresse aus dem aufgeführten privaten IP-Adressbereich auswählen.

    Klicken Sie unten rechts auf **Advanced**.

    Wählen Sie anschließend **TCP/IP**. Die folgende Seite wird angezeigt.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: Wählen Sie "Manually".

    - IPv4 Address: Geben Sie eine statische IP-Adresse ein. Behalten Sie die ersten drei Oktette Ihrer aktuellen IP-Adresse bei und ändern Sie das letzte Oktett in einen ungenutzten Wert. Wählen Sie zum Beispiel im Netzwerk `192.168.7.0/24` eine noch nicht verwendete Adresse von `192.168.7.2` bis `192.168.7.254` (vermeiden Sie `.1`, die Adresse des Routers). Verwenden Sie weder `192.168.7.0` noch `192.168.7.255`.

    - Subnet Mask: Geben Sie `255.255.255.0` ein (oder die von Ihrem Netzwerkadministrator bereitgestellte Subnetzmaske).

    - Router: Geben Sie die LAN-IP-Adresse Ihres Routers ein, zum Beispiel `192.168.7.1`.

    Klicken Sie auf **OK** und anschließend auf **Apply**.

=== "iOS"

    Die Schritte können je nach iOS-Version abweichen. Die folgenden Schritte basieren auf iOS 26.2.2.

    1. Gehen Sie zu **Settings** -> **WLAN**. Tippen Sie neben dem aktuell verbundenen Wi-Fi-Netzwerk auf das blaue Informationssymbol (i).

        ![Statische IP-Adresse in iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Scrollen Sie zu **IPv4 Address** und stellen Sie **Configure IP** auf **Manual**.

        ![Statische IP-Adresse in iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Geben Sie die **IP Address**, **Subnet Mask** und **Router IP** an, die Sie auf Ihrem iPhone/iPad verwenden möchten. Tippen Sie anschließend oben rechts auf **Save**.

        ![Statische IP-Adresse in iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    Die Schritte können je nach Android-Version abweichen. Die folgenden Schritte basieren auf Android 11.

    1. Gehen Sie zu **Settings** -> **Network & Internet** -> **Wi-Fi**. Tippen Sie auf das aktuell verbundene Netzwerk, um das Einstellungsmenü zu öffnen.

        ![list_available_networks](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Tippen Sie oben rechts auf das Stiftsymbol, um auf die Netzwerkeinstellungen zuzugreifen.

        ![pencil_icon](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Tippen Sie auf **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Tippen Sie auf **IP Settings** und wählen Sie **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/de/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Geben Sie die **IP address** ein. Das Feld **Gateway** sollte anhand der IP-Adresse automatisch ausgefüllt werden. Falls nicht, geben Sie Ihr Netzwerk-Gateway ein. Das Gateway ist üblicherweise die LAN-IP-Adresse Ihres Routers im selben Subnetz.

        **Hinweis**: Wenn Sie statische IP-Adressen in Heimnetzwerken und anderen privaten Netzwerken verwenden, wählen Sie eine freie Hostadresse in Ihrem aktuellen Subnetz. Die Standardbereiche für private IP-Adressen sind:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Tippen Sie auf **Save** und warten Sie, bis die Netzwerkverbindung wiederhergestellt ist.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
