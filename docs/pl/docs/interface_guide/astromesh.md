# AstroMesh

> Ta funkcja została wprowadzona w firmware v4.10.

AstroMesh to autorska globalna technologia mesh GL.iNet, łącząca EasyMesh i AstroWarp. W przeciwieństwie do typowych bezprzewodowych systemów mesh działających tylko w jednej sieci lokalnej, AstroMesh usuwa ograniczenia geograficzne i pozwala łączyć się z siecią domową z dowolnego miejsca.

W domu router podróżny działa jako zwykły Mesh Node, rozszerzając zasięg Wi-Fi z płynnym roamingiem. Poza domem może automatycznie przełączyć się w tryb Astro Node i zsynchronizować przez chmurę ustawienia domowego Wi-Fi, umożliwiając zdalny dostęp do urządzeń LAN oraz kierowanie ruchu przez wyjście sieci domowej. Dzięki działaniu plug-and-play bez skomplikowanej konfiguracji AstroMesh zapewnia płynne korzystanie z Internetu zarówno w domu, jak i w podróży.

## Szybka konfiguracja

W tym przykładzie do utworzenia sieci AstroMesh używane są Flint 3 (GL-BE9300) i Slate 7 (GL-BE3600).

- **Flint 3**: Main Node, brama internetowa, menedżer Mesh Nodes oraz wyjście sieciowe dla zdalnych Astro Nodes.
- **Slate 7**: Mesh Node do lokalnego rozszerzenia zasięgu EasyMesh lub zdalnego rozszerzenia przez AstroWarp.

Wykonaj poniższe kroki, aby zakończyć konfigurację.

1. Zaloguj się do Web Admin Panel urządzenia Flint 3 i przejdź do **INTERNET**. Połącz je z Internetem przez Ethernet, Repeater, Tethering lub Cellular.
2. Przejdź do **ASTROMESH** i kliknij **Main Node**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Dodaj węzły przez **Wi-Fi Scan** lub **Pairing Code**.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    ??? note "Wi-Fi Scan"

        Przed skanowaniem upewnij się, że:

        1. Dodawany router jest włączony i znajduje się blisko głównego routera.
        2. Dodawany router ma włączone AstroMesh i działa w trybie **Mesh Node**.
        ---

        Kliknij **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        W oknie podręcznym kliknij **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        Router wyszuka pobliskie Mesh Nodes przez Wi-Fi.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Wybierz węzeł i kliknij **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Mesh Node zostanie dodany do AstroMesh. Kliknij **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Uwaga**: Po połączeniu ten Mesh Node nie będzie już dostępny pod pierwotnym adresem IP. Użyj nowego adresu IP przypisanego przez Main Node i zarządzaj wszystkimi węzłami z Admin Panel urządzenia Main Node. Zobacz [tutaj](#manage-nodes).

    ??? note "Pairing Code"

        Kliknij **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Skopiuj kod parowania wygenerowany przez Main Node.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Zaloguj się do Web Admin Panel urządzenia Slate 7, przejdź do **AstroMesh** i kliknij **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Wprowadź kod parowania i kliknij **Apply**.

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Mesh Node rozpocznie łączenie z Main Node. Kliknij **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Uwaga**: Po połączeniu ten Mesh Node nie będzie już dostępny pod pierwotnym adresem IP. Użyj nowego adresu IP przypisanego przez Main Node i zarządzaj wszystkimi węzłami z Admin Panel urządzenia Main Node. Zobacz [tutaj](#manage-nodes).

4. Po dodaniu węzła do sieci AstroMesh Admin Panel urządzenia Main Node pokaże topologię sieci, jak poniżej.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    Admin Panel urządzenia Mesh Node również pokaże stan połączenia, jak poniżej.

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **Uwaga**: Po dodaniu do sieci AstroMesh Mesh Node nie będzie już dostępny pod pierwotnym adresem IP. Aby uzyskać do niego ponowny dostęp, użyj nowego adresu IP otrzymanego z Main Node. Zarządzaj wszystkimi węzłami z Admin Panel urządzenia Main Node. Zobacz [tutaj](#manage-nodes).

5. Gdy zabierzesz Mesh Node poza dom, automatycznie przełączy się w tryb Astro Node.

## Zarządzanie węzłami {#manage-nodes}

Zarządzaj AstroMesh z Admin Panel urządzenia Main Node.

### Wyświetlanie informacji o węźle

Kliknij **Main Node** w topologii AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Możesz wyświetlić szczegóły Main Node, w tym model, adres IP i MAC, czas pracy oraz połączonych klientów.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Kliknij **Mesh Node** w topologii AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Możesz wyświetlić szczegóły Mesh Node, w tym model, adres IP i MAC, wersję firmware, czas pracy oraz połączonych klientów.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Edycja Mesh Node

Kliknij **Mesh Node** w topologii AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Domyślnie każdy Mesh Node ma nazwę "Node" oraz ostatnie cztery cyfry adresu MAC. Kliknij ikonę edycji, aby zmienić nazwę.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Dostęp do Mesh Node

Kliknij **Mesh Node** w topologii AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Nastąpi przekierowanie na stronę logowania Mesh Node. Wprowadź hasło administratora, aby uzyskać dostęp do jego Admin Panel pod adresem IP przypisanym przez Main Node.

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
