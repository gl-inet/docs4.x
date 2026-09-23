# Filtr treści

**Uwaga**: Ta funkcja została wprowadzona w firmware v4.9.

Niektóre modele, takie jak Mango 2 (GL-MG1300), nie obsługują Content Filter ze względu na zbyt małą ilość pamięci, nawet z firmware v4.9 lub nowszym. Szczegółowe informacje znajdują się w sekcji [Obsługiwane modele](#supported-models).

---

Filtr treści to inteligentna funkcja bezpieczeństwa online oparta na klasyfikacji DPI. Automatycznie blokuje szkodliwe i złośliwe strony internetowe, pomagając utrzymać sieć w czystości i bezpieczeństwie, a także obsługuje własne reguły blokowania określonych aplikacji, domen lub adresów IP.

**Uwaga**:

1. Filtr treści nie działa, gdy router pracuje w trybie Drop-in Gateway.
2. Filtr treści nie współpracuje z funkcją Network Acceleration. Włączenie filtra treści automatycznie wyłączy Network Acceleration, aby zapewnić stabilną wydajność.

## Obsługiwane modele {#supported-models}

??? "Obsługiwane modele"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Nieobsługiwane modele"
    - GL-MG1300 (Mango 2)
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

## Szybka konfiguracja

W lewym panelu webowego panelu administracyjnego przejdź do **FLOW CONTROL** -> **Content Filter**.

Włącz przełącznik w prawym górnym rogu, dostosuj blokowane treści (np. aplikacje, domeny lub adresy IP), a następnie kliknij **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Ta strona składa się z dwóch części:

- **Blocked Apps List**: ta sekcja zawiera trzy wstępnie wybrane kategorie: Gambling, Adult i Malware. Po ich włączeniu wszystkie strony internetowe, usługi i aplikacje należące do tych trzech kategorii zostaną zablokowane.

    Możesz także kliknąć **Edit App**, aby dodać więcej kategorii (np. Game, Social Media) zgodnie z potrzebami.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    W wyskakującym oknie wybierz kategorie, które chcesz blokować. Domyślne trzy kategorie są puste; wszystkie pozostałe kategorie zawierają listę aplikacji.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Kliknij dowolną kategorię, aby wyświetlić i wybrać aplikacje do zablokowania, albo kliknij **Select All** w prawym górnym rogu, aby zablokować wszystkie aplikacje z tej kategorii jednocześnie, a następnie kliknij **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

    Następnie wybrane aplikacje pojawią się na liście **Blocked App List**.

- **Blocked Domain / IP List**: ta sekcja umożliwia ręczne wpisanie konkretnych domen (np. `google.com`), zakresów CIDR (np. `192.168.8.0/24`) lub adresów IP (np. `192.168.10.10`) w celu zablokowania dostępu do nich. Lista obsługuje maksymalnie 10000 wpisów.

    Wprowadź domeny lub adresy IP, które chcesz zablokować, a następnie kliknij **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Test filtra treści

Na przykład wybraliśmy kategorię **Game**, która zawiera Nintendo.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

Na laptopie podłączonym do routera strona `nintendo.com` nie jest już dostępna, mimo że przed włączeniem filtra treści była osiągalna.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

W webowym panelu administracyjnym routera możesz sprawdzić liczbę zablokowanych żądań dostępu.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
