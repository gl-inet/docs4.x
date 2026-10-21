# Blockera vissa klientenheter på en GL.iNet-router {#how-to-block-specific-client-devices-on-a-glinet-router}

Den här guiden visar hur du blockerar vissa klientenheter på en GL.iNet-router. Genom att blockera klientenheter förhindrar du obehörig åtkomst till nätverket. Det förbättrar nätverkssäkerheten och hjälper dig att styra familjens internetåtkomst.

GL.iNet-routrar blockerar klientenheter utifrån deras MAC-adresser, en unik identifierare med 12 tecken som tilldelas varje enhet i ett nätverk. Metoden kallas även MAC-adressfiltrering.

Du kan blockera klientenheter på GL.iNet-routern på två sätt: via [routerns administrationspanel](#block-client-devices-via-the-admin-panel) eller [GL.iNet-mobilappen](#block-client-devices-via-the-glinet-mobile-app).

## Blockera klientenheter via administrationspanelen {#block-client-devices-via-the-admin-panel}

### 1. Logga in på administrationspanelen {#1-sign-in-to-the-admin-panel}

Ange `192.168.8.1` i en webbläsare. Ange lösenordet och klicka sedan på **Login**.

### 2. Blockera klientenheter {#2-block-client-devices}

Det finns två sätt att blockera klientenheter beroende på om du har deras MAC-adresser:

* Om du saknar MAC-adresserna använder du [den första metoden](#method-1-block-devices-without-their-mac-addresses), som låter dig blockera enheter som visas i listorna.
* Om du har MAC-adresserna använder du [den andra metoden](#method-2-block-devices-with-their-mac-addresses).

#### Metod 1: Blockera enheter utan deras MAC-adresser {#method-1-block-devices-without-their-mac-addresses}

1. Klicka på **Clients** i det vänstra sidofältet.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Aktivera reglaget bredvid enheten.
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Om enheterna som du vill blockera inte visas i listorna måste du blockera dem genom att [lägga till deras MAC-adresser i blockeringslistan](#method-2-block-devices-with-their-mac-addresses).

#### Metod 2: Blockera enheter med deras MAC-adresser {#method-2-block-devices-with-their-mac-addresses}

För metoden behöver du enhetens MAC-adress. Följ anvisningarna från enhetens tillverkare. När du har MAC-adressen följer du dessa steg:

1. Klicka på **Clients** i det vänstra sidofältet.
2. Klicka på **Blocklist** högst upp.
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Blockera enheter med någon av metoderna:
    - Ange MAC-adresserna en i taget i det tomma fältet.
    - Importera en lista med MAC-adresser genom att klicka på **Import Clients**. Importera en fil och klicka sedan på **Import**.
4. Klicka på **Apply**.
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Blockera klientenheter via GL.iNet-mobilappen {#block-client-devices-via-the-glinet-mobile-app}

**Obs!** Installera och konfigurera GL.iNet-mobilappen på enheten innan du börjar.

Det finns två sätt att blockera klientenheter beroende på om du har deras MAC-adresser:

* Om du saknar MAC-adresserna använder du [den första metoden](#mobile-1), som låter dig blockera enheter som visas i listan.
* Om du har MAC-adresserna använder du [den andra metoden](#mobile-2).

### Metod 1: Blockera enheter utan deras MAC-adresser {#mobile-1}

1. Tryck på enheten som du vill blockera under **Connected Clients** eller **Offline Clients** på appens huvudskärm.
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. Aktivera reglaget **Block** under **Settings**.
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Om enheterna som du vill blockera inte visas i listorna måste du blockera dem genom att [lägga till deras MAC-adresser i blockeringslistan](#mobile-2).

### Metod 2: Blockera enheter med deras MAC-adresser {#mobile-2}

För metoden behöver du MAC-adressen för enheten som du vill blockera. Följ anvisningarna från tillverkaren. När du har MAC-adressen följer du dessa steg:

1. Tryck på inställningsikonen > **Access Control** på appens huvudskärm.
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Tryck på **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Blockera enheter med någon av metoderna:
    - Ange MAC-adresserna en i taget genom att trycka på **Add MAC address**. Ange MAC-adressen och tryck på **Done**.
    - Importera en lista med MAC-adresser genom att klicka på **Import Clients** > **Import Clients**. Tryck på en fil.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
