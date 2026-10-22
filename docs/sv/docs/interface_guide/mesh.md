# Mesh {#mesh}

**Note**: This feature was introduced in firmware v4.10.

Mango 2 (GL-MG1300) och Mudi 7 (GL-E5800) stöder inte Mesh, inte heller med firmware v4.10 eller senare. Se [Supported Models](#supported-models).

---

Öppna **MESH**.

Mesh bygger på Wi-Fi EasyMesh™ och utökar Wi-Fi-täckningen med sömlös roaming. Ange en GL.iNet-router som huvudrouter och övriga som mesh-noder.

Se [Mesh kontra Extender kontra Access Point](#mesh-vs-extender-vs-access-point-mode) om du är osäker på läge.

## Supported Models {#supported-models}

??? "Supported Models"
    - ※GL-BE14000 (Flint 4)
    - ※GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

    **Note**: Models marked with ※ support Mesh in Beta firmware.

??? "Unsupported Models"
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

## Quick Setup {#quick-setup}

The following example uses Flint 3 (GL‑BE9300) and Slate 7 (GL‑BE3600) to build a Mesh network.

**Flint 3** är huvudroutern som ansluter till internet och hanterar noderna.

**Slate 7** är mesh-noden som utökar huvudrouterns täckning.

1. Slå på mesh-noden och placera den nära huvudroutern.

    Ha noden bredvid huvudroutern under första konfigurationen. Flytta den sedan halvvägs mot den döda zonen.

2. Logga in på nodens webbadministrationspanel, öppna **MESH** och klicka på **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Noden blir sökbar men saknar nätverksanslutning tills den läggs till.

3. Logga in på huvudroutern, öppna **INTERNET** och anslut via Ethernet, Repeater, Tethering eller Cellular.

4. Öppna **MESH** och klicka på **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. The page indicates two ways to add Mesh nodes: Wi-Fi Scan and Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Välj guiden nedan för att lägga till noder.

    ??? note "Wi-Fi Scan"

        Click **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Sökningen efter närliggande noder startar. Välj enheter och klicka på **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Noden läggs till. Klicka på **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Anslut nodens WAN-port till huvudrouterns LAN-port med Ethernet. Ethernet Backhaul konfigureras automatiskt.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Once the Mesh node is added, the topology appears in the main router's Admin Panel.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Manage Nodes {#manage-nodes}

Efter konfigurationen kan noden inte nås via sin ursprungliga IP-adress. Hantera alla enheter via huvudrouterns Admin Panel.

### View Node Details {#view-node-details}

Öppna **MESH** och klicka på **Main Router** i topologin.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Visa modell, IP- och MAC-adress, drifttid och anslutna klienter.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Klicka på **Mesh Node** i topologin.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Visa modell, IP- och MAC-adress, firmwareversion, drifttid och klienter.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Edit Mesh Node {#edit-mesh-node}

Öppna **MESH** i huvudrouterns Admin Panel och klicka på **Mesh Node** i topologin.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Varje nod heter som standard "Node" följt av de fyra sista tecknen i MAC-adressen. Klicka på redigeringsikonen för att byta namn.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Access Mesh Node {#access-mesh-node}

Öppna **MESH** i huvudrouterns Admin Panel och klicka på **Mesh Node** i topologin.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Klicka på kugghjulet uppe till höger och välj **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Nodens inloggningssida öppnas på IP-adressen som huvudroutern tilldelat.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Add More Nodes {#add-more-nodes}

Klicka på **Add** uppe till höger för fler noder.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

## Mesh vs. Extender vs. Access Point Mode {#mesh-vs-extender-vs-access-point-mode}

Alla tre lägen utökar Wi-Fi-täckningen. Skillnaderna gäller anslutning, konfiguration och hantering. **Backhaul** är länken mellan huvudroutern och en Extender, Access Point eller mesh-nod.

Tabellen jämför GL.iNets fristående Extender- och Access Point-lägen med Mesh.

| Feature | Extender Mode | Access Point Mode | Mesh Mode |
|---|---|---|---|
| **Wireless backhaul** | ✅ Supported | ❌ Not applicable | ✅ Supported |
| **Ethernet backhaul** | ❌ Används inte i detta läge | ✅ Stöds | ✅ Stöds |
| **Full-duplex backhaul** | ❌ Wi-Fi is half-duplex | ✅ Ethernet | ✅ Ethernet only; wireless backhaul remains half-duplex |
| **2.4/5 GHz wireless backhaul** | ⚠️ Available bands depend on model and firmware | ❌ Not applicable | ⚠️ Available bands depend on model and firmware |
| **6 GHz wireless backhaul** | ⚠️ Model and firmware dependent | ❌ Not applicable | 🔜 Coming soon |
| **Wi-Fi roaming** | ✅ Client-controlled | ✅ Client-controlled | ✅ Client-controlled, with 802.11k/v assistance |
| **Automatic Wi-Fi settings synchronization** | ❌ Konfigureras separat | ❌ Konfigureras separat | ✅ Från huvudroutern |
| **Centralized node management** | ❌ Configure separately | ❌ Configure separately | ✅ Through the main router |
| **Network topology and client overview** | ❌ No Mesh-wide overview | ❌ No Mesh-wide overview | ✅ Available on the main router |
| **Centrally managed expansion** | ❌ Independent extenders | ❌ Independent access points | ✅ One main router and up to eight nodes |
| **Centrally managed wireless hops** | ❌ Not Mesh-managed | ❌ Not applicable | ✅ Up to three wireless hops |
| **Automatic wired/wireless backhaul switching** | ❌ No Mesh-managed switching | ❌ No Mesh-managed switching | ✅ Prioritizes Ethernet |
| **Best suited for** | Simple wireless coverage extension | Extending coverage where Ethernet is available | Coordinated coverage with wired, wireless, or mixed connections |

✅ Stöds · ❌ Stöds inte eller gäller inte i läget · ⚠️ Beror på maskinvara, firmware eller konfiguration · 🔜 Planerad funktion

Mesh synkroniserar inställningar för huvud-, gäst-, IoT- och MLO-Wi-Fi och ger central hantering av omstart, borttagning och uppdatering. Noder läggs till via Wi-Fi-sökning, Ethernet eller Mesh/WPS-knapp. Backhaul-hantering omfattar Ethernet-prioritet, växling mellan kabel och trådlöst samt loopskydd.

### Understanding Performance Differences {#understanding-performance-differences}

#### Extender Mode {#extender-mode}

Enheten ansluter till befintligt Wi-Fi. Radion för uppströmsanslutningen följer huvudrouterns kanal. Klienter på samma radio delar kanalens sändningstid.

På multibandsmodeller kan separata radioenheter betjäna andra band. En Extender kan ansluta uppströms på 2.4 GHz och klienter på separat 5 GHz-radio utan att dela sändningstid. Kombinationer beror på modell och firmware.

Samma kanalregel gäller GL.iNets Repeater, även om Repeater och fristående Extender skiljer sig i övrigt.

#### Wireless Mesh {#wireless-mesh}

I den testade trebandskonfigurationen används **5 GHz för trådlös backhaul**. Nodens 5 GHz-kanal följer huvudroutern medan **2.4 GHz och 6 GHz kan konfigureras separat**. Kanalinställningarna avgör inte vilka band klienter kan använda, och en klientkanal ändrar inte backhaul-bandet.

The performance impact therefore depends on how the client connects:

- **Enheter på 5 GHz:** Om samma radio används för klient och trådlös backhaul delar anslutningarna sändningstid. Låst kanal hindrar inte nödvändigtvis klientanslutning.
- **Enheter på 2.4 GHz eller 6 GHz:** Med separat radio från 5 GHz-backhaul delar länkarna inte samma kanalstraff.

Detta gäller den testade konfigurationen, inte alla modeller. Separata radioenheter är inte unikt för Mesh, och byte från Extender förbättrar inte automatiskt kapaciteten.

#### Access Point-läge och kabelanslutet Mesh {#access-point-mode-and-wired-mesh}

Båda använder Ethernet till huvudroutern. Ethernet-backhaul är full duplex och undviker backhaul-trafik över Wi-Fi, medan klient-Wi-Fi förblir halv duplex. Access Point och kabel-Mesh kan ge liknande kapacitet; Mesh lägger till samordnad konfiguration och hantering.

Mesh prioriterar Ethernet-backhaul och kan växla till trådlöst. I testet följer nodens 5 GHz-kanal huvudroutern även med Ethernet-backhaul, men trafiken går inte därför trådlöst. Närliggande noder och klienter på samma kanal konkurrerar fortfarande om sändningstid.

!!! note "6 GHz Mesh backhaul — Coming soon"

    6 GHz Mesh-backhaul kräver kompatibel 6 GHz-maskinvara i både huvudrouter och nod samt firmwarestöd. Alla Mesh-modeller stöder inte funktionen.

    Detta skiljer sig från klientanslutning till nodens 6 GHz-nätverk. Med 6 GHz-backhaul kan en separat 5 GHz-radio betjäna klienter utan delad sändningstid. En radio är dedikerad endast om den reserveras för backhaul.

!!! important "Separate radios do not make Wi-Fi full-duplex"

    Varje Wi-Fi-länk är halv duplex. Separata radioenheter undviker delad kanal mellan backhaul och klient men tar inte bort annan störning, konkurrens eller flerhoppsbegränsning. Kapaciteten begränsas fortfarande av den långsammare länken och nätverksförhållandena.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
