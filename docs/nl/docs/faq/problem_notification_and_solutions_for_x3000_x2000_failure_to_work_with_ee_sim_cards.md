# Probleemmelding en oplossingen wanneer GL-X3000/GL-XE3000/GL-X2000 niet met EE-simkaarten werkt {#problem-notification-and-solutions-for-gl-x3000gl-xe3000gl-x2000-failure-to-work-with-ee-sim-cards}

Dear GL.iNet Customers,

We hebben vastgesteld dat sommige klanten verbindingsproblemen met GL-X3000/GL-XE3000/GL-X2000 ondervinden bij gebruik van EE-simkaarten. Bepaalde EE-simkaarten ondersteunen alleen IPv4, terwijl GL.iNet-cellulaire routers standaard IPv4 en IPv6 tegelijk inschakelen. Dit veroorzaakt het probleem.

## Solutions & Workarounds {#solutions-workarounds}

1. **Firmware Update**

    We hebben nieuwe firmware uitgebracht waarin het standaardprotocol naar IPv4 is gewijzigd. Gebruikers die IPv6 nodig hebben, kunnen de instelling in het beheerpaneel wijzigen naar IPv4 & IPv6.

    | Router Model                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Firmware Download](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Firmware Download](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Firmware Download](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Workaround for Other Models**

    Als je een ander model hebt of de bovenstaande firmware niet wilt gebruiken, voer je na het starten van de mobiele verbinding de AT-opdrachten achtereenvolgens uit.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Opmerking**: voor EE-simkaarten is "User_APN" meestal "everywhere". Herhaal dit proces na elke herstart van de router.

    ??? note "How do I run AT command?"

        1. Ga in het webbeheerpaneel naar INTERNET -> Cellular, klik rechtsboven op het pictogram met drie puntjes en selecteer **Modem AT Command**.

            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/faq/ee_sim_failure/at_command_0.jpg){class="glboxshadow"}

            Klik bij oudere firmware rechtsboven op de gereedschapsknop om de modembeheerpagina te openen.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/faq/ee_sim_failure/modem_management_button.png){class="glboxshadow"}

        2. Locate the AT command, as shown below.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/faq/ee_sim_failure/at_command_1.png){class="glboxshadow"}

Neem bij verdere problemen contact op met ons ondersteuningsteam via [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Sincerely,

GL.iNet Technical Support

June 17, 2025
