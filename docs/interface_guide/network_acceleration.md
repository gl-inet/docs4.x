# Network Acceleration

[Hardware Acceleration](hardware_acceleration.md) features have been renamed to Network Acceleration since v4.3.

Network acceleration reduces CPU load and speeds up traffic packet forwarding, but can conflict with some features.

When Network acceleration is enabled, the following functions will not work properly: Client Speed and Traffic Statistics, Client Speed Limit.

## Supported models

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-BE6500 (Flint 3e)           | √         |
| GL-BE9300 (Flint 3)            | √         |
| GL-BE3600 (Slate 7)            | √         |
| GL-X2000 (Spitz Plus)          | √         |
| GL-B3000 (Marble)              | √         |
| GL-MT6000 (Flint2)             | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-MT2500/GL-MT2500A (Brume 2) | √         |
| GL-SFT1200 (Opal)              | √         |
| GL-MT1300 (Beryl)              | √         |
| GL-AXT1800 (Slate AX)          | -         |
| GL-AX1800 (Flint)              | -         |
| GL-A1300 (Slate Plus)          | -         |
| GL-E750/E750V2 (Mudi)          | -         |
| GL-AR750S (Slate)              | -         |
| GL-XE300 (Puli)                | -         |
| GL-X750 (Spitz)                | -         |
| GL-MT300N-V2 (Mango)           | -         |
| GL-AR300M Series (Shadow)      | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-X300B (Collie)              | -         |

## Setup

On the left side of web Admin Panel -> NETWORK -> Network Acceleration.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Mode has three options.

- Auto
    
    Auto mode will automatically switch between the two acceleration modes based on actual usage.

- Hardware Acceleration

    Hardware acceleration works on Ethernet and Repeater.

- Software Acceleration

    Software acceleration works on Cellular.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
