# Guida utente di GL-S20

## Informazioni hardware

[Specifiche di GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## Elenco GPIO

| Etichettatura GPIO ESP32-WROOM-32U | SEGNALE        | FUNZIONE                                                     |
| ---------------------------------- | -------------- | ------------------------------------------------------------ |
| GPIO0                              | GPIO0          | collegato al pin DTR di ch340c per consentire al dispositivo di entrare in modalità download |
| GPIO1                              | BUTTON         | ingresso pulsante, utilizzato per il reset                   |
| GPIO2                              | GPIO2          | utilizzato per controllare l'IO di reset h2                  |
| GPIO3                              | GPIO3          | utilizzato per controllare l'IO di boot h2                   |
| GPIO4                              | PHY_SPI_INT    | numero GPIO di interrupt del modulo Ethernet SPI             |
| GPIO5                              | PHY_RESET      | numero GPIO di reset PHY del modulo Ethernet SPI             |
| GPIO6                              | NETWORK_LED    | controllo LED di rete (verde)                                |
| GPIO7                              | NETWORK_LED    | controllo LED di rete (rosso)                                |
| GPIO8                              | UART1 RX       | utilizzato per collegarsi a h2 uart0 tx                      |
| GPIO9                              | POWER_LED      | controllo LED di alimentazione (verde)                       |
| GPIO10                             | PHY_SPI_CSN    | numero GPIO SPI CS del modulo Ethernet SPI                   |
| GPIO11                             | PHY_SPI_MOSI   | numero GPIO SPI MOSI del modulo Ethernet SPI                 |
| GPIO12                             | PHY_SPI_CK     | numero GPIO SPI SCLK del modulo Ethernet SPI                 |
| GPIO13                             | PHY_SPI_MISO   | numero GPIO SPI MISO del modulo Ethernet SPI                 |
| GPIO14                             | POWER_LED      | controllo LED di alimentazione (rosso)                       |
| GPIO15                             | NETWORK_LED    | controllo LED di rete (giallo)                               |
| GPIO16                             | BUTTON         | ingresso pulsante, utilizzato per il controllo delle funzioni IoT |
| GPIO17                             | IOT_LED        | controllo LED IoT (verde)                                    |
| GPIO18                             | IOT_LED        | controllo LED IoT (rosso)                                    |
| GPIO19                             | IOT_LED        | controllo LED IoT (giallo)                                   |
| GPIO20                             | POWER_LED      | controllo LED di alimentazione (giallo)                      |
| GPIO21                             | UART1 RTS      | utilizzato per collegarsi a h2 uart0 cts                     |
| GPIO35                             | GPIO35         | NC                                                           |
| GPIO36                             | GPIO36         | NC                                                           |
| GPIO37                             | GPIO37         | NC                                                           |
| GPIO38                             | GPIO38         | NC                                                           |
| GPIO39                             | GPIO39         | NC                                                           |
| GPIO40                             | PTA_REQUEST    | utilizzato per PTA                                           |
| GPIO41                             | PTA_PRIORITY   | utilizzato per PTA                                           |
| GPIO42                             | PTA_GRANT      | utilizzato per PTA                                           |
| GPIO43                             | UART0 TX       | utilizzato per l'output della porta seriale di debug         |
| GPIO44                             | UART0 RX       | utilizzato per l'output della porta seriale di debug         |
| GPIO45                             | PTA_TX_LINE    | utilizzato per PTA                                           |
| GPIO46                             | GPIO46         | NC                                                           |
| GPIO47                             | UART1 CTS      | utilizzato per collegarsi a h2 uart0 rts                     |
| GPIO48                             | UART1 TX       | utilizzato per collegarsi a h2 uart0 rx                      |

## Piedinatura PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Configurazione iniziale

Fai riferimento a [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"} nella documentazione IoT.

---

## Manuale utente

Fai riferimento a [User Manual](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"} nella documentazione IoT.

---

## Guida alla compilazione del firmware

Fai riferimento a [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"} nella documentazione IoT.
