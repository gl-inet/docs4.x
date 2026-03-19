# Guía de usuario de GL-S20

## Información del hardware

[Especificaciones del GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="\_blank"}

## Lista de GPIO

| Etiquetado GPIO de ESP32-WROOM-32U | SIGNAL       | FUNCTION                                                                          |
| ---------------------------------- | ------------ | --------------------------------------------------------------------------------- |
| GPIO0                              | GPIO0        | conectado al pin DTR del ch340c para que el dispositivo entre en modo de descarga |
| GPIO1                              | BUTTON       | entrada del botón; utilizada para reinicio                                        |
| GPIO2                              | GPIO2        | utilizado para controlar el reset io de h2                                        |
| GPIO3                              | GPIO3        | utilizado para controlar el boot io de h2                                         |
| GPIO4                              | PHY_SPI_INT  | número GPIO de interrupción del módulo SPI Ethernet                               |
| GPIO5                              | PHY_RESET    | número GPIO de reinicio del PHY del módulo SPI Ethernet                           |
| GPIO6                              | NETWORK_LED  | control del LED de red, verde                                                     |
| GPIO7                              | NETWORK_LED  | control del LED de red, rojo                                                      |
| GPIO8                              | UART1 RX     | utilizado para conectar a h2 uart0 tx                                             |
| GPIO9                              | POWER_LED    | control del LED de alimentación, verde                                            |
| GPIO10                             | PHY_SPI_CSN  | número GPIO del CS SPI para el módulo SPI Ethernet                                |
| GPIO11                             | PHY_SPI_MOSI | número GPIO del MOSI SPI para el módulo SPI Ethernet                              |
| GPIO12                             | PHY_SPI_CK   | número GPIO del SCLK SPI para el módulo SPI Ethernet                              |
| GPIO13                             | PHY_SPI_MISO | número GPIO del MISO SPI para el módulo SPI Ethernet                              |
| GPIO14                             | POWER_LED    | control del LED de alimentación, rojo                                             |
| GPIO15                             | NETWORK_LED  | control del LED de red, amarillo                                                  |
| GPIO16                             | BUTTON       | entrada del botón; utilizada para el control de funciones IoT                     |
| GPIO17                             | IOT_LED      | control del LED IoT, verde                                                        |
| GPIO18                             | IOT_LED      | control del LED IoT, rojo                                                         |
| GPIO19                             | IOT_LED      | control del LED IoT, amarillo                                                     |
| GPIO20                             | POWER_LED    | control del LED de alimentación, amarillo                                         |
| GPIO21                             | UART1 RTS    | utilizado para conectar a h2 uart0 cts                                            |
| GPIO35                             | GPIO35       | NC                                                                                |
| GPIO36                             | GPIO36       | NC                                                                                |
| GPIO37                             | GPIO37       | NC                                                                                |
| GPIO38                             | GPIO38       | NC                                                                                |
| GPIO39                             | GPIO39       | NC                                                                                |
| GPIO40                             | PTA_REQUEST  | utilizado para PTA                                                                |
| GPIO41                             | PTA_PRIORITY | utilizado para PTA                                                                |
| GPIO42                             | PTA_GRANT    | utilizado para PTA                                                                |
| GPIO43                             | UART0 TX     | utilizado para la salida del puerto serie de depuración                           |
| GPIO44                             | UART0 RX     | utilizado para la salida del puerto serie de depuración                           |
| GPIO45                             | PTA_TX_LINE  | utilizado para PTA                                                                |
| GPIO46                             | GPIO46       | NC                                                                                |
| GPIO47                             | UART1 CTS    | utilizado para conectar a h2 uart0 rts                                            |
| GPIO48                             | UART1 TX     | utilizado para conectar a h2 uart0 rx                                             |

## Pinout de la PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Configuración inicial

Consulte [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="\_blank"} en la documentación IoT.

---

## Manual de usuario

Consulte [User Manual](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="\_blank"} en la documentación IoT.

---

## Guía de compilación del firmware

Consulte [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="\_blank"} en la documentación IoT.
