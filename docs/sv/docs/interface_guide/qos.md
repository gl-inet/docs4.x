# QoS (Quality of Service) {#qos-quality-of-service}

**Note**: This feature was introduced in firmware v4.9.

Vissa modeller, till exempel Mango 2 (GL-MG1300), stöder inte QoS på grund av otillräckligt minne, även med firmware v4.9 eller senare. Se [Supported Models](#supported-models).

---

Öppna **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service) optimerar bandbredden genom att prioritera videosamtal, spel och andra viktiga aktiviteter vid överbelastning.

**Note**:

1. Funktionen påverkar endast trafik genom routern när den fungerar som gateway, inklusive lokal klient- och VPN-klienttrafik. Inkommande VPN-servertrafik påverkas inte.
2. QoS får ingen effekt i Drop-in Gateway-läge.
3. QoS and SQM cannot be enabled simultaneously.
4. QoS cannot work with Network Acceleration. Enabling QoS will automatically disable Network Acceleration to ensure stable performance.

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

## För firmware v4.11 och senare {#for-firmware-v411-and-above}

Aktivera QoS och följ stegen nedan.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Ange WAN-uppladdning och nedladdning (1-10000) eller klicka på **Run Speedtest**. Internetanslutning krävs.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Obs!** Värden anges i **Mbps**. Motsvarande **MB/s** visas som referens.

2. **Scheduling Policy**

    Välj ett principläge. Avancerade regler åsidosätter grundprincipen för matchande trafik.

    - **Device Priority**

        Valda lokala klienter får högre prioritet vid WAN-överbelastning. Klicka på **Add Device** och välj enheter.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Sök efter klientnamn, MAC- eller IP-adress. Välj enheter och klicka på **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        Ange programprioriteter; routern fördelar bandbredd därefter.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Välj **Customize** och klicka på **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        Alla kategorier har Medium Priority som standard.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Dra kategorierna till önskad prioritet och klicka på **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        Skapa avancerade QoS-regler för högprioriterad trafik. Klicka på **Add Rule** och ange protokoll, port och käll-IP.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Ange Name, Protocol, Source Address och Destination Port och klicka på **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## For firmware v4.9 to v4.10 {#for-firmware-v49-to-v410}

Aktivera QoS med reglaget.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Ange maximal uppladdnings- och nedladdningshastighet (1-10000) efter faktisk bandbredd.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Obs!** Värden anges i **Mbps**. Motsvarande **MB/s** visas som referens.

Ange sedan programprioriteter; routern fördelar bandbredd därefter.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Välj **Customize** och klicka på **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

Alla kategorier har Medium Priority som standard.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Dra kategorierna till önskad prioritet och klicka på **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
