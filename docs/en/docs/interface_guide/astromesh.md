# AstroMesh

> This feature is introduced in firmware v4.10.

AstroMesh is GL.iNet's proprietary global mesh technology based on EasyMesh. Unlike conventional wireless mesh systems that only work within a single local network, AstroMesh eliminates geographical restrictions to connect you to your home network anywhere.

At home, your travel router acts as a regular Mesh Node to extend household Wi-Fi coverage with seamless device roaming. When you head out, it can be automatically switched to Astro Node mode and sync all your home Wi-Fi settings via cloud, letting you access your home LAN devices remotely while routing traffic through your home network exit. Plug-and-play with zero complicated configuration, AstroMesh delivers a seamless internet experience whether you are relaxing at home or traveling on the road.

## Quick Setup

In the following example, we'll use Flint 3 (GL-BE9300) and Slate 7 (GL-BE3600) to build an AstroMesh network.

- **Flint 3**: serves as the Main Router that connects to the Internet and manages all Mesh Nodes. It also acts as the network exit for all remote Astro Nodes.

- **Slate 7**: functions as the Mesh Node that extends the Main Router's Wi-Fi coverage locally, or extends the home network to remote sites.

Follow the steps below to complete setup.

###  Set up Main Router

1. Log in to Flint 3's web Admin Panel and go to **INTERNET**. Connect it to the Internet via any supported connection type: Ethernet, Repeater, Tethering, and Cellular.

2. Go to **ASTROMESH** and click **Main Router**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

### Set up Mesh Node

Log in to Slate 7's web Admin Panel. Go to **ASTROMESH** and click **Mesh/Astro Node**.

![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

### Pairing

Add Mesh Nodes into your AstroMesh network via **Wi-Fi Scan** or **Pairing Code**.

![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

Refer to the corresponding instructions below.

??? note "Wi-Fi Scan"
    
    Before scanning, make sure that:

    1. The Mesh Node is powered on and near the Main router.
    2. The Mesh Node has AstroMesh enabled and is working on **Mesh Node** mode.
     ---

    Log in to Flint 3's web Admin Panel and go to **ASTROMESH**. Click **Add nodes via Wi-Fi Scan**.

    ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

    In the pop-up window, click **Scan**.

    ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

    It will start scanning for nearby Mesh Nodes using Wi-Fi.

    ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

    Select one node and click **Add**.

    ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

    The Mesh Node will then be added to your AstroMesh network. Click **Finish**.

    ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

    **Note**: Once a node joins the AstroMesh network, it will no longer be accessible via its original IP address. All nodes can be managed via the Main Router's Admin Panel. See [Manage Mesh Nodes](#manage-mesh-nodes) for details.

??? note "Pairing Code"

    Log in to Flint 3's web Admin Panel and go to **ASTROMESH**. Click **Add nodes via Pairing Code**.

    ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

    The Main Router will generate a pairing code. Copy this code. 

    ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

    Log in to Slate 7's web Admin Panel and go to **ASTROMESH**. Enter the copied pairing code and click **Apply**.

    ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

    ***Note**: The pairing code is time-limited. Please enter it before it expires.*

    The Mesh Node will starting connecting to the Main Router. Click **Done**.

    ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

    **Note**: Once a node joins the AstroMesh network, it will no longer be accessible via its original IP address. All nodes can be managed via the Main Router's Admin Panel. See [Manage Mesh Nodes](#manage-mesh-nodes) for details.

Once nodes have been successfully added to AstroMesh, a topology will appear on the Main Router's Admin Panel, as shown below.

![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Manage Mesh Nodes

Manage your Mesh Nodes on the Main Router's Admin Panel.

### View Node Information

On the Main Router's Admin Panel, go to **ASTROMESH** and click the **Main Router** on the AstroMesh topology.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

You can view the Main Router details, including model, IP & MAC address, up time, and connected clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Click the **Mesh Node** on the AstroMesh topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

You can view the Mesh Node details, including model, IP & MAC address, firmware version, up time, and connected clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Edit Mesh Node

On the Main Router's Admin Panel, go to **ASTROMESH** and click the **Mesh Node** on the AstroMesh topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Each Mesh Node is named "Node" followed by the last four digits of its MAC address by default. Click the edit icon to rename your Mesh Node.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Access Mesh Node

On the Main Router's Admin Panel, go to **ASTROMESH** and click the **Mesh Node** on the AstroMesh topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Click the gear icon in the upper-right corner and select **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

You will be redirected to the Mesh Node login page at the IP address assigned by the Main Router. Enter your admin password to log in.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

After logging in, go to **ASTROMESH** to view connection status.

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### Add More Nodes

To add more nodes, click **Add** in the upper-right corner of the AstroMesh topology.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Manage Astro Nodes

When you move a Mesh Node away from your home network, it will automatically switch to **Astro Node** mode. 

For example, bring the Slate 7 to another location. Power it on and select **Mesh Node** Mode on the touchscreen.

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

It will detect the current network environment, switch to **Astro Node** mode automatically, and initiate the connection.

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

Once connected, it will show its original IP address, which can be used to access its web Admin Panel.

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

Use this IP address to log in to your Astro Node.

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

After logging in, go to **ASTROMESH** to view connection status. The default connection mode is **Exit Node Mode**. You may switch to **Traffic Split Mode** as needed.

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode**: In this mode, all traffic from the Astro Node will be routed through your home network to access the internet. The Astro Node's public IP will match your home network's public IP address.

- **Traffic Split Mode**: In this mode, only traffic heading to your home network is forwarded back to the Main Router, while other internet traffic passes directly through the Astro Node's local WAN. Ensure the Astro Node is connected to a local internet network.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
