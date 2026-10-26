# Använd HTTPS för att öppna GL.iNet-routern och AdGuard Home {#access-glinet-router-and-adguard-home-via-https}

Följ stegen nedan om du vill använda HTTPS för att öppna GL.iNet-routern och AdGuard Home.

## 1. Uppdatera certifikatet och nyckeln på GL.iNet-routern {#1-update-certificate-and-key-in-glinet-router}

Skaffa först ett SSL-certifikat eller använd ett självsignerat SSL-certifikat.

Anslut sedan till GL.iNet-routern via SSH eller använd WinSCP för att ladda upp det uppdaterade certifikatet och nyckeln till GL.iNet-routern. Sökvägarna är:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Aktivera AdGuard Home {#2-enable-adguard-home}

Logga in på GL.inet-webbadministrationspanelen -> APPLICATIONS -> AdGuard Home och aktivera AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Klicka sedan på **Settings Page** högst upp på sidan. Du omdirigeras till inställningssidan för AdGuard Home.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Redigera krypteringsinställningarna {#3-edit-encryption-settings}

Gå till Settings -> Encryption settings på inställningssidan för AdGuard Home.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Markera rutan Enable Encryption längst upp till vänster och ange 3001 som HTTPS-port.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Lägg till sökvägarna till det uppdaterade certifikatet och nyckeln och klicka på Save.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Du kan sedan använda HTTPS för att öppna **192.168.8.1** eller **192.168.8.1:3001**.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
