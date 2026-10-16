# Як перевірити стан агрегації несучих на стільниковому маршрутизаторі? {#how-to-check-the-carrier-aggregation-status-on-your-cellular-router}

Агрегація несучих поєднує кілька мережевих частотних діапазонів для збільшення пропускної здатності та швидкості стільникового з’єднання.

Цю функцію не можна ввімкнути у вебпанелі адміністрування маршрутизатора: вона залежить від підтримки оператора SIM-картки.

Проте стан агрегації несучих можна перевірити AT-командами у вебпанелі адміністрування маршрутизатора.

!!! note "Підтримувані моделі"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Виконайте наведені нижче дії, щоб перевірити стан агрегації несучих.

1. Вставте SIM-картку в маршрутизатор.
2. Відкрийте веббраузер, уведіть `192.168.8.1` в адресний рядок і ввійдіть.
3. Перейдіть до розділу **INTERNET** -> **Cellular**, натисніть значок із трьома крапками вгорі праворуч і виберіть **Modem AT Command**.

    ![Відкриття Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. У спливному вікні введіть **AT+QCAINFO** і натисніть **Send**.

    Якщо агрегація несучих активна, у списку відображатимуться кілька мережевих діапазонів.

    ![Відомості агрегації несучих за командою AT+QCAINFO](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
