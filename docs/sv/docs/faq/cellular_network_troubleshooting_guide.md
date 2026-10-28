# Felsökningsguide för mobilnät {#cellular-network-troubleshooting-guide}

Kontrollera följande om det inte går att upprätta en mobilanslutning.

??? "Kontrollera enhetens maskinvara"

    **1.1** Använd en standardnätadapter för enheten. Nätadaptrar som inte följer standarden kan ge otillräcklig strömförsörjning.

    **1.2** Kontrollera att **Modem name**, **IMEI** och **SIM ICCID** visas i webbadministrationspanelen.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/no_sim.png){class="glboxshadow"}

    För firmware v4.8 och senare klickar du på **View More Information** för att hitta SIM ICCID.

    Starta om routern om informationen inte visas. Om modemnamnet och IMEI fortfarande inte kan identifieras kontaktar du oss på [support@gl-inet.com](mailto:support@gl-inet.com).

    **1.3** Klicka på **View More** för att kontrollera **Cells Info** och bekräfta att signalen är stabil. Om signalen är mycket svag kontrollerar du att antennerna är korrekt installerade eller flyttar routern till en plats med bra signal och testar igen.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/cells_info.png){class="glboxshadow"}

    **1.4** Klicka på **View More** för att kontrollera om det frekvensband som enheten stöder är kompatibelt med din region.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Kontrollera programvaruinställningarna"

    **2.1** Logga in på webbadministrationspanelen och kontrollera att programmet för mobilanslutning har startats. Du kan även klicka på **Abort** och sedan på **Connect**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/2.png){class="glboxshadow gl-90-desktop"}

    **2.2** Vissa nätoperatörer kan kräva **3G protocol** för anslutningen. Byt till 3G-protokollet och testa igen.

    För firmware v4.7 och tidigare går du till **Manual Setup** -> **Protocol**, väljer **3G** och klickar sedan på **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/3.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/4.png){class="glboxshadow gl-90-desktop"}

    För firmware v4.8 och senare går du till **SIM Card Settings** -> **Protocol**, väljer **3G** och klickar sedan på **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    Enheten återansluter automatiskt. Vänta i några minuter och kontrollera om anslutningen lyckas.

    **2.3** Vissa SIM-kort kräver ett särskilt APN. Om SIM-kortet inte kan registreras kontaktar du operatören för att kontrollera eventuella begränsningar. Konfigurera rätt APN på routern om det behövs och klicka sedan på **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}

    **2.4** Aktivera **Band Masking** och testa igen. För firmware v4.7 och tidigare följer du [den här länken](../interface_guide/internet_cellular_v4.7.md#band-masking). För firmware v4.8 och senare följer du [den här länken](../interface_guide/internet_cellular.md#band-masking).

    **2.5** Lås eller lås upp en mobilmast och testa igen. Funktionen är tillgänglig på GL-E5800 (Mudi 7), GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) och GL-X2000 (Spitz Plus). GL-X2000 (Spitz Plus) stöder funktionen från firmware v4.7. Klicka [här](../interface_guide/internet_cellular.md#lock-tower) för fler instruktioner.

    Genom att låsa till en viss mobilmast kan routern använda en nätverksresurs av hög kvalitet och behålla en stabil mobilanslutning.

    När en mast har låsts fortsätter routern dock att försöka återansluta till den efter en omstart, även om routern har flyttats till en ny plats. Det kan förhindra att routern ansluter automatiskt till mobilnätet. Om det händer kan du antingen låsa upp den aktuella masten via routerns webbadministrationspanel eller låsa routern manuellt till en ny mast.

    **Obs!**
    1. Den låsta masten måste använda frekvensband som stöds av operatören och enheten. Annars kan anslutningen misslyckas.
    2. International Data Roaming är aktiverat som standard på routerns mobilmodul. Om alternativet inaktiveras kan SIM-kortet förlora internetåtkomsten. Låt därför funktionen vara aktiverad.

??? "Kontrollera SIM-kompatibiliteten"

    **3.1** Kontrollera SIM-kompatibiliteten. GL.iNets nordamerikanska mobilroutermodeller är IoT-certifierade. Det innebär dock inte att IoT-SIM-kort krävs: vanliga SIM-kort för konsumenter kan också vara kompatibla. Kontakta operatören om du är osäker på vilken SIM-typ du ska använda.

    Vanliga SIM-typer är: endast data, endast data + tal, IoT och hotspot. Vi rekommenderar SIM-kort för IoT eller hotspot. Det finns ingen garanti för att SIM-kort med endast data eller endast data + tal fungerar.

    **3.2** Vissa SIM-kort måste aktiveras först. Kontrollera att SIM-kortet kan ansluta till internet när det sitter i en telefon och flytta det sedan till routern.

    **3.3** Vissa anpassade SIM-kort kan endast användas i mobiltelefoner eller särskilda enheter. Kontrollera om SIM-kortet är låst till en viss enhet.

    **3.4** I vissa delstater och städer i USA (t.ex. AT&T i Seattle) kan du behöva registrera enhetens IMEI hos operatören. Kontakta operatören om du är osäker på registreringen.

    **3.5** Om "SIM card not registered" visas i webbadministrationspanelen provar du först stegen ovan.

    Vi rekommenderar att du stänger av routern, sätter i SIM-kortet och sedan startar om routern. Vissa modeller stöder inte byte under drift och kanske inte identifierar SIM-kortet om det sätts i när routern är påslagen.

    Kontrollera att alla antenner är korrekt installerade och testa sedan igen utomhus på en plats med stark mobilsignal. En svag signal kan förhindra att SIM-kortet registreras i nätverket.

    Om problemet kvarstår kan SIM-kortet vara inkompatibelt med routern. Kontakta nätoperatören för mer hjälp.

    Om operatören bekräftar att problemet inte gäller SIM-kortet kontaktar du vår support på [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Om SIM-kortet kan registreras och hämta en IP-adress men inte kan nå internet (uppladdning fungerar men nedladdning gör det inte) är SIM-kortet sannolikt begränsat av nätoperatören. Kontakta operatören för att ta bort begränsningen eller ställ in TTL på 65 och testa igen enligt nedan.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/5.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/6.png){class="glboxshadow gl-90-desktop"}

    När du kontaktar nätoperatören anger du enhetens modemnamn, IMEI, SIM ICCID och routermodell.

Om inget av ovanstående löser problemet kontaktar du vår support på [support@gl-inet.com](mailto:support@gl-inet.com).
