# SQM (Smart Queue Management)

SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls. 

**Note**:

1. This feature affects traffic passing through the router as a gateway (including local client traffic and VPN Client traffic) but not incoming traffic when the router acts as a VPN Server.
2. Since SQM is resource-intensive, it works best for low-bandwidth or congested networks. Enabling it on high-speed connections may reduce peak throughput.
3. SQM will not take effect when the router is in Drop-in Gateway mode.
4. SQM and QoS cannot be enabled simultaneously.
5. SQM cannot work with Network Acceleration. Enabling SQM will automatically disable Network Acceleration to ensure stable performance.

## Supported Models

!!! note "Supported Models"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Quick Setup

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **SQM**. 

Toggle the switch to enable SQM, and set your maximum upload and download speeds (input range: 1 - 10000) for traffic scheduling. Match them to your actual internet bandwidth for the best results.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Note**: Values entered in the input field are in **Mbps** (megabits per second). The equivalent **MB/s** (megabytes per second) is displayed for your reference.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

For Queue Rule, two options are available:

- **cake**: Smart, automatic traffic shaping with superior overall latency control (recommended).

- **fq_codel**: Simple, efficient fair queueing with basic latency reduction.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.