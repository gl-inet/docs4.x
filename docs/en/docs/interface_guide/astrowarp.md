# AstroWarp

**Note**: This guide covers the new version of AstroWarp.

The legacy AstroWarp, while visible in the web Admin Panel, relied on a standalone AstroWarp platform to establish remote network connections. See [here](https://docs.astrowarp.net/){target="_blank"} for documentation on the legacy AstroWarp.

By contrast, the new AstroWarp is integrated into the GL.iNet router SDK. It adopts the AmneziaWG protocol with built-in traffic obfuscation, delivering stable and secure connections for reliable remote access anytime, anywhere.

This feature enables seamless remote access to your home network. You can directly set up and pair devices via a dynamic access code in the web Admin Panel, quickly establishing a secure connection between your travel router and home network in just seconds, with no registration or login required.

**Note:** 

1. It is not recommended to use AstroWarp with any of the following features at the same time, as this may cause routing conflicts: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. When AstroWarp is enabled, the Network Mode cannot be used.

## Supported Models

??? "Supported Models"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **Note**: Models marked with ※ support the integrated AstroWarp in Beta firmware.

??? "Unsupported Models"
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Quick Setup

In the following example, we'll use **Flint 3 (GL-BE9300)** and **Slate 7 (GL-BE3600)** to set up an AstroWarp network. 

Flint 3 will act as the home router, while Slate 7 will act as the travel router that routes network traffic back to Flint 3 for Internet access.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Note**: Each GL.iNet router comes with **10 GB free data per month** for AstroWarp networking. Devices in an AstroWarp network will use the home router's data to access the Internet. You can upgrade to the AstroWarp+ plan for unlimited data as needed.
 
1. Configure Flint 3 for Internet.

    Log in to the Flint 3's web admin panel and navigate to the **INTERNET** page. Connect it to the Internet using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular.

    As shown below, the Flint 3 home router is connected to the ISP modem (Hong Kong Broadband Network Ltd) via an Ethernet cable.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Generate Access Code.

    On the Flint 3's web admin panel, navigate to **CLOUD SERVICES** -> **AstroWarp**. Click **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    It will generate an **Access Code**. Copy this code for later use.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configure Slate 7 for Internet.

    Log in to the Slate 7's web admin panel, and navigate to the **INTERNET** page. Connect it to the Internet using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular.

    As shown below, the Slate 7 travel router is connected to the personal hotspot of an iPhone 15 Pro (located in Shenzhen, using the China Unicom Guangdong Province network).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Enter Access Code.

    On the Slate 7's web admin panel, navigate to **CLOUD SERVICES** -> **AstroWarp**. Click **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Enter the Access Code obtained in Step 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Wait for the verification to complete.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    It will then connect to the Flint 3 home router successfully. Now you can browse the Internet through your home network securely.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    On the Flint 3's web admin panel, it also displays the connection status, as shown below.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Test Connectivity

1. Connect a laptop or smartphone to the Wi-Fi of the Slate 7 travel router.

2. Open a browser and visit [ipcheck.ing](https://ipcheck.ing/){target="_blank"} or any other IP address lookup website.

    It will show the public IP address of Flint 3, indicating that Slate 7 is accessing the Internet through your Flint 3 home router.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Disconnect the AstroWarp connection on Slate 7, then refresh the webpage to resubmit the IP query request. 

    It will show the public IP address of Slate 7, indicating that Slate 7 is accessing the Internet through its local network.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Upgrade Plan

Each GL.iNet router comes with **10 GB free data per month** for AstroWarp networking. Devices in an AstroWarp network will use the home router's data to access the Internet. 

You can upgrade to the **AstroWarp+** plan for unlimited data as needed.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
