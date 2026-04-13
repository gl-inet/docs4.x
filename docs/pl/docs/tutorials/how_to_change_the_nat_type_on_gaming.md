# Jak zmienić typ NAT w grach

Większość producentów gier zaleca włączenie UPnP na routerze, aby uzyskać lepszy typ NAT, jednak badania pokazują, że UPnP jest niebezpiecznym protokołem.

Możesz osiągnąć ten sam cel w bezpieczniejszy sposób, używając funkcji DMZ lub przekierowania portów.

## Sprawdź IP gry

Przejdź do listy klientów i sprawdź adres IP przypisany do Twojej gry. Będziesz potrzebować tego adresu IP w dalszej konfiguracji

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Metoda 1 DMZ

Przejdź do paska bocznego **Network > Port Forwarding** i włącz DMZ z adresem IP gry.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Metoda 2 Przekierowanie portów

Przejdź do paska bocznego **Network > Port Forwarding** i dodaj niezbędne porty z adresem IP gry.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Przykład: Porty dla PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480


![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Porty Xbox

UDP 88, 3074

TCP 3074

Niektóre gry mogą wymagać przekierowania innych portów, więcej szczegółów znajdziesz na tej stronie.

[Przekierowanie portów w różnych grach](https://portforward.com/games/)

## Full Cone NAT

Możesz włączyć Full Cone NAT w **Network > NAT Settings**, aby poprawić opóźnienia.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* Ta funkcja jest dostępna w firmware 4.5 lub nowszym.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
