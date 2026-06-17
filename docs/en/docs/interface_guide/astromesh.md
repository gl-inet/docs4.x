# AstroMesh

> This feature is introduced in firmware v4.10.

AstroMesh is GL.iNet's proprietary global mesh technology, combining EasyMesh and AstroWarp. Unlike conventional wireless mesh systems that only work within a single local network, AstroMesh eliminates geographical restrictions to connect you to your home network anywhere.

At home, your travel router acts as a regular Mesh Node to extend household Wi-Fi coverage with seamless device roaming. When you head out, it can be automatically switched to Astro Node mode and sync all your home Wi-Fi settings via cloud, letting you access your home LAN devices remotely while routing traffic through your home network exit. Plug-and-play with zero complicated configuration, AstroMesh delivers a seamless internet experience whether you are relaxing at home or traveling on the road.

## Quick Setup

In the following example, we'll use Flint 3 (GL-BE9300) and Slate 7 (GL-BE3600) to build an AstroMesh network.

- **Flint 3**: serves as the Main Node that connects to the Internet and manages all Mesh Nodes. It also acts as the network exit for all remote Astro Nodes.

- **Slate 7**: functions as the Mesh Node that extends the Main Node's Wi-Fi coverage locally via EasyMesh, or extends the home network to remote sites via AstroWarp.

Follow the steps below to complete setup.

1. Log in to Flint 3's web Admin Panel and navigate to **INTERNET**. Connect it to the Internet via any supported connection type: Ethernet, Repeater, Tethering, and Cellular.

2. Navigate to **ASTROMESH** and click **Main Node**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Add nodes via **Wi-Fi Scan** or **Pairing Code**.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    ??? note "Wi-Fi Scan"
    
        Before scanning, make sure that:

        1. The router to be added is powered on and near the Main router.
        2. The router to be added has AstroMesh enabled and is working on **Mesh Node** mode.
        ---

        Click **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        In the pop-up window, click **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        It will start scanning for nearby Mesh Nodes using Wi-Fi.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Select one node and click **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        The Mesh Node will then be added to your AstroMesh network. Click **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Note**: Once connected, this Mesh Node will no longer be able to accessed via the original IP address. To access it again, use the new IP address it gets from the Main Node instead. Please go to the Main Node's Admin Panel to manage all nodes. Click [here](#manage-nodes) for details.

    ??? note "Pairing Code"

        Click **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        The Main Node will generate a pairing code. Copy this code.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Log in to Slate 7's web Admin Panel, go to **AstroMesh** and click **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Enter the copied pairing code and click **Apply**.

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        The Mesh Node will starting connecting to the Main Node. Click **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Note**: Once connected, this Mesh Node will no longer be able to accessed via the original IP address. To access it again, use the new IP address it gets from the Main Node instead. Please go to the Main Node's Admin Panel to manage all nodes. Click [here](#manage-nodes) for details.

4. Once the node is added to your AstroMesh network, the Main Node's Admin Panel will display the network topology, as shown below.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    The Mesh Node's Admin Panel will also show the connection status, as shown below.

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **Note**: Once added to the AstroMesh network, the Mesh Node will no longer be able to accessed via the original IP address. To access it again, use the new IP address it gets from the Main Node instead. Please go to the Main Node's Admin Panel to manage all nodes. Click [here](#manage-nodes) for details.

5. When you bring the Mesh Node away from your home, it will automatically switch to Astro Node mode.

## Manage Nodes

Manage your AstroMesh network on the Main Node's Admin Panel.

### View Node Information

Click the **Main Node** on your AstroMesh topology.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

You can view the Main Node details, including model, IP & MAC address, up time, and connected clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Click the **Mesh Node** on your AstroMesh topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

You can view the Mesh Node details, including model, IP & MAC address, firmware version, up time, and connected clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Edit Mesh Node

Click the **Mesh Node** on your AstroMesh topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Each Mesh Node is named "Node" followed by the last four digits of its MAC address by default. Click the edit icon to rename your Mesh Node.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Access Mesh Node

Click the **Mesh Node** on your AstroMesh topology.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Click the gear icon in the upper-right corner and select **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

You will be redirected to the Mesh Node login page. Enter your admin password to access its Admin Panel at the IP address assigned by the Main Node.

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
