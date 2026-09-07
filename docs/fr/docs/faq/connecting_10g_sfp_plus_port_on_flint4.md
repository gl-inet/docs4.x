# Connexion du port 10G SFP+ de Flint 4

Flint 4 (GL-BE14000) est équipé d’un port 10G SFP+ qui peut fonctionner en mode WAN ou LAN. Ce port prend en charge plusieurs types de modules et câbles SFP+ pour les connexions Ethernet sur fibre optique ou cuivre, notamment les liaisons fibre longue distance, le câblage conventionnel à paire torsadée et la terminaison fibre PON avancée.

Cet article décrit trois options de connexion du port SFP+ de Flint 4 (GL-BE14000), avec leurs scénarios d’utilisation, topologies, avantages et inconvénients, précautions et modèles compatibles.

## Solution 1. Émetteur-récepteur optique + câble à fibre optique

### 1.1 Scénarios

Cette solution est destinée aux connexions Ethernet 10G fiables sur de longues distances. Les utilisations courantes comprennent :

- la connexion à une liaison montante Ethernet 10G sur fibre d’un FAI, pour un accès haut débit domestique ou professionnel rapide ;
- le déploiement de liaisons réseau longue distance en intérieur ou en extérieur, par exemple entre Flint 4 et un commutateur 10G distant, entre les étages d’une habitation ou pour le réseau dorsal d’un petit bureau.

### 1.2 Topologie

Port 10G SFP+ de Flint 4 → Émetteur-récepteur optique 10G SFP+ standard (SR/MR/LR) → Câble à fibre optique → Commutateur réseau 10G distant / terminal fibre-Ethernet du FAI

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Avantages et inconvénients

Le tableau ci-dessous évalue les principaux aspects liés aux performances et à l’utilisation de la solution avec émetteur-récepteur optique et câble à fibre optique. Les notes sous forme d’étoiles et les remarques détaillées sont fournies à titre indicatif :

|Critère|Note|Remarques|
|---|---|---|
|Distance de transmission|★★★★★|Prend en charge des distances allant jusqu’à 300 m sur fibre multimode ou plus de 10 km sur fibre monomode, et convient ainsi aux connexions longue distance.|
|Résistance aux interférences|★★★★★|La transmission du signal optique est insensible aux interférences électromagnétiques, à l’électricité statique et à la diaphonie, pour un fonctionnement stable dans les environnements complexes.|
|Économie d’énergie|★★★★★|Offre une faible consommation électrique et un faible dégagement de chaleur. La conception éprouvée du chipset permet un fonctionnement stable et prolongé à pleine charge sans surchauffe.|
|Compatibilité|★★★★★|Officiellement pris en charge et conforme aux protocoles Ethernet 10G standard ; aucune adaptation du firmware n’est nécessaire.|
|Facilité de déploiement|★★★☆☆|Nécessite de connaître les exigences de base d’une connexion fibre. Une manipulation incorrecte peut atténuer le signal, ce qui rend le déploiement plus complexe qu’avec un câblage cuivre.|
|Coût|★★★☆☆|Nécessite des émetteurs-récepteurs optiques et des câbles à fibre supplémentaires ; le coût global est supérieur à celui d’une solution traditionnelle à paire torsadée.|

### 1.4 Précautions

- Seuls les émetteurs-récepteurs optiques Ethernet 10G standard sont pris en charge ; les modules optiques utilisant le protocole PON ne conviennent pas à cette solution.

- Sélectionnez des modules optiques monomodes ou multimodes et des câbles à fibre adaptés à la distance de transmission réelle afin d’éviter une baisse du débit ou l’échec de la liaison.

- Cette solution prend uniquement en charge les services Ethernet 10G sur fibre du FAI et ne peut pas être directement connectée aux lignes fibre résidentielles GPON/XGS-PON traditionnelles.

### 1.5 Modèles compatibles

Vous trouverez ci-dessous quelques émetteurs-récepteurs optiques standard dont la compatibilité avec Flint 4 a été testée par GL.iNet et des utilisateurs. Cette liste est fournie à titre indicatif uniquement.

