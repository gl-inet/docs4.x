# How to resolve a LAN subnet conflict?

When you plug an ethernet cable from home router to the WAN port of GL.iNet router, sometimes you might see this message:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

It is because your home router is using the same LAN IP of GL.iNet router, and this is called a LAN conflict.

Follow the steps below to change the LAN subnet.

## 1. Change LAN Subnet

Please click the hyperlink **Change LAN Subnet** and it will re-direct you to the **LAN** setup page.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Change the number after the second dot (which is **8** by default) to another number. For example, 192.168.10.1, and then click **Apply**.

After changing, wait a few seconds and the page will be refreshed and automatically redirected to the changed IP address **192.168.10.1**. You will see that the subnet conflict prompt disappears.

If the page is not redirected, proceed to the next step.

## 2. Login with New LAN IP

Manually enter the changed LAN IP in the address bar and press Enter.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Login with your admin password and the subnet conflict prompt will disappear.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.