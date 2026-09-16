# Firmware v4.10

This release focuses on improving Cloud Services, network management, and network security. Key updates include enhancements to Mesh and GL.iNet Account, native VLAN support, improved GoodCloud account management, and conflict detection for cascaded VPN configurations.

Get the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Mesh

Mesh is a feature based on the Wi-Fi EasyMesh™ standard that extends whole-home Wi‑Fi coverage and enables seamless roaming. If you have multiple GL.iNet routers, set one as the main router and the rest as mesh nodes for seamless Wi-Fi roaming around your home.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/mesh.png){class="glboxshadow"}

## Cloud Services

Cloud Services is a suite of cloud-based features built into the router and managed centrally through your GL.iNet Account. It enables real-time status monitoring, remote device management, batch firmware deployment, and secure remote access. In firmware v4.10, this module provides enhanced unified cloud management.

The Cloud Services module includes GL.iNet Account, GoodCloud, and GoodPAS.

### GL.iNet Account

The GL.iNet Account provides a centralized profile page where you can connect or manage your devices and access cloud services. With a single GL.iNet Account, you can seamlessly access GoodCloud and the GL.iNet App for more convenient network management. 

![gl.inet account](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/account.png){class="glboxshadow"}

### GoodCloud

GoodCloud is a cloud platform for remotely deploying and managing GL.iNet routers. It centralizes devices across multiple locations and supports batch configuration and firmware upgrades. It also provides remote access to the web Admin Panel and the device terminal via SSH, making it easier to manage routers remotely.

In firmware v4.10, GoodCloud simplifies account binding and lets you clear cloud account data during a factory reset.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/goodcloud.png){class="glboxshadow"}

### GoodPAS

GoodPAS is an advanced remote access solution integrated into the GL.iNet router SDK. Built on the AmneziaWG protocol, it enables secure access to a home network through simple device pairing, without requiring account registration or user login.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/goodpas.png){class="glboxshadow"}

## VPN

Firmware v4.10 adds detection for IP address and DNS conflicts in cascaded VPN configurations.

### Cascaded VPN

A cascaded VPN configuration routes network traffic through two or more VPN tunnels in sequence. In such configurations, overlapping IP subnets or conflicting DNS settings between VPN layers may cause connection failures or DNS resolution issues. The new detection feature helps identify these configuration conflicts before they affect connectivity.

The figure below illustrates two common configuration conflicts in a cascaded VPN setup: overlapping subnets and conflicting DNS settings.

![cascaded vpn](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/vpn.png){class="glboxshadow"}

## Subnet

The Subnet consolidates the configuration of LAN, Guest Network, IoT Network, and custom VLAN Networks into a single unified view. It provides a centralized management interface for all subnet-related settings, allowing you to create and manage multiple subnets to isolate different types of devices or traffic.

The following figure shows the Subnet on the Flint 3 (GL-BE9300).

![subnet](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/subnet.png){class="glboxshadow"}

## Ethernet Port

The Ethernet page displays all Ethernet interfaces on the router. It allows you to check connection status, switch ports between WAN and LAN roles, and view details such as the MAC address, negotiated speed, and link status. Physical interfaces can also be assigned to subnets you have created.

The following figure shows the Ethernet Port on the Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/ehternet_port.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.