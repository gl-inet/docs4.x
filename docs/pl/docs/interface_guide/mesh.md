# Mesh

**Uwaga**: ta funkcja została wprowadzona w oprogramowaniu sprzętowym v4.10.

---

W panelu administracyjnym po lewej stronie przejdź do **MESH**.

Mesh to funkcja oparta na standardzie Wi-Fi EasyMesh™, która rozszerza zasięg Wi‑Fi w całym domu i umożliwia płynny roaming. Jeśli masz kilka routerów GL.iNet, ustaw jeden jako router główny, a pozostałe jako węzły Mesh.

Poniższy przykład wykorzystuje Flint 3 (GL‑BE9300) i Slate 7 (GL‑BE3600) do utworzenia sieci Mesh.

- **Flint 3** jest routerem głównym, który łączy się z Internetem i zarządza wszystkimi węzłami Mesh.
- **Slate 7** jest węzłem Mesh rozszerzającym zasięg Wi-Fi routera głównego.

## Szybka konfiguracja

1. Włącz węzeł Mesh i umieść go w pobliżu routera głównego.

    Podczas pierwszej konfiguracji ustaw węzeł obok routera głównego, aby przyspieszyć skanowanie. Po konfiguracji możesz przenieść go w połowę odległości między routerem a obszarem bez zasięgu Wi-Fi.

2. Zaloguj się do panelu administracyjnego węzła Mesh, przejdź do **MESH** i kliknij **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Węzeł stanie się wykrywalny. Do czasu dodania do sieci Mesh nie będzie miał połączenia sieciowego.

3. Zaloguj się do panelu routera głównego i przejdź do **INTERNET**. Połącz go z Internetem przez Ethernet, Repeater, Tethering lub Cellular.

4. Po skonfigurowaniu Internetu przejdź do **MESH** i kliknij **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. Strona przedstawia dwie metody dodawania węzłów: Wi-Fi Scan i Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Wybierz odpowiednią instrukcję.

    ??? note "Wi-Fi Scan"

        Kliknij **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Router rozpocznie wyszukiwanie pobliskich węzłów Mesh przez Wi-Fi. Wybierz urządzenia i kliknij **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Węzeł zostanie dodany do sieci Mesh. Kliknij **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Połącz port WAN węzła Mesh z portem LAN routera głównego kablem Ethernet. Sieć Ethernet Backhaul zostanie skonfigurowana automatycznie.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Po dodaniu węzła topologia pojawi się w panelu routera głównego.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Zarządzanie węzłami

Po zakończeniu konfiguracji węzeł Mesh nie będzie dostępny pod pierwotnym adresem IP. Routerem głównym i wszystkimi węzłami można zarządzać z panelu routera głównego.

### Wyświetlanie szczegółów węzła

W panelu routera głównego przejdź do **MESH** i kliknij **Main Router** w topologii.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Można sprawdzić model, adresy IP i MAC, czas działania oraz podłączone urządzenia.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Kliknij **Mesh Node** w topologii.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Można sprawdzić model, adresy IP i MAC, wersję oprogramowania, czas działania i podłączone urządzenia węzła.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Edytowanie węzła Mesh

W panelu routera głównego przejdź do **MESH** i kliknij **Mesh Node** w topologii.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Domyślna nazwa każdego węzła to „Node” i cztery ostatnie cyfry adresu MAC. Kliknij ikonę edycji, aby zmienić nazwę.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Dostęp do węzła Mesh

W panelu routera głównego przejdź do **MESH** i kliknij **Mesh Node** w topologii.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Nastąpi przekierowanie do strony logowania węzła pod adresem IP przydzielonym przez router główny.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Dodawanie kolejnych węzłów

W razie potrzeby kliknij **Add** w prawym górnym rogu topologii.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
