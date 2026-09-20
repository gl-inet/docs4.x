# QoS (Quality of Service)

**Note**: This feature was introduced in firmware v4.9. Some models, such as Mango 2 (GL-MG1300), do not support SQM due to insufficient memory, even when running firmware v4.9 or later.

---

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **QoS**. 

QoS (Quality of Service) optimizes bandwidth allocation by prioritizing critical activities (e.g., video calls, gaming) during network congestion, reducing latency and improving overall network performance. 

**Note**: 

1. This feature only affects traffic passing through the router when it operates as a gateway, including local client traffic and VPN client traffic. It does not apply to inbound traffic when the router acts as a VPN server.
2. QoS will not take effect when the router is in Drop-in Gateway mode.
3. QoS and SQM cannot be enabled simultaneously.
4. QoS cannot work with Network Acceleration. Enabling QoS will automatically disable Network Acceleration to ensure stable performance.

## For firmware v4.11 and above

Toggle the switch to enable QoS, then complete the configuration by following the steps below.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Enter your WAN upload and download speeds (input range: 1 - 10000) manually, or click **Run Speedtest** to measure them and automatically populate the fields. An active internet connection is required to run the speed test.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Note**: Values entered in the input field are in **Mbps** (megabits per second). The equivalent **MB/s** (megabytes per second) is displayed for your reference.

2. **Scheduling Policy**

    You can select one policy mode. Advanced rules override the basic policy for matched traffic.

    - **Device Priority**

        When the WAN connection is congested, selected local clients receive higher network priority. Click **Add Device** to add target devices, and these devices get bandwidth priority during heavy WAN load.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        You can search for devices by client name, MAC address or IP address. Select target devices and click **Apply** to confirm your selection.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        Toggle the switch to enable Application Priority and set priorities for different applications. The router will allocate bandwidth accordingly.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        To customize application priority, select **Customize** and click **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        In the pop-up window, all categories are set to Medium Priority by default.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Drag the categories to adjust their priority as needed, then click Confirm.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        Toggle the switch to enable Advanced QoS and create custom high-priority traffic rules. Click **Add Rule** to define rules based on protocol, port, and source IP to assign higher priority to matched traffic.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        You can enter parameters to create an Advanced QoS Rule. Specify the rule Name, Protocol, Source Address, and Destination Port. 

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

        Then, click **Apply** at the bottom to activate the configured rule.

## For firmware v4.9 to v4.10

Toggle the switch to enable QoS, and the page displays as follows.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Set your maximum upload and download speeds (input range: 1 - 10000) for traffic scheduling. Match them to your actual internet bandwidth for the best results. 

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Note**: Values entered in the input field are in **Mbps** (megabits per second). The equivalent **MB/s** (megabytes per second) is displayed for your reference.

Then set priorities for different applications. The router will allocate bandwidth accordingly.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

To customize application priority, select **Customize** and click **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

In the pop-up window, all categories are set to Medium Priority by default.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Drag the categories to adjust their priority as needed, then click **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.