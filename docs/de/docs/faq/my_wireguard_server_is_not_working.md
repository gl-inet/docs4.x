# Der WireGuard-Server auf meinem GL.iNet-Router funktioniert nicht richtig







Es gibt verschiedene Gründe, warum der WireGuard-Server, den Sie auf Ihrem GL.iNet-Router eingerichtet haben, nicht richtig funktioniert.







Wenn Probleme auftreten, folgen Sie diesen Schritten zur Fehlerbehebung entsprechend Ihrer jeweiligen Situation.







#### Situation 1: Der WireGuard-Server startet, es kann aber keine Verbindung hergestellt werden







??? "Folgen Sie diesen Schritten"







    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}







    Die Portweiterleitung, die Sie auf Ihrem Primärrouter eingerichtet haben, der mit Ihrem Sekundärrouter (GL.iNet) verbunden ist, funktioniert möglicherweise nicht richtig.



    Um zu prüfen, ob die Portweiterleitung richtig funktioniert, leiten Sie testweise den HTTPS-Port des Primärrouters an Ihren WireGuard-Server weiter. Gehen Sie dazu wie folgt vor:







    1. Leiten Sie den HTTPS-Port Ihres Primärrouters an Ihren WireGuard-Server weiter







        1. Melden Sie sich im Admin-Panel Ihres Primärrouters an.



        2. Öffnen Sie die Seite für die Portweiterleitung.



        3. Erstellen Sie einen neuen Eintrag und nennen Sie ihn **HTTPS**.



        4. Geben Sie die folgenden Informationen ein:



            * **External port/Internal port:** Geben Sie **443** ein.



            * **Protocol:** Wählen Sie **All** oder **UDP/TCP**.



            * **Internal IP** (oder als **Host IP** angezeigt): Geben Sie die WAN-IP-Adresse Ihres Sekundärrouters ein oder wählen Sie Ihren Sekundärrouter aus der Dropdown-Liste aus, falls verfügbar.



            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}







    2. Aktivieren Sie DDNS und den HTTPS-Fernzugriff (auf dem GL.iNet-Router)







        1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres GL.iNet-Routers ein (z. B. 192.168.8.1) und melden Sie sich an.



        2. Klicken Sie in der linken Seitenleiste auf **Applications** > **Dynamic DNS**.



        3. Schalten Sie **Enable DDNS** ein und aktivieren Sie das Kontrollkästchen für **I have read and agree to the Terms of Service & Privacy Policy**.



            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}



        4. Speichern Sie den Hostnamen an einem Ort, auf den Sie später zugreifen können, und klicken Sie dann auf **Apply**.



        5. Klicken Sie in der linken Seitenleiste auf **System** > **Security**.



        6. Schalten Sie unter **Remote Access Control** die Option **HTTPS Remote Access** ein.



            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}



        7. Klicken Sie auf **Apply**.







    3. Prüfen Sie, ob Sie auf das Admin-Panel des GL.iNet-Routers zugreifen können







        1. Verbinden Sie sich auf einem anderen Gerät (z. B. Laptop oder Mobilgerät) mit einem anderen Wi-Fi-Netzwerk oder dem Mobilfunknetz.

        2. Geben Sie in die Adressleiste eines Webbrowsers den zuvor gespeicherten Hostnamen ein (abcd123.glddns.com).



        3. Klicken Sie auf **Advanced**.



            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}



        4. Klicken Sie auf **Proceed to abcd123.glddns.com(unsafe)**.



            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}







    Wenn Sie den Anmeldebildschirm Ihres GL.iNet-Routers (Sekundärrouter) sehen, funktioniert die Portweiterleitung, die Sie auf Ihrem Primärrouter eingerichtet haben, ordnungsgemäß.







    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}







    Wenn Sie den Anmeldebildschirm Ihres GL.iNet-Routers (Sekundärrouter) nicht sehen, funktioniert die Portweiterleitung nicht ordnungsgemäß. Richten Sie die Portweiterleitung erneut ein oder stellen Sie sicher, dass Ihr Primärrouter die Portweiterleitung korrekt unterstützt.





