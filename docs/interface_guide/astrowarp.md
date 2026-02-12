# AstroWarp

!!! note

    This guide introduces the new version of AstroWarp, which is currently available on **Flint 3 (GL-BE9300)** and **Slate 7 (GL-BE3600)** in firmware v4.8.4 and v4.8.3 respectively. 

    For other models, please refer to [this link](https://docs.astrowarp.net/){target="_blank"} for more information.

AstroWarp is an advanced networking feature integrated into GL.iNet routers. It enables seamless remote access to your home network without registration or login. Using the AmneziaWG protocol with built-in traffic obfuscation, it keeps your connection stable and secure, making it ideal for reliable remote access wherever you go.

Users can set up an AstroWarp network directly through the GL.iNet router admin panel. Simply pair your routers using an access code and you can securely connect your travel router to your home network in seconds.

**Note:** 

1. It is not recommended to use AstroWarp with any of the following features at the same time, as this may cause routing conflicts: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. When AstroWarp is enabled, the Network Mode cannot be used.

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
