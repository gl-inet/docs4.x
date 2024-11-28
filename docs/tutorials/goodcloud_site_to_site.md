# GoodCloud Site to Site

## Introduction

GoodCloud Site to Site allows offices in multiple locations to establish secure connections with each other over internet. It extends the company's network, making computers resources from one location available to employees at other locations.

<a href="https://static.gl-inet.com/www/images/solutions/s2s/s2s_main_5.png" target="_blank"><img alt="site to site diagram" src="https://static.gl-inet.com/www/images/solutions/s2s/s2s_main_5.png"></a>

Senerio 1: A company has dozens of branch offices that they wish to join in a single private network to share resources.

Senerio 2: A company has a close relationship with a partner company, the Site to Site allows the companies to work together in a secure, shared network environment.

Senerio 3: A family has IP camera and when they are not at home, the Site to Site allows to remote access the IP camera.

## Conditions

It requires at least two GL.iNet routers, each in a different location, one of which has a public IP address. Please [check if your ISP assigns you a public IP address](how_to_check_if_isp_assigns_you_a_public_ip_address.md). It requires firmware version 3.026 and above.

!!! note

    It is not recommended to run Site to Site while its nodes are also running VPN client, which can make the network particularly complex.

## Steps to build a Site to Site network

1. Bind your routers to GoodCloud. [how?](../interface_guide/cloud.md#add-device)

2. Follow the steps below to create a Site to Site network.

    ![create a site to site network](https://static.gl-inet.com/goodcloud/docs/create-s2s-01.png){class="glboxshadow"}

    Default port is 51830, if you want to use another port, find the `Advanced` option at the lower left corner.

    Due to the device's performance, each Site to Site network can have up to 10 devices.

    After you had chosen the devices, click Continue.

    ![create a site to site network](https://static.gl-inet.com/goodcloud/docs/create-s2s-02.png){class="glboxshadow"}

    Then, it will test each device if it can be set as the Main Node of Site to Site.

    We suggest that the router with strong performance and best network speed to be the Main Node.

    ![testing each device](https://static.gl-inet.com/goodcloud/docs/testing-s2s-01.png){class="glboxshadow"}

    If none of the devices can be used as the Main Node, make sure that:

    - One of routers has a public IP, either static public IP or dynamic public IP.
    - Port is open, default is 51830.
    - If the router is behind NAT, you may need to set up port forwading.

    You can also change port and try again.

    ![testing each device](https://static.gl-inet.com/goodcloud/docs/testing-s2s-02.png){class="glboxshadow"}

    If there are more than one device can be set as the Main Node, you need to choose one to continue.

    ![testing each device](https://static.gl-inet.com/goodcloud/docs/testing-s2s-03.png){class="glboxshadow"}

    If there is only one device can be set as the Main Node, it will go to the Site to Site detail page directly.

    The network is stopped by default, check the LAN IP, if it is OK then you need to click Start button, otherwise click Setting to change LAN IP.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

    Wait a few minutes, the node's connect status will display as lines. Solid line means connected, dashed line means disconnected.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Testing the Site to Site connection

Now the Site to Site network is created and started, let's test the connection.

Use your PC or Phone to connect to one of the Node of this Site to Site, and use browser to access another Node's LAN ip, if you see the login page, the connection between these two nodes is worked.

For example, my PC connect to Node 1 device, and then I use browser to access Main Node's LAN IP (192.168.48.1), if I see the login page, it means the connection between Node1 and Main Node is worked.

## Route and other options

You can change each device's LAN IP and routes.

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s.png){class="glboxshadow"}

By default, each node can access other's LAN, based on security, we recommend only open the corresponding service IPs.

E.g. There is a Server A(172.30.97.100) in Node 1's subnet, if you want other Site to Site nodes  only can access Node 1's Service A, you can set it like below:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

You can add node's parent routes too.

Each sub Node build an encrypted tunnel Network to Main Node, if you want to change the IP of tunnel subnet. Click 'IP Address Range'.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
