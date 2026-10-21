# GL.iNet-router en AdGuard Home via HTTPS openen {#access-glinet-router-and-adguard-home-via-https}

Volg de onderstaande stappen om je GL.iNet-router en AdGuard Home via HTTPS te openen.

## 1. Certificaat en sleutel op de GL.iNet-router bijwerken {#1-update-certificate-and-key-in-glinet-router}

Vraag eerst een SSL-certificaat aan of gebruik een zelfondertekend SSL-certificaat.

Maak daarna via SSH verbinding met je GL.iNet-router of gebruik WinSCP om het bijgewerkte certificaat en de sleutel te uploaden. De paden zijn:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Enable AdGuard Home {#2-enable-adguard-home}

Log in to the GL.inet web Admin Panel -> APPLICATIONS -> AdGuard Home, enable AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Klik bovenaan op **Settings Page**. Je wordt doorgestuurd naar de instellingenpagina van AdGuard Home.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Edit Encryption settings {#3-edit-encryption-settings}

In the Adguard Home Settings Page, navigate to the Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Schakel linksboven Enable Encryption in en voer 3001 in als HTTPS-poort.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Voeg de paden van het bijgewerkte certificaat en de sleutel toe en klik op Save.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Daarna kun je **192.168.8.1** of **192.168.8.1:3001** via HTTPS openen.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
