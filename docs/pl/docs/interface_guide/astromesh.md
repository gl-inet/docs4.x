# AstroMesh

> Ta funkcja została wprowadzona w firmware v4.10.

AstroMesh to autorska globalna technologia mesh GL.iNet, łącząca EasyMesh i AstroWarp. W przeciwieństwie do typowych bezprzewodowych systemów mesh działających tylko w jednej sieci lokalnej, AstroMesh usuwa ograniczenia geograficzne i pozwala łączyć się z siecią domową z dowolnego miejsca.

W domu router podróżny działa jako zwykły Mesh Node, rozszerzając zasięg Wi-Fi z płynnym roamingiem. Poza domem może automatycznie przełączyć się w tryb Astro Node i zsynchronizować przez chmurę ustawienia domowego Wi-Fi, umożliwiając zdalny dostęp do urządzeń LAN oraz kierowanie ruchu przez wyjście sieci domowej. Dzięki działaniu plug-and-play bez skomplikowanej konfiguracji AstroMesh zapewnia płynne korzystanie z Internetu zarówno w domu, jak i w podróży.

## Szybka konfiguracja

W tym przykładzie do utworzenia sieci AstroMesh używane są Flint 3 (GL-BE9300) i Slate 7 (GL-BE3600).

- **Flint 3**: działa jako Main Router, łączy się z Internetem i zarządza wszystkimi Mesh Nodes. Pełni także rolę wyjścia sieciowego dla wszystkich zdalnych Astro Nodes.
- **Slate 7**: działa jako Mesh Node, który lokalnie rozszerza zasięg Wi-Fi Main Router przez EasyMesh albo rozszerza sieć domową do zdalnych lokalizacji przez AstroWarp.

Wykonaj poniższe kroki, aby zakończyć konfigurację.

1. Zaloguj się do Web Admin Panel urządzenia Flint 3 i przejdź do **INTERNET**. Połącz je z Internetem przez dowolny obsługiwany typ połączenia: Ethernet, Repeater, Tethering albo Cellular.

2. Przejdź do **ASTROMESH** i kliknij **Main Router**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Dodaj węzły przez **Wi-Fi Scan** lub **Pairing Code**.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    Zapoznaj się z odpowiednimi instrukcjami poniżej.

    ??? note "Wi-Fi Scan"

        Przed skanowaniem upewnij się, że:

        1. Dodawany router jest włączony i znajduje się blisko głównego routera.
        2. Dodawany router ma włączone AstroMesh i działa w trybie **Mesh Node**.
        ---

        Kliknij **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        W oknie podręcznym kliknij **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        Rozpocznie się skanowanie pobliskich Mesh Nodes przez Wi-Fi.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Wybierz węzeł i kliknij **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Mesh Node zostanie dodany do sieci AstroMesh. Kliknij **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Uwaga**: Gdy węzeł dołączy do sieci AstroMesh, nie będzie już dostępny pod pierwotnym adresem IP. Wszystkimi węzłami można zarządzać z Admin Panel urządzenia Main Router. Szczegóły znajdziesz w sekcji [Zarządzanie Mesh Nodes](#manage-mesh-nodes).

    ??? note "Pairing Code"

        Kliknij **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Main Router wygeneruje kod parowania. Skopiuj ten kod.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Zaloguj się do Web Admin Panel urządzenia Slate 7, przejdź do **ASTROMESH** i kliknij **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Wprowadź skopiowany kod parowania i kliknij **Apply**. *Kod parowania jest ograniczony czasowo. Wprowadź go przed wygaśnięciem.*

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Mesh Node rozpocznie łączenie z Main Router. Kliknij **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Uwaga**: Gdy węzeł dołączy do sieci AstroMesh, nie będzie już dostępny pod pierwotnym adresem IP. Wszystkimi węzłami można zarządzać z Admin Panel urządzenia Main Router. Szczegóły znajdziesz w sekcji [Zarządzanie Mesh Nodes](#manage-mesh-nodes).

4. Po pomyślnym dodaniu węzłów do AstroMesh w Admin Panel urządzenia Main Router pojawi się topologia, jak poniżej.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Zarządzanie Mesh Nodes {#manage-mesh-nodes}

Zarządzaj Mesh Nodes z Admin Panel urządzenia Main Router.

### Wyświetlanie informacji o węźle

W Admin Panel urządzenia Main Router przejdź do **ASTROMESH** i kliknij **Main Router** w topologii AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Możesz wyświetlić szczegóły Main Router, w tym model, adres IP i MAC, czas pracy oraz połączonych klientów.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Kliknij **Mesh Node** w topologii AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Możesz wyświetlić szczegóły Mesh Node, w tym model, adres IP i MAC, wersję firmware, czas pracy oraz połączonych klientów.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Edycja Mesh Node

W Admin Panel urządzenia Main Router przejdź do **ASTROMESH** i kliknij **Mesh Node** w topologii AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Domyślnie każdy Mesh Node ma nazwę "Node" oraz ostatnie cztery cyfry adresu MAC. Kliknij ikonę edycji, aby zmienić nazwę Mesh Node.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Dostęp do Mesh Node

W Admin Panel urządzenia Main Router przejdź do **ASTROMESH** i kliknij **Mesh Node** w topologii AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Nastąpi przekierowanie na stronę logowania Mesh Node pod adresem IP przypisanym przez Main Router. Wprowadź hasło administratora, aby się zalogować.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

Po zalogowaniu przejdź do **ASTROMESH**, aby wyświetlić stan połączenia.

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### Dodawanie kolejnych węzłów

Aby dodać więcej węzłów, kliknij **Add** w prawym górnym rogu topologii AstroMesh.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Zarządzanie Astro Nodes

Gdy przeniesiesz Mesh Node poza sieć domową, automatycznie przełączy się w tryb **Astro Node**.

Na przykład zabierz Slate 7 do innej lokalizacji. Włącz go i wybierz tryb **Mesh Node** Mode na ekranie dotykowym.

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

Urządzenie wykryje bieżące środowisko sieciowe, automatycznie przełączy się w tryb **Astro Node** i rozpocznie połączenie.

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

Po połączeniu pokaże pierwotny adres IP, którego można użyć do uzyskania dostępu do jego Web Admin Panel.

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

Użyj tego adresu IP, aby zalogować się do Astro Node.

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

Po zalogowaniu przejdź do **ASTROMESH**, aby wyświetlić stan połączenia. Domyślny tryb połączenia to **Exit Node Mode**. W razie potrzeby możesz przełączyć na **Traffic Split Mode**.

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode**: W tym trybie cały ruch z Astro Node jest kierowany przez sieć domową w celu dostępu do internetu. Publiczny adres IP Astro Node będzie taki sam jak publiczny adres IP sieci domowej.

- **Traffic Split Mode**: W tym trybie tylko ruch kierowany do sieci domowej jest przekazywany z powrotem do Main Router, a pozostały ruch internetowy przechodzi bezpośrednio przez lokalny WAN Astro Node. Upewnij się, że Astro Node jest połączony z lokalną siecią internetową.

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
