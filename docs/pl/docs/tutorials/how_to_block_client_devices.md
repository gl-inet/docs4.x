# Jak blokować określone urządzenia klienckie na routerze GL.iNet

Ten samouczek pokazuje, jak blokować określone urządzenia klienckie na routerze GL.iNet. Blokując urządzenia klienckie, zapobiegasz nieautoryzowanemu dostępowi do swojej sieci. Pomaga to zwiększyć bezpieczeństwo sieci lub kontrolować dostęp domowników do internetu.

Routery GL.iNet blokują urządzenia klienckie na podstawie ich adresów MAC (unikalnych 12-znakowych identyfikatorów przypisanych poszczególnym urządzeniom w sieci). Ta metoda jest również nazywana filtrowaniem adresów MAC. 

Istnieją dwie metody blokowania urządzeń klienckich na routerze GL.iNet: przez [panel administracyjny routera](#block-client-devices-via-the-admin-panel) lub [aplikację mobilną GL.iNet](#block-client-devices-via-the-glinet-mobile-app). 

## Blokowanie urządzeń klienckich przez panel administracyjny {#block-client-devices-via-the-admin-panel}

### 1. Zaloguj się do panelu administracyjnego

W przeglądarce internetowej wpisz `192.168.8.1`. Wprowadź hasło, a następnie kliknij **Login**. 

### 2. Zablokuj urządzenia klienckie

Istnieją dwa sposoby blokowania urządzeń klienckich, w zależności od tego, czy znasz ich adresy MAC:

* Jeśli nie znasz ich adresów MAC: skorzystaj z [pierwszej metody](#method-1-block-devices-without-their-mac-addresses), która pozwala zablokować urządzenia widoczne na listach.
* Jeśli znasz ich adresy MAC: skorzystaj z [drugiej metody](#method-2-block-devices-with-their-mac-addresses). 

#### Metoda 1: Blokowanie urządzeń bez ich adresów MAC {#method-1-block-devices-without-their-mac-addresses}

1. Na lewym pasku bocznym kliknij **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Przy danym urządzeniu przestaw przełącznik do pozycji włączonej. 
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Jeśli na listach nie widać urządzeń, które chcesz zablokować, trzeba je zablokować przez [dodanie ich adresów MAC do listy blokowanych](#method-2-block-devices-with-their-mac-addresses). 

#### Metoda 2: Blokowanie urządzeń z użyciem ich adresów MAC {#method-2-block-devices-with-their-mac-addresses}

Aby skorzystać z tej metody, musisz uzyskać adres MAC urządzenia. Skorzystaj z instrukcji udostępnionych przez producenta urządzenia. 
Po uzyskaniu adresu MAC urządzenia wykonaj poniższe kroki: 

1. Na lewym pasku bocznym kliknij **Clients**.
2. U góry kliknij **Blocklist**. 
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Zablokuj urządzenia jedną z poniższych metod: 
    - Aby wprowadzić adresy MAC pojedynczo: wpisz je w pustym polu.
    - Aby zaimportować listę adresów MAC: kliknij **Import Clients**. Zaimportuj plik, a następnie kliknij **Import**. 
4. Kliknij **Apply**. 
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Blokowanie urządzeń klienckich przez aplikację mobilną GL.iNet {#block-client-devices-via-the-glinet-mobile-app}

**Uwaga:** Przed rozpoczęciem zainstaluj i skonfiguruj aplikację mobilną GL.iNet na swoim urządzeniu. 

Istnieją dwa sposoby blokowania urządzeń klienckich, w zależności od tego, czy znasz ich adresy MAC:

* Jeśli nie znasz ich adresów MAC: skorzystaj z [pierwszej metody](#mobile-1), która pozwala zablokować urządzenia widoczne na liście. 
* Jeśli znasz ich adresy MAC: skorzystaj z [drugiej metody](#mobile-2). 

### Metoda 1: Blokowanie urządzeń bez ich adresów MAC {#mobile-1}

1. Na ekranie głównym aplikacji dotknij urządzenia, które chcesz zablokować, w sekcji **Connected Clients** lub **Office Clients**. 
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. W sekcji **Settings** przestaw przełącznik **Block** do pozycji włączonej. 
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Jeśli na listach nie widać urządzeń, które chcesz zablokować, trzeba je zablokować przez [dodanie ich adresów MAC do listy blokowanych](#mobile-2)

### Metoda 2: Blokowanie urządzeń z użyciem ich adresów MAC {#mobile-2}

Aby skorzystać z tej metody, musisz uzyskać adres MAC urządzenia, które chcesz zablokować. Skorzystaj z instrukcji udostępnionych przez producenta. 
Po uzyskaniu adresu MAC urządzenia wykonaj poniższe kroki: 

1. Na ekranie głównym aplikacji dotknij ikony Settings > **Access Control**. 
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Dotknij **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Zablokuj urządzenia jedną z poniższych metod: 
    - Aby wprowadzić adresy MAC pojedynczo: dotknij **Add MAC address**. Wprowadź adres MAC, a następnie dotknij **Done**.  
    - Aby zaimportować listę adresów MAC, kliknij **Import Clients** > **Import Clients**. Dotknij pliku.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

