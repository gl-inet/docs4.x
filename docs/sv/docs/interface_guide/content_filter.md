# Content Filter {#content-filter}

**Note**: This feature was introduced in firmware v4.9.

Vissa modeller, till exempel Mango 2 (GL-MG1300), stöder inte Content Filter på grund av otillräckligt minne, även med firmware v4.9 eller senare. Mer information finns i [Supported Models](#supported-models).

---

Content Filter är en intelligent funktion för säkerhet online som bygger på DPI-klassificering. Den blockerar automatiskt skadliga webbplatser för att hålla nätverket rent och säkert och stöder anpassade regler för att blockera vissa program, domäner eller IP-adresser.

**Note**:

1. Content Filter får ingen effekt när routern är i Drop-in Gateway-läge.
2. Content Filter cannot work with Network Acceleration. Enabling Content Filter will automatically disable Network Acceleration to ensure stable performance.

## Supported Models {#supported-models}

??? "Supported Models"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Unsupported Models"
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

## Quick Setup {#quick-setup}

Öppna **FLOW CONTROL** -> **Content Filter** på vänster sida i webbadministrationspanelen.

Aktivera reglaget i det övre högra hörnet, anpassa blockerat innehåll (t.ex. program, domäner eller IP-adresser) och klicka sedan på **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Sidan består av två delar:

- **Blocked Apps List**: Avsnittet innehåller tre förvalda kategorier: Gambling, Adult och Malware. När de är aktiverade blockeras webbplatser, tjänster och program som hör till kategorierna.

    Du kan även klicka på **Edit App** för att lägga till fler kategorier, till exempel Game och Social Media.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    Välj kategorierna som du vill blockera i popup-fönstret. De tre standardkategorierna är tomma; alla andra kategorier innehåller en lista över program.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Klicka på en kategori för att visa och välja programmen som ska blockeras, eller klicka på **Select All** uppe till höger för att blockera alla program i kategorin. Klicka sedan på **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    De valda programmen visas sedan i Blocked App List.

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

- **Blocked Domain / IP List**: I avsnittet kan du manuellt ange vissa domäner (t.ex. google.com), CIDR-intervall (t.ex. 192.168.8.0/24) eller IP-adresser (t.ex. 192.168.10.10) som ska blockeras. Listan stöder upp till 10000 poster.

    Ange domänerna eller IP-adresserna som ska blockeras och klicka sedan på **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Content Filter Test {#content-filter-test}

I följande exempel har kategorin **Game**, som innehåller Nintendo, valts.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

På en bärbar dator som är ansluten till routern går det inte längre att öppna `nintendo.com`, även om webbplatsen kunde öppnas innan Content Filter aktiverades.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

I routerns webbadministrationspanel kan du se antalet blockerade åtkomstförfrågningar.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
