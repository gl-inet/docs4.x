# Data Statistics

Data Statistics offers an intelligent traffic insight dashboard that categorizes and visualizes network usage by applications, helping you monitor real-time and historical traffic for better network awareness and control.

**Note**:

1. This feature is now available only on **GL-MT5000 (Brume 3)**.

2. This feature cannot work with Network Acceleration. Enabling it will automatically disable Network Acceleration to ensure proper operation.

---

## Quick Setup

On the left side of the web Admin Panel, go to **FLOW CONTROL** > **Data Statistics**.

Toggle the switch in the upper right corner to view the **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage**: It presents a time-based trend chart (e.g., for the past day) to show the bandwidth consumption of the top 10 applications over the selected period. 

    Switch the timeline among Past Hour, Past Day, and Past Week if required. 

- **App Traffic Statistics**: It displays detailed traffic metrics for each application, including Download, Upload, and Total Bandwidth data. 

    Search for specific apps in the search bar if required.

## Data Storage Rules

1. Traffic statistics are saved to RAM every 15 seconds and stored in flash every 1 hour. Frequent flash writes are avoided to protect flash memory lifespan.

2. A soft reboot will not cause data loss. The system first writes data from RAM to flash before restarting.

3. A hard reboot (unplugging and replugging the power) or a firmware upgrade (retaining settings) may result in data loss of up to the most recent hour.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.