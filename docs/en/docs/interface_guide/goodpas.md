# GoodPAS

**Note**: This feature was introduced in firmware v4.10, where AstroWarp was renamed to GoodPAS. If your device is running an older firmware version, please refer to [AstroWarp](./astrowarp.md).

---

On the left side of web Admin Panel, go to the **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS is an advanced remote access solution integrated into the GL.iNet router SDK. It adopts the AmneziaWG protocol with built-in traffic obfuscation, delivering stable and secure connections for reliable remote access anytime, anywhere.

This feature enables seamless remote access to your home network. You can directly set up and pair devices via a dynamic access code in the web Admin Panel, quickly establishing a secure connection between your travel router and home network in just seconds, with no registration or login required.

**Note**:

1. It is not recommended to use GoodPAS with any of the following features at the same time, as this may cause routing conflicts: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.

2. When GoodPAS is enabled, the Network Mode cannot be used.

## Quick Setup

In the following example, we'll use **Flint 3(GL-BE9300)** and **Mango 2(GL-MG1300)** to set up an GoodPAS network.

Flint 3 will act as the home router, while Mango 2 will act as the travel router that routes network traffic back to Flint 3 for Internet access.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Configure Flint 3 for Internet.

    Log in to the Flint 3's web Admin Panel and navigate to the INTERNET page. Connect it to the Internet using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular.

    As shown below, the Flint 3 home router is connected to the ISP modem (Hong Kong Broadband Network Ltd) via an Ethernet cable.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Generate Access Code.

    On the Flint 3's web admin panel, navigate to **CLOUD SERVICES** -> **GoodPAS**. Click **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    It will generate an Access Code. Copy this code for later use.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Configure Mango 2 for Internet.

    Log in to the Mango 2's web Admin Panel, and navigate to the INTERNET page. Connect it to the Internet using one of the supported internet connection methods: Ethernet, Repeater, Tethering, and Cellular.

    As shown below, the Mango 2 travel router is connected to the personal hotspot of an iPhone 17 (located in Shenzhen, using the China Unicom Guangdong Province network).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Enter Access Code.

    On the Mango 2's web Admin Panel, navigate to **CLOUD SERVICES** -> **GoodPAS**. Click **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Enter the Access Code obtained in Step 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Wait for the verification to complete.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    It will then connect to the Flint 3 home router successfully. Now you can browse the Internet through your home network securely.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    On the Flint 3's web Admin Panel, it also displays the connection status, as shown below.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Test Connectivity

1. Connect a laptop or smartphone to the Wi-Fi of the Mango 2 travel router.

2. Open a browser and visit [ipcheck.ing](https://ipcheck.ing/){target="_blank"} or any other IP address lookup website.

    It will show the public IP address of Mango 2, indicating that Mango 2 is accessing the Internet through your Flint 3 home router.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Disconnect the GoodPAS connection on Mango 2, then refresh the webpage to resubmit the IP query request. 

    It will show the public IP address of Mango 2, indicating that Mango 2 is accessing the Internet through its local network.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **Q: What is the format of the dynamic access code, and how long is it valid?**

    A: It is an 8-character code combining numbers and uppercase letters, valid for 10 minutes.

2. **Q: What happens to the travel router if I terminate the connection on the home router?**

    A: The travel router will disconnect and be pending with no network access. Once the home router resumes connection, the travel router can reconnect automatically without entering the access code again.

3. **Q: In what scenarios will the travel router enter pending state?**
    
    A: The travel router will enter pending state when the home router meets any of the following conditions:
    
    - Terminates the GoodPAS connection
    - Loses internet access

4. **Q: What does the Reset button in the top right corner do?**

    A: It will clear all authorized devices and revert to the router role selection page for re-selection.

5. **Q: What happens to the travel router if I reset the GoodPAS on the home router?**

    A: Once the home router is reset, the remotely connected devices will be disconnected from the GoodPAS network and revert to their local network for internet access.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.