|Modèle|Testeur|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Utilisateur|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Utilisateur|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Utilisateur|
|XZSNET SFP10G-SR|GL.iNet|
|10Gtek AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|10Gtek AZS85-192-M1 25G SFP28-SR 850nm 100m|GL.iNet|
|10Gtek ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|10Gtek ASF85-24-X2-D 1.25G SFP-SX 850nm 550m|GL.iNet|
|FS Cisco SFP-10G-SR Compatible 10GBASE-SR|GL.iNet|
|FS Juniper EX-SFP-10GE-SR 10GBASE-SR SFP+|GL.iNet|
|FS Arista SFP-10G-SR 10GBASE-SR SFP+|GL.iNet|
|FS Brocade 10G-SFPP-SR 10GBASE-SR SFP+|GL.iNet|
|HUAWEI 6G-850nm-120m-MM-SFP+ MTRS-6A11-01|GL.iNet|
|HUAWEI 2.5G-1310nm-SM-ESFP MXPD-483II|GL.iNet|
|netLINK 10G/850nm/300m/DDM HTB-10G-SR|GL.iNet|
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100m|GL.iNet|
|H!Fiber ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Utilisateur|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Utilisateur|

## Solution 2. Module SFP+ vers RJ45 (SFP‑10G‑T)

### 2.1 Scénarios

Le module SFP-10G-T convertit le logement SFP+ en interface RJ45 à paire torsadée standard. Il convient ainsi aux réseaux 10G courte distance utilisant des câbles Ethernet conventionnels. Les applications courantes comprennent la connexion de Flint 4 à un commutateur 10G ou à un NAS proche, l’ajout d’un port RJ45 10G sans installer de fibre et la création d’un LAN domestique ou SOHO à haut débit avec le câblage à paire torsadée existant. Cette option convient aux utilisateurs qui ont besoin d’Ethernet 10G sans disposer d’un câblage fibre.

### 2.2 Topologie

Port 10G SFP+ de Flint 4 → Module SFP+ vers RJ45 (SFP‑10G‑T) → Câble à paire torsadée CAT6A/CAT7 → Commutateur 10G / appareil terminal filaire 10G

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Avantages et inconvénients

Le tableau ci-dessous évalue les principaux aspects liés aux performances et à l’utilisation de la solution avec module SFP+ vers RJ45 (SFP‑10G‑T). Les notes sous forme d’étoiles et les remarques détaillées sont fournies à titre indicatif :

|Critère|Note|Remarques|
|---|---|---|
|Distance de transmission|★★☆☆☆|Le PHY limite la distance de transmission stable à 30 m, ce qui rend le module inadapté au câblage longue distance.|
|Résistance aux interférences|★★★☆☆|La transmission traditionnelle à paire torsadée est sensible aux interférences électromagnétiques et à la diaphonie dans les installations complexes.|
|Économie d’énergie|★★☆☆☆|Consomme davantage d’énergie et produit beaucoup de chaleur sous forte charge continue. Une dissipation thermique adéquate est nécessaire pour une utilisation prolongée.|
|Compatibilité|★★★★☆|Compatible avec les appareils RJ45 10G standard. Un câblage CAT6A ou CAT7 est requis pour une transmission 10G stable.|
|Facilité de déploiement|★★★★★|Offre un déploiement prêt à l’emploi sans configuration du chemin optique et fonctionne avec un câblage Ethernet conventionnel.|
|Coût|★★★★☆|Permet de réutiliser le câblage RJ45 existant sans installer de fibre, bien qu’un module 10GBASE-T distinct soit nécessaire.|

### 2.4 Précautions

- Utilisez des câbles Ethernet CAT6A ou de catégorie supérieure pour assurer une transmission 10G stable. Les câbles de catégorie inférieure peuvent réduire le débit ou provoquer des pertes de paquets.

- Limitez la longueur du câblage à 30 mètres ; tout dépassement peut provoquer une instabilité de la liaison, une baisse du débit ou une déconnexion.

- Prévoyez un espace de dissipation thermique autour du module SFP‑10G‑T afin d’éviter les pannes dues à la surchauffe.

