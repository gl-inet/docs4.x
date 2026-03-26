# Guide d'utilisation du GL-S20

## Informations matérielles

[Spécifications du GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## Liste des GPIO

| Désignation GPIO ESP32-WROOM-32U | SIGNAL         | FONCTION                                                    |
| -------------------------------- | -------------- | ----------------------------------------------------------- |
| GPIO0                            | GPIO0          | connecté à la broche DTR du ch340c pour permettre à l'appareil d'entrer en mode téléchargement |
| GPIO1                            | BUTTON         | entrée du bouton, utilisée pour la réinitialisation         |
| GPIO2                            | GPIO2          | utilisé pour contrôler l'IO de réinitialisation h2          |
| GPIO3                            | GPIO3          | utilisé pour contrôler l'IO de démarrage h2                 |
| GPIO4                            | PHY_SPI_INT    | numéro GPIO d'interruption du module SPI Ethernet           |
| GPIO5                            | PHY_RESET      | numéro GPIO de réinitialisation PHY du module SPI Ethernet  |
| GPIO6                            | NETWORK_LED    | contrôle du voyant réseau (vert)                            |
| GPIO7                            | NETWORK_LED    | contrôle du voyant réseau (rouge)                           |
| GPIO8                            | UART1 RX       | utilisé pour se connecter au TX uart0 de h2                 |
| GPIO9                            | POWER_LED      | contrôle du voyant d'alimentation (vert)                    |
| GPIO10                           | PHY_SPI_CSN    | numéro GPIO CS SPI du module SPI Ethernet                   |
| GPIO11                           | PHY_SPI_MOSI   | numéro GPIO MOSI SPI du module SPI Ethernet                 |
| GPIO12                           | PHY_SPI_CK     | numéro GPIO SCLK SPI du module SPI Ethernet                 |
| GPIO13                           | PHY_SPI_MISO   | numéro GPIO MISO SPI du module SPI Ethernet                 |
| GPIO14                           | POWER_LED      | contrôle du voyant d'alimentation (rouge)                   |
| GPIO15                           | NETWORK_LED    | contrôle du voyant réseau (jaune)                           |
| GPIO16                           | BUTTON         | entrée du bouton, utilisée pour le contrôle des fonctions IoT |
| GPIO17                           | IOT_LED        | contrôle du voyant IoT (vert)                               |
| GPIO18                           | IOT_LED        | contrôle du voyant IoT (rouge)                              |
| GPIO19                           | IOT_LED        | contrôle du voyant IoT (jaune)                              |
| GPIO20                           | POWER_LED      | contrôle du voyant d'alimentation (jaune)                   |
| GPIO21                           | UART1 RTS      | utilisé pour se connecter au CTS uart0 de h2                |
| GPIO35                           | GPIO35         | NC                                                          |
| GPIO36                           | GPIO36         | NC                                                          |
| GPIO37                           | GPIO37         | NC                                                          |
| GPIO38                           | GPIO38         | NC                                                          |
| GPIO39                           | GPIO39         | NC                                                          |
| GPIO40                           | PTA_REQUEST    | utilisé pour PTA                                            |
| GPIO41                           | PTA_PRIORITY   | utilisé pour PTA                                            |
| GPIO42                           | PTA_GRANT      | utilisé pour PTA                                            |
| GPIO43                           | UART0 TX       | utilisé pour la sortie du port série de débogage            |
| GPIO44                           | UART0 RX       | utilisé pour la sortie du port série de débogage            |
| GPIO45                           | PTA_TX_LINE    | utilisé pour PTA                                            |
| GPIO46                           | GPIO46         | NC                                                          |
| GPIO47                           | UART1 CTS      | utilisé pour se connecter au RTS uart0 de h2                |
| GPIO48                           | UART1 TX       | utilisé pour se connecter au RX uart0 de h2                 |

## Brochage du PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Configuration initiale

Veuillez consulter [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"} dans la documentation IoT.

---

## Manuel de l'utilisateur

Veuillez consulter le [manuel de l'utilisateur](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"} dans la documentation IoT.

---

## Guide de compilation du firmware

Veuillez consulter le [guide de compilation du firmware](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"} dans la documentation IoT.
