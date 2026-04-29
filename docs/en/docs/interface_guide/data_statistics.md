# Data Statistics

Data Statistics provides an intuitive traffic dashboard that identifies network usage by application and protocol. It supports viewing 1‑hour, 1‑day, and 7‑day historical trends, displays usage rankings, monitors per‑device traffic, and allows one‑click blocking of unwanted apps.

**Note**:

1. Data Statistics will not take effect when the router is in Drop-in Gateway mode.
2. Data Statistics cannot work with Network Acceleration. Enabling Data Statistics will automatically disable Network Acceleration to ensure stable performance.

## Supported Models

!!! note "Supported Models"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Quick Setup

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **Data Statistics**.

Toggle the switch in the upper right corner to view the **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

This page consists of two parts:

- **Top 10 Apps by Bandwidth Usage**: It presents a time-based trend chart (e.g., for the past day) to show the bandwidth consumption of the top 10 applications over the selected period.

    Hover your mouse over the chart to view data usage of the top 10 bandwidth-consuming apps at a specific time.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: It displays detailed traffic metrics for each application, including Download, Upload, and Total Bandwidth. Search for specific apps in the search bar if required. 
    
    Click the sort arrow next to the column header to sort the list in ascending or descending order.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## Data Storage Rules

1. Traffic statistics are saved to RAM every 15 seconds and stored in flash every 1 hour. Frequent flash writes are avoided to protect flash memory lifespan.

2. A soft reboot will not cause data loss. The system first writes data from RAM to flash before restarting.

3. A hard reboot (unplugging and replugging the power) or a firmware upgrade (retaining settings) may result in data loss of up to the most recent hour.

## Switch Time Range

You can switch the time range between Past hour, Past day, and Past week as needed.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

The time range you choose determines how the data is displayed:

- **For a closer look (e.g., Past Hour)**: The chart shows fine-grained, real-time fluctuations. Peaks are taller and drops are steeper, making it easy to spot sudden spikes in bandwidth usage.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **For a broad overview (e.g., Past Day or Past Week)**: The chart condenses the data into a longer timeline. The curves become smoother, showing the general traffic trend rather than every small change.

    ![past day](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_day.png){class="glboxshadow"}

## Clear Statistics

Click the broom icon in the upper left corner to clear statistics as needed.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

After clearing, the page will update as shown below. You may need to wait a moment for new statistics to start loading.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.