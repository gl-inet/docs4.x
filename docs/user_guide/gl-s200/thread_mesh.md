# Thread Mesh

## Thread Network

You can configure and manage Thread Network settings on the **Thread Network** page.

![Thread-Network](https://static.gl-inet.com/docs-iot/en/thread_web_guide/thread-network.png){class="glboxshadow"}

- **EUI-64**：Unique device identifier, hexadecimal number of 8 bytes in length.
- **Ext Mac**：The device extension address, a unique identifier in the Thread network, is a hexadecimal number of 8 bytes in length. The extended address is randomly generated and will be re-randomized when the system is restored to factory settings.
- **Thread Version**：Current thread protocol version.
- **Tx Power**：Transmit power, 0~20dBm, default is 20dBm.
- **Network Name**：Thread network name, 1 to 16 characters long, used to generate PSKc (Pre-Shared Key for the Commissioner), default format <GL-model> - <3 characters after MAC address>.
- **PAN ID**：IEEE 802.15.4 MAC layer unique identifier, default value is 2 bytes after the MAC address in hexadecimal format.
- **Extended PAN ID**：Thread network extension PAN ID for PSKc generation.
- **Network Key**：Thread network key, a hexadecimal number of 16 bytes in length.
- **Channel**：Thread network channel, 11~26, default value is 26.
- **Commissioner Credential**：User-defined string, UTF-8 encoded characters from 6 to 255 in length, used to generate PSKc, default value is **goodlife**.

Network Name/ PAN ID/ Extended PAN ID/ Network Key is generated based on the MAC address of the device.

### Create a new network

You can create a new network directly by using the default configuration and clicking **Enable**. You can then see that the status of the S200 has changed from **Detached** to **Leader**, which means that a new network has been created.

**Note**: If you have the same network settings as an existing Thread network in your current environment, then the S200 will automatically join that network.

![create-new-network](https://static.gl-inet.com/docs-iot/en/thread_web_guide/create-new-network.png){class="glboxshadow"}

If you want to set some parameters manually, you can configure them by clicking on the **Manual Setup**.

![Manual-Setup](https://static.gl-inet.com/docs-iot/en/thread_web_guide/manual-setup.png){class="glboxshadow"}

### Join an existing network

We support the following 4 ways to add the S200 to an existing network.

#### Join the network by using Network Key

Click on the **Join Network** and the GL-S200 will scan the surrounding available Thread networks.

![using-Network-Key](https://static.gl-inet.com/docs-iot/en/thread_web_guide/using-network-key.png){class="glboxshadow"}

Select the Thread network you want to join in the pop-up window, enter its Network Key and apply it.

![using-Network-Key2](https://static.gl-inet.com/docs-iot/en/thread_web_guide/using-network-key2.png){class="glboxshadow"}

#### Join the network by using the Commissioner

1. Using another GL.iNET S200 as the Commissioner (please refer to the **Thread Commissioning** page guide), enter the Joiner EUI64 and Joiner Credential of the S200 to be connected to the network.

2. Click on the  "**Join Network**" on the S200 to be connected to the network, select "**Join With Commissioner**" in the pop-up window, enter the Joiner Credential and apply it.

3. A successful Join Network will automatically jump to display the status page.

    ![using the commissioner](https://static.gl-inet.com/docs-iot/en/thread_web_guide/using-the-commissioner.png){class="glboxshadow"}

#### Networking using import Thread network configuration

To facilitate deployment, we can import the same Thread network configuration directly to the device so that devices with the same Thread network configuration are automatically networked after they are up.
You can import and export by clicking on Import Setting/Export Setting in the top right hand corner of the Thread Network page.


![export](https://static.gl-inet.com/docs-iot/en/thread_web_guide/export.png){class="glboxshadow gl-80-desktop"}

![import](https://static.gl-inet.com/docs-iot/en/thread_web_guide/import.png){class="glboxshadow gl-80-desktop"}

**Note**: You can only export when the Thread Network is up, or import when the Thread Network is down.

#### Join the network by using External Commissioner

In the Thread network, the GL.iNET S200 acts as a border agent to support external commissioners, which can be a mobile phone or a PC.

![using-External-Commissioner](https://static.gl-inet.com/docs-iot/en/thread_web_guide/using-external-commissioner.png){class="glboxshadow"}

1. Download Commissioner App

    - [OT Commissioner Android App](https://github.com/openthread/ot-commissioner/tree/main/android)

    - [Thread Group Android App](https://play.google.com/store/apps/details?id=org.threadgroup.commissioner&hl=en)

2. Open the app after connecting the GL-S200 via WiFi.

3. Select one of the AVALABLE BORDER ROUTERS and click on it and enter the Commissioner Credential.

    ![Commissioner-App](https://static.gl-inet.com/docs-iot/en/thread_web_guide/commissioner-app.png){class="glboxshadow"}

4. If step 3 is entered correctly, you can scan the QR code on the GL-S200 Join With Commissioner page and click Apply on the GL-S200 page to start the process.

    ![using the commissioner](https://static.gl-inet.com/docs-iot/en/thread_web_guide/using-the-commissioner.png){class="glboxshadow"}

### Export thread network settings

You can copy the thread network dataset TLV data or download it in the file.

![export_thread_network_settings](https://static.gl-inet.com/docs-iot/en/thread_web_guide/export_thread_network_settings.png){class="glboxshadow"}

## Thread Commissioning

You can add new devices to the network on this page, and GL-S200 supports bulk imports.

![thread commissioning](https://static.gl-inet.com/docs-iot/en/thread_web_guide/commissioning.png){class="glboxshadow"}

- The **Joiners** card shows the list of Joiners to be added to the network

- The **Commission Records** card shows Joiner's network entry history.

    - For Joined/Timeout devices, click **Action -> Rejoin** to re-enter the network without re-entering；

        ![rejion](https://static.gl-inet.com/docs-iot/en/thread_web_guide/rejoin.png){class="glboxshadow"}

    - For all devices with Joined/Join Fail status, you can also click on **Rejoin All** to re-enter the network in bulk

        ![rejoin all](https://static.gl-inet.com/docs-iot/en/thread_web_guide/rejoin-all.png){class="glboxshadow"}

### Add a single device

![add a single device](https://static.gl-inet.com/docs-iot/en/thread_web_guide/add-a-single-device.png){class="glboxshadow"}

- **Joiner EUI-64**: Joiner's EUI-64 or type ***** to match all Joiners.
- **Joiner Credential**: The device credentials to be added must be a string containing all uppercase letters and numbers and must not contain the letters I, O, Q and Z, between 6 and 32 characters in length.
- **Joiner Timeout**: Joiner access timeout, during which a Joiner can access the network using valid credentials.

### Add devices in batches

If the device vendor has set different Joiner credentials for each Thread device, you will need this feature when deploying. Clicking **Download template** to download the template or export the saved Joiner list, fill in or add the Joiner EUI64 and Joiner Credential, then click **Select** to import.

![add devices in batches](https://static.gl-inet.com/docs-iot/en/thread_web_guide/add-devices-in-batches.png){class="glboxshadow"}

## Thread Topologies

The network topology data is obtained by sending multicast packets. The network topology data allows you to view information about each node such as IPv6 address, mode of operation, directly connected sub-nodes, etc.

![topologies](https://static.gl-inet.com/docs-iot/en/thread_web_guide/topologies.png){class="glboxshadow"}

![topologies overview](https://static.gl-inet.com/docs-iot/en/thread_web_guide/topologies-overview.png){class="glboxshadow"}

You can click on any device to view information about that device.

![device information](https://static.gl-inet.com/docs-iot/en/thread_web_guide/device-information.png){class="glboxshadow"}

## Advanced

We have provided some advanced configurations related to Thread networking. Normally we do not recommend that users modify these parameters.

### SRP Server

SRP (Service Registration Protocol) is a service registration and discovery protocol. The IP of devices on an IP-based network is not usually fixed, so communication is not possible without determining the IP of the other end, and this SRP protocol allows automatic discovery of devices and services on the Thread network.

![SPR server](https://static.gl-inet.com/docs-iot/en/thread_web_guide/srp-server.png){class="glboxshadow"}

- Host: SRP Server domain.
- Lease: The lifetime of the DNS-SD PTR, SRV, A, AAAA and TXT records.
- Key Lease: The lifetime of the KEY records.

![registered servers](https://static.gl-inet.com/docs-iot/en/thread_web_guide/srp-services.png){class="glboxshadow"}

### Backbone Routers

The Backbone Router (BBR) function is primarily used to receive multicast inbound/outbound requests. Refer to [Thread Border Router - Thread 1.2 Multicast](https://openthread.google.cn/codelabs/openthread-border-router-ipv6-multicast#0) for experimentation.

![backbone routers](https://static.gl-inet.com/docs-iot/en/thread_web_guide/bbr_settings.png){class="glboxshadow"}

- Backbone Interface: Select the interface that bbr use.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
