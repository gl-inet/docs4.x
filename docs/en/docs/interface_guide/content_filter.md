# Content Filter

Content Filter is an intelligent online safety feature powered by DPI classification. It automatically blocks harmful and malicious websites to keep your network clean and secure, and also supports custom rules to block specific apps, domains, or IP addresses.

**Note**:

1. Content Filter will not take effect when the router is in Drop-in Gateway mode.
2. Content Filter cannot work with Network Acceleration. Enabling Content Filter will automatically disable Network Acceleration to ensure stable performance.

## Supported Models

!!! note "Supported Models"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    
## Quick Setup

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **Content Filter**. 

Toggle the switch in the upper right corner, customize blocked content (such as apps, domains or IP addresses), then click **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

This page consists of two parts:

- **Blocked Apps List**: This section includes three pre-selected categories: Gambling, Adult, and Malware. When enabled, any websites, services or apps related to these three categories will be blocked. 

    You can also click **Edit App** to add more categories (e.g., Game, Social Media) as needed.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    In the pop-up window, select the categories you want to block. The default three categories are empty; all other categories include a list of apps.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Click any category to view and select the apps you want to block, or click **Select All** in the upper right to block all apps in that category at once, then click **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    You will then see the selected apps in the Blocked App List.

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

- **Blocked Domain / IP List**: This section allows you to manually enter specific domains (e.g., google.com), CIDR range (e.g., 192.168.8.0/24), or IP addresses (e.g., 192.168.10.10) to block access to them. The list supports up to 10000 entries.

    Enter the domains or IP addresses you want to block, then click **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Content Filter Test

For example, we have selected the **Game** category, which includes Nintendo.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

On a laptop connected to your router, the site `nintendo.com` can no longer be accessed, though it was reachable before Content Filter was enabled.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

In the router's web Admin Panel, you can see the number of access requests that have been blocked.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.