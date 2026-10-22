# Problemmeddelande och lösningar när GL-X3000/GL-XE3000/GL-X2000 inte fungerar med EE SIM-kort {#problem-notification-and-solutions-for-gl-x3000gl-xe3000gl-x2000-failure-to-work-with-ee-sim-cards}

Bästa GL.iNet-kund,

Vi har nyligen uppmärksammat att vissa kunder får anslutningsproblem med GL-X3000/GL-XE3000/GL-X2000 när de använder EE SIM-kort. Vid ytterligare felsökning upptäckte vi att vissa EE SIM-kort endast stöder IPv4-protokollet. Standardinställningarna på GL.iNets mobilroutrar aktiverar dock både IPv4 och IPv6 samtidigt, vilket orsakar problemet.

## Lösningar och tillfälliga lösningar {#solutions-workarounds}

1. **Firmwareuppdatering**

    Vi har publicerat nya firmwareuppdateringar som ändrar standardprotokollet till IPv4 för att lösa problemet. Kunder som behöver IPv6 kan fortfarande ändra inställningen till IPv4 och IPv6 i administrationspanelen.

    | Routermodell                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Ladda ned firmware](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Ladda ned firmware](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Ladda ned firmware](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Tillfällig lösning för andra modeller**

    Om du har en annan modell eller inte vill använda firmwareversionerna ovan kör du AT-kommandona i tur och ordning efter att mobilanslutningen har startats.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Obs!** "User_APN" är vanligtvis "everywhere" för EE SIM-kort. Upprepa proceduren varje gång routern har startats om.

    ??? note "Hur kör jag ett AT-kommando?"

        1. Gå till INTERNET -> avsnittet Cellular i webbadministrationspanelen, klicka på ikonen med tre punkter i det övre högra hörnet och välj **Modem AT Command**.

            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/faq/ee_sim_failure/at_command_0.jpg){class="glboxshadow"}

            På äldre firmware klickar du på verktygsknappen i det övre högra hörnet för att öppna sidan för modemhantering.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/faq/ee_sim_failure/modem_management_button.png){class="glboxshadow"}

        2. Leta reda på AT-kommandot, som visas nedan.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/faq/ee_sim_failure/at_command_1.png){class="glboxshadow"}

Om du får fler problem kontaktar du vår support på [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Med vänlig hälsning,

GL.iNet Technical Support

17 juni 2025
