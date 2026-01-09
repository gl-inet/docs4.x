# AdGuard Home

AdGuard Home is a network-wide software for blocking ads and tracking. Once set up, it will cover ALL the devices on your home network, and there is no need for any additional client-side software. 

## Supported models

??? "Supported Models"
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

??? "Unsupported Models"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Setup

Log in to the router's web Admin Panel -> APPLICATIONS -> AdGuard Home. Toggle the switch to enable AdGuard Home and click Apply. 

![adguard home apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/apply.png){class="glboxshadow"}

- AdGuard Home Handle Client Requests: If this option is enabled, DNS queries from client devices will be handled directly by AdGuard Home. AdGuard Home will show DNS query logs by clients, but this will cause VPN policies based on domain not to work.

This page displays statistics such as the DNS queries, blocked domains, etc, which is through the API provided by AdGuard Home. 

![adguard home web panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/adguardhome_web_panel.png){class="glboxshadow"}

Then please click **Settings Page**.

![adguard home started](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/settings_page.png){class="glboxshadow"}

It will be re-directed to the AdGuard Home's official settings page, where you can perform advanced configuration for the filter rules, etc.

![adguard home settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/adguardhome_dashboard.png){class="glboxshadow"}

If you have any questions, please visit [Adguard Home Support Center](https://adguard.com/en/support.html){target="_blank"} for further assistance.

---