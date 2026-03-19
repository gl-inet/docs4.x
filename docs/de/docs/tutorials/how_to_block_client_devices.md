# So blockieren Sie bestimmte Client-Geräte auf einem GL.iNet-Router

In diesem Tutorial erfahren Sie, wie Sie bestimmte Client-Geräte auf einem GL.iNet-Router blockieren. Durch das Blockieren von Client-Geräten verhindern Sie unbefugten Zugriff auf Ihr Netzwerk. Das erhöht die Netzwerksicherheit und hilft Ihnen dabei, den Internetzugang Ihrer Familie zu steuern.

GL.iNet-Router blockieren Client-Geräte anhand ihrer MAC-Adressen (eine eindeutige 12-stellige Kennung, die einzelnen Geräten in einem Netzwerk zugewiesen wird). Diese Methode wird auch als MAC-Adressfilterung bezeichnet.

Sie können Client-Geräte auf Ihrem GL.iNet-Router auf zwei Arten blockieren: über das [Admin-Panel des Routers](#block-client-devices-via-the-admin-panel) oder über die [GL.iNet-App](#block-client-devices-via-the-glinet-mobile-app).

## Client-Geräte über das Admin-Panel blockieren {#block-client-devices-via-the-admin-panel}

### 1. Im Admin-Panel anmelden

Geben Sie in einem Webbrowser `192.168.8.1` ein. Geben Sie Ihr Passwort ein und klicken Sie dann auf **Login**.

### 2. Client-Geräte blockieren

Je nachdem, ob Ihnen die MAC-Adressen vorliegen, gibt es zwei Möglichkeiten, Client-Geräte zu blockieren:

* Wenn Sie die MAC-Adressen nicht haben: Verwenden Sie die [erste Methode](#method-1-block-devices-without-their-mac-addresses), mit der Sie Geräte blockieren können, die in den Listen angezeigt werden.
* Wenn Sie die MAC-Adressen haben: Verwenden Sie die [zweite Methode](#method-2-block-devices-with-their-mac-addresses).

#### Methode 1: Geräte ohne ihre MAC-Adressen blockieren {#method-1-block-devices-without-their-mac-addresses}

1. Klicken Sie in der linken Seitenleiste auf **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Schalten Sie den Schalter neben dem Gerät ein.
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Wenn die Geräte, die Sie blockieren möchten, nicht in den Listen angezeigt werden, müssen Sie sie blockieren, indem Sie [ihre MAC-Adressen zur Blocklist hinzufügen](#method-2-block-devices-with-their-mac-addresses).

#### Methode 2: Geräte mit ihren MAC-Adressen blockieren {#method-2-block-devices-with-their-mac-addresses}

Für diese Methode müssen Sie die MAC-Adresse des Geräts ermitteln. Beachten Sie dazu die Anweisungen des Geräteherstellers.
Sobald Sie die MAC-Adresse des Geräts haben, gehen Sie wie folgt vor:

1. Klicken Sie in der linken Seitenleiste auf **Clients**.
2. Klicken Sie oben auf **Blocklist**.
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Verwenden Sie eine der folgenden Methoden, um Geräte zu blockieren:
    - Um die MAC-Adressen einzeln einzugeben: Geben Sie sie in das leere Feld ein.
    - Um eine Liste mit MAC-Adressen zu importieren: Klicken Sie auf **Import Clients**. Importieren Sie eine Datei und klicken Sie dann auf **Import**.
4. Klicken Sie auf **Apply**.
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Client-Geräte über die GL.iNet-App blockieren {#block-client-devices-via-the-glinet-mobile-app}

**Hinweis:** Bevor Sie beginnen, installieren Sie die GL.iNet-App auf Ihrem Gerät und richten Sie sie ein.

Je nachdem, ob Ihnen die MAC-Adressen vorliegen, gibt es zwei Möglichkeiten, Client-Geräte zu blockieren:

* Wenn Sie die MAC-Adressen nicht haben: Verwenden Sie die [erste Methode](#mobile-1), mit der Sie die in der Liste angezeigten Geräte blockieren können.
* Wenn Sie die MAC-Adressen haben: Verwenden Sie die [zweite Methode](#mobile-2).

### Methode 1: Geräte ohne ihre MAC-Adressen blockieren {#mobile-1}

1. Tippen Sie im Hauptbildschirm der App unter **Connected Clients** und **Office Clients** auf das Gerät, das Sie blockieren möchten.
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. Schalten Sie unter **Settings** den Schalter **Block** ein.
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Wenn die Geräte, die Sie blockieren möchten, nicht in den Listen angezeigt werden, müssen Sie sie blockieren, indem Sie [ihre MAC-Adressen zur Blocklist hinzufügen](#mobile-2).

### Methode 2: Geräte mit ihren MAC-Adressen blockieren {#mobile-2}

Für diese Methode müssen Sie die MAC-Adresse des Geräts ermitteln, das Sie blockieren möchten. Beachten Sie dazu die Anweisungen des Herstellers.
Sobald Sie die MAC-Adresse des Geräts haben, gehen Sie wie folgt vor:

1. Tippen Sie im Hauptbildschirm der App auf das Symbol **Settings** > **Access Control**.
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Tippen Sie auf **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Verwenden Sie eine der folgenden Methoden, um Geräte zu blockieren:
    - Um die MAC-Adressen einzeln einzugeben: Tippen Sie auf **Add MAC address**. Geben Sie die MAC-Adresse ein und tippen Sie dann auf **Done**.
    - Um eine Liste mit MAC-Adressen zu importieren, klicken Sie auf **Import Clients** > **Import Clients**. Tippen Sie auf eine Datei.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
