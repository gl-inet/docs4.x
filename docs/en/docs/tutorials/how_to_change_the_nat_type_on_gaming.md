# How to change the NAT type on Gaming {#how-to-change-the-nat-type-on-gaming}

Some game developers recommend enabling UPnP on your router to get a better NAT type. However, UPnP carries potential security risks.

You can configure DMZ or port forwarding on your router to achieve the same purpose. Before enabling either feature, make sure you understand how it works and the associated security risks.

## Check your Game IP {#check-your-game-ip}

First, log in to your router and go to the Client list to check the IP address assigned to your game. You need to use this IP address on the following setup.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Method 1. DMZ {#method-1-dmz}

Go to **Network** -> **Port Forwarding** and enable the DMZ with your game IP.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Method 2. Port Forwarding {#method-2-port-forward}

Go to **Network** -> **Port Forwarding** and add necessary ports with your game IP.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Here's an example of forwarding ports for PS5.

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox port

UDP 88, 3074

TCP 3074

Some games may need other ports to be forwarded. You may refer to [How To Forward Ports In Your Router For a Better Gaming Experience](https://portforward.com/games/){target="_blank"} for details.

## Full Cone NAT {#full-cone-nat}

You can enable the Full Cone NAT to improve the latency. This feature has been available since firmware v4.5.

Go to **Network** -> **NAT Settings** and enable **Full Cone NAT** if needed, then click **Apply**.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
