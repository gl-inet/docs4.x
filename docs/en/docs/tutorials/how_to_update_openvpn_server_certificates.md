# How to update OpenVPN server certificates?

This tutorial explains how to update OpenVPN server certificates on your GL.iNet routers.

**Note**: This process requires updating the Root CA certificate, which will invalidate all existing client certificates (embedded in configuration files). You must re‑export all configuration files for your OpenVPN clients to reconnect to the server.

1. Log in to your router's web Admin Panel and go to **VPN** -> **OpenVPN Server**.

    If your OpenVPN server is running, stop the service.
    
2. Under the Configuration tab, click **Advanced Configuration** to unfold the settings.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Find the **Server Root Certificate** and delete all contents within the text box.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    The paired Server Certificate and Server Key will also be removed automatically, as shown below.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Leave all three boxes blank, and click **Apply** at the bottom. New certificates will be automatically generated and populated in the boxes.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. The OpenVPN Server certificates are now updated. Click **Export Client Configuration** at the bottom to export new configuration files for your devices to connect.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.