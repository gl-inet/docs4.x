# Tâches planifiées

Dans la partie gauche du panneau d'administration web, accédez à **SYSTEM** -> **Scheduled Tasks**.

Les tâches planifiées vous permettent de configurer des horaires quotidiens pour des opérations de base telles que l'activation/désactivation des LED, le redémarrage du routeur, l'activation/désactivation du Wi‑Fi et le changement du niveau de puissance TX.

**Remarque** : Veuillez d'abord synchroniser l'heure dans [Fuseau horaire](time_zone.md) avant d'utiliser cette fonction. Si l'appareil est éteint à l'heure planifiée, la tâche ne sera pas exécutée.

## Planification de l'affichage LED

Cette fonction vous permet de définir un horaire d'activation/désactivation pour le voyant LED de votre routeur.

Une fois activée, définissez les heures d'activation et de désactivation, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

Pour les modèles dotés d'un écran tactile (par exemple, GL-BE3600 Slate 7), la planification de l'affichage LCD vous permet de définir un horaire d'activation/désactivation pour l'écran tactile.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Redémarrage planifié

Cette fonction vous permet de définir un horaire pour redémarrer automatiquement votre routeur.

Une fois activée, définissez les heures de redémarrage, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Planification Wi-Fi

Cette fonction vous permet de définir des horaires Wi-Fi en fonction des bandes de fréquences Wi-Fi prises en charge par votre routeur (telles que 2,4 GHz, 5 GHz, 6 GHz et MLO Wi-Fi).

À l'exception du MLO Wi-Fi, qui ne prend en charge que le mode de planification activation/désactivation, toutes les autres bandes de fréquences Wi-Fi prennent en charge deux modes de planification : Turn On/Off et Switch TX Power.

- **Turn On/Off** : Permet d'équilibrer la commodité de la connectivité et l'économie d'énergie en activant ou désactivant automatiquement le réseau sans fil à des heures spécifiques (par exemple, désactivation pendant les heures de sommeil pour réduire la consommation d'énergie inutile).

- **Switch TX Power** : Permet d'ajuster automatiquement la puissance de transmission sans fil (qui détermine la force du signal et la couverture) à des heures spécifiques, équilibrant performance et efficacité énergétique (par exemple, réduction de la puissance pendant les périodes de faible utilisation).

### Planification MLO Wi-Fi

| Modèles pris en charge   |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

Vous pouvez définir un horaire d'activation/désactivation pour le MLO Main Wi-Fi et le Guest Wi-Fi.

Activez la planification Main ou Guest Wi-Fi, définissez les heures d'activation et de désactivation, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### Planification Wi-Fi 6 GHz

| Modèles pris en charge   |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-BE9300 (Flint 3)      |    √    |

Lorsque le mode de planification Wi-Fi est **Turn On/Off**, vous pouvez définir un horaire d'activation/désactivation pour le 6 GHz Main Wi-Fi et le Guest Wi-Fi.

Activez la planification Main ou Guest Wi-Fi, définissez les heures d'activation et de désactivation, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Lorsque le mode de planification Wi-Fi est **Switch TX Power**, vous pouvez définir un horaire de changement de puissance TX pour le 6 GHz Main Wi-Fi. Notez que le 6 GHz Guest Wi-Fi n'est pas pris en charge pour ce mode de planification.

Activez la planification Main Wi-Fi, définissez deux actions programmées pour changer la puissance TX, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch** : Définit la puissance TX à un certain niveau (par exemple, Low) à une heure spécifique (par exemple, 22:00).
- **Restore** : Restaure la puissance TX à un autre niveau (par exemple, Max) à une autre heure (par exemple, 07:00).
- **days** : Sélectionnez les jours effectifs de la semaine pour ces paramètres.

### Planification Wi-Fi 5 GHz

Lorsque le mode de planification Wi-Fi est **Turn On/Off**, vous pouvez définir un horaire d'activation/désactivation pour le 5 GHz Main Wi-Fi et le Guest Wi-Fi.

Activez la planification Main ou Guest Wi-Fi, définissez les heures d'activation et de désactivation, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Lorsque le mode de planification Wi-Fi est **Switch TX Power**, vous pouvez définir un horaire de changement de puissance TX pour le 5 GHz Main Wi-Fi. Notez que le 5 GHz Guest Wi-Fi n'est pas pris en charge pour ce mode de planification.

Activez la planification Main Wi-Fi, définissez deux actions programmées pour changer la puissance TX, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch** : Définit la puissance TX à un certain niveau (par exemple, Low) à une heure spécifique (par exemple, 22:00).
- **Restore** : Restaure la puissance TX à un autre niveau (par exemple, Max) à une autre heure (par exemple, 07:00).
- **days** : Sélectionnez les jours effectifs de la semaine pour ces paramètres.

### Planification Wi-Fi 2,4 GHz

Lorsque le mode de planification Wi-Fi est **Turn On/Off**, vous pouvez définir un horaire d'activation/désactivation pour le 2,4 GHz Main Wi-Fi et le Guest Wi-Fi.

Activez la planification Main ou Guest Wi-Fi, définissez les heures d'activation et de désactivation, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Lorsque le mode de planification Wi-Fi est **Switch TX Power**, vous pouvez définir un horaire de changement de puissance TX pour le 2,4 GHz Main Wi-Fi. Notez que le 2,4 GHz Guest Wi-Fi n'est pas pris en charge pour ce mode de planification.

Activez la planification Main Wi-Fi, définissez deux actions programmées pour changer la puissance TX, sélectionnez les jours de la semaine effectifs, puis cliquez sur Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch** : Définit la puissance TX à un certain niveau (par exemple, Low) à une heure spécifique (par exemple, 22:00).
- **Restore** : Restaure la puissance TX à un autre niveau (par exemple, Max) à une autre heure (par exemple, 07:00).
- **days** : Sélectionnez les jours effectifs de la semaine pour ces paramètres.

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
