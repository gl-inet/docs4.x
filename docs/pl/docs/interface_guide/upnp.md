# UPnP {#upnp}

**Uwaga**: Ta funkcja została wprowadzona w firmware v4.11.

---

W menu po lewej stronie panelu administracyjnego przejdź do **SECURITY** -> **UPnP**.

UPnP (Universal Plug and Play) pozwala zgodnym urządzeniom LAN i aplikacjom automatycznie żądać mapowania portów na routerach GL.iNet. Mapowania przekierowują przychodzący ruch WAN na określone adresy IP i porty LAN, umożliwiając klientom zewnętrznym łączenie się z usługami lokalnymi bez ręcznej konfiguracji reguł przekierowania portów.

UPnP różni się od [przekierowania portów](./port_forwarding.md) i [DMZ](./port_forwarding.md#dmz): UPnP tworzy mapowania automatycznie na żądanie urządzeń. Przekierowanie portów udostępnia wybrane porty, a DMZ udostępnia wszystkie porty hosta LAN. Zarówno przekierowanie portów, jak i DMZ wymagają ręcznej konfiguracji. Przed włączeniem tych funkcji upewnij się, że rozumiesz ich działanie oraz związane z nimi zagrożenia bezpieczeństwa.

**Uwaga**: 

1. Gdy UPnP jest włączone, zgodne urządzenia LAN i aplikacje mogą żądać mapowania portów bez zatwierdzania każdego żądania.

2. Przejęte urządzenie lub złośliwa aplikacja może użyć UPnP do udostępnienia usług lokalnych w Internecie. Włączaj UPnP tylko w zaufanych sieciach i wyłączaj je, gdy nie jest potrzebne.

3. UPnP wymaga publicznego adresu IP na interfejsie WAN routera, aby przyjmować połączenia przychodzące z Internetu. Nie będzie działać, jeśli dostawca Internetu używa CGNAT.

Typowe zastosowania UPnP obejmują:

- **Gry online**: zgodne gry i konsole (np. gry wieloosobowe Steam, Xbox Series X|S, PlayStation 5, Nintendo Switch) mogą automatycznie tworzyć mapowania portów, aby ułatwić nawiązywanie połączeń z innymi graczami.

- **Udostępnianie plików peer-to-peer**: klienci BitTorrent i inne zgodne aplikacje P2P mogą automatycznie mapować porty nasłuchu, aby przyjmować połączenia przychodzące od innych uczestników.

- **Dostęp zdalny**: urządzenia i aplikacje obsługujące mapowanie portów UPnP, takie jak niektóre urządzenia NAS, kamery IP i serwery multimedialne, mogą automatycznie konfigurować mapowania zapewniające dostęp spoza sieci lokalnej.

## Szybka konfiguracja {#quick-setup}

Włącz UPnP za pomocą przełącznika. Zgodne urządzenia i aplikacje mogą następnie żądać mapowania portów w razie potrzeby, jak w poniższym przykładzie.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- **Client / Application**: opis klienta lub aplikacji oraz adres IP LAN urządzenia wysyłającego żądanie.

- **Protocol**: protokół transportowy mapowania, np. `TCP` lub `UDP`.

- **External Port**: port WAN dla połączeń przychodzących.

- **Internal Target**: docelowy adres IP LAN i port.

- **Lease**: czas pozostały do wygaśnięcia mapowania. Domyślna długość dzierżawy wynosi 7 dni.

- **Action**: kliknij ikonę kosza, aby usunąć mapowanie. Klient lub aplikacja może zażądać go ponownie, jeśli nadal działa.

Aktywne mapowania portów są usuwane, gdy klient je zwolni lub gdy wygasną ich dzierżawy. Kliknij **Refresh**, aby wyświetlić najnowsze mapowania portów.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
