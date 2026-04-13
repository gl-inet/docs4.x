# Come configurare regole di filtraggio per domini e IP sui router GL.iNet tramite un file di testo online

A partire dal firmware v4.7, le seguenti funzioni supportano l'importazione di regole da un URL che punta a un file di testo online:

- VPN Policy basata sui domini o sugli indirizzi IP di destinazione (nella sezione VPN)
- Add a New Ruleset (nella sezione Parental Control)

Questo tutorial spiega come usare un file di testo online per importare regole di filtraggio per domini e IP sui router GL.iNet.

## Formati URL e file supportati

Sono supportati i seguenti formati URL:

- URL di file di testo normale (HTTP/HTTPS)
- URL Raw Content di GitHub

Sono supportati i file `.txt`, `.conf`, `.log` e altri formati di testo semplice.

**Nota**: i file binari non sono supportati, ad esempio `.exe`, `.zip`, `.jpg`, `.png` e simili.

## Usare GitHub per ospitare il file di testo

Se ospiti il file di testo in un repository GitHub pubblico, assicurati di usare l'URL del contenuto raw invece del normale URL GitHub.

Ad esempio, il seguente URL GitHub punta al contenuto web invece che al contenuto raw:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Per assicurarti che il router scarichi il contenuto corretto, usa l'URL raw content nel seguente formato:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

In questo modo il router potrà recuperare il contenuto in testo semplice del file.

## Formati di filtro per VPN Policy (dominio/IP)

La funzione "VPN Policy Based on Target Domain or IP Address" supporta i seguenti formati di filtro nel file di testo online:

* **Nome di dominio**: usa il nome di dominio, ad esempio `netflix.com` (corrisponde a tutti i sottodomini).
* **Sottodominio**: specifica il sottodominio completo, ad esempio `www.netflix.com` (corrisponde solo a quel sottodominio).
* **Intervallo CIDR**: usa la notazione CIDR per specificare intervalli di indirizzi IP, ad esempio `192.168.10.0/24`.
* **Indirizzo IPv4**: specifica singoli indirizzi IPv4, ad esempio `192.168.10.10`.

## Formati di filtro per Parental Control (Ruleset)

La funzione "Add a New Ruleset" in Parental Control supporta i seguenti formati di filtro nel file di testo online:

* **Nome di dominio**: usa il nome di dominio, ad esempio `instagram.com` (corrisponde a tutti i sottodomini).
* **Sottodominio**: specifica il sottodominio completo, ad esempio `www.instagram.com` (corrisponde solo a quel sottodominio).

Quando crei il file di testo online, usa un filtro per riga. Il router elaborerà ogni riga secondo il formato specificato e applicherà le regole corrispondenti alla funzione VPN o Parental Control.

Seguendo questi formati di filtro, puoi creare e mantenere facilmente il file di testo online per configurare le funzioni VPN e Parental Control sul router.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
