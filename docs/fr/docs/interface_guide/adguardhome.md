# AdGuard Home

AdGuard Home est un logiciel de blocage des publicités et du pistage à l’échelle du réseau. Une fois configuré, il protège tous les appareils de votre réseau domestique sans nécessiter de logiciel supplémentaire côté client.

## Modèles pris en charge

??? "Modèles pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

??? "Modèles non pris en charge"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Configuration

Connectez-vous au panneau d’administration web du routeur et allez à **APPLICATIONS** -> **AdGuard Home**.

Activez le commutateur pour activer AdGuard Home, puis cliquez sur **Apply**.

![adguard home apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/apply.png){class="glboxshadow"}

- **AdGuard Home Handle Client Requests** : si cette option est activée, les requêtes DNS des appareils clients seront traitées directement par AdGuard Home. AdGuard Home affichera les journaux de requêtes DNS des clients, mais les politiques VPN basées sur les domaines ne fonctionneront alors pas.

Cette page affiche des statistiques telles que les requêtes DNS, les domaines bloqués, etc., via l’API fournie par AdGuard Home.

![adguard home web panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/adguardhome_web_panel.png){class="glboxshadow"}

Cliquez ensuite sur **Settings Page**.

![adguard home started](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/settings_page.png){class="glboxshadow"}

Vous serez redirigé vers la page officielle des paramètres d’AdGuard Home, où vous pourrez effectuer une configuration avancée, notamment pour les règles de filtrage.

![adguard home settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/adguard_home/adguardhome_dashboard.png){class="glboxshadow"}

Si vous avez des questions, consultez le [centre d’assistance AdGuard Home](https://adguard.com/en/support.html){target="_blank"}.

---
