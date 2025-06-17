# Problem Notification and Solutions for GL-X3000/GL-X2000 Failure to Work with EE SIM Cards

Dear GL.iNet Customers,

Recently we noticed that some customers come across connectivity failures with GL-X3000/GL-X2000 when using EE SIM cards. Through further troubleshooting, we found that certain EE SIM cards only support the IPv4 protocol. However, the default settings on GL.iNet cellular routers enable both IPv4 & IPv6 simultaneously, which causes this issue.

## Solutions & Workarounds

1. **Firmware Update**

    We will release a new firmware update by the end of June to change the default protocol to IPv4, resolving the issue. Customers who need IPv6 can still modify the settings to IPv4&IPv6 in the admin panel.

2. **Existing Fix for GL-X3000/GL-XE3000**

    The SDK v4.8 firmware already includes this fix. You can manually download and upgrade it via [this link](https://dl.gl-inet.com/router/x3000/beta).

3. **Temporary Workaround for Other Models**

    If you have other models or prefer not to use the beta firmware, follow these steps to run the AT commands sequentially after starting the cellular connection.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Note**: "User_APN" is typically "everywhere" for EE SIM cards. Repeat this process after each router restart.

If you encounter further issues, please contact our support team at [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Sincerely,

GL.iNet Technical Support

June 17, 2025