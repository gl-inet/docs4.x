# Firmware v4.11 {#firmware-v411}

Deze release is gericht op betere bewaking van de netwerkkwaliteit en beoordeling van de beveiliging. Zo kun je verbindingsproblemen en mogelijke beveiligingsrisico’s opsporen. Daarnaast zijn DNS, QoS, SQM en Data Statistics uitgebreid voor flexibeler netwerkbeheer en verkeersbeheer.

Download de nieuwste firmware via het [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Network Quality {#network-quality}

[Network Quality](../interface_guide/network_quality.md) is een nieuwe functie die je internetverbinding in realtime bewaakt. De functie beoordeelt de reactiesnelheid, latentie en DNS-prestaties en detecteert verbindingsuitval en pakketverlies. Zo kun je netwerkinstabiliteit en verbindingsproblemen opsporen die alleen met bandbreedtetests mogelijk niet zichtbaar worden.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Security Scan {#security-scan}

[Security Scan](../interface_guide/security_scan.md) is een nieuwe functie die de beveiligingsinstellingen van je router beoordeelt en een beveiligingsscore, risicowaarschuwingen en optimalisatiesuggesties geeft. De functie controleert onder meer de Wi-Fi-beveiliging, WAN-ping, externe SSH-toegang, port forwarding en DPI-contentbeveiliging, zodat je mogelijke beveiligingsrisico’s kunt opsporen en aanpakken. Wanneer je de pagina opent, start automatisch een scan. Je kunt ook op het scorepictogram klikken om de scan te resetten en opnieuw uit te voeren.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## UPnP {#upnp}

Met [UPnP](../interface_guide/upnp.md) kunnen compatibele LAN-apparaten en toepassingen automatisch poorttoewijzingen aanvragen zonder handmatige configuratie van port forwarding. Dit vereenvoudigt verbindingen voor online gaming, peer-to-peerbestandsdeling en externe toegang. Op de UPnP-pagina kun je actieve toewijzingen bekijken, de resterende leasetijd controleren en toewijzingen zo nodig verwijderen.

![UPnP](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/upnp.png){class="glboxshadow"}

## DNS {#dns}

Deze release verbetert de configuratie van [DNS](../interface_guide/dns_v4.11.md) door WAN DNS, VPN DNS en Manual DNS op één pagina samen te brengen. Je kunt eenvoudig de DNS-status voor elk verbindingstype bekijken, aangepaste DNS-servers configureren en bepalen of handmatige DNS-instellingen op VPN-tunnels of op de router zelf worden toegepast.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) biedt de optie **Run Speedtest** voor de WAN-bandbreedte. Hiermee worden de download- en uploadsnelheid gemeten en de relevante velden automatisch ingevuld. Voor planningsbeleid voegt deze release naast Application Priority twee opties toe: **Device Priority** en **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: geselecteerde lokale clients krijgen tijdens WAN-congestie een hogere netwerkprioriteit.

- **Application Priority**: stel aangepaste prioriteiten in voor verschillende toepassingen. De router wijst de bandbreedte dienovereenkomstig toe.

- **Advanced QoS**: maak geavanceerde QoS-regels voor verkeer met hoge prioriteit.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) biedt de optie **Run Speedtest** voor de WAN-bandbreedte. Hiermee worden de download- en uploadsnelheid gemeten en de relevante velden automatisch ingevuld. Er zijn twee wachtrijdisciplines beschikbaar: **cake** en **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: slimme, automatische verkeersregeling met de beste algehele beheersing van de latentie (aanbevolen).

    Voor deze wachtrijdiscipline past de nieuw toegevoegde functie **Cake Autorate** de geconfigureerde bandbreedte dynamisch aan op basis van probe RTT. De functie gebruikt lichte pingtests in plaats van actieve snelheidstests en wordt aanbevolen voor WAN-verbindingen met wisselende bandbreedte.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: eenvoudige en efficiënte fair queueing met basisverlaging van de latentie.

## Data Statistics {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) ondersteunt nu het filteren van verkeer per client en introduceert nieuwe grafiekweergaven, waaronder staaf- en cirkeldiagrammen. Wanneer je App Traffic Statistics bekijkt, kun je een specifieke client selecteren en tussen grafiekweergaven schakelen voor een duidelijkere analyse van het verkeersgebruik.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
