# Network Acceleration

[Hardware Acceleration](hardware_acceleration.md) features have been renamed to Network Acceleration since v4.3.

Network acceleration reduces CPU load and speeds up traffic packet forwarding, but can conflict with some features.

When Network acceleration is enabled, the following functions will not work properly: Client Speed and Traffic Statistics, Client Speed Limit.

The following models have this option:

GL-XE3000(Puli AX), GL-X3000(Spitz AX), GL-MT2500(Brume 2), GL-MT3000(Beryl AX), GL-MT2500A(Brume 2), GL-SFT1200(Opal), GL-MT1300(Beryl)

## Setup

On the left side of web Admin Panel -> NETWORK -> Network Acceleration.

![Network Acceleration](https://static.gl-inet.com/docs/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Mode has three options.

- Auto
    
    Auto mode will automatically switch between the two acceleration modes based on actual usage.

- Hardware Acceleration

- Software Acceleration

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
