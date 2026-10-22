# GL-S20 Benutzerhandbuch {#gl-s20-user-guide}

## Hardwareinformationen {#hardware-info}

[Technische Daten des GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## GPIO-Liste {#gpio-list}

| ESP32-WROOM-32U GPIO-Bezeichnung | SIGNAL         | FUNKTION                                                     |
| ----------------------------- | -------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0          | mit Pin DTR des ch340c verbunden, damit das Gerät in den Download-Modus wechselt |
| GPIO1                         | BUTTON         | Tasteneingang, für Reset verwendet                           |
| GPIO2                         | GPIO2          | zur Steuerung des h2-Reset-IO                                |
| GPIO3                         | GPIO3          | zur Steuerung des h2-Boot-IO                                 |
| GPIO4                         | PHY_SPI_INT    | Interrupt-GPIO-Nummer des SPI-Ethernet-Moduls                |
| GPIO5                         | PHY_RESET      | PHY-Reset-GPIO-Nummer des SPI-Ethernet-Moduls                |
| GPIO6                         | NETWORK_LED    | Steuerung der Netzwerk-LED (grün)                                  |
| GPIO7                         | NETWORK_LED    | Steuerung der Netzwerk-LED (rot)                                    |
| GPIO8                         | UART1 RX	     | zur Verbindung mit h2 uart0 tx                                |
| GPIO9                         | POWER_LED      | Steuerung der Power-LED (grün)                                    |
| GPIO10                        | PHY_SPI_CSN    | SPI-CS-GPIO-Nummer des SPI-Ethernet-Moduls                   |
| GPIO11                        | PHY_SPI_MOSI   | SPI-MOSI-GPIO-Nummer des SPI-Ethernet-Moduls                 |
| GPIO12                        | PHY_SPI_CK     | SPI-SCLK-GPIO-Nummer des SPI-Ethernet-Moduls                 |
| GPIO13                        | PHY_SPI_MISO   | SPI-MISO-GPIO-Nummer des SPI-Ethernet-Moduls                 |
| GPIO14                        | POWER_LED      | Steuerung der Power-LED (rot)                                      |
| GPIO15                        | NETWORK_LED    | Steuerung der Netzwerk-LED (gelb)                                 |
| GPIO16                        | BUTTON         | Tasteneingang, zur Steuerung der IoT-Funktion                 |
| GPIO17                        | IOT_LED        | Steuerung der IoT-LED (grün)                                      |
| GPIO18                        | IOT_LED        | Steuerung der IoT-LED (rot)                                        |
| GPIO19                        | IOT_LED        | Steuerung der IoT-LED (gelb)                                     |
| GPIO20                        | POWER_LED	     | Steuerung der Power-LED (gelb)                                   |
| GPIO21                        | UART1 RTS      | zur Verbindung mit h2 uart0 cts                               |
| GPIO35                        | GPIO35         | NC                                                           |
| GPIO36                        | GPIO36         | NC                                                           |
| GPIO37                        | GPIO37         | NC                                                           |
| GPIO38                        | GPIO38         | NC                                                           |
| GPIO39                        | GPIO39         | NC                                                           |
| GPIO40                        | PTA_REQUEST    | für PTA                                                      |
| GPIO41                        | PTA_PRIORITY   | für PTA                                                      |
| GPIO42                        | PTA_GRANT      | für PTA                                                      |
| GPIO43                        | UART0 TX       | Ausgang des seriellen Debugging-Ports                        |
| GPIO44                        | UART0 RX       | Eingang des seriellen Debugging-Ports |
| GPIO45                        | PTA_TX_LINE    | für PTA                                                      |
| GPIO46                        | GPIO46         | NC                                                           |
| GPIO47                        | UART1 CTS      | zur Verbindung mit h2 uart0 rts                               |
| GPIO48                        | UART1 TX       | zur Verbindung mit h2 uart0 rx                                |

## PCB-Pinbelegung {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/de/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/de/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Erste Einrichtung {#first-time-setup}

Bitte lesen Sie in der IoT-Dokumentation die Seite [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"}.

---

## Benutzerhandbuch {#user-manual}

Bitte lesen Sie in der IoT-Dokumentation das [Benutzerhandbuch](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"}.

---

## Anleitung zur Firmware-Kompilierung {#firmware-compilation-guide}

Bitte lesen Sie in der IoT-Dokumentation die [Anleitung zur Firmware-Kompilierung](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"}.
