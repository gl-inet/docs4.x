# Jak zmienić typ NAT w grach {#how-to-change-the-nat-type-on-gaming}

Niektórzy twórcy gier zalecają włączenie UPnP na routerze, aby uzyskać lepszy typ NAT. UPnP wiąże się jednak z potencjalnymi zagrożeniami dla bezpieczeństwa.

Ten sam cel można osiągnąć, konfigurując DMZ lub przekierowanie portów na routerze. Przed włączeniem którejkolwiek z tych funkcji zapoznaj się z jej działaniem i związanymi z nią zagrożeniami dla bezpieczeństwa.

## Sprawdź IP gry {#check-your-game-ip}

Najpierw zaloguj się do routera. Przejdź do listy klientów i sprawdź adres IP przypisany do Twojej gry. Będziesz potrzebować tego adresu IP w dalszej konfiguracji

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Metoda 1 DMZ {#method-1-dmz}

Przejdź do paska bocznego **Network** -> **Port Forwarding** i włącz DMZ z adresem IP gry.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Metoda 2 Przekierowanie portów {#method-2-port-forward}

Przejdź do paska bocznego **Network** -> **Port Forwarding** i dodaj niezbędne porty z adresem IP gry.

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

## Full Cone NAT {#full-cone-nat}

Możesz włączyć Full Cone NAT, aby zmniejszyć opóźnienia. Ta funkcja jest dostępna od firmware v4.5.

Przejdź do **Network** -> **NAT Settings**, w razie potrzeby włącz **Full Cone NAT**, a następnie kliknij **Apply**.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
