# Vue d'ensemble du système

Dans la partie gauche du panneau d'administration web, accédez à **SYSTEM** -> **Overview**.

La page Overview affiche l'état de certains composants matériels et propose quelques commandes simples, notamment :

- l'état du CPU, de la mémoire, de la mémoire flash et des périphériques de stockage externes ;
- l'état d'éléments matériels comme le ventilateur, la batterie, etc. ;
- le contrôle des LED et du ventilateur ;
- les informations de l'appareil.

Voici un exemple avec le GL-MT3000.

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## Charge moyenne du CPU

Pour la plupart des modèles sans ventilateur, la charge moyenne du CPU s'affiche comme ci-dessous.

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

Pour certains modèles dotés d'un ventilateur intégré, la charge moyenne du CPU s'affiche comme ci-dessous.

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Survolez le graphique pour afficher les valeurs détaillées.

Cliquez sur la température à droite pour basculer entre Celsius et Fahrenheit.

Cliquez sur l'icône du ventilateur en haut à droite pour accéder aux paramètres du ventilateur.

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Modèles avec ventilateur intégré"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Utilisation de la mémoire

Survolez le graphique pour afficher les valeurs détaillées.

**Remarque** : la mémoire affichée ici est celle disponible pour le système Linux. Le total affiché sera inférieur à la mémoire physique, car une partie est allouée au sous-système Wi-Fi ou à d'autres zones de démarrage.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

Cliquez sur l'icône d'engrenage pour accéder aux [Scheduled Tasks](scheduled_tasks.md) des LED.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

Cette section affiche la capacité totale de la mémoire flash, y compris l'espace utilisé par le système, l'espace utilisé par les applications et l'espace disponible restant.

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## Informations sur l'appareil

Cette section affiche les informations de base de l'appareil.

L'ID de l'appareil, l'adresse MAC de l'appareil et le numéro de série sont disponibles depuis le firmware v4.7.

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## Stockage externe

Cette section, disponible depuis la v4.5, affiche la capacité totale et la capacité disponible du disque USB.

Certains modèles équipés du firmware v4.7 ou version ultérieure prennent en charge le changement de protocole USB.

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
