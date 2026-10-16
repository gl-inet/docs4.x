# Мережа Mesh {#mesh}

**Примітка**: цю функцію додано у прошивці v4.10.

Mango 2 (GL-MG1300) і Mudi 7 (GL-E5800) не підтримують Mesh навіть із прошивкою v4.10 або новішою. Докладніше див. [підтримувані моделі](#supported-models).

---

У лівому меню вебпанелі адміністрування відкрийте **MESH**.

Mesh — це функція на основі стандарту Wi-Fi EasyMesh™, яка розширює покриття Wi-Fi у всьому домі та забезпечує безперервний роумінг. Якщо у вас кілька маршрутизаторів GL.iNet, налаштуйте один як головний маршрутизатор, а решту — як вузли Mesh для безперервного роумінгу Wi-Fi вдома.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Непідтримувані моделі"
    - GL-MG1300 (Mango 2)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Швидке налаштування {#quick-setup}

У цьому прикладі для створення мережі Mesh використано Flint 3 (GL‑BE9300) і Slate 7 (GL‑BE3600).

**Flint 3** — головний маршрутизатор, який підключається до інтернету та керує всіма вузлами Mesh.

**Slate 7** — вузол Mesh, який розширює покриття Wi-Fi головного маршрутизатора.

1. Увімкніть вузол Mesh і розмістіть його поруч із головним маршрутизатором.

    Під час початкового налаштування тримайте вузол Mesh поруч із головним маршрутизатором для швидкого виявлення. Після завершення налаштування перемістіть його приблизно посередині між головним маршрутизатором і зоною без сигналу Wi-Fi, щоб розширити покриття.

2. Увійдіть у вебпанель адміністрування вузла Mesh та відкрийте **MESH**. Натисніть **Mesh Node**.

    ![Вузол Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Вузол стане доступним для виявлення. До додавання в мережу Mesh він не матиме мережевого з’єднання.

3. Увійдіть у вебпанель адміністрування головного маршрутизатора та відкрийте **INTERNET**. Підключіть його до інтернету будь-яким підтримуваним способом: Ethernet, ретранслятор, спільний доступ до інтернету через USB або стільниковий зв’язок.

4. Після налаштування інтернету відкрийте **MESH** і натисніть **Main Router**.

    ![Головний маршрутизатор](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. На сторінці наведено два способи додавання вузлів Mesh: Wi-Fi Scan та Ethernet Backhaul.

    ![Додавання вузла Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Виберіть відповідну інструкцію нижче, щоб додати вузли Mesh.

    ??? note "Wi-Fi Scan"

        Натисніть **Start Scanning**.

        ![Початок пошуку вузлів](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Розпочнеться пошук сусідніх вузлів Mesh через Wi-Fi. Виберіть пристрої для додавання та натисніть **Add**.

        ![Вибір вузлів після пошуку Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Вузол Mesh буде додано до вашої мережі Mesh. Натисніть **Finish**.

        ![Вузол додано до мережі Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Підключіть порт WAN вузла Mesh до порту LAN головного маршрутизатора кабелем Ethernet. Мережа з магістральним з’єднанням Ethernet буде налаштована автоматично.

        ![Магістральне з’єднання Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Після додавання вузла Mesh у вебпанелі адміністрування головного маршрутизатора з’явиться схема мережі.

    ![Схема мережі головного маршрутизатора](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Керування вузлами {#manage-nodes}

Після завершення налаштування вузол Mesh більше не буде доступний за початковою IP-адресою. Керуйте головним маршрутизатором і всіма вузлами Mesh через вебпанель адміністрування головного маршрутизатора.

### Перегляд відомостей про вузол {#view-node-details}

У вебпанелі адміністрування головного маршрутизатора відкрийте **MESH** і натисніть **Main Router** на схемі мережі.

![Відомості про головний маршрутизатор](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Відобразяться відомості про головний маршрутизатор: модель, IP-адреса та MAC-адреса, час роботи й підключені клієнти.

![Відомості про головний маршрутизатор](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Натисніть **Mesh Node** на схемі мережі.

![Відомості про вузол Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Відобразяться відомості про вузол Mesh: модель, IP-адреса та MAC-адреса, версія прошивки, час роботи й підключені клієнти.

![Відомості про вузол Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Редагування вузла Mesh {#edit-mesh-node}

У вебпанелі адміністрування головного маршрутизатора відкрийте **MESH** і натисніть **Mesh Node** на схемі мережі.

![Відомості про вузол Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

За замовчуванням назва кожного вузла Mesh складається з «Node» та останніх чотирьох цифр його MAC-адреси. Натисніть піктограму редагування, щоб перейменувати вузол Mesh.

![Редагування назви вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![Нова назва вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Доступ до вузла Mesh {#access-mesh-node}

У вебпанелі адміністрування головного маршрутизатора відкрийте **MESH** і натисніть **Mesh Node** на схемі мережі.

![Відомості про вузол Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Натисніть піктограму шестерні у верхньому правому куті та виберіть **Open Admin Panel**.

![Дії з вузлом Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Відкриється сторінка входу вузла Mesh за IP-адресою, призначеною головним маршрутизатором. Тепер увійдіть у вебпанель вузла Mesh.

![Вхід у вебпанель вузла Mesh](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Додавання інших вузлів {#add-more-nodes}

За потреби натисніть **Add** у верхньому правому куті схеми мережі, щоб додати інші вузли.

![Додавання інших вузлів](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
