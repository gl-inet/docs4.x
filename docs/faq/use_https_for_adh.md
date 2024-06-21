# Use HTTPS to access GL-iNet Router and Adguard Home

First, please apply a SSL cert or use a self-signed SSL cert.
Then, SSH into your GL-iNet Router or use WinSCP to replace the updated certificate and key to our router. The paths are
`/etc/nginx/nginx.cer`
`/etc/nginx/nginx.key`

## After that, enable AdGuard on GLiNet Router

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg)

## Go to Adguard Home Settings Page

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg)

## Go to Encryption settings

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg)

## Check the Enable box and put 3001 at the HTTPS port

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg)

## Add the paths of your updated certificate and key and save

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg)

Then you can use HTTPS to visit 192.168.8.1 or 192.168.8.1:3001