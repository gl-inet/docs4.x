# GoodCloud Site to Site

## Introduction

GoodCloud Site to Site allows offices in multiple locations to establish secure connections with each other over the internet. It extends the company's network, making computer resources from one location available to employees at other locations across the network.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenario 1**: Dozens of branch offices under the same company need to be integrated into a unified private network, enabling seamless resource sharing across all locations.

**Scenario 2**: When two companies with close partnerships require business collaboration, Site to Site facilitates their work in a shared and secure network environment.

**Scenario 3**: For families with IP cameras, Site to Site enables remote access to the device when members are away from home, ensuring easy monitoring from anywhere.

## Conditions

1. At least two GL.iNet routers are required to build Site to Site network.

2. At least one router should have a public IP address in order to be set as the primary node. [Check if your ISP assigns you a public IP address](how_to_check_if_isp_assigns_you_a_public_ip_address.md). 

    A router with strong performance and the best network speed is preferred as the main node.

3. It is **NOT** recommended to run Site to Site while the Sub nodes are also running a VPN client / Tailscale / ZeroTier / AstroWarp, as this can make the network configuration particularly complex.

## Build a Site to Site network

1. Bind your routers to your GoodCloud account. [How](../interface_guide/cloud.md/#setup-your-goodcloud-account)?

2. Log in to [GoodCloud](https://www.goodcloud.xyz/#/login), navigate to **Site to Site** at the leftside bar. Click **Create Network** at the upper right.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Check the box at the left side to select at lest two devices.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}
    
    The selected devices will be displayed in the lower part of the page. 

    The default port of Site to Site is **51830**. If you want to use another port, click on **Advanced** at the lower left corner to modify it. Then click **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    A Site to Site network can have up to 10 devices to ensure stable performance.

4. Name your network, and click **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing will start testing to check if any device can be set as the Main Node.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    If none of your devices can be used as the Main Node, please make sure that:

    - At least one router has a public IP, either static or dynamic public IP.
    - Port is open. The default port for Site to Site is 51830. You can also change port and try again.
    - If the router you want to set as Main Node is behind NAT, you may need to set up port forwarding.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    If more than one device can be set as the Main Node, please choose one to continue. We suggest selecting the router with strong performance and the best network speed as the Main Node.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    If there is only one device can be set as the Main Node, it will go to the Site to Site detail page directly.

6. The network is disabled by default. Ensure that the LAN IP addresses of all nodes do not conflict with each other. Click the gear icon to change LAN IP if needed, and click on **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Wait a few minutes. Once the dashed line turns to solid, it means the Site to Site network has been established successfully.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Testing the Site to Site connection

1. Connect your PC or smartphone to one of the Node in this Site to Site network.

2. Launch a web browser to access another Node's LAN IP. If you can access the login page, the connection between these two nodes is working.

## Route and other options

By default, each node can access other node's LAN. For security reasons, we recommend only opening the IP addresses of specific services.

For example, there is a Server A (172.30.97.100) in Node 1's subnet. If you want other nodes to only access Service A of Node 1, you can set it up as follows:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

You can add node's parent routes too.

Each Sub Node builds an encrypted tunnel network to Main Node. If you want to change the IP of tunnel subnet, click **IP Address Range** to modify.

Applying change of IP address range will cause network disconnection for a few minutes.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
