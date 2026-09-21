# Mesh

**Note**: This feature was introduced in firmware v4.10.

Mango 2 (GL-MG1300) and Mudi 7 (GL-E5800) do not support Mesh even with firmware v4.10 or later. Please refer to [Supported Models](#supported-models) for details.

---

On the left side of the web Admin Panel, go to **MESH**.

Mesh is a feature based on the Wi-Fi EasyMesh™ standard that extends whole-home Wi‑Fi coverage and enables seamless roaming. If you have multiple GL.iNet routers, set one as the main router and the rest as mesh nodes for seamless Wi-Fi roaming around your home.

## Supported Models

??? "Supported Models"
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Unsupported Models"
    - GL-MG1300 (Mango 2)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
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
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Quick Setup

The following example uses Flint 3 (GL‑BE9300) and Slate 7 (GL‑BE3600) to build a Mesh network.

**Flint 3** is the main router that connects to the Internet and manages all Mesh nodes.

**Slate 7** is the Mesh node that extends the main router's Wi-Fi coverage.

1. Power on your Mesh node and place it near the main router. 

    During first-time setup, keep the Mesh node next to the main router for quick scanning. After setup completes, you may relocate it midway between the main router and the Wi-Fi dead zone to extend Wi-Fi coverage.

2. Log in to the Mesh node's web Admin Panel and go to **MESH**. Click **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    It becomes discoverable, and has no network connection before being added to the Mesh network.

3. Log in to the main router's web Admin Panel and go to **INTERNET**. Connect it to the Internet via any supported connection type: Ethernet, Repeater, Tethering, or Cellular.

4. After Internet setup, go to **MESH** and click **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. The page indicates two ways to add Mesh nodes: Wi-Fi Scan and Ethernet Backhaul. 

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Select the corresponding tutorial below to add your Mesh nodes.

    ??? note "Wi-Fi Scan"

        Click **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}
                    
        It will start scanning for nearby Mesh nodes through Wi-Fi. Select the devices you want to add and click **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        The Mesh node will then be added to your Mesh network. Click **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Connect the Mesh node's WAN port to the main router's LAN port via an Ethernet cable, then an Ethernet Backhaul network will be automatically configured.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Once the Mesh node is added, the topology appears in the main router's Admin Panel.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Manage Nodes

Once setup is complete, the Mesh node will no longer be accessible via its original IP address. You can manage the main router and all Mesh nodes through the main router's Admin Panel.

### View Node Details

In the main router's Admin Panel, go to **MESH** and click the **Main Router** on the topology.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

You can view the main router details, including model, IP & MAC address, up time, and connected clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Click the **Mesh Node** on the topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

You can view the Mesh node details, including model, IP & MAC address, firmware version, up time, and connected clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Edit Mesh Node

In the main router's Admin Panel, go to **MESH** and click the **Mesh Node** on the topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Each Mesh node is named "Node" followed by the last four digits of its MAC address by default. Click the edit icon to rename your Mesh node.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Access Mesh Node

In the main router's Admin Panel, go to **MESH** and click the **Mesh Node** on the topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Click the gear icon in the upper-right corner and select **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

You will be redirected to the Mesh node's login page at the IP address assigned by the main router. Now you can log in to the Mesh node.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Add More Nodes

Click **Add** in the upper-right corner of the topology to add more nodes if needed.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
