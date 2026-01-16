# SQM (Smart Queue Management)

!!! Note

    1. This feature is now available only on **GL-MT5000 (Brume 3)**.
    
    2. This feature affects traffic passing through the router as a gateway (including local client traffic and VPN Client traffic) but not incoming traffic when the router acts as a VPN Server.

    3. Since SQM is resource-intensive, it works best for low-bandwidth or congested networks. Enabling it on high-speed connections may reduce peak throughput.

SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls. 

Log in to the router's web admin panel, navigate to **FLOW CONTROL** > **SQM**. 

Set your maximum upload and download speeds first (input range: 1 - 10000) for traffic scheduling. Match them to your actual internet bandwidth for the best results.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

For Queue Rule, two options are available:

- **cake**: Smart, automatic traffic shaping with superior overall latency control (recommended).

- **fq_codel**: Simple, efficient fair queueing with basic latency reduction.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.