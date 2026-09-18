# SQM (Smart Queue Management)

**Note**: This feature was introduced in firmware v4.9. Some models, such as Mango 2 (GL-MG1300), do not support SQM due to insufficient memory, even when running firmware v4.9 or later.

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **SQM**. 

SQM (Smart Queue Management) intelligently manages your router's network traffic to minimize latency and "bufferbloat", ensuring smoother gaming and voice calls. 

**Note**:

1. This feature only affects traffic passing through the router when it operates as a gateway, including local client traffic and VPN client traffic. It does not apply to inbound traffic when the router acts as a VPN server.
2. Since SQM is resource-intensive, it works best for low-bandwidth or congested networks. Enabling it on high-speed connections may reduce peak throughput.
3. SQM will not take effect when the router is in Drop-in Gateway mode.
4. SQM and QoS cannot be enabled simultaneously.
5. SQM cannot work with Network Acceleration. Enabling SQM will automatically disable Network Acceleration to ensure stable performance.

## For firmware v4.11 and above

Toggle the switch to enable SQM, then complete the configuration following the steps below.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Enter your WAN upload and download speeds (input range: 1 - 10000) manually, or click **Run Speedtest** to measure them and automatically populate the fields. An active internet connection is required to run the speed test.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Note**: Values entered in the input field are in **Mbps** (megabits per second). The equivalent **MB/s** (megabytes per second) is displayed for your reference.

2. **Queue Discipline**

    Select a queueing rule to manage traffic and reduce latency under load.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: Smart, automatic traffic shaping with superior overall latency control (recommended). 
    
        When **cake** is selected as the queue discipline, **Cake Autorate** is available as an optional feature.

        Cake Autorate is a latency-driven shaper that reduces or raises CAKE bandwidth in real time based on probe RTT. No active speed tests are performed; only lightweight pings are used. Recommended whenever the WAN bandwidth fluctuates; not needed on stable links.
            
        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Note**: Cake Autorate generates continuous background probe traffic. Consider this additional data usage when using a metered connection.

        The default settings are suitable for most connections. Only change the following parameters if you understand how they affect Cake Autorate. If needed, click **Reset to Default** to restore the default probe and threshold settings.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: A list of IP addresses separated by commas, used for network quality probing.

        - **Probe Interval**: Shorter intervals enable faster response but consume more CPU resources.

        - **Concurrent Probes**: The number of concurrent probes must not exceed the number of probe servers; higher values increase CPU load.

        - **Idle Detection Threshold**: When the transfer rate falls below this value, the connection will be considered idle. This value must not exceed 25% of the configured speed limit.

        - **Download Latency Threshold**: When download latency exceeds this threshold, bandwidth reduction is triggered.

        - **Upload Latency Threshold**: When upload latency exceeds this threshold, bandwidth reduction is triggered.

    - **fq_codel**: Simple, efficient fair queueing with basic latency reduction.

## For firmware v4.9 to v4.10

Toggle the switch to enable SQM, and set your maximum upload and download speeds (input range: 1 - 10000) for traffic scheduling. Match them to your actual internet bandwidth for the best results.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Note**: Values entered in the input field are in **Mbps** (megabits per second). The equivalent **MB/s** (megabytes per second) is displayed for your reference.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

For Queue Rule, two options are available:

- **cake**: Smart, automatic traffic shaping with superior overall latency control (recommended).

- **fq_codel**: Simple, efficient fair queueing with basic latency reduction.

!!! Tip

    A difference between QoS and SQM settings is that the QoS allows you to set the application priorities, with the router allocating bandwidth accordingly; while the SQM allows you to select a queue rule.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
