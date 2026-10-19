# Посібник користувача GL-S10 {#gl-s10-user-guide}

## Апаратна інформація {#hardware-info}

[Технічні характеристики GL-S10](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## Список GPIO {#gpio-list}

| Позначення GPIO ESP32-WROOM-32U | СИГНАЛ | ФУНКЦІЯ |
| ----------------------------- | ------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0         | Керування кнопкою завантаження: за замовчуванням високий рівень; низький рівень під час запуску вмикає режим завантаження |
| GPIO1                         | UART_TX0      | Вихід послідовного порту для налагодження |
| GPIO2                         | TP3           | Резервні тестові точки JTAG |
| GPIO3                         | UART_RX0      | Вхід послідовного порту для налагодження |
| GPIO4                         | GPIO4         | NC |
| GPIO5                         | PHY_RESET     | Керування скиданням PHY MAC |
| GPIO6                         | PSRAM_CLK     | Тактовий сигнал PSRAM |
| GPIO7                         | PSRAM SDO/SD0 | Сигнал даних PSRAM SDO/SD0 |
| GPIO8                         | PSRAM SDI/SD1 | Сигнал даних PSRAM SDI/SD1 |
| GPIO9                         | PSRAM SHD/SD2 | Сигнал даних PSRAM SHD/SD2 |
| GPIO10                        | PSRAM SWP/SD3 | Сигнал даних PSRAM SWP/SD3 |
| GPIO11                        | GPIO11        | NC |
| GPIO12                        | BT LED        | Керування індикатором BLE: низький рівень вмикає світіння |
| GPIO13                        | I2C_CLK       | Тактовий сигнал I2C |
| GPIO14                        | POWER_LED     | Керування індикатором живлення |
| GPIO15                        | I2C_DATA      | Сигнал даних I2C |
| GPIO16                        | PSRAM_CE      | Сигнал керування PSRAM |
| GPIO17                        | PHY_CLK       | Тактовий сигнал мікросхеми PHY |
| GPIO18                        | MDIO          | Сигнал керування мікросхемою PHY MDIO |
| GPIO19                        | RMII_TXD0     | Дані передавання TXD0 інтерфейсу RMII |
| GPIO21                        | RMII_TXEN     | Сигнал дозволу передавання TXEN інтерфейсу RMII |
| GPIO22                        | RMII_TXD1     | Дані передавання TXD1 інтерфейсу RMII |
| GPIO23                        | MDC           | Сигнал керування мікросхемою PHY MDC |
| GPIO25                        | RMII_RXD0     | Дані приймання RXD0 інтерфейсу RMII |
| GPIO26                        | RMII_RXD1     | Дані приймання RXD1 інтерфейсу RMII |
| GPIO27                        | RMII_CS_DV    | Сигнал виявлення колізій CS_DV інтерфейсу RMII |
| GPIO32                        | NETWORK LED   | Керування мережевим індикатором |
| GPIO33                        | BUTTON        | Вхід кнопки |
| GPIO34                        | GPIO34        | NC |
| GPIO35                        | GPIO35        | NC |
| GPIO36                        | GPIO36        | NC |
| GPIO39                        | GPIO39        | NC |

## Розпінування друкованої плати {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="Розпінування gl-s10" loading="lazy" />
    </a>
  </figure>
</div>

---

## Перше налаштування {#first-time-setup}

Див. [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"} у документації IoT.

---

## Посібник користувача {#user-manual}

Див. [Посібник користувача](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"} у документації IoT.

---

## Посібник із компіляції прошивки {#firmware-compilation-guide}

Див. [Посібник із компіляції прошивки](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"} у документації IoT.
