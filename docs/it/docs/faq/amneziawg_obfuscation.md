# Offuscamento AmneziaWG {#amneziawg-obfuscation}

AmneziaWG è un protocollo VPN basato su WireGuard con offuscamento del traffico integrato. I suoi parametri di offuscamento controllano come il traffico viene mascherato per evitare il rilevamento in reti con ispezione restrittiva.

Di seguito sono descritti in dettaglio AmneziaWG e le sue diverse versioni.

## Perché AmneziaWG? {#why-amneziawg}

Il predecessore di AmneziaWG, WireGuard, si è affermato come protocollo VPN veloce e affidabile grazie alla sua base di codice compatta e all'elevata efficienza. Tuttavia, i suoi header di pacchetto fissi e le dimensioni prevedibili dei pacchetti creano una firma facilmente riconoscibile. I sistemi DPI possono identificare questi pacchetti senza difficoltà e interrompere immediatamente le connessioni, un problema critico nei Paesi con una forte censura di Internet.

AmneziaWG eredita la semplicità architetturale e le alte prestazioni dell'implementazione WireGuard originale, aggiungendo un modulo di offuscamento dedicato che nasconde i modelli del traffico VPN. Questo aiuta utenti privati e aziendali a proteggere la privacy online e a mantenere connessioni stabili in ambienti di rete restrittivi.

In breve:

- Maschera le caratteristiche VPN per impedire il rilevamento da parte di ISP, firewall o Deep Packet Inspection (DPI).
- Fa apparire la connessione VPN come normale traffico web, migliorando stabilità e probabilità di successo nelle reti con restrizioni.

## AmneziaWG V2.0 {#amneziawg-v20}

### Panoramica {#amneziawg-v20-overview}

<font color="red">**Nota**: AmneziaWG 2.0 è supportato sui router GL.iNet con firmware v4.9.0 o successivo.</font>

AmneziaWG 2.0 mantiene i meccanismi di offuscamento della v1.0: la sequenza di pacchetti spazzatura (**Jc**, **Jmin**, **Jmax**) e i prefissi casuali per i pacchetti Init e Response (**S1–S2**). Aggiunge i meccanismi seguenti per nascondere gli aspetti della connessione ancora prevedibili:

* **S3–S4**: prefissi casuali per i pacchetti Cookie e Data. La v1.0 aggiungeva riempimento solo ai pacchetti Init e Response, quindi i pacchetti Cookie erano sempre di 64 byte e i pacchetti Data avevano esattamente la lunghezza del payload.

* **H1–H4 come intervalli**: il valore dell'intestazione di ciascun tipo di pacchetto viene estratto da un intervallo anziché essere un numero fisso. In ricezione viene accettato qualsiasi valore compreso nell'intervallo. I quattro intervalli non devono sovrapporsi.

* **I1–I5**: pacchetti UDP definiti dall'utente e inviati prima di ogni handshake. La sessione inizia così con traffico simile a quello di un protocollo UDP comune anziché a un handshake WireGuard.

Questi miglioramenti rendono il traffico VPN più difficile da rilevare, mantenendo al tempo stesso l'elevata velocità e la bassa latenza di WireGuard.

!!! Tip "Come distinguere AmneziaWG 1.0 e 2.0?"

    **V1.0**: nessun parametro S3-S4; H1-H4 sono singoli numeri interi fissi.
    
    **V2.0**: è V2.0 se viene soddisfatta una delle condizioni seguenti:
            
    - Include parametri S3-S4
    - H1-H4 sono impostati come intervalli numerici
    - Include parametri I1-I5 personalizzati.
            
    > Nota: I1-I5 non vengono generati automaticamente. Gli utenti possono aggiungerli manualmente come righe aggiuntive nel file di configurazione per far sembrare il traffico AmneziaWG simile ad altri protocolli comuni, come QUIC o WebRTC.

### Parametri {#amneziawg-v20-parameters}

| Parametro | Descrizione | Vincoli | Generato automaticamente |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Il numero di pacchetti spazzatura prima che il client avvii l'handshake (per interferire con il rilevamento delle caratteristiche del traffico) | 1~128 | 4~12 |
| Jmin         | Dimensione minima dei pacchetti spazzatura casuali (byte); deve essere configurata insieme a Jmax per definire la dimensione dei pacchetti spazzatura | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Dimensione massima dei pacchetti spazzatura casuali | 0 ≤ Jmin < Jmax < 1280 | 0≤ Jmin < Jmax < 1280 |
| S1           | Prefissi casuali per i pacchetti Init | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2           | Prefissi casuali per i pacchetti Response | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Prefissi casuali per i pacchetti Cookie | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4           | Prefissi casuali per i pacchetti Data | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4        | Intestazioni dinamiche per i tipi di pacchetto; valori casuali (v1.0) o intervalli (v2.0) | 5~2147483647; H1, H2, H3 e H4 devono essere diversi | 5~2147483647 |
| I1~I5        | Pacchetti firma per l'imitazione del protocollo | blocco esadecimale arbitrario | N/A |

