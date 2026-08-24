# Connexion du port 10G SFP+ de Flint 4

Flint 4 (GL‑BE14000) est équipé d’un port 10G SFP+ qui peut fonctionner en mode WAN ou LAN. Ce port est compatible avec plusieurs types de modules et câbles SFP+ pour les connexions Ethernet optiques et cuivre. Il répond ainsi à différents besoins réseau, notamment les accès fibre longue distance, le câblage conventionnel à paire torsadée et la terminaison fibre PON avancée.

Vous trouverez ci-dessous une présentation détaillée des trois solutions de connexion du port SFP+ de Flint 4 (GL-BE14000). Les scénarios d’utilisation, topologies, avantages et inconvénients, précautions et modèles compatibles sont fournis à titre indicatif uniquement.

## Solution 1. Émetteur-récepteur optique + câble à fibre optique

### 1.1 Scénarios

Cette solution convient aux réseaux Ethernet 10G longue distance exigeant une grande stabilité. Elle est principalement utilisée dans les deux scénarios suivants :

- connexion à une liaison montante Ethernet 10G entièrement en fibre d’un FAI, pour un accès haut débit domestique ou professionnel à très grande vitesse ;
- déploiement d’une interconnexion réseau intérieure ou extérieure longue distance, par exemple entre Flint 4 et un commutateur 10G distant, pour un câblage domestique entre plusieurs étages ou pour le réseau dorsal d’un petit bureau.

### 1.2 Topologie

Port 10G SFP+ de Flint 4 → Émetteur-récepteur optique 10G SFP+ standard (SR/MR/LR) → Câble à fibre optique → Commutateur réseau 10G distant / terminal fibre-Ethernet du FAI

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Avantages et inconvénients

Le tableau ci-dessous évalue les principaux aspects liés aux performances et à l’utilisation de la solution avec émetteur-récepteur optique et câble à fibre optique. Les notes sous forme d’étoiles et les remarques détaillées sont fournies à titre indicatif :

|Critère|Note|Remarques|
|---|---|---|
|Distance de transmission|★★★★★|Prend en charge jusqu’à 300 m en multimode ou plus de 10 km en monomode, au-delà des limites des câbles cuivre, et convient aux réseaux longue distance.|
|Résistance aux interférences|★★★★★|La transmission du signal optique est insensible aux interférences électromagnétiques, à l’électricité statique et à la diaphonie, pour un fonctionnement stable dans les environnements complexes.|
|Économie d’énergie|★★★★★|Faible consommation électrique et faible dégagement de chaleur ; la conception éprouvée de la puce permet un fonctionnement stable et prolongé à pleine charge sans risque de surchauffe.|
|Compatibilité|★★★★★|Entièrement pris en charge officiellement, conforme aux protocoles Ethernet 10G standard, sans risque d’adaptation du micrologiciel.|
|Facilité de déploiement|★★★☆☆|Nécessite de connaître les spécifications de raccordement de base de la fibre ; une manipulation incorrecte peut atténuer le signal, ce qui rend l’installation légèrement plus complexe qu’avec un câblage cuivre.|
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

Le module SFP‑10G‑T convertit le logement optique SFP+ en interface standard RJ45 à paire torsadée. Il convient aux réseaux 10G courte distance utilisant des câbles réseau conventionnels. Les utilisations courantes incluent la connexion courte distance entre Flint 4 et des commutateurs 10G ou appareils NAS, l’ajout rapide de ports réseau 10G RJ45 sans installer de fibre et le câblage d’un réseau local domestique ou SOHO à haut débit conservant les paires torsadées existantes. Il s’agit de la meilleure solution de remplacement pour les utilisateurs qui ont besoin d’Ethernet 10G sans disposer d’un câblage fibre.

### 2.2 Topologie

Port 10G SFP+ de Flint 4 → Module SFP+ vers RJ45 (SFP‑10G‑T) → Câble à paire torsadée CAT6A/CAT7 → Commutateur 10G / appareil terminal filaire 10G

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Avantages et inconvénients

Le tableau ci-dessous évalue les principaux aspects liés aux performances et à l’utilisation de la solution avec module SFP+ vers RJ45 (SFP‑10G‑T). Les notes sous forme d’étoiles et les remarques détaillées sont fournies à titre indicatif :

