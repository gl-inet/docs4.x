# Come configurare regole di filtraggio dominio e IP per i router GL.iNet tramite un file di testo online

A partire dal firmware v4.7.0, la funzione "VPN Policy Based on the Target Domain or IP" nella funzione VPN e "Add a New Ruleset" nella funzione Parental Control supportano l'importazione di regole da un link a un file di testo online. Questo articolo presenta il formato di questo file di testo.

## Descrizione del formato URL

### Formati URL supportati e non supportati

- Formati file supportati per il file di testo: `.txt`, `.conf`, `.log` e cosi' via.
- Formati file non supportati: file binari come `.exe`, `.zip`, `.jpg` e cosi' via.

### Usare GitHub per ospitare il file di testo

Se ospiti il file di testo in un repository GitHub pubblico, assicurati di usare l'URL del contenuto raw invece del normale URL GitHub.

Ad esempio, il seguente URL GitHub punta al contenuto web invece che al contenuto raw:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Per assicurarti che il router scarichi il contenuto corretto, usa l'URL raw content nel seguente formato:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

In questo modo il router potra' recuperare il contenuto in testo semplice del file.

## Formati di filtro per VPN Policy Based on the Target Domain or IP

La funzione "VPN Policy Based on the Target Domain or IP" supporta i seguenti formati di filtro nel file di testo online:

* Formato nome di dominio: usa il nome di dominio, ad esempio `netflix.com`, per corrispondere a tutti i sottodomini di `netflix.com`.
* Formato sottodominio: specifica il sottodominio completo, ad esempio `www.netflix.com`, per corrispondere solo a quel sottodominio specifico.
* Formato CIDR: usa la notazione CIDR per specificare intervalli di indirizzi IP, ad esempio `192.168.10.0/24`.
* Formato indirizzo IPv4: specifica singoli indirizzi IPv4, ad esempio `192.168.10.10`.

## Formati di filtro per Parental Control Add a New Ruleset

La funzione "Add a New Ruleset" in Parental Control supporta i seguenti formati di filtro nel file di testo online:

* Formato nome di dominio: usa il nome di dominio, ad esempio `instagram.com`, per corrispondere a tutti i sottodomini di `instagram.com`.
* Formato sottodominio: specifica il sottodominio completo, ad esempio `www.instagram.com`, per corrispondere solo a quel sottodominio specifico.

Quando crei il file di testo online, usa un filtro per riga. Il router elaborera' ogni riga secondo il formato specificato e applichera' le regole corrispondenti alla funzione VPN o Parental Control.

## Esempi

Per "VPN Policy Based on the Target Domain or IP":

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

Per "Parental Control Add a New Ruleset":

```
instagram.com
facebook
x.com
snapchat
```

Seguendo questi formati di filtro, puoi creare e mantenere facilmente il file di testo online per configurare le funzioni VPN e Parental Control sul router.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