Esempio di sezione di offuscamento v2.0:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1318795025-1318795156
H2 = 1029272944-1029273095
H3 = 966737016-966737098
H4 = 282229905-429495047
```

Riferimenti: [Documentazione ufficiale di AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Panoramica {#amneziawg-v31-overview}

<font color="red">**Nota**: AmneziaWG 3.1 è supportato sui router GL.iNet con firmware v4.11.1 o successivo.</font>

AmneziaWG 3.1 mantiene tutti i meccanismi di offuscamento della v2.0: i prefissi casuali per tutti i tipi di pacchetto (**S1–S4**), le intestazioni dinamiche (**H1–H4**), i pacchetti di firma inviati prima dell'handshake (**I1–I5**) e la sequenza di pacchetti spazzatura (**Jc**, **Jmin**, **Jmax**). Aggiunge i meccanismi seguenti per rendere più difficile identificare il traffico in base alle sue caratteristiche.

- **Protezione delle intestazioni**: usa ChaCha20 per nascondere i campi delle intestazioni dei pacchetti WireGuard che altrimenti rimarrebbero in chiaro.
- **Riempimento del contenuto**: aggiunge una quantità casuale di riempimento ai pacchetti di dati di trasporto, entro lo spazio disponibile secondo la MTU.
- **Temporizzazioni personalizzate**: consente di configurare valori o intervalli per il rinnovo delle chiavi, i tentativi di handshake, i messaggi di mantenimento della connessione e le operazioni correlate. Si consiglia di usare i valori generati automaticamente sia sul server sia sul client.
- **Code casuali**: aggiunge code di lunghezza variabile ai pacchetti di handshake e ai pacchetti di dati di trasporto per variare ulteriormente le dimensioni dei pacchetti.
- **Disattivazione delle risposte Cookie**: consente al dispositivo di interrompere l'invio delle risposte Cookie di handshake, mantenendo la ricezione di queste risposte e le altre operazioni di handshake.

### Parametri {#amneziawg-v31-parameters}

I parametri seguenti sono stati introdotti in AmneziaWG V3.1.

| Parametro | Descrizione | Vincoli | Intervallo o valore GL.iNet |
| --------- | ----------- | ----------- | ----------- |
| `HeaderProtectionKey` | Protegge con ChaCha20 i campi delle intestazioni dei pacchetti che altrimenti rimarrebbero in chiaro | Esattamente 32 byte. Se è attiva, occorre impostare S1, S2, S3 e S4, ciascuno con un valore ≥ 12. La combinazione consigliata è `H1=1`, `H2=2`, `H3=3`, `H4=4`: disattiva le intestazioni personalizzate e affida alla protezione delle intestazioni il compito di nascondere il tipo di messaggio | Chiave di 32 byte |
| `ContentPaddingAddition` | Aggiunge ai pacchetti di dati di trasporto un numero casuale di byte, estratto dall'intervallo configurato per ogni pacchetto | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` disattiva la funzione | 0–65535 (esempio: `10-50`) |
| `RekeyAfterTime` | Durata d'uso della chiave corrente prima di avviare un rinnovo attivo (secondi) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` ripristina il valore predefinito di WireGuard | 100–150 (valore predefinito di WireGuard: 120) |
| `RekeyTimeout` | Tempo di attesa di una risposta a una richiesta di handshake prima di riprovare (secondi) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` ripristina il valore predefinito di WireGuard | 4–7 (valore predefinito di WireGuard: 5) |
| `RejectAfterTime` | Tempo senza ricevere dati prima che la connessione avvii un nuovo handshake (secondi) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` ripristina il valore predefinito di WireGuard | 180–240 (valore predefinito di WireGuard: 180) |
| `KeepaliveTimeout` | Tempo senza inviare dati prima dell'invio di un messaggio interno di mantenimento della connessione (secondi) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` ripristina il valore predefinito di WireGuard | 8–20 (valore predefinito di WireGuard: 10) |
| `MaxHandshakeAttempts` | Numero massimo di nuovi tentativi di handshake | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` ripristina il valore predefinito di WireGuard | 12–18 (valore predefinito di WireGuard: 18) |
| `RandomTrailers` | Aggiunge un numero variabile di byte in coda: dati casuali nei pacchetti di handshake e zeri dopo il pacchetto IP interno nei pacchetti di trasporto. La lunghezza è scelta dinamicamente in modo da non superare la MTU di nessuna delle due estremità | `off` disattiva la funzione. Se è attiva, si consiglia `S1 = S2 = S3 = S4` per ridurre il rischio di identificare erroneamente il tipo di pacchetto a causa delle dimensioni casuali | `on` / `off` |
| `DisableCookies` | Impedisce al dispositivo locale di inviare risposte Cookie di handshake. La ricezione delle risposte Cookie dal peer e le altre operazioni di handshake non cambiano | `off` disattiva la funzione. S3 e H3 devono restare validi perché possono essere ancora utilizzati in ricezione | `on` / `off` |

**Note**

* Il router può generare gli intervalli dell'ultima colonna. Le opzioni `RandomTrailers` e `DisableCookies` si impostano su ciascun dispositivo.
* `HeaderProtectionKey` deve essere identica sul client e sul server.
* Durante il funzionamento, le temporizzazioni fuori dagli intervalli indicati sono sostituite da valori casuali interni all'intervallo. Il valore personalizzato potrebbe quindi non essere applicato come immesso.
* `ContentPaddingAddition` e `S4` modificano la lunghezza del pacchetto di trasporto in punti diversi e possono essere usati insieme.
* La protezione delle intestazioni è compatibile con valori `H` dinamici. `H1–H4` possono rimanere dinamici, anche se l'impostazione consigliata è `1/2/3/4`.

---

Esempio di sezione di offuscamento v3.1:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

Riferimenti: [Documentazione ufficiale di AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Articolo correlato:

- [Come configurare l'offuscamento VPN sui router GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [Contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
