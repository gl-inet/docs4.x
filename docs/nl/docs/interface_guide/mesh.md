# Mesh {#mesh}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.10.

Mango 2 (GL-MG1300) en Mudi 7 (GL-E5800) ondersteunen Mesh niet, ook niet met firmware v4.10 of hoger. Raadpleeg [Ondersteunde modellen](#supported-models).

---

Ga links in het webbeheerpaneel naar **MESH**.

Mesh is gebaseerd op Wi-Fi EasyMesh™ en vergroot de Wi-Fi-dekking in huis met naadloos roamen. Stel bij meerdere GL.iNet-routers één apparaat als hoofdrouter in en de overige als mesh-nodes.

Weet je niet welke modus je moet kiezen? Raadpleeg [Mesh versus Extender versus Access Point](#mesh-vs-extender-vs-access-point-mode).

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - ※GL-BE14000 (Flint 4)
    - ※GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

    **Opmerking**: modellen met ※ ondersteunen Mesh in bètafirmware.

??? "Niet-ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
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

## Snelle installatie {#quick-setup}

In het volgende voorbeeld maken Flint 3 (GL‑BE9300) en Slate 7 (GL‑BE3600) een Mesh-netwerk.

**Flint 3** is de hoofdrouter die verbinding maakt met internet en alle Mesh-nodes beheert.

**Slate 7** is de Mesh-node die de Wi-Fi-dekking van de hoofdrouter vergroot.

1. Schakel de Mesh-node in en plaats deze bij de hoofdrouter.

    Houd de Mesh-node tijdens de eerste installatie naast de hoofdrouter voor snel scannen. Plaats deze daarna halverwege de hoofdrouter en de zone zonder dekking.

2. Meld je aan bij het webbeheerpaneel van de Mesh-node, ga naar **MESH** en klik op **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    De node wordt vindbaar en heeft vóór toevoeging aan het Mesh-netwerk geen netwerkverbinding.

3. Meld je aan bij het webbeheerpaneel van de hoofdrouter, ga naar **INTERNET** en verbind via Ethernet, Repeater, Tethering of Cellular.

4. Ga na de internetconfiguratie naar **MESH** en klik op **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. De pagina toont twee manieren om Mesh-nodes toe te voegen: Wi-Fi Scan en Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Selecteer hieronder de bijbehorende instructies.

    ??? note "Wi-Fi Scan"

        Klik op **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Er wordt via Wi-Fi naar Mesh-nodes in de buurt gescand. Selecteer de apparaten en klik op **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        De Mesh-node wordt aan het netwerk toegevoegd. Klik op **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Sluit de WAN-poort van de Mesh-node met een Ethernet-kabel aan op de LAN-poort van de hoofdrouter. Ethernet Backhaul wordt automatisch geconfigureerd.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Nadat de Mesh-node is toegevoegd, verschijnt de topologie in het Admin Panel van de hoofdrouter.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Nodes beheren {#manage-nodes}

Na de installatie is de Mesh-node niet meer via het oorspronkelijke IP-adres toegankelijk. Beheer de hoofdrouter en nodes via het Admin Panel van de hoofdrouter.

### Nodegegevens bekijken {#view-node-details}

Ga in het Admin Panel van de hoofdrouter naar **MESH** en klik in de topologie op **Main Router**.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Je kunt model, IP- en MAC-adres, uptime en verbonden clients van de hoofdrouter bekijken.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Klik in de topologie op **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Je kunt model, IP- en MAC-adres, firmwareversie, uptime en verbonden clients van de Mesh-node bekijken.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh-node bewerken {#edit-mesh-node}

Ga in het Admin Panel van de hoofdrouter naar **MESH** en klik in de topologie op **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Elke Mesh-node heet standaard "Node" gevolgd door de laatste vier cijfers van het MAC-adres. Klik op het bewerkingspictogram om de naam te wijzigen.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Mesh-node openen {#access-mesh-node}

Ga in het Admin Panel van de hoofdrouter naar **MESH** en klik in de topologie op **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Klik rechtsboven op het tandwielpictogram en selecteer **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

De aanmeldpagina van de Mesh-node op het door de hoofdrouter toegewezen IP-adres wordt geopend. Meld je aan bij de node.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Meer nodes toevoegen {#add-more-nodes}

Klik rechtsboven in de topologie op **Add** om meer nodes toe te voegen.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

## Mesh versus Extender versus Access Point {#mesh-vs-extender-vs-access-point-mode}

Alle drie de modi vergroten Wi-Fi-dekking. Ze verschillen in verbinding met de hoofdrouter en configuratie en beheer. **Backhaul** is de verbinding tussen de hoofdrouter en extender, access point of Mesh-node.

Deze tabel vergelijkt de zelfstandige modi Extender en Access Point met Mesh.

| Functie | Extender Mode | Access Point Mode | Mesh Mode |
|---|---|---|---|
| **Wireless backhaul** | ✅ Ondersteund | ❌ Niet van toepassing | ✅ Ondersteund |
| **Ethernet backhaul** | ❌ Niet gebruikt | ✅ Ondersteund | ✅ Ondersteund |
| **Full-duplex backhaul** | ❌ Wi-Fi is half-duplex | ✅ Ethernet | ✅ Alleen Ethernet; draadloze backhaul blijft half-duplex |
| **2.4/5 GHz wireless backhaul** | ⚠️ Banden hangen af van model en firmware | ❌ Niet van toepassing | ⚠️ Banden hangen af van model en firmware |
| **6 GHz wireless backhaul** | ⚠️ Afhankelijk van model en firmware | ❌ Niet van toepassing | 🔜 Binnenkort beschikbaar |
| **Wi-Fi roaming** | ✅ Door client beheerd | ✅ Door client beheerd | ✅ Door client beheerd met 802.11k/v |
| **Automatische synchronisatie van Wi-Fi-instellingen** | ❌ Afzonderlijk configureren | ❌ Afzonderlijk configureren | ✅ Vanaf de hoofdrouter |
| **Centraal nodebeheer** | ❌ Afzonderlijk configureren | ❌ Afzonderlijk configureren | ✅ Via de hoofdrouter |
| **Netwerktopologie en clientoverzicht** | ❌ Geen Mesh-breed overzicht | ❌ Geen Mesh-breed overzicht | ✅ Op de hoofdrouter |
| **Centraal beheerde uitbreiding** | ❌ Onafhankelijke extenders | ❌ Onafhankelijke access points | ✅ Eén hoofdrouter en maximaal acht nodes |
| **Centraal beheerde draadloze hops** | ❌ Niet door Mesh beheerd | ❌ Niet van toepassing | ✅ Maximaal drie draadloze hops |
| **Automatic wired/wireless backhaul switching** | ❌ No Mesh-managed switching | ❌ No Mesh-managed switching | ✅ Prioritizes Ethernet |
| **Meest geschikt voor** | Eenvoudige draadloze uitbreiding | Dekking uitbreiden waar Ethernet beschikbaar is | Gecoördineerde bekabelde, draadloze of gemengde dekking |

✅ Ondersteund · ❌ Niet ondersteund of niet van toepassing · ⚠️ Afhankelijk van hardware, firmware of configuratie · 🔜 Geplande functie

Mesh synchroniseert ondersteunde Main-, Guest-, IoT- en MLO Wi-Fi-instellingen en biedt centraal nodebeheer, waaronder herstarten, verwijderen en bijwerken. Nodes kunnen via Wi-Fi-scan, Ethernet of een Mesh/WPS-knop worden toegevoegd. Backhaulbeheer omvat Ethernet-prioriteit, bekabeld/draadloos wisselen en luspreventie.

### Prestatieverschillen begrijpen {#understanding-performance-differences}

#### Extender Mode {#extender-mode}

Het apparaat verbindt met een bestaand Wi-Fi-netwerk. De radio voor de upstream verbinding volgt het kanaal van de hoofdrouter. Clients op dezelfde radio delen dat kanaal en de airtime.

Op ondersteunde multi-bandmodellen kunnen afzonderlijke radio's clients op andere banden bedienen. Een extender kan bijvoorbeeld upstream via 2.4 GHz verbinden en clients via een afzonderlijke 5 GHz-radio bedienen. Deze verbindingen delen geen kanaal-airtime. Combinaties hangen af van model en firmware; Extender is niet beperkt tot één band.

Dezelfde eis voor het upstream kanaal geldt voor Repeater, hoewel Repeater en de zelfstandige Extender-modus verder verschillen.

#### Draadloze Mesh {#wireless-mesh}

In de geteste tri-bandconfiguratie gebruikt de node **5 GHz voor draadloze backhaul**. Het 5 GHz-kanaal volgt de hoofdrouter en kan niet afzonderlijk worden gewijzigd; de **2.4 GHz- en 6 GHz-kanalen blijven afzonderlijk instelbaar**. Dit zijn kanaalinstellingen, niet de banden waarmee clients kunnen verbinden.

De gevolgen voor prestaties hangen af van de clientverbinding:

- **Apparaten via 5 GHz:** als een client via de 5 GHz-radio verbindt terwijl diezelfde radio draadloze backhaul draagt, delen de verbindingen airtime. Een vergrendeld kanaal voorkomt niet noodzakelijk clientverbindingen op die band.
- **Apparaten via 2.4 GHz of 6 GHz:** wanneer deze clients een andere radio gebruiken dan de 5 GHz-backhaul, delen de links niet de nadelen van doorsturen op hetzelfde kanaal.

Dit beschrijft de geteste configuratie, niet elk Mesh-model. Doorsturen via afzonderlijke radio's is niet exclusief voor Mesh en overschakelen van Extender verbetert de doorvoer niet automatisch.

#### Access Point en bekabelde Mesh {#access-point-mode-and-wired-mesh}

Beide gebruiken Ethernet naar de hoofdrouter. Ethernet-backhaul werkt full-duplex en vermijdt backhaulverkeer via Wi-Fi. Client-Wi-Fi blijft half-duplex. Bij vergelijkbare hardware kunnen Access Point en bekabelde Mesh een vergelijkbare doorvoer bieden; Mesh voegt gecoördineerde configuratie en beheer toe.

Mesh geeft Ethernet-backhaul prioriteit en kan bij een geschikte verbinding naar draadloos schakelen. In de test blijft het 5 GHz-kanaal met de hoofdrouter uitgelijnd terwijl Ethernet actief is; dit betekent niet dat draadloze backhaul verkeer draagt. Nodes en clients op hetzelfde kanaal kunnen nog om airtime concurreren.

!!! note "6 GHz-Mesh-backhaul — binnenkort beschikbaar"

    6 GHz-Mesh-backhaul vereist compatibele 6 GHz-hardware in hoofdrouter en node en ondersteunende firmware. Niet elk Mesh-model zal dit ondersteunen.

    Dit verschilt van een clientverbinding met het bestaande 6 GHz-netwerk van een node. Met 6 GHz-backhaul kan een afzonderlijke 5 GHz-radio clients bedienen zonder backhaul-airtime te delen. Een radio is alleen exclusief voor backhaul als deze daarvoor is gereserveerd.

!!! important "Afzonderlijke radio's maken Wi-Fi niet full-duplex"

    Elke Wi-Fi-link blijft half-duplex. Afzonderlijke radio's voorkomen dat backhaul en clients één kanaal delen, maar verwijderen geen andere interferentie, contention of multi-hopbeperkingen. De end-to-enddoorvoer blijft beperkt door de langzaamste link en netwerkomstandigheden.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
