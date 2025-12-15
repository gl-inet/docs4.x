# Network Acceleration

[Hardware Acceleration](hardware_acceleration.md) features have been renamed to Network Acceleration since v4.3.

Network acceleration reduces CPU load and speeds up traffic packet forwarding, but can conflict with some features.

When Network acceleration is enabled, the following functions will not work properly: Client Speed and Traffic Statistics, Client Speed Limit.

## Supported Models

??? "Supported Models"
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Unsupported Models"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Setup

On the left side of web Admin Panel -> NETWORK -> Network Acceleration.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

There are three modes.

- **Auto**
    
    Auto mode will automatically switch between the two acceleration modes based on actual usage.

- **Hardware Acceleration**

    Hardware acceleration works on <u>Ethernet</u> and <u>Repeater</u>. 
    
    Hardware acceleration offloads high-frequency network tasks (e.g., NAT, packet forwarding, checksum verification) to dedicated hardware like NPUs or HWNAT chips. It specifically works on Ethernet (wired WAN/LAN) and Repeater connections, excelling in these scenarios with fixed paths and simple rules to deliver high throughput, low latency, and minimal CPU load for wire-speed data transmission.

- **Software Acceleration**

    Software acceleration works on <u>Cellular</u>. 
    
    Software acceleration relies on a router's general CPU paired with optimized kernels or drivers (e.g., SWNAT). It works on Cellular (4G/5G) access, typically the primary scenario where hardware acceleration is unavailable, offering strong compatibility and support for complex protocols. While flexible, it may hit CPU bottlenecks under high-bandwidth loads, especially when running advanced features like DPI, QoS, or port forwarding.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
