# Przewodnik użytkownika GL-S10

## Informacje o sprzęcie

[Specyfikacja GL-S10](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## Lista GPIO

| Oznaczenie GPIO ESP32-WROOM-32U | SYGNAŁ        | FUNKCJA                                                     |
| ------------------------------- | ------------- | ----------------------------------------------------------- |
| GPIO0                           | GPIO0         | sterowanie przyciskiem pobierania, domyślnie stan wysoki, podczas uruchamiania stan niski w celu wejścia w tryb pobierania |
| GPIO1                           | UART_TX0      | używane do wyjścia debugowania portu szeregowego            |
| GPIO2                           | TP3           | zarezerwowane punkty testowe JTAG                           |
| GPIO3                           | UART_RX0      | używane do wejścia debugowania portu szeregowego            |
| GPIO4                           | GPIO4         | NC                                                          |
| GPIO5                           | PHY_RESET     | sterowanie resetem MAC phy                                  |
| GPIO6                           | PSRAM_CLK     | sygnał zegara psram                                         |
| GPIO7                           | PSRAM SDO/SD0 | sygnał danych psram SDO/SD0                                 |
| GPIO8                           | PSRAM SDI/SD1 | sygnał danych psram SDI/SD1                                 |
| GPIO9                           | PSRAM SHD/SD2 | sygnał danych psram SHD/SD2                                 |
| GPIO10                          | PSRAM SWP/SD3 | sygnał danych psram SWP/SD3                                 |
| GPIO11                          | GPIO11        | NC                                                          |
| GPIO12                          | BT LED        | sterowanie diodą ble, stan niski powoduje jej zapalenie     |
| GPIO13                          | I2C_CLK       | sygnał zegara I2C                                           |
| GPIO14                          | POWER_LED     | sterowanie diodą zasilania                                  |
| GPIO15                          | I2C_DATA      | sygnał danych I2C                                           |
| GPIO16                          | PSRAM_CE      | sygnał sterujący psram                                      |
| GPIO17                          | PHY_CLK       | sygnał zegara układu phy                                    |
| GPIO18                          | MDIO          | sygnał sterujący MDIO układu phy                            |
| GPIO19                          | RMII_TXD0     | dane TXD0 interfejsu RMII                                   |
| GPIO21                          | RMII_TXEN     | sygnał włączenia transmisji TXEN interfejsu RMII            |
| GPIO22                          | RMII_TXD1     | dane TXD1 interfejsu RMII                                   |
| GPIO23                          | MDC           | sygnał sterujący MDC układu phy                             |
| GPIO25                          | RMII_RXD0     | dane RXD0 interfejsu RMII                                   |
| GPIO26                          | RMII_RXD1     | dane RXD1 interfejsu RMII                                   |
| GPIO27                          | RMII_CS_DV    | sygnał wykrywania kolizji CS_DV interfejsu RMII             |
| GPIO32                          | NETWORK LED   | sterowanie diodą sieci                                      |
| GPIO33                          | BUTTON        | wejście przycisku                                           |
| GPIO34                          | GPIO34        | NC                                                          |
| GPIO35                          | GPIO35        | NC                                                          |
| GPIO36                          | GPIO36        | NC                                                          |
| GPIO39                          | GPIO39        | NC                                                          |

## Wyprowadzenia PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Pierwsza konfiguracja

Zapoznaj się z dokumentacją [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"} w sekcji IoT docs.

---

## Instrukcja obsługi

Zapoznaj się z [Instrukcją obsługi](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"} w sekcji IoT docs.

---

## Przewodnik kompilacji firmware

Zapoznaj się z [Przewodnikiem kompilacji firmware](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"} w sekcji IoT docs.
