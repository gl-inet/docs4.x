# Teknisk support via GoodCloud {#technical-support-via-goodcloud}

Ibland behöver du dela din enhet via GoodCloud för att få teknisk support från GL.iNet. Den här guiden visar hur du delar enheten med GL.iNets tekniska support.

## Aktivera GoodCloud och fjärråtkomst {#enable-goodcloud-and-remote-access}

Innan du delar enheten med GL.iNets tekniska support bör du se till att routern har ytterligare en internetanslutning för stabilitet. Konfigurera en Ethernet- eller repeateranslutning som reservanslutning för redundansväxling och kontrollera att den fungerar korrekt.

Logga sedan in på routerns webbadministrationspanel för att aktivera GoodCloud och fjärråtkomst.

Välj den instruktion som motsvarar enhetens firmwareversion.

??? "För firmwareversion 4.10 och senare"

    Gå till **CLOUD SERVICES** -> **GoodCloud** och klicka på **Get Started**.

    ![GoodCloud 4.10 1](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/goodcloud_v4.10_1.png){class="glboxshadow"}

    En URL visas på sidan. Klicka på **link** för att logga in via sidan GL.iNet Account eller kopiera länken för fjärrbindning. Registrera först ett konto om du inte redan har ett.

    ![GoodCloud 4.10 2](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/goodcloud_v4.10_2.png){class="glboxshadow"}

    När du har loggat in binds enheten automatiskt till ditt Cloud-konto. På GoodCloud-sidan kan du se **Device Identity** och **Recent Cloud Logs**. **Remote Web Access** och **Remote SSH** är också aktiverade som standard.

    ![GoodCloud 4.10 3](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/goodcloud_v4.10_3.png){class="glboxshadow"}

??? "För firmwareversion 4.7.x–4.9.x"

    Gå till **CLOUD SERVICES** -> **GoodCloud**, klicka på **Get Started** och logga in på ditt Cloud-konto i det övre högra hörnet. Registrera först ett konto om du inte redan har ett.

    ![get started log in](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/get_started_v4.7.x.png){class="glboxshadow"}

    När du har loggat in binds enheten automatiskt till ditt Cloud-konto.

    Gå tillbaka till sidan **GoodCloud**, aktivera **Remote SSH** och **Remote Web Access** och klicka på **Apply**.

    ![enable remote access 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.7.x.png){class="glboxshadow"}

??? "För firmwareversion 4.6.x eller tidigare"

    Gå till **APPLICATIONS** -> **GoodCloud**, aktivera **GoodCloud**, **Remote SSH** och **Remote Web Access**, markera **Terms of Service & Privacy Policy** och klicka sedan på **Apply**.

    ![enable GoodCloud 4.6](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.6.x.png){class="glboxshadow"}

## Logga in på Cloud-kontot och bind enheten {#log-in-cloud-account-and-bind-device}

Om routern kör firmware v4.7 eller senare kan du registrera ett konto i routerns webbadministrationspanel och logga in direkt. När du har loggat in binds den aktuella enheten automatiskt till ditt Cloud-konto.

Om routern kör firmware v4.6 eller tidigare följer du stegen nedan för att logga in på kontot och binda enheten.

1. Besök [GoodCloud](https://www.goodcloud.xyz){target="_blank"} och logga in på ditt konto. Registrera först ett konto om du inte redan har ett.

2. Bind enheten till GoodCloud. Se [Bind Devices to Cloud](../interface_guide/cloud.md#bind-devices-to-cloud).

## Dela enheten med GL.iNets tekniska support {#share-device-with-glinet-technical-support}

1. Besök [GoodCloud](https://www.goodcloud.xyz){target="_blank"} och logga in.

2. Gå till **Devices** -> **Bound Devices** och klicka på enheten som du vill dela.

    ![bound devices](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/bound_devices.png){class="glboxshadow"}

3. Sidan med enhetsinformation öppnas. Klicka på fliken **SHARE** och sedan på **Share Device** enligt nedan.

    ![share device](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device.png){class="glboxshadow"}

    Dela sedan enheten med GL.iNets tekniska support. Skydda ditt privata nätverk genom att aktivera **Auto Expire Sharing** och ange att delningen ska upphöra efter 7 dagar. Klicka därefter på **Confirm**.

    ![share device with GL.iNet support](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device_confirm.png){class="glboxshadow"}

**Sekretessmeddelande**

1. Enheter som delas med GL.iNets tekniska support används ENDAST för felsökning. GL.iNets support sparar, säkerhetskopierar eller öppnar inte din privata information.

2. För att skydda lösenordet rekommenderar vi att du ändrar inloggningslösenordet till webbadministrationspanelen till ett tillfälligt lösenord innan du delar enheten med GL.iNets support. Du kan återställa ditt vanliga lösenord när felsökningen är klar.

## Lämna information till GL.iNets tekniska support {#provide-information-to-glinet-technical-support}

När du har delat enheten skickar du routerns **MAC-adress** och **administratörslösenord** till berörd GL.iNet-supportmedarbetare via e-post eller ett privat meddelande i forumet för fjärrfelsökning.

**Skicka inte informationen via både e-post och privat meddelande samtidigt.**

- **Via e-post:** Skicka informationen till berörd GL.iNet-supportmedarbetare på [support@gl-inet.com](mailto:support@gl-inet.com).

- **Via ett privat meddelande i det officiella forumet:** Skicka ett privat meddelande till berörd GL.iNet-supportmedarbetare i det [officiella forumet](https://forum.gl-inet.com){target="_blank"}.

    Följ dessa steg för att skicka ett privat meddelande i forumet.

    1. Öppna det [officiella forumet](https://forum.gl-inet.com){target="_blank"}.
    2. Klicka på användarnamnet för GL.iNet-supportmedarbetaren som du har kontakt med.
    3. Klicka på knappen **Message** för att skicka ett privat meddelande.

        ![How to send a private message](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/PM_via_forum.gif){class="glboxshadow"}

Nya användare kan ibland inte skicka privata meddelanden till GL.iNets tekniska support. Svara i så fall i samma tråd där ni redan har kontakt och be supportmedarbetaren att skicka ett privat meddelande till dig först.

Dela **INTE** enhetsinformationen offentligt. Dela den endast med GL.iNets tekniska support via ett privat meddelande.

När problemet har lösts avslutar du delningen och ändrar routerns administratörslösenord.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
