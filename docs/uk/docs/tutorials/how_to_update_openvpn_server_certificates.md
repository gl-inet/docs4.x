# Як оновити сертифікати сервера OpenVPN? {#how-to-update-openvpn-server-certificates}

У цьому посібнику описано оновлення сертифікатів сервера OpenVPN на маршрутизаторах GL.iNet.

**Примітка**: Потрібно оновити кореневий сертифікат CA, після чого всі наявні сертифікати клієнтів, вбудовані у файли конфігурації, втратять чинність. Щоб клієнти OpenVPN могли знову підключатися до сервера, обов’язково повторно експортуйте всі файли конфігурації.

1. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **VPN** -> **OpenVPN Server**.

    Якщо сервер OpenVPN працює, зупиніть службу.

2. На вкладці Configuration натисніть **Advanced Configuration**, щоб розгорнути налаштування.

    ![Розширені налаштування сертифікатів](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Знайдіть **Server Root Certificate** і видаліть увесь вміст текстового поля.

    ![Видалення наявних сертифікатів і ключа сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Відповідні Server Certificate і Server Key також буде видалено автоматично, як показано нижче.

    ![Видалення наявних сертифікатів і ключа сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Залиште всі три поля порожніми та натисніть **Apply** внизу. Нові сертифікати буде автоматично створено та внесено в поля.

    ![Створення нових сертифікатів](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. Сертифікати сервера OpenVPN оновлено. Натисніть **Export Client Configuration** внизу, щоб експортувати нові конфігурації для підключення пристроїв.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
