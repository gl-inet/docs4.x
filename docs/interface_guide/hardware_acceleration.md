# Hardware Acceleration

**Note**: Hardware Acceleration features have been renamed to [Network Acceleration](network_acceleration.md) since v4.3.

---

Hardware acceleration (sometimes called _hardware NAT, flow offloading, or offload_) reduces CPU load by moving packet forwarding out of the CPU and into the router SoC/NIC hardware. That usually increases maximum throughput and reduces CPU utilization, but it comes iwth important trade-offs, especially for features that rely on the Linux networking stack (netfilter / iptables / nftables) or on the kernel queuing disciplines (qdisc) used by SQM (Smart Queue Management)  

When hardware acceleration is enabled, the following functions will not work properly: Client Speed and Traffic Statistics, Client Speed Limit.

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

On the left side of web Admin Panel -> NETWORK -> Hardware Acceleration.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

---

## Quick summary — Hardware NAT vs Software NAT
* You care most about throughput (e.g., multi-gigabit broadband) and don’t need on-router SQM or per-client shaping → enable Hardware NAT / Network Acceleration. This will give the highest throughput and lowest CPU use.

* You care about low latency, consistent QoS, per-client limits, or you rely on SQM (cake/fq_codel) → use Software NAT (disable hardware offload). SQM and QoS require packets to traverse the kernel qdisc stack — offloaded packets bypass that path and therefore are not shaped.

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
