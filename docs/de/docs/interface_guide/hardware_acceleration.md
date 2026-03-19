# Hardware-Beschleunigung

**Hinweis**: Diese Anleitung gilt für Firmware v4.2 und früher. Für neuere Versionen lesen Sie bitte [Network Acceleration](network_acceleration.md). 

---

Die Hardware-Beschleunigung (manchmal auch *Hardware NAT, Flow Offloading oder Offloading* genannt) reduziert die CPU-Last, indem die Paketweiterleitung von der CPU auf die SoC-/NIC-Hardware des Routers verlagert wird. Dadurch steigen in der Regel der maximale Durchsatz und die Effizienz der CPU-Auslastung. Allerdings gibt es wichtige Einschränkungen, insbesondere bei Funktionen, die auf dem Linux-Netzwerkstack (netfilter/iptables/nftables) oder den Kernel-Queueing-Disziplinen (qdisc) basieren, die von SQM (Smart Queue Management) verwendet werden.

Wenn die Hardware-Beschleunigung aktiviert ist, funktionieren die folgenden Funktionen nicht ordnungsgemäß: Client Speed and Traffic Statistics, Client Speed Limit.

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Nicht unterstützte Modelle"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **Hardware Acceleration**.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

Aktivieren Sie den Schalter und klicken Sie auf Apply.

---

## Hardware NAT vs. Software NAT

* Wenn für Sie der Durchsatz am wichtigsten ist (z. B. bei Multi-Gigabit-Breitband) und Sie weder SQM auf dem Router noch eine Begrenzung pro Client benötigen → aktivieren Sie Hardware NAT / Network Acceleration. Dadurch erhalten Sie den höchsten Durchsatz und die geringste CPU-Auslastung.

* Wenn Ihnen geringe Latenz, konstantes QoS, Begrenzungen pro Client wichtig sind oder Sie auf SQM (cake/fq_codel) angewiesen sind → verwenden Sie Software NAT (deaktivieren Sie Hardware-Offload). SQM und QoS erfordern, dass Pakete den qdisc-Stack des Kernels durchlaufen. Offloaded-Pakete umgehen diesen Pfad und werden daher nicht geformt.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
