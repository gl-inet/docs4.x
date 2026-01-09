# Problem Notification and Solutions for GL-X3000/GL-XE3000/GL-X2000 Failure to Work with EE SIM Cards

Dear GL.iNet Customers,

Recently we noticed that some customers come across connectivity failures with GL-X3000/GL-XE3000/GL-X2000 when using EE SIM cards. Through further troubleshooting, we found that certain EE SIM cards only support the IPv4 protocol. However, the default settings on GL.iNet cellular routers enable both IPv4 & IPv6 simultaneously, which causes this issue.

## Solutions & Workarounds

1. **Firmware Update**

    We have released new firmware updates that changed the default protocol to IPv4 to resolve the issue. Customers who need IPv6 can still modify the settings to IPv4 & IPv6 in the admin panel.

    | Router Model                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Firmware Download](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Firmware Download](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Firmware Download](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Workaround for Other Models**

    If you have other models or prefer not to use the above firmware, please run the AT commands sequentially after starting the cellular connection.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Note**: "User_APN" is typically "everywhere" for EE SIM cards. Repeat this process after each router restart.

    ??? note "How do I run AT command?"

        1. In the web admin panel, navigate to INTERNET -> Cellular section, click the three-dot icon in the upper-right corner and select **Modem AT Command**.
        
            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}
        
            For older firmware, click the tool button in the upper-right corner to enter the modem management page.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}
        
        2. Locate the AT command, as shown below.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

If you encounter further issues, please contact our support team at [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Sincerely,

GL.iNet Technical Support

June 17, 2025