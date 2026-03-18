# How to change the NAT type on Gaming

Most of the game makers will ask you to turn on the UPnP on the router to get a better NAT type, however studies show UPnP is a non-secure protocol.

You can achieve the same purpose in a more secure may, either by the function of DMZ or port forward.

## Check you Game IP

Go to the client list and check the IP assigned to your game. You need to use this IP address on the following setup

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Method 1 DMZ

Go to side-bar **Network > Port Forwarding** and enable the DMZ with your game IP.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Method 2 Port forward

Go to side-bar **Network > Port Forwarding** and add necessary ports with your game IP.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Example: Ports for PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480


![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox port

UDP 88, 3074

TCP 3074

Some games may need other ports to be forwarded, you can refer to this website for more detail.

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT

You can enable the Full Cone NAT at **Network > NAT Settings** to imporve the latency.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* This function is available on Firmware 4.5 or above.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.