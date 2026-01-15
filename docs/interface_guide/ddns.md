# Dynamic DNS

Dynamic Domain Name Service (Dynamic DNS or DDNS) is a service used to map a domain name to the dynamic IP address of a network device. With Dynamic DNS, you can access your router remotely. An Internet public IP address is required for this functionality.

## Enable DDNS

On the left side of web Admin Panel -> APPLICATIONS -> Dynamic DNS, the page is displayed as below.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Toggle on **Enable DDNS**, agree to the **Terms of Services & Privacy Policy**, then click **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Click on **Security Settings** in the bottom right corner.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

In the pop-up window, check if the remote access protocol you want to apply is enabled. If not, go to SYSTEM -> Security -> Remote Access Control to enable it.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Enable the remote access protocol you want, and click **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

There may be a delay of up to 10 minutes in record synchronization between DNS servers. This may prevent you from accessing through the DDNS domain name immediately after enabling it or when your public IP changes.

**Note**: If you enable DDNS and VPN Client at the same time, make sure that **Services From GL.iNet Use VPN** is disabled. This feature can be found in the [VPN Client Options](vpn_dashboard.md#tunnel-options) of the VPN Dashboard.

## Check If DDNS Works

You can check if DDNS works using the DDNS test tool or check it manually using commands.

=== "Using the DDNS Test tool"

    In the Dynamic DNS page, click the **DDNS Test**

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Make sure the IP address from DDNS domain resolution matches the router’s WAN IP. 
    
    If not, a yellow prompt will appear at the top, indicating that the router might be behind NAT, and you need to set up port forwarding on the upstream router.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Check it manually"

    1. Use `nslookup` command to obtain the mapping between domain name and IP address, as shown below.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        Replace the "xxxxxxx.glddns.com" in the image above with your Host Name. 
        
        The "8.8.8.8" in the image above is the Google DNS. Use it or replace it with other DNS, then press Enter.

    2. If you get a public IP address as an output, such as "103.81.180.10" in the image below, it indicates that your DDNS domain has been successfully mapped to a public IP address.

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}
        
        On a device connected to the router, search for "what is my ip address" in a browser, or visit a website like [What Is My IP Address](https://whatismyipaddress.com){target="_blank"}. You will get your public IP address. Compare the two IP addresses obtained from Step 1 and 2. If they are the same, the DDNS is in effect, otherwise it is not.

    3. If you get a message `** server can't find xxxxxxx.glddns.com: NXDOMAIN`, as shown below, it indicates that domain resolution failed, and your DDNS domain has not been successfully mapped to a public IP address.

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## HTTPS Remote Access

!!! Note

    1. A **Public IP** address is required for HTTPS remote access. 
    
        Click [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) to check if your Internet Provider Service (ISP) assigns you a public IP address.
    
    2. If your router is behind NAT, configure port forwarding (port **443**) on the upstream router for HTTPS access.

Follow the steps below to enable HTTPS remote access for your router.

1. On the Dynamic DNS page, toggle on **Enable DDNS**, agree to the **Terms of Services & Privacy Policy**, then click **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. In the web admin panel, go to SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Enable **HTTPS Remote Access**, and click **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Once enabled, you can access the router’s admin panel from anywhere using the DDNS host name over **HTTPS** (e.g., `https://xxxxxxx.glddns.com`). 

If port forwarding is configured, access it as `https://xxxxxxx.glddns.com:external_port `(replace the external_port with your actual port number). 

**Note**: This function uses self-signed certificates, therefore the browsers will indicate **Your connection is not private** when accessing the router's admin panel via the DDNS host name over **HTTPS**, as shown below (port 8001 is used below as an example).

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

To proceed the HTTPS remote access, click **Advanced** at the bottom.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Then click **Proceed to xxxxxxx.glddns.com** to continue.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

You will then be able to access the web admin panel using the DDNS host name over HTTPS.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSH Remote Access

!!! Note

    1. A **Public IP** address is required for SSH remote access. 
    
        Click [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) to check if your Internet Provider Service (ISP) assigns you a public IP address.
    
    2. If your router is behind NAT, configure port forwarding (port **22**) on the upstream router for SSH access.

Follow the steps below to enable SSH remote access for your router.

1. On the Dynamic DNS page, toggle on **Enable DDNS**, agree to the **Terms of Services & Privacy Policy**, then click **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. In the web admin panel, go to SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Enable **SSH Remote Access**, and click **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Once enabled, you can access the router's admin panel from anywhere using the DDNS host name over **SSH** (e.g., `ssh root@xxxxxxx.glddns.com`). 

If port forwarding is configured, access it as `ssh root@xxxxxxx.glddns.com:external_port` (replace the external_port with your actual port number). 

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