### 2.5 Modèles compatibles

Vous trouverez ci-dessous quelques modules SFP+ vers RJ45 dont la compatibilité avec Flint 4 a été testée par GL.iNet et des utilisateurs. Cette liste est fournie à titre indicatif uniquement.

|Modèle|Testeur|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Utilisateur|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Utilisateur|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Utilisateur|

## Solution 3. Module PON‑ONU SFP+

### 3.1 Scénarios

Le module PON-ONU SFP+ fournit les fonctions d’un modem optique ONU, ce qui permet au port SFP+ de Flint 4 de terminer directement les lignes fibre résidentielles GPON/XGS-PON traditionnelles. Cette option combine l’accès fibre et le routage dans un seul appareil, ce qui évite d’utiliser un modem optique externe distinct. Elle est destinée aux déploiements avancés par des utilisateurs expérimentés, en particulier à ceux qui souhaitent réduire le nombre d’appareils sur leur réseau domestique et connecter directement le routeur à une ligne fibre PON du FAI.

### 3.2 Topologie

Port 10G SFP+ de Flint 4 → Module PON‑ONU SFP+ → Ligne fibre GPON/XGS-PON du FAI (câble de branchement, répartiteur PON et OLT du FAI inclus)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Avantages et inconvénients

Le tableau ci-dessous évalue les principaux aspects liés aux performances et à l’utilisation de la solution avec module PON‑ONU SFP+. Les notes sous forme d’étoiles et les remarques détaillées sont fournies à titre indicatif :

|Critère|Note|Remarques|
|---|---|---|
|Distance de transmission|★★★★★|Prend en charge les distances de transmission PON standard pour les accès fibre résidentiels et professionnels courants.|
|Résistance aux interférences|★★★★★|La transmission par fibre optique offre une excellente résistance aux interférences et un signal stable, conformément aux normes courantes d’accès fibre PON.|
|Économie d’énergie|★★☆☆☆|Dégagement de chaleur élevé à haut débit ; une dissipation thermique auxiliaire est indispensable pour éviter une baisse des performances et des déconnexions.|
|Compatibilité|★★☆☆☆|Il s’agit d’une solution non officielle destinée aux utilisateurs expérimentés. La compatibilité dépend de la liste blanche du FAI et du modèle du module, et le fonctionnement à long terme peut être instable.|
|Facilité de déploiement|★★☆☆☆|Nécessite une confirmation préalable du FAI, la configuration de l’authentification SN/PLOAM et un refroidissement adéquat. Le déploiement est relativement complexe.|
|Coût|★★★☆☆|Supprime le coût d’un modem optique distinct, mais peut affecter des services tels que l’IPTV et la téléphonie et n’inclut pas d’assistance technique officielle.|

### 3.4 Précautions

- **Confirmez au préalable l’autorisation du FAI** : vérifiez auprès de l’opérateur si du matériel ONU tiers appartenant au client peut accéder au réseau PON et obtenez les paramètres d’authentification obligatoires, notamment le code d’enregistrement SN et le mot de passe PLOAM.

- **La dissipation thermique est obligatoire** : équipez le module PON‑ONU d’un dispositif de dissipation thermique auxiliaire afin d’éviter la réduction de fréquence, la perte de paquets et les déconnexions dues à une température élevée.

- **Aucune garantie de service** : GL.iNet ne fournit aucune assistance technique pour cette option. Les problèmes tels que l’instabilité du réseau, les variations de débit ou les incidents affectant des services à valeur ajoutée ne sont couverts ni par le firmware officiel ni par le service après-vente.

- Les règles de liste blanche des modèles de modules varient selon les opérateurs. Avant l’achat, confirmez auprès de l’opérateur les modèles de modules PON pris en charge.

### 3.5 Modèles compatibles

Vous trouverez ci-dessous quelques modules PON-ONU SFP+ dont la compatibilité avec Flint 4 a été testée par GL.iNet et des utilisateurs. Cette liste est fournie à titre indicatif uniquement.

|Modèle|Testeur|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Utilisateur|

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
