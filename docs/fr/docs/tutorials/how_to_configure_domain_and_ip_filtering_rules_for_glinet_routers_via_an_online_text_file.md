# Comment configurer des règles de filtrage de domaines et d'adresses IP pour les routeurs GL.iNet via un fichier texte en ligne

À partir du firmware v4.7.0, la fonctionnalité "VPN Policy Based on the Target Domain or IP" dans la fonction VPN et "Add a New Ruleset" dans la fonction Parental Control prennent en charge l'importation de règles à partir d'un lien vers un fichier texte en ligne. Cet article présente le format de ce fichier texte.

## Description du format d'URL

### Formats d'URL pris en charge et non pris en charge

- Formats de fichiers pris en charge pour le fichier texte : .txt, .conf, .log, etc.
- Formats de fichiers non pris en charge : fichiers binaires tels que .exe, .zip, .jpg, etc.

### Utiliser GitHub pour héberger le fichier texte

Si vous hébergez le fichier texte dans un dépôt GitHub public, veillez à utiliser l'URL du contenu brut plutôt que l'URL GitHub classique.

Par exemple, l'URL GitHub suivante pointe vers le contenu web plutôt que vers le contenu brut :

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Pour que le routeur télécharge le bon contenu, utilisez l'URL du contenu brut au format suivant :

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

Ainsi, le routeur pourra récupérer le contenu en texte brut du fichier.

## Formats de filtre pour "VPN Policy Based on the Target Domain or IP"

La fonctionnalité "VPN Policy Based on the Target Domain or IP" prend en charge les formats de filtre suivants dans le fichier texte en ligne :

* Format de nom de domaine : utilisez le nom de domaine, par exemple `netflix.com`, pour faire correspondre tous les sous-domaines de `netflix.com`.
* Format de sous-domaine : indiquez le sous-domaine complet, par exemple `www.netflix.com`, pour faire correspondre uniquement ce sous-domaine précis.
* Format CIDR : utilisez la notation CIDR pour définir des plages d'adresses IP, par exemple `192.168.10.0/24`.
* Format d'adresse IPv4 : indiquez des adresses IPv4 individuelles, par exemple `192.168.10.10`.

## Formats de filtre pour "Add a New Ruleset" dans Parental Control

La fonctionnalité "Add a New Ruleset" dans Parental Control prend en charge les formats de filtre suivants dans le fichier texte en ligne :

* Format de nom de domaine : utilisez le nom de domaine, par exemple `instagram.com`, pour faire correspondre tous les sous-domaines de `instagram.com`.
* Format de sous-domaine : indiquez le sous-domaine complet, par exemple `www.instagram.com`, pour faire correspondre uniquement ce sous-domaine précis.

Lors de la création du fichier texte en ligne, utilisez un filtre par ligne. Le routeur traitera chaque ligne selon le format indiqué et appliquera les règles correspondantes à la fonction VPN ou Parental Control.

## Exemples

Pour "VPN Policy Based on the Target Domain or IP" :

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

Pour "Parental Control Add a New Ruleset" :

```
instagram.com
facebook
x.com
snapchat
```

En respectant ces formats de filtre, vous pouvez facilement créer et maintenir le fichier texte en ligne pour configurer les fonctions VPN et Parental Control sur votre routeur.

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
