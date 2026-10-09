# Firmware v4.11

This release focuses on improving network quality monitoring and security assessment, helping you identify connectivity issues and potential security risks. It also enhances DNS, QoS, SQM, and Data statistics for more flexible network management and traffic control.

Get the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Network Quality

[Network Quality](../interface_guide/network_quality.md) is a new feature that monitors your Internet connection in real time. It evaluates responsiveness, latency, and DNS performance, while detecting connection drops and packet loss to help identify network instability and connectivity issues that bandwidth tests alone may not reveal.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Security Scan

[Security Scan](../interface_guide/security_scan.md) is a new feature that evaluates your router's security settings and provides a security score, risk alerts, and optimization suggestions. It checks items such as Wi-Fi security, WAN ping, remote SSH, port forwarding, and DPI content protection, helping you identify and address potential security risks. A scan starts automatically when you open the page. You can also click the score icon to reset and rerun the scan.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## DNS

This release improves [DNS](../interface_guide/dns_v4.11.md) configuration by bringing WAN DNS, VPN DNS, and Manual DNS together on a single page. You can easily view the DNS status for each connection type, configure custom DNS servers, and choose whether manual DNS settings apply to VPN tunnels or the router itself.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS

[QoS](../interface_guide/qos.md) (Quality of Service) provides a **Run Speedtest** option for WAN bandwidth, measuring download and upload speeds and auto-filling the relevant fields. In terms of scheduling policies, this release adds two options in addition to Application Priority: **Device Priority** and **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Selected local clients get higher network priority during WAN congestion. 

- **Application Priority**: Set custom priorities for different applications, and the router will allocate bandwidth accordingly.

- **Advanced QoS**: Create advanced QoS rules for high-priority traffic. 

## SQM

[SQM](../interface_guide/sqm.md) (Smart Queue Management) provides a **Run Speedtest** option for WAN bandwidth, measuring download and upload speeds and auto-filling the relevant fields. Two queue disciplines are available: **cake** and **fq_codel**.

![sqm fq_codel](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: Smart, automatic traffic shaping with the best overall latency control (recommended).

    For this queue discipline, the newly added **Cake Autorate** dynamically adjusts the configured bandwidth based on probe RTT. It uses lightweight pings rather than active speed tests and is recommended for WAN connections with fluctuating bandwidth.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: Simple and efficient fair-queueing with basic latency reduction.

## Data Statistics

[Data Statistics](../interface_guide/data_statistics.md) now supports traffic filtering by client and introduces new chart views, including bar charts and pie charts. When viewing App Traffic Statistics, you can select a specific client and switch between chart views for a clearer analysis of traffic usage.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