|Critère|Note|Remarques|
|---|---|---|
|Distance de transmission|★★☆☆☆|Limitée par le matériel de la puce PHY : la distance de transmission stable maximale est de seulement 30 mètres et ne convient pas au câblage longue distance.|
|Résistance aux interférences|★★★☆☆|La transmission traditionnelle à paire torsadée est sensible aux interférences électromagnétiques et à la diaphonie dans les installations complexes.|
|Économie d’énergie|★★☆☆☆|Consommation élevée et dégagement de chaleur important sous forte charge continue ; une gestion de la dissipation thermique est nécessaire pour une utilisation prolongée.|
|Compatibilité|★★★★☆|Compatible avec tous les terminaux RJ45 10G standard ; seuls les câbles CAT6A/CAT7 assurent une transmission 10G stable.|
|Facilité de déploiement|★★★★★|Prêt à l’emploi, sans réglage du chemin optique ; compatible avec les pratiques habituelles de déploiement de câbles réseau et très simple à installer.|
|Coût|★★★★☆|Réutilise le câblage RJ45 existant sans coût de conversion à la fibre ; seul un module 10G-T doit être acheté séparément.|

### 2.4 Précautions

- Utilisez impérativement des câbles réseau CAT6A ou de catégorie supérieure pour assurer une transmission 10G stable ; les câbles CAT6 et de catégorie inférieure entraînent une baisse de débit et des pertes de paquets.

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

Le module PON‑ONU SFP+ intègre toutes les fonctions d’un modem optique ONU, ce qui permet au port SFP+ de Flint 4 de terminer directement les lignes fibre résidentielles GPON/XGS-PON traditionnelles. Cette solution évite d’utiliser un modem optique externe indépendant et assure l’accès fibre et le routage avec un seul appareil. Elle est destinée aux configurations réseau avancées pour utilisateurs expérimentés, notamment à ceux qui souhaitent réduire le nombre d’équipements de leur réseau domestique et connecter directement le routeur aux lignes fibre PON de l’opérateur.

### 3.2 Topologie

Port 10G SFP+ de Flint 4 → Module PON‑ONU SFP+ → Ligne fibre GPON/XGS-PON du FAI (câble de branchement, répartiteur PON et OLT du FAI inclus)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Avantages et inconvénients

Le tableau ci-dessous évalue les principaux aspects liés aux performances et à l’utilisation de la solution avec module PON‑ONU SFP+. Les notes sous forme d’étoiles et les remarques détaillées sont fournies à titre indicatif :

|Critère|Note|Remarques|
|---|---|---|
|Distance de transmission|★★★★★|S’adapte aux distances de transmission standard de la fibre PON et couvre tous les scénarios d’accès fibre domestiques et professionnels courants.|
|Résistance aux interférences|★★★★★|La transmission par fibre optique offre une excellente résistance aux interférences et un signal stable, conformément aux normes courantes d’accès fibre PON.|
|Économie d’énergie|★★☆☆☆|Dégagement de chaleur élevé à haut débit ; une dissipation thermique auxiliaire est indispensable pour éviter une baisse des performances et des déconnexions.|
|Compatibilité|★★☆☆☆|Solution pour utilisateurs expérimentés non validée officiellement ; la compatibilité dépend de la liste blanche du FAI et du modèle du module, et le fonctionnement à long terme peut être instable.|
|Facilité de déploiement|★★☆☆☆|Nécessite une confirmation préalable du FAI, la configuration de l’authentification SN/PLOAM et l’optimisation de la dissipation thermique ; le déploiement est globalement complexe.|
|Coût|★★★☆☆|Supprime le coût d’un modem optique indépendant, mais présente des risques pour certains services, notamment l’indisponibilité de l’IPTV ou de la téléphonie et l’absence d’assistance technique officielle.|

### 3.4 Précautions

- **Confirmez au préalable l’autorisation du FAI** : vérifiez auprès de l’opérateur si du matériel ONU tiers appartenant au client peut accéder au réseau PON et obtenez les paramètres d’authentification obligatoires, notamment le code d’enregistrement SN et le mot de passe PLOAM.

- **La dissipation thermique est obligatoire** : équipez le module PON‑ONU d’un dispositif de dissipation thermique auxiliaire afin d’éviter la réduction de fréquence, la perte de paquets et les déconnexions dues à une température élevée.

- **Aucune garantie de service** : GL.iNet ne fournit aucune assistance technique pour cette solution. Les problèmes tels que l’instabilité du réseau, les variations de débit et les anomalies des services à valeur ajoutée ne peuvent pas être résolus par le micrologiciel officiel ni par le service après-vente.

- Les règles de liste blanche des modèles de modules varient selon les opérateurs. Avant l’achat, confirmez auprès de l’opérateur les modèles de modules PON pris en charge.

### 3.5 Modèles compatibles

Vous trouverez ci-dessous quelques modules PON-ONU SFP+ dont la compatibilité avec Flint 4 a été testée par GL.iNet et des utilisateurs. Cette liste est fournie à titre indicatif uniquement.

|Modèle|Testeur|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Utilisateur|

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
