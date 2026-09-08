# Firmware v4.9

This release focuses on more precise network control, improved traffic management, enhanced network security, and a revamped user interface — all designed to deliver a better overall user experience. 

Get the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control

Flow Control is a core network management module that enables precise identification, monitoring, regulation and filtering of network traffic, effectively optimizing network resource allocation, eliminating bandwidth congestion, and standardizing network access behaviors to deliver a smoother, safer and more controllable network experience. In firmware v4.9, this module integrates with multiple practical functions for comprehensive traffic management.

The Flow Control module includes DPI Engine, Data Statistics, Content Filter, QoS, SQM, and Parental Control.

### DPI Engine

Unlike traditional routers that only identify source and destination addresses, DPI (Deep Packet Inspection) performs in-depth analysis of packet payloads and accurately identifies applications and websites using a feature-matching library, enabling fine-grained traffic classification and control.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics
    
Data Statistics provides an intuitive traffic dashboard that identifies network usage by application and protocol. It supports viewing 1‑hour, 1‑day, and 7‑day historical trends, displays usage rankings, monitors per‑device traffic, and allows one‑click blocking of unwanted apps.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter
    
Content Filter is an intelligent online safety feature powered by DPI classification. It automatically blocks harmful and malicious websites to keep your network clean and secure, and also supports custom rules to block specific apps, domains, or IP addresses.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS
    
QoS (Quality of Service) optimizes bandwidth allocation by prioritizing critical activities (e.g., video calls, gaming) during network congestion, reducing latency and improving overall network performance.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control
    
Previously categorized under the **Applications** menu, this feature is migrated to the **Flow Control** menu in firmware v4.9. It leverages the upgraded DPI engine to accurately identify and block inappropriate applications and network content, achieving more professional and precise traffic-based access restriction.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

Firmware v4.9 has comprehensively improved the underlying routing logic and interactive interface of the VPN module, fixing potential routing conflicts, simplifying configuration logic, and improving operational intuitiveness. 
    
The detailed adjustments are as follows.

### Isolated VPN Tunnel

Each VPN tunnel operates as an independent group without cross-group failover. Once the network traffic matches to a specific VPN group, it will not automatically switch to other VPN groups even if the current tunnel fails, ensuring stable and predictable traffic routing.

**Note**: The traditional "Not Use VPN" policy is removed in firmware v4.9, eliminating redundant configuration to avoid routing conflicts caused by multiple and complex tunnel rules.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### VPN Profile Failover
    
A single VPN tunnel group can accommodate multiple configuration profiles. Users can customize the priority of each profile within the same group, enabling automatic internal failover to maintain continuous VPN connectivity when a single profile fails.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}
    
### Redesigned Dashboard
        
The VPN Dashboard features a complete redesign for a more intuitive layout. Tunnel status, connection details, and configuration entries are presented for clearer visibility, significantly boosting day‑to‑day operational and management efficiency. In addition, Kill Switch is enabled by default for all VPN tunnels under the new architecture to keep your traffic protected at all times.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

Firmware v4.9 officially introduces the AmneziaWG 2.0 protocol, equipped with multiple new traffic obfuscation parameters. The upgraded protocol effectively evades detection by DPI and other traffic identification systems, significantly improving connection concealment and anti-interference capabilities. This enables stable and reliable VPN connection establishment in network-restricted regions and complex network environments.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## IoT Network

In firmware v4.9, you can create an independent dedicated Wi-Fi network for IoT smart devices. Physically and logically isolated from the primary network, it avoids network resource occupation and security risks brought by IoT device access to the main network. This optimization delivers broader device compatibility for various smart IoT clients and overall enhances the home network security system.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL, short for Access Control List, is a core network security management feature that allows users to create customized access rules to manage internal and external network traffic based on connection protocols, device IP addresses, and port. It supports precise permission control to allow or block specific network access behaviors. When multiple ACL rules generate conflicts, the system automatically executes the rule with higher priority to ensure accurate policy implementation.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

Distinguished from Port Forwarding in core positioning, ACL focuses on network security management by controlling device and traffic access permissions; while Port Forwarding is used for network resource redirection, forwarding external network traffic to specified local terminal devices to implement remote access to local network services.

## Wireless UI
    
The Wireless UI is fully redesigned with a streamlined layout and unified visual style, reducing operational complexity and greatly improving overall interface simplicity and user-friendliness.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## Encrypted DNS
    
The encrypted DNS is expanded to cover more encryption protocols including DoH, DoT and DoQ. Meanwhile, more official DNS service providers are integrated, and the manual configuration for custom encrypted DNS servers is added to meet diverse secure domain resolution demands.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}
    
## Tailscale Exit Node
    
GL.iNet routers now support running as a Tailscale exit node. All outbound internet traffic from devices in the Tailnet can be routed through the router's public IP address, realizing unified and secure network exit management for the entire Tailscale network. Please refer to [here](../interface_guide/tailscale.md#run-exit-node) for details.

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.