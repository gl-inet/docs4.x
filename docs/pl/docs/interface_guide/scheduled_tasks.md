# Zaplanowane zadania

W lewym panelu bocznym panelu administracyjnego przejdź do **SYSTEM** -> **Scheduled Tasks**.

Funkcja Zaplanowane zadania umożliwia skonfigurowanie codziennych harmonogramów podstawowych operacji, takich jak włączanie i wyłączanie diody LED, ponowne uruchamianie routera, włączanie i wyłączanie Wi‑Fi oraz przełączanie poziomu mocy TX.

**Uwaga**: Przed użyciem tej funkcji najpierw zsynchronizuj czas w sekcji [Time Zone](time_zone.md). Jeśli urządzenie będzie wyłączone o zaplanowanej godzinie, zadanie nie zostanie wykonane.

## Harmonogram wyświetlacza LED

Ta funkcja umożliwia ustawienie harmonogramu włączania i wyłączania diody LED routera.

Po jej włączeniu ustaw godzinę włączenia i wyłączenia, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

W modelach z ekranem dotykowym (np. GL-BE3600 Slate 7) harmonogram wyświetlacza LCD pozwala ustawić godziny włączania i wyłączania ekranu dotykowego.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Zaplanowany restart

Ta funkcja umożliwia ustawienie harmonogramu automatycznego ponownego uruchamiania routera.

Po jej włączeniu ustaw godzinę restartu, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Harmonogram Wi‑Fi

Ta funkcja umożliwia ustawienie harmonogramów Wi‑Fi zależnie od pasm obsługiwanych przez router, takich jak 2.4 GHz, 5 GHz, 6 GHz i MLO Wi‑Fi.

Z wyjątkiem MLO Wi‑Fi, które obsługuje wyłącznie tryb planowania włączania i wyłączania, wszystkie pozostałe pasma Wi‑Fi obsługują dwa tryby harmonogramu: **Turn On/Off** i **Switch TX Power**.

- **Turn On/Off**: Pomaga zachować równowagę między wygodą korzystania z sieci a oszczędnością energii, automatycznie włączając lub wyłączając sieć bezprzewodową o określonych godzinach (np. wyłączając ją na czas snu, aby ograniczyć niepotrzebne zużycie energii).

- **Switch TX Power**: Oznacza automatyczne dostosowywanie mocy nadawania bezprzewodowego (która wpływa na siłę sygnału i zasięg) o określonych godzinach, tak aby zrównoważyć wydajność i efektywność energetyczną (np. obniżyć moc przy małym obciążeniu).

### Harmonogram MLO Wi‑Fi

| Obsługiwane modele       |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

Możesz ustawić harmonogram włączania i wyłączania zarówno dla głównej sieci MLO Wi‑Fi, jak i sieci Wi‑Fi dla gości.

Włącz harmonogram dla głównej sieci Wi‑Fi lub sieci dla gości, ustaw godziny włączenia i wyłączenia, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### Harmonogram Wi‑Fi 6 GHz

| Obsługiwane modele       |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-BE9300 (Flint 3)      |    √    |

Gdy tryb harmonogramu Wi‑Fi to **Turn On/Off**, możesz ustawić harmonogram włączania i wyłączania zarówno dla głównej sieci Wi‑Fi 6 GHz, jak i sieci Wi‑Fi dla gości.

Włącz harmonogram dla głównej sieci Wi‑Fi lub sieci dla gości, ustaw godziny włączenia i wyłączenia, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Gdy tryb harmonogramu Wi‑Fi to **Switch TX Power**, możesz ustawić harmonogram przełączania mocy TX dla głównej sieci Wi‑Fi 6 GHz. Pamiętaj, że sieć Wi‑Fi dla gości 6 GHz nie jest obsługiwana w tym trybie harmonogramu.

Włącz harmonogram dla głównej sieci Wi‑Fi, ustaw dwie akcje czasowe przełączania mocy TX, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Ustawia moc TX na określony poziom (np. Low) o wybranej godzinie (np. 22:00).
- **Restore**: Przywraca moc TX do innego poziomu (np. Max) o innej godzinie (np. 07:00).
- **days**: Wybierz dni tygodnia, w których te ustawienia mają obowiązywać.

### Harmonogram Wi‑Fi 5 GHz

Gdy tryb harmonogramu Wi‑Fi to **Turn On/Off**, możesz ustawić harmonogram włączania i wyłączania zarówno dla głównej sieci Wi‑Fi 5 GHz, jak i sieci Wi‑Fi dla gości.

Włącz harmonogram dla głównej sieci Wi‑Fi lub sieci dla gości, ustaw godziny włączenia i wyłączenia, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Gdy tryb harmonogramu Wi‑Fi to **Switch TX Power**, możesz ustawić harmonogram przełączania mocy TX dla głównej sieci Wi‑Fi 5 GHz. Pamiętaj, że sieć Wi‑Fi dla gości 5 GHz nie jest obsługiwana w tym trybie harmonogramu.

Włącz harmonogram dla głównej sieci Wi‑Fi, ustaw dwie akcje czasowe przełączania mocy TX, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Ustawia moc TX na określony poziom (np. Low) o wybranej godzinie (np. 22:00).
- **Restore**: Przywraca moc TX do innego poziomu (np. Max) o innej godzinie (np. 07:00).
- **days**: Wybierz dni tygodnia, w których te ustawienia mają obowiązywać.

### Harmonogram Wi‑Fi 2.4 GHz

Gdy tryb harmonogramu Wi‑Fi to **Turn On/Off**, możesz ustawić harmonogram włączania i wyłączania zarówno dla głównej sieci Wi‑Fi 2.4 GHz, jak i sieci Wi‑Fi dla gości.

Włącz harmonogram dla głównej sieci Wi‑Fi lub sieci dla gości, ustaw godziny włączenia i wyłączenia, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Gdy tryb harmonogramu Wi‑Fi to **Switch TX Power**, możesz ustawić harmonogram przełączania mocy TX dla głównej sieci Wi‑Fi 2.4 GHz. Pamiętaj, że sieć Wi‑Fi dla gości 2.4 GHz nie jest obsługiwana w tym trybie harmonogramu.

Włącz harmonogram dla głównej sieci Wi‑Fi, ustaw dwie akcje czasowe przełączania mocy TX, wybierz dni tygodnia, w których harmonogram ma obowiązywać, a następnie kliknij **Apply**.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Ustawia moc TX na określony poziom (np. Low) o wybranej godzinie (np. 22:00).
- **Restore**: Przywraca moc TX do innego poziomu (np. Max) o innej godzinie (np. 07:00).
- **days**: Wybierz dni tygodnia, w których te ustawienia mają obowiązywać.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
