# Firmware Features v4.9

## Flow Control

Flow Control is a core network management module that enables precise identification, monitoring, regulation and filtering of network traffic, effectively optimizing network resource allocation, eliminating bandwidth congestion, and standardizing network access behaviors to deliver a smoother, safer and more controllable network experience. In firmware v4.9, this module integrates with multiple practical functions for comprehensive traffic management.

The Flow Control module includes the following features:

!!! note "DPI Engine"
    
    Deep Packet Inspection technology for accurate identification of application protocols, traffic types and network behaviors.

!!! note "Data Statistics"
    
    Real-time and historical network traffic data collection, analysis and visualization for intuitive network status monitoring.

!!! note "Content Filtering"
    
    Intelligent interception and filtering of inappropriate network content to standardize network access.

!!! note "QoS (Quality of Service)"
    
    Bandwidth allocation and traffic priority scheduling to guarantee network quality for key applications.

!!! note "SQM (Smart Queue Management)"
    
    Optimizes network queue scheduling to reduce latency and packet loss for smoother network transmission.

!!! note "Parental Control"
    
    Previously categorized under the **Applications** menu, this feature is migrated to the **Flow Control** menu in v4.9. It leverages the upgraded DPI engine to accurately identify and block inappropriate applications and network content, achieving more professional and precise traffic-based access restriction.

## VPN

Firmware v4.9 has comprehensively improved the underlying routing logic and interactive interface of the VPN module, fixing potential routing conflicts, simplifying configuration logic, and improving operational intuitiveness. 
    
The detailed adjustments are as follows:

!!! note "Independent VPN Grouping"

    Each VPN tunnel operates as an independent group without cross-group failover. When network traffic matches to a specific VPN group, it will not automatically switch to other VPN groups even if the current tunnel fails, ensuring stable and predictable traffic routing.

!!! note "In-group Profile Failover"
    
    A single VPN tunnel group can accommodate multiple configuration profiles. Users can customize the priority of each profile within the same group, enabling automatic internal failover to maintain continuous VPN connectivity when a single profile fails.
    
!!! note "Removed "Not Use VPN" Policy"
    
    The traditional "Not Use VPN" option for VPN policy setup is removed in v4.9, eliminating redundant configuration entries and effectively avoiding complex routing logic conflicts caused by multiple policy settings.
    
!!! note "Redesigned VPN Dashboard"
        
    The VPN Dashboard has been fully redesigned with a more intuitive layout, displaying tunnel status, connection information and configuration entries more clearly, greatly improving daily operation and management efficiency.

## AmneziaWG 2.0 Protocol

Firmware v4.9 officially introduces the AmneziaWG 2.0 protocol, equipped with multiple new traffic obfuscation parameters. The upgraded protocol effectively evades detection by DPI and other traffic identification systems, significantly improving connection concealment and anti-interference capabilities. This enables stable and reliable VPN connection establishment in network-restricted regions and complex network environments.

## IoT Network

The newly built IoT network feature supports creating an independent dedicated Wi-Fi network for IoT smart devices. Physically and logically isolated from the primary network, it avoids network resource occupation and security risks brought by IoT device access to the main network. This optimization delivers broader device compatibility for various smart IoT clients and overall enhances the home network security system.

## ACL (Access Control List)

ACL, short for Access Control List, is a core network security management feature that allows users to create customized access rules to manage internal and external network traffic based on connection protocols, device IP addresses, and port. It supports precise permission control to allow or block specific network access behaviors. When multiple ACL rules generate conflicts, the system automatically executes the rule with higher priority to ensure accurate policy implementation.

Distinguished from Port Forwarding in core positioning: ACL focuses on network security management by controlling device and traffic access permissions; while Port Forwarding is used for network resource redirection, forwarding external network traffic to specified local terminal devices to implement remote access to local network services.

## Other Enhancements

!!! note "Wireless UI Redesign"
    
    The Wireless setting interface is fully redesigned with a streamlined layout and unified visual style, reducing operational complexity and greatly improving overall interface simplicity and user-friendliness.

!!! note "Upgraded Encrypted DNS"
    
    The encrypted DNS is expanded to cover more encryption protocols including DoH, DoT and DoQ. Meanwhile, more official DNS service providers are integrated, and the manual configuration for custom encrypted DNS servers is added to meet diverse secure domain resolution demands.
    
!!! note "Tailscale Exit Node Support"
    
    GL.iNet routers now support running as a Tailscale exit node. All outbound internet traffic from devices in the Tailnet can be routed through the router's public IP address, realizing unified and secure network exit management for the entire Tailscale network.
    
!!! note "AstroWarp Integration"
    
    AstroWarp is officially integrated into the GL.iNet router SDK in v4.9. Built on the AmneziaWG protocol with native traffic obfuscation capability, it provides stable, encrypted and secure remote access. Users can complete device pairing and connection setup quickly via a dynamic access code on the web Admin Panel. It supports one-click secure connection between travel routers and home networks within seconds, with no account registration or login required.