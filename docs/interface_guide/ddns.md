# Dynamic DNS

Dynamic Domain Name Service (Dynamic DNS or DDNS) is a service used to map a domain name to the dynamic IP address of a network device.

On the left side of web Admin Panel -> APPLICATIONS -> Dynamic DNS

![ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/ddns.png){class="glboxshadow"}

## Enable DDNS

Toggle on **Enabled DDNS**, option in Terms of Services & Privacy Policy, then click **Apply** button. Generally it take several minutes to take effect.

DDNS update frequency is once every 10 minutes.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/enable_ddns.png){class="glboxshadow"}

**Note**: If you using DDNS and VPN Client at the same time, please make sure to enable **Services From GL.iNet Doesn't Use VPN** in [Global Option of VPN Client](vpn_dashboard.md#global-options-of-vpn-client).

## Check if DDNS is in effect

=== "Using the DDNS Test tool"

    Click the **DDNS Test**

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/click_ddns_test.png){class="glboxshadow"}

    If it says **Your DDNS is resolved as x.x.x.x** as show below, it means the DDNS is worked. In other words, this **Host Name** has maped to the final exit IP of the router for Internet access.

    ![ddns works](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/ddns_test_resolved.png){class="glboxshadow"}

=== "Or check it manually"

    Check the two IP address below to see if they are the same, if yes, the DDNS is in effect, otherwise not.

    * Use `nslookup` command as show below to obtain the mapping between domain name and IP address. You need to change `zw72cd7.glddns.com` to your Host Name. `8.8.8.8` is Google DNS, you can change to other DNS.

        `nslookup zw72cd7.glddns.com 8.8.8.8`

        ![nslookup](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/nslookup.png){class="glboxshadow"}

        The output above means the Host Name has maped to an IP address.

    * Use phone/computer that connected to the router, search **my ip address** on Google, or access website like [https://whatismyipaddress.com/](https://whatismyipaddress.com/){target="_blank"}

## HTTP Remote Access

This function requires a public IP address. To check if your Internet Provider Service assign your a public IP address, please check [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

If your router is behind NAT, you may need to set up port forwarding in higher level router. It use port **80**.

![HTTP-Remote-Access](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/http_remote_access.png){class="glboxshadow"}

Follow the steps above, to enable HTTP Remote Access. 

***HTTP is not encrypted, use at your own risk.***

After you enable HTTP Remote Access, you can access Admin Panel anywhere by your DDNS Host Name of **http**, e.g. `http://xxxxxxx.glddns.com`. If you use port forwarding, you should be access like `http://xxxxxxx.glddns.com:YourExternalPort`.

## HTTPS Remote Access

This function requires a public IP address. To check if your Internet Provider Service assign your a public IP address, please check [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

If your router is behind NAT, you may need to set up port forwarding in higher level router. It use port **443**.

![HTTPS-Remote-Access](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access.png){class="glboxshadow"}

After you enable HTTPS Remote Access, you can access Admin Panel anywhere by your DDNS Host Name of **https**, e.g. `https://xxxxxxx.glddns.com`. If you use port forwarding, you should be access like `https://xxxxxxx.glddns.com:YourExternalPort`.

This function use self-signed certificates, so the browers will indicate that **Your connection is not private**. I will show you how to use it anyway on Chrome Android, other browers are the similar process. I will turn off the WiFi on my phone and only use 4G to access the Internet.

Open chrome and type the URL in the address bar, I'll use `https://zw72cd7.glddns.com:8001` as an example. Click **Advanced** at the bottom to continue.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Click **Processed to xxxxxxx.glddns.com (unsafe)** to continue.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Then, it will access the web Admin Panel.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSH Remote Access

This function requires a public IP address. To check if your Internet Provider Service assign your a public IP address, please check [here](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md).

If your router is behind NAT, you may need to set up port forwarding in higher level router. It use port **22**.

![SSH-Remote-Access](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/ssh_remote_access.png){class="glboxshadow"}

Follow the steps above, to enable SSH Remote Access, then you can ssh to your router anywhere. 

Your SSH command should like below.

`ssh root@xxxxxxx.glddns.com`

or 

`ssh root@xxxxxxx.glddns.com:YourExternalPort`

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
