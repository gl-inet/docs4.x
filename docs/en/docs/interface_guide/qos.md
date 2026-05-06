# QoS (Quality of Service)

QoS (Quality of Service) optimizes bandwidth allocation by prioritizing critical activities (e.g., video calls, gaming) during network congestion, reducing latency and improving overall network performance. 

**Note**: 

1. This feature only affects traffic passing through the router when it operates as a gateway, including local client traffic and VPN client traffic. It does not apply to inbound traffic when the router acts as a VPN server.
2. QoS will not take effect when the router is in Drop-in Gateway mode.
3. QoS and SQM cannot be enabled simultaneously.
4. QoS cannot work with Network Acceleration. Enabling QoS will automatically disable Network Acceleration to ensure stable performance.

## Supported Models

!!! note "Supported Models"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Quick Setup

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **QoS**. 

Toggle the switch to enable QoS, and the page displays as follows.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

Set your maximum upload and download speeds (input range: 1 - 10000) for traffic scheduling. Match them to your actual internet bandwidth for the best results. 

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Note**: Values entered in the input field are in **Mbps** (megabits per second). The equivalent **MB/s** (megabytes per second) is displayed for your reference.

Then set priorities for different applications. The router will allocate bandwidth accordingly.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## Customize App Priority

To customize application priority, select **Customize** and click **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

In the pop-up window, all categories are set to Medium Priority by default.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Drag the categories to adjust their priority as needed, then click **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.