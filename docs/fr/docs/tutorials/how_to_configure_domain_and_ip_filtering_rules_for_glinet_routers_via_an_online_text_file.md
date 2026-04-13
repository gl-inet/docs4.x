# Comment configurer des règles de filtrage de domaine et d’IP pour les routeurs GL.iNet via un fichier texte en ligne

À partir du firmware v4.7, les fonctionnalités suivantes prennent en charge l’importation de règles depuis l’URL d’un fichier texte en ligne :

- la politique VPN basée sur les domaines ou adresses IP de destination (dans VPN)
- **Add a New Ruleset** (dans Parental Control)

Ce tutoriel explique comment utiliser un fichier texte en ligne pour importer des règles de filtrage de domaines et d’adresses IP sur les routeurs GL.iNet.

## Formats d’URL et de fichiers pris en charge

Les formats d’URL pris en charge sont les suivants :

- URL de fichiers texte brut (HTTP/HTTPS)
- URL GitHub Raw content

Les types de fichiers pris en charge sont `.txt`, `.conf`, `.log` et d’autres formats texte brut.

**Remarque** : les fichiers binaires ne sont pas pris en charge, comme `.exe`, `.zip`, `.jpg`, `.png`, etc.

## Utiliser GitHub pour héberger le fichier texte

Si vous hébergez le fichier texte dans un dépôt GitHub public, veillez à utiliser l’URL du contenu brut plutôt que l’URL GitHub classique.

Par exemple, l’URL GitHub suivante pointe vers le contenu web et non vers le contenu brut :

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Pour que le routeur télécharge le bon contenu, utilisez une URL de contenu brut au format suivant :

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

De cette manière, le routeur pourra récupérer le contenu texte brut du fichier.

## Formats de filtre pour la politique VPN (domaine/IP)

La fonctionnalité **VPN Policy Based on Target Domain or IP Address** prend en charge les formats de filtre suivants dans le fichier texte en ligne :

* Nom de domaine : utilisez le nom de domaine, par exemple `netflix.com` (correspond à tous les sous-domaines).
* Sous-domaine : indiquez le sous-domaine complet, par exemple `www.netflix.com` (correspond uniquement à ce sous-domaine).
* Plage CIDR : utilisez la notation CIDR pour définir des plages d’adresses IP, par exemple `192.168.10.0/24`.
* Adresse IPv4 : indiquez des adresses IPv4 individuelles, par exemple `192.168.10.10`.

## Formats de filtre pour Parental Control (Ruleset)

La fonctionnalité **Add a New Ruleset** dans Parental Control prend en charge les formats de filtre suivants dans le fichier texte en ligne :

* Nom de domaine : utilisez le nom de domaine, par exemple `instagram.com` (correspond à tous les sous-domaines).
* Sous-domaine : indiquez le sous-domaine complet, par exemple `www.instagram.com` (correspond uniquement à ce sous-domaine).

Lorsque vous créez le fichier texte en ligne, utilisez un filtre par ligne. Le routeur traitera chaque ligne selon le format spécifié et appliquera les règles correspondantes à la fonctionnalité VPN ou Parental Control.

En respectant ces formats de filtre, vous pouvez facilement créer et maintenir le fichier texte en ligne pour configurer les fonctions VPN et Parental Control sur votre routeur.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
