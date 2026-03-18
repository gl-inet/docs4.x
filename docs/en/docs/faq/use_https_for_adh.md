# Access GL.iNet router and Adguard Home via HTTPS

If you want to use HTTPS to access GL.iNet router and Adguard Home, follow the steps below.

## 1. Update certificate and key in GL.iNet router

First, please apply for an SSL cert or use a self-signed SSL cert.

Then SSH into your GL.iNet router or use WinSCP to upload the updated certificate and key to your GL.iNet router. The paths are:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Enable AdGuard Home

Log in to the GL.inet web Admin Panel -> APPLICATIONS -> AdGuard Home, enable AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Then click the **Settings Page** at the top of this page, you will be re-directed to Adguard Home Settings Page.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Edit Encryption settings

In the Adguard Home Settings Page, navigate to the Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Check the Enable Encryption box on the top left, and input 3001 at the HTTPS port.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Add the paths of your updated certificate and key, and click Save.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Then you can use HTTPS to visit **192.168.8.1** or **192.168.8.1:3001**.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.