#### Situation 2: Der WireGuard-Server zeigt an, dass mein VPN-Client verbunden ist, aber der VPN-Client kann nicht auf das Internet zugreifen







??? "Folgen Sie diesen Schritten"







    Befolgen Sie die unten beschriebenen Schritte für jede mögliche Ursache und prüfen Sie, ob das Problem behoben ist. Wenn das Problem behoben ist, können Sie den Rest dieses Abschnitts überspringen.







    **Mögliche Ursache 1: Ihr Internetdienstanbieter kann die DNS-Server von GL.iNet möglicherweise nicht auflösen**







    Versuchen Sie, die DNS-Serveradressen manuell zu konfigurieren, indem Sie die folgenden Schritte ausführen:







    1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres GL.iNet-Routers ein (z. B. 192.168.8.1) und melden Sie sich an.



    2. Klicken Sie in der linken Seitenleiste auf **Network** > **DNS**.



    3. Wählen Sie bei **Mode** die Option **Manual DNS** aus.



    4. Wählen Sie bei **DNS Server 1** die Option **Google Public DNS** aus.



    5. Klicken Sie auf **Apply**.







    **Mögliche Ursache 2: Die Gateway-IP Ihres Primärrouters steht in Konflikt mit der IP-Adresse des WireGuard-Servers**







    Versuchen Sie, die IPv4-Adresse zu ändern, indem Sie die folgenden Schritte ausführen:







    1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres GL.iNet-Routers ein (z. B. 192.168.8.1) und melden Sie sich an.



    2. Klicken Sie in der linken Seitenleiste auf **VPN** > **WireGuard Server**.



    3. Geben Sie auf der Registerkarte **Configuration** im Feld **IPv4 Address** eine neue IP-Adresse ein (z. B. 10.1.0.1/24).



    4. Klicken Sie auf **Apply**.







    **Mögliche Ursache 3: Wenn sowohl Ihr WireGuard-Server als auch Ihr WireGuard-Client auf GL.iNet-Routern eingerichtet wurden, stehen ihre LAN-IP-Adressen in Konflikt**







    Versuchen Sie, die LAN-IP-Adresse auf einem der beiden Router zu ändern, indem Sie die folgenden Schritte ausführen:







    1. Melden Sie sich in einem Webbrowser beim Admin-Panel eines der beiden GL.iNet-Router an (z. B. 192.168.8.1).



    2. Klicken Sie in der linken Seitenleiste auf **Network** > **LAN**.



    3. Geben Sie im Feld **Router IP address** eine neue LAN-IP-Adresse ein (z. B. 192.168.10.1).



    4. Klicken Sie auf **Apply**.







    **Mögliche Ursache 4: Die IP-Adresse des WireGuard-Servers wurde aktualisiert, aber das Subnetz fehlt**







    Fügen Sie Ihrer WireGuard-Server-IP-Adresse ein Subnetz hinzu, indem Sie die folgenden Schritte ausführen:







    1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres GL.iNet-Routers ein (z. B. 192.168.8.1) und melden Sie sich an.



    2. Klicken Sie in der linken Seitenleiste auf **VPN** > **WireGuard Server**.



    3. Fügen Sie auf der Registerkarte **Configuration** im Feld **IPv4 Address** hinter **10.0.0.1** den Wert **/24** hinzu.



    4. Klicken Sie auf **Apply**.







#### Situation 3: Der WireGuard-Server läuft, aber ich kann meinen VPN-Client nicht damit verbinden







??? "Folgen Sie diesen Schritten"







    Befolgen Sie die unten beschriebenen Schritte für jede mögliche Ursache und prüfen Sie, ob das Problem behoben ist. Wenn das Problem behoben ist, können Sie den Rest dieses Abschnitts überspringen.







    **Mögliche Ursache 1: Die Portweiterleitung, die Sie auf Ihrem Primärrouter eingerichtet haben, funktioniert möglicherweise nicht richtig**







    Um zu prüfen, ob die Portweiterleitung richtig funktioniert, leiten Sie testweise den HTTPS-Port an Ihren WireGuard-Server weiter, indem Sie die in Situation 1 beschriebenen Lösungsschritte ausführen.







    **Mögliche Ursache 2: Möglicherweise haben Sie keine öffentliche IP-Adresse**







    Um dies zu prüfen, folgen Sie dieser [Seite](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).







    **Mögliche Ursache 3: Wenn sowohl Ihr WireGuard-Server als auch Ihr WireGuard-Client auf GL.iNet-Routern eingerichtet wurden, stehen ihre LAN-IP-Adressen in Konflikt**







    Ändern Sie die LAN-IP-Adresse auf einem der beiden Router, indem Sie die folgenden Schritte ausführen:







    1. Melden Sie sich in einem Webbrowser beim Admin-Panel eines der beiden GL.iNet-Router an (z. B. 192.168.8.1).



    2. Klicken Sie in der linken Seitenleiste auf **Network** > **LAN**.



    3. Geben Sie im Feld **Router IP address** eine neue LAN-IP-Adresse ein (z. B. 192.168.10.1).



    4. Klicken Sie auf **Apply**.







    **Mögliche Ursache 4: Das Gerät, mit dem Sie eine Verbindung zum WireGuard-Server herstellen, ist mit dessen Wi-Fi-Netzwerk oder LAN-Port verbunden**







    Verbinden Sie Ihr Gerät mit einem anderen Wi-Fi-Netzwerk oder dem Mobilfunknetz.







    **Mögliche Ursache 5: In der Konfigurationsdatei, die Sie auf Ihr Client-Gerät hochgeladen haben, fehlen möglicherweise einige Zeilen**







    Laden Sie Ihre Konfigurationsinformationen erneut hoch.







#### Situation 4: Der WireGuard-Server ist verbunden, aber die Verbindung ist nicht stabil







??? "Folgen Sie diesen Schritten"







    Führen Sie die folgenden Schritte aus, um das Problem zu beheben. Prüfen Sie nach jedem Schritt, ob das Problem behoben ist. Wenn das Problem behoben ist, können Sie die restlichen Schritte überspringen.







    1. Ändern Sie auf Ihrem VPN-Client-Gerät die MTU von **1420** auf einen kleineren Wert (z. B. **1380**).



    2. Aktivieren Sie auf Ihrem Primärrouter, falls verfügbar, die Funktion VPN Passthrough.



    3. Versuchen Sie, DNS-Server auf Ihrem GL.iNet-Router manuell zu konfigurieren, indem Sie die folgenden Schritte ausführen:



        1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres GL.iNet-Routers ein (z. B. 192.168.8.1) und melden Sie sich an.



        2. Klicken Sie in der linken Seitenleiste auf **Network** > **DNS**.



        3. Wählen Sie bei Mode die Option **Manual DNS** aus.



        4. Wählen Sie bei **DNS Server 1** die Option **Google Public DNS** aus.



        5. Klicken Sie auf **Apply**.







#### Situation 5: Der WireGuard-Server hat plötzlich aufgehört zu funktionieren







??? "Folgen Sie diesen Schritten"







    Befolgen Sie die unten beschriebenen Schritte für jede mögliche Ursache und prüfen Sie, ob das Problem behoben ist. Wenn das Problem behoben ist, können Sie den Rest dieses Abschnitts überspringen.







    **Mögliche Ursache 1: An dem Ort, an dem Sie Ihren WireGuard-Server eingerichtet haben, könnte ein Stromausfall vorliegen**







    Prüfen Sie mithilfe der in Situation 1 beschriebenen Lösungsschritte oder über [GoodCloud](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/) (falls Sie Ihren Router zuvor damit verbunden haben), ob Ihr WireGuard-Server noch online ist.







    **Mögliche Ursache 2: Sie haben Dynamic DNS (DDNS) nicht aktiviert**







    Wenn Sie eine dynamische IP-Adresse haben (was sehr wahrscheinlich ist), müssen Sie DDNS aktivieren. [Aktivieren Sie DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) und führen Sie anschließend die übrigen Schritte aus, um den WireGuard-Server erneut einzurichten.







    **Mögliche Ursache 3: Die Portweiterleitung funktioniert aus unbekannten Gründen nicht mehr**







    [Richten Sie die Portweiterleitung](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) mit einem anderen Port erneut ein.







---







Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.



