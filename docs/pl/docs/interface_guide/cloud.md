# GL.iNet GoodCloud

## Spis treści

- [Wprowadzenie](#introduction)
- [Powiązywanie urządzeń z GoodCloud](#bind-devices-to-goodcloud)
    - [Dla firmware v4.6 lub wcześniejszego](#for-firmware-v46-or-earlier)
        - [Włączanie GoodCloud](#enable-goodcloud)
        - [Rejestracja konta](#sign-up-an-account)
        - [Dodawanie urządzeń](#add-devices)
        - [Szczegóły powiązania](#binding-details)
        - [Usuwanie powiązania urządzenia](#unbind-device)
    - [Dla firmware v4.7 lub nowszego](#for-firmware-v47-or-later)
        - [Włączanie usługi chmurowej](#enable-cloud-service)
        - [Szczegóły powiązania](#binding-details_1)
        - [Usuwanie powiązania urządzenia](#unbind-device_1) 
- [Zarządzanie urządzeniami](#manage-devices)
    - [Informacje o systemie i akcje](#system-info-and-actions)
    - [Szczegóły urządzenia](#device-details)  
        - [Podstawowe informacje](#basic-info)
        - [Statystyki](#statistics)
        - [Ustawienia sieci](#network-settings)
        - [Lista klientów](#clients-list)
- [Zdalny dostęp](#remote-access)
    - [Remote GUI](#remote-gui)
    - [Remote SSH](#remote-ssh)
- [Modyfikacja ustawień](#modify-settings)
- [Alarm e-mail](#email-alarm)
- [Site to Site](#site-to-site)
- [GoodCloud i VPN](#goodcloud-and-vpn)
- [Przeglądanie logów](#view-logs)
- [Wyłączanie chmury](#disable-cloud)
- [Usuwanie konta](#delete-account)

## Wprowadzenie {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} to platforma zaprojektowana w celu uproszczenia zdalnego wdrażania i zarządzania podłączonymi urządzeniami. Zapewnia łatwy sposób na zdalny dostęp do routerów GL.iNet i zarządzanie nimi. Dzięki centralizacji urządzeń sieciowych w chmurze użytkownicy mogą sprawnie wykonywać zadania zbiorczego zarządzania, takie jak wdrażanie konfiguracji sieciowych i aktualizacje oprogramowania. Mogą także zdalnie uzyskać dostęp do webowego panelu administracyjnego routera lub połączyć się z terminalem routera przez SSH, realizując kompleksowe zarządzanie urządzeniami sieciowymi niezależnie od regionu.

Dzięki GoodCloud możesz:

1. Sprawdzać stan routera w czasie rzeczywistym
    - Monitorować stan online/offline
    - Wyświetlać bieżące użycie RAM i średnie obciążenie
    - Otrzymywać alerty e-mail o zmianach stanu online/offline

2. Zdalnie konfigurować routery
    - Konfigurować ustawienia routera (np. SSID i hasło)
    - Uzyskiwać zdalny dostęp SSH
    - Uzyskiwać zdalny dostęp do WebUI
    - Udostępniać dostęp do routera innym osobom

3. Zdalnie monitorować podłączonych klientów
    - Wyświetlać urządzenia podłączone do Twojej sieci
    - Monitorować ruch w czasie rzeczywistym i blokować klientów
    - Otrzymywać alerty e-mail o nowych połączeniach i zdarzeniach blokowania

4. Wykonywać operacje zbiorcze
    - Zbiorczy restart
    - Zbiorcza aktualizacja firmware

5. Tworzyć połączenia Site-to-Site
    - Wirtualne biuro: rozszerzenie sieci biurowej na inne oddziały
    - Podróże służbowe: zdalny dostęp do systemów biurowych (np. OA, CRM, MySQL)
    - Inteligentny dom: zdalny dostęp do urządzeń domowych (np. kamer IP, NAS)

Jeśli chcesz zarządzać wieloma urządzeniami i odblokować zaawansowane funkcje, takie jak operacje zbiorcze, zarządzanie wieloma kontami i rozwiązania niestandardowe, wybierz nasze plany dodatkowe. Kliknij [tutaj](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"}, aby poznać szczegóły, i skontaktuj się z nami pod adresem [support@glinet.biz](mailto:support@glinet.biz).

## Powiązywanie urządzeń z GoodCloud {#bind-devices-to-goodcloud}

Aby prawidłowo połączyć urządzenia z platformą chmurową, postępuj zgodnie z procedurą powiązania odpowiednią dla swojej wersji firmware.

### Dla firmware v4.6 lub wcześniejszego {#for-firmware-v46-or-earlier}

#### Włączanie GoodCloud {#enable-goodcloud}

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **GoodCloud**. Włącz przełącznik GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

W razie potrzeby włącz **Remote SSH** i **Remote Web Access**, wybierz najbliższy serwer, przeczytaj i zaakceptuj **Terms of Service & Privacy Policy**, a następnie kliknij **Apply**.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH**: Umożliwia zdalny dostęp do terminala routera przez GoodCloud.

- **Remote Web Access**: Umożliwia zdalny dostęp do webowego panelu administracyjnego routera przez GoodCloud.

- **Data Server**: Wybierz serwer położony najbliżej lokalizacji urządzenia. Dostępne są trzy opcje: Asia Pacific (Japan), America (Oregon) i Europe (Ireland).

#### Rejestracja konta {#sign-up-an-account}

Odwiedź [stronę GoodCloud](https://www.goodcloud.xyz){target="_blank"}, aby utworzyć konto i się zalogować.

Jeśli nie otrzymasz wiadomości weryfikacyjnej, sprawdź folder spam lub odczekaj kilka minut i spróbuj ponownie. W razie problemów z rejestracją napisz na adres [support@glinet.biz](mailto:support@glinet.biz), aby uzyskać pomoc.

#### Dodawanie urządzeń {#add-devices}

Na platformie GoodCloud przejdź do **Devices** -> **Bound Devices** -> **Add Devices**. 

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

Są trzy sposoby powiązania urządzenia z kontem GoodCloud: Auto Discover, Manually Add i Bulk Import.

??? "Auto Discover"

    Możesz użyć **Auto Discover**, jeśli router i urządzenie używane do wejścia na stronę GoodCloud znajdują się w tej samej sieci.
    
    Wybierz urządzenie z listy rozwijanej i wprowadź **DDNS / Device ID**, które znajdziesz na spodzie routera lub na stronie GoodCloud w webowym panelu administracyjnym. 

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Informacje o tym, gdzie znaleźć Device ID, znajdziesz pod [tym linkiem](../faq/where_to_find_the_device_id_mac_sn.md).

??? "Manually Add"

    Jeśli urządzenia nie ma na liście, kliknij **Manually add** i wprowadź dane routera. Wszystkie wymagane informacje znajdziesz na spodzie routera lub na stronie GoodCloud w webowym panelu administracyjnym.

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** jest przeznaczone dla użytkowników zarządzających dużą liczbą urządzeń. Możesz zaimportować wiele urządzeń z pliku Microsoft Excel.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### Szczegóły powiązania {#binding-details}

Po pomyślnym powiązaniu zaloguj się ponownie do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **GoodCloud**. Odśwież tę stronę, a zobaczysz powiązaną nazwę użytkownika GoodCloud i datę.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Usuwanie powiązania urządzenia {#unbind-device}

Jeśli chcesz usunąć powiązanie routera, zaloguj się do webowego panelu administracyjnego routera, przejdź do **APPLICATION** -> **GoodCloud** i kliknij **Unbind**. 

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

Możesz też usunąć odpowiednie urządzenie z Bound Devices List na platformie GoodCloud. Webowy panel administracyjny routera zsynchronizuje wtedy najnowszy stan powiązania urządzenia.

W razie trudności napisz na adres [support@glinet.biz](mailto:support@glinet.biz), aby uzyskać pomoc.

### Dla firmware v4.7 lub nowszego {#for-firmware-v47-or-later}

#### Włączanie usługi chmurowej {#enable-cloud-service}

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **CLOUD SERVICE** -> **GoodCloud**. 

Kliknij przycisk **Get Started**, a w prawym górnym rogu pojawi się okno podręczne Cloud Service. Kliknij **Enable**, aby korzystać z Cloud Service.

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

Zaloguj się na konto GoodCloud. 

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

Jeśli nie masz konta, zarejestruj je i zaloguj się. Po zakończeniu rejestracji router zostanie automatycznie powiązany z tym kontem. 

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

Jeśli nie otrzymasz wiadomości weryfikacyjnej, sprawdź folder spam lub odczekaj kilka minut i spróbuj ponownie. W razie problemów z rejestracją napisz na adres [support@glinet.biz](mailto:support@glinet.biz), aby uzyskać pomoc.

#### Szczegóły powiązania {#binding-details_1}

Po pomyślnym powiązaniu zaloguj się ponownie do webowego panelu administracyjnego routera, kliknij ikonę chmury w prawym górnym rogu i zobacz szczegóły powiązania, w tym powiązaną nazwę użytkownika GoodCloud i datę, Device ID, Device MAC oraz Device S/N.

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

W webowym panelu administracyjnym przejdź do **CLOUD SERVICES** -> **GoodCloud**, gdzie możesz włączać lub wyłączać zdalny dostęp do routera.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH**: Umożliwia zdalny dostęp do terminala routera przez GoodCloud.

- **Remote Web Access**: Umożliwia zdalny dostęp do webowego panelu administracyjnego routera przez GoodCloud.

- **View Logs**: Wyświetla logi wywołań API wykonywanych przez GoodCloud.

#### Usuwanie powiązania urządzenia {#unbind-device_1}

Jeśli chcesz usunąć powiązanie routera, zaloguj się do webowego panelu administracyjnego routera. Kliknij ikonę chmury w prawym górnym rogu, a następnie kliknij **Unbind**. 

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

Możesz też usunąć odpowiednie urządzenie z Bound Devices List na platformie GoodCloud. Webowy panel administracyjny routera zsynchronizuje wtedy najnowszy stan powiązania urządzenia.

W razie trudności napisz na adres [support@glinet.biz](mailto:support@glinet.biz), aby uzyskać pomoc.

## Zarządzanie urządzeniami {#manage-devices}

### Informacje o systemie i akcje {#system-info-and-actions}

Na [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** możesz wyświetlić informacje systemowe (np. model, wersję, adres MAC, adres IP) oraz stan (np. online, offline) wszystkich urządzeń powiązanych z kontem.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Po wybraniu urządzenia możesz wykonywać akcje w prawym górnym rogu, takie jak zmiana ustawień, aktualizacja firmware, zdalny dostęp do urządzenia, restart lub reset.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Kliknij ikonę koła zębatego po prawej stronie nagłówka listy, aby dostosować wyświetlane kolumny i ich kolejność zgodnie z informacjami o urządzeniach, które są dla Ciebie najważniejsze.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Szczegóły urządzenia {#device-details}

Na [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** kliknij nazwę urządzenia, a zostaniesz przekierowany na stronę szczegółów urządzenia, gdzie wyświetlane są podstawowe informacje o routerze, dane statystyczne, ustawienia sieci, lista klientów itp. 

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Podstawowe informacje {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statystyki {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Ustawienia sieci {#network-settings}

Na tej stronie wyświetlana jest konfiguracja sieciowa routera i ustawienia Wi-Fi.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Lista klientów {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Zdalny dostęp {#remote-access}

Na [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** kliknij nazwę urządzenia, do którego chcesz uzyskać dostęp, aby wejść na stronę szczegółów. W prawym górnym rogu zobaczysz wtedy akcje zdalne.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

Kliknij **Remote GUI**, aby zdalnie uzyskać dostęp do webowego panelu administracyjnego routera.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Jeśli ta opcja jest wyszarzona lub niedostępna, prawdopodobnie funkcja jest wyłączona. Włącz ją najpierw w webowym panelu administracyjnym routera, zanim spróbujesz uzyskać do niej dostęp przez GoodCloud.

Jeśli tę opcję można kliknąć, ale nie odpowiada, spróbuj użyć trybu incognito/inPrivate w przeglądarce.

### Remote SSH {#remote-ssh}

Kliknij **Remote SSH**, aby zdalnie uzyskać dostęp do terminala routera przez SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Jeśli ta opcja jest wyszarzona lub niedostępna, prawdopodobnie funkcja jest wyłączona. Włącz ją najpierw w webowym panelu administracyjnym routera, zanim spróbujesz uzyskać do niej dostęp przez GoodCloud.

Jeśli tę opcję można kliknąć, ale nie odpowiada, spróbuj użyć trybu incognito/inPrivate w przeglądarce.

## Modyfikacja ustawień {#modify-settings}

Możesz skonfigurować wiele parametrów dla jednego urządzenia lub wielu urządzeń.

Na [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** wybierz urządzenie, które chcesz skonfigurować, a następnie w prawym górnym rogu kliknij **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Tutaj możesz sprawdzić i zmienić ustawienia sieciowe routera, w tym ustawienia sieci bezprzewodowej, Ethernet, zabezpieczeń, przekierowania portów, LAN i systemu.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Alarm e-mail {#email-alarm}

Możesz skonfigurować alarm e-mail, gdy zmieni się stan urządzenia (online/offline) lub gdy połączą się nowi klienci.

Na [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** kliknij przycisk **Add Rule** w prawym górnym rogu.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Wybierz urządzenie, które chcesz monitorować, i kliknij **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Wybierz zdarzenie wyzwalające, takie jak stan online/offline urządzenia, i kliknij **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Sprawdź ustawienia reguły i kliknij **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Na liście Notifications możesz wyświetlić utworzone reguły alertów. Pojedynczy użytkownik może utworzyć tylko jedną regułę alertu. Jeśli potrzebujesz zbiorczego zarządzania urządzeniami, skontaktuj się z nami, aby przejść na wyższy plan.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site {#site-to-site}

Zapoznaj się z dokumentem [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud i VPN {#goodcloud-and-vpn}

Jeśli jednocześnie włączysz **GoodCloud** i **klienta VPN** na routerze, połączenie między routerem a serwerem GoodCloud domyślnie nie będzie przechodzić przez VPN. Zapewnia to bardziej stabilne połączenie z usługami GoodCloud.

Jeśli jednak chcesz, aby połączenie GoodCloud przechodziło przez VPN, możesz zmienić to ustawienie w webowym panelu administracyjnym routera. Przejdź do VPN -> VPN Dashboard -> VPN Client -> Options i włącz opcję "Services from GL.iNet Use VPN".

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Pamiętaj, że kierowanie GoodCloud przez VPN może wpływać na stabilność połączenia z chmurą, zwłaszcza jeśli:

* Połączenie VPN jest niestabilne
* Dostawca VPN filtruje lub blokuje ruch GoodCloud
* VPN znacząco zwiększa opóźnienia połączenia

Zwykle zaleca się pozostawienie ustawień domyślnych, w których GoodCloud omija VPN, aby uzyskać optymalną wydajność i niezawodność.

## Przeglądanie logów {#view-logs}

W razie potrzeby możesz przeglądać logi GoodCloud, w tym Activity Logs, Device Logs, Upgrade Logs, Alert Logs i Device Settings Logs. 

Na [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** wybierz z listy rozwijanej logi, które chcesz wyświetlić.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Wyłączanie chmury {#disable-cloud}

Jeśli nie chcesz już, aby urządzenie było połączone z platformą chmurową, możesz wyłączyć usługę chmurową w webowym panelu administracyjnym routera.

??? "Dla firmware v4.6 lub wcześniejszego"

    Zaloguj się do webowego panelu administracyjnego routera, przejdź do **APPLICATIONS** -> **GoodCloud**, wyłącz przełącznik GoodCloud i kliknij **Apply**

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Po wyłączeniu interfejs będzie wyglądał następująco.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Dla firmware v4.7 lub nowszego"

    Zaloguj się do webowego panelu administracyjnego routera i kliknij ikonę chmury w prawym górnym rogu.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Po wyłączeniu interfejs będzie wyglądał następująco.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Usuwanie konta {#delete-account}

Ze względów bezpieczeństwa możesz usunąć konto, jeśli nie jest już używane. 

Na platformie [GoodCloud](https://www.goodcloud.xyz){target="_blank"} kliknij nazwę użytkownika w prawym górnym rogu i wybierz **Personal Center**. Przewiń na dół strony i kliknij **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Usunięcie konta bezpowrotnie skasuje wszystkie powiązane usługi, dane i informacje osobiste, bez możliwości odzyskania. 
    
    Jeśli Twoje konto należy do jakiejkolwiek organizacji, przed usunięciem konta najpierw opuść wszystkie organizacje.

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
