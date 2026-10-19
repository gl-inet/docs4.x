# Посібник користувача GL-S20 {#gl-s20-user-guide}

## Апаратна інформація {#hardware-info}

[Технічні характеристики GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## Список GPIO {#gpio-list}

| Позначення GPIO ESP32-WROOM-32U | СИГНАЛ | ФУНКЦІЯ |
| ----------------------------- | -------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0          | Підключено до виводу DTR ch340c для переходу пристрою в режим завантаження |
| GPIO1                         | BUTTON         | Вхід кнопки для скидання |
| GPIO2                         | GPIO2          | Керування лінією скидання h2 |
| GPIO3                         | GPIO3          | Керування лінією завантаження h2 |
| GPIO4                         | PHY_SPI_INT    | Вивід GPIO переривання модуля Ethernet SPI |
| GPIO5                         | PHY_RESET      | Вивід GPIO скидання PHY модуля Ethernet SPI |
| GPIO6                         | NETWORK_LED    | Керування мережевим індикатором (зелений) |
| GPIO7                         | NETWORK_LED    | Керування мережевим індикатором (червоний) |
| GPIO8                         | UART1 RX	     | Підключення до h2 uart0 tx |
| GPIO9                         | POWER_LED      | Керування індикатором живлення (зелений) |
| GPIO10                        | PHY_SPI_CSN    | Вивід GPIO SPI CS модуля Ethernet SPI |
| GPIO11                        | PHY_SPI_MOSI   | Вивід GPIO SPI MOSI модуля Ethernet SPI |
| GPIO12                        | PHY_SPI_CK     | Вивід GPIO SPI SCLK модуля Ethernet SPI |
| GPIO13                        | PHY_SPI_MISO   | Вивід GPIO SPI MISO модуля Ethernet SPI |
| GPIO14                        | POWER_LED      | Керування індикатором живлення (червоний) |
| GPIO15                        | NETWORK_LED    | Керування мережевим індикатором (жовтий) |
| GPIO16                        | BUTTON         | Вхід кнопки керування функцією IoT |
| GPIO17                        | IOT_LED        | Керування індикатором IoT (зелений) |
| GPIO18                        | IOT_LED        | Керування індикатором IoT (червоний) |
| GPIO19                        | IOT_LED        | Керування індикатором IoT (жовтий) |
| GPIO20                        | POWER_LED	     | Керування індикатором живлення (жовтий) |
| GPIO21                        | UART1 RTS      | Підключення до h2 uart0 cts |
| GPIO35                        | GPIO35         | NC |
| GPIO36                        | GPIO36         | NC |
| GPIO37                        | GPIO37         | NC |
| GPIO38                        | GPIO38         | NC |
| GPIO39                        | GPIO39         | NC |
| GPIO40                        | PTA_REQUEST    | Використовується для PTA |
| GPIO41                        | PTA_PRIORITY   | Використовується для PTA |
| GPIO42                        | PTA_GRANT      | Використовується для PTA |
| GPIO43                        | UART0 TX       | Вихід послідовного порту для налагодження |
| GPIO44                        | UART0 RX       | Вихід послідовного порту для налагодження |
| GPIO45                        | PTA_TX_LINE    | Використовується для PTA |
| GPIO46                        | GPIO46         | NC |
| GPIO47                        | UART1 CTS      | Підключення до h2 uart0 rts |
| GPIO48                        | UART1 TX       | Підключення до h2 uart0 rx |

## Розпінування друкованої плати {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="Розпінування gl-s20" loading="lazy" />
    </a>
  </figure>
</div>

---

## Перше налаштування {#first-time-setup}

Див. [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"} у документації IoT.

---

## Посібник користувача {#user-manual}

Див. [Посібник користувача](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"} у документації IoT.

---

## Посібник із компіляції прошивки {#firmware-compilation-guide}

Див. [Посібник із компіляції прошивки](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"} у документації IoT.
