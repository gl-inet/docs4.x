# Introduzione ai parametri di offuscamento di AmneziaWG

AmneziaWG è un protocollo VPN basato su WireGuard con offuscamento del traffico integrato. I suoi parametri di offuscamento controllano il modo in cui il traffico viene camuffato per evitare il rilevamento da parte di reti con controlli rigidi. Di seguito trovi una panoramica dettagliata delle differenze tra le versioni di AmneziaWG, dei parametri di offuscamento, dei relativi vincoli e delle impostazioni consigliate.

## AmneziaWG V2.0

Rispetto ad AmneziaWG v1.0, la versione v2.0 offre un offuscamento più efficace grazie all'aggiunta di nuovi parametri (**S3~S4**) e all'uso di intestazioni dinamiche per i tipi di pacchetto (**H1~H4** come intervalli invece di valori fissi). Inoltre, AmneziaWG 2.0 supporta i parametri **I1~I5**, che inviano pacchetti UDP formattati prima di ogni handshake per far sembrare il traffico AmneziaWG un normale traffico non VPN, aggirando efficacemente l'ispezione approfondita dei pacchetti e migliorando la connettività nelle reti con restrizioni.

Questi miglioramenti rendono il traffico VPN più difficile da rilevare, mantenendo al tempo stesso l'elevata velocità e la bassa latenza di WireGuard.

Ecco come identificare la versione di AmneziaWG:

- **V1.0**: nessun parametro S3~S4; H1~H4 sono singoli numeri interi fissi.
- **V2.0**: include i parametri **S3~S4**; **H1~H4** sono definiti come intervalli numerici; supporta i parametri **I1~I5**.

**Nota**: i parametri I1-I5 non vengono generati automaticamente. Gli utenti possono aggiungerli manualmente come righe extra nel file di configurazione VPN per far sembrare il traffico AmneziaWG simile ad altri protocolli comuni, come QUIC o WebRTC.

## Panoramica dei parametri

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Il numero di pacchetti spazzatura prima che il client avvii l'handshake (per interferire con il rilevamento delle caratteristiche del traffico) | 1~128 | 4~12 |
| Jmin         | Dimensione minima dei pacchetti spazzatura casuali (byte); deve essere configurata insieme a Jmax per definire la dimensione dei pacchetti spazzatura | 0 ≤ Jmin < Jmax < 65535 | 0 <= jmin < jmax < 1280 |
| Jmax         | Dimensione massima dei pacchetti spazzatura casuali | 0 ≤ Jmin < Jmax < 65535 | 0≤ Jmin < Jmax < 1280 |
| S1           | Prefissi casuali per i pacchetti Init | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2           | Prefissi casuali per i pacchetti Response | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Prefissi casuali per i pacchetti Cookie | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4           | Prefissi casuali per i pacchetti Data | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4        | Intestazioni dinamiche per i tipi di pacchetto; valori casuali (v1.0) o intervalli (v2.0) | 5~2147483647; H1, H2, H3 e H4 devono essere diversi | 5~2147483647 |
| I1~I5        | Pacchetti firma per l'imitazione del protocollo | arbitrary hex-blob | N/A |

Riferimenti: [Documentazione ufficiale di AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
