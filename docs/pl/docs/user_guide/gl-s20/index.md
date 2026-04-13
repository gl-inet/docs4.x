# Przewodnik użytkownika GL-S20

## Informacje o sprzęcie

[Specyfikacja GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## Lista GPIO

| Oznaczenie GPIO ESP32-WROOM-32U | SYGNAŁ         | FUNKCJA                                                     |
| ------------------------------- | -------------- | ----------------------------------------------------------- |
| GPIO0                           | GPIO0          | podłączone do pinu DTR układu ch340c, aby urządzenie mogło wejść w tryb pobierania |
| GPIO1                           | BUTTON         | wejście przycisku, używane do resetowania                   |
| GPIO2                           | GPIO2          | używane do sterowania wejściem resetu h2                    |
| GPIO3                           | GPIO3          | używane do sterowania wejściem boot h2                      |
| GPIO4                           | PHY_SPI_INT    | numer GPIO przerwania modułu SPI Ethernet                   |
| GPIO5                           | PHY_RESET      | numer GPIO resetu PHY dla modułu SPI Ethernet               |
| GPIO6                           | NETWORK_LED    | sterowanie diodą sieci (zielona)                            |
| GPIO7                           | NETWORK_LED    | sterowanie diodą sieci (czerwona)                           |
| GPIO8                           | UART1 RX	     | używane do połączenia z h2 uart0 tx                         |
| GPIO9                           | POWER_LED      | sterowanie diodą zasilania (zielona)                        |
| GPIO10                          | PHY_SPI_CSN    | numer GPIO SPI CS dla modułu SPI Ethernet                   |
| GPIO11                          | PHY_SPI_MOSI   | numer GPIO SPI MOSI dla modułu SPI Ethernet                 |
| GPIO12                          | PHY_SPI_CK     | numer GPIO SPI SCLK dla modułu SPI Ethernet                 |
| GPIO13                          | PHY_SPI_MISO   | numer GPIO SPI MISO dla modułu SPI Ethernet                 |
| GPIO14                          | POWER_LED      | sterowanie diodą zasilania (czerwona)                       |
| GPIO15                          | NETWORK_LED    | sterowanie diodą sieci (żółta)                              |
| GPIO16                          | BUTTON         | wejście przycisku, używane do sterowania funkcją iot        |
| GPIO17                          | IOT_LED        | sterowanie diodą iot (zielona)                              |
| GPIO18                          | IOT_LED        | sterowanie diodą iot (czerwona)                             |
| GPIO19                          | IOT_LED        | sterowanie diodą iot (żółta)                                |
| GPIO20                          | POWER_LED	     | sterowanie diodą zasilania (żółta)                          |
| GPIO21                          | UART1 RTS      | używane do połączenia z h2 uart0 cts                        |
| GPIO35                          | GPIO35         | NC                                                          |
| GPIO36                          | GPIO36         | NC                                                          |
| GPIO37                          | GPIO37         | NC                                                          |
| GPIO38                          | GPIO38         | NC                                                          |
| GPIO39                          | GPIO39         | NC                                                          |
| GPIO40                          | PTA_REQUEST    | używane dla PTA                                             |
| GPIO41                          | PTA_PRIORITY   | używane dla PTA                                             |
| GPIO42                          | PTA_GRANT      | używane dla PTA                                             |
| GPIO43                          | UART0 TX       | używane do wyjścia debugowania portu szeregowego            |
| GPIO44                          | UART0 RX       | używane do wyjścia debugowania portu szeregowego            |
| GPIO45                          | PTA_TX_LINE    | używane dla PTA                                             |
| GPIO46                          | GPIO46         | NC                                                          |
| GPIO47                          | UART1 CTS      | używane do połączenia z h2 uart0 rts                        |
| GPIO48                          | UART1 TX       | używane do połączenia z h2 uart0 rx                         |

## Wyprowadzenia PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Pierwsza konfiguracja

Zapoznaj się z dokumentacją [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"} w sekcji IoT docs.

---

## Instrukcja obsługi

Zapoznaj się z [Instrukcją obsługi](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"} w sekcji IoT docs.

---

## Przewodnik kompilacji firmware

Zapoznaj się z [Przewodnikiem kompilacji firmware](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"} w sekcji IoT docs.
