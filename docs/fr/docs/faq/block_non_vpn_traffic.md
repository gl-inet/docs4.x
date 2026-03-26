# Comment faire passer tout le trafic par le VPN ?

Si vous souhaitez que tout le trafic réseau du routeur soit acheminé via le VPN et que toutes les connexions Internet soient bloquées en cas de défaillance du VPN, suivez les étapes ci-dessous pour activer le **VPN Kill Switch**.

**Remarque** : configurez d'abord le client VPN sur votre routeur GL.iNet avant d'activer le **VPN Kill Switch**.

## Pour le firmware v4.7 ou antérieur

Connectez-vous au panneau d'administration Web de votre routeur, accédez à **VPN** -> **VPN Dashboard** -> section **VPN Client**, puis cliquez sur **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Activez **Block Non-VPN Traffic** (également appelé Kill Switch dans certaines versions du firmware), puis cliquez sur **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Remarque :** lorsque **Block Non-VPN Traffic** / Kill Switch est activé et que votre VPN est désactivé ou déconnecté, tous les appareils connectés au routeur ne pourront plus accéder à Internet afin d'éviter les fuites DNS.

## Pour le firmware v4.8 ou version ultérieure

Dans le firmware v4.8, le **VPN Kill Switch** a été divisé en deux modes.

- **Tunnel Kill Switch** : il est activé par défaut lorsque le tunnel VPN correspondant est activé.

- **Enhanced Kill Switch (in Policy Mode)** : il est désactivé par défaut afin que tout le trafic non couvert par les tunnels VPN et les stratégies ci-dessus puisse toujours accéder à Internet. En d'autres termes, il maintient un accès Internet normal pour le trafic hors VPN.

### Tunnel Kill Switch

Dans le panneau d'administration Web du routeur, accédez à **VPN** -> **VPN Dashboard**.

Si vous configurez votre routeur comme client VPN, le Kill Switch de ce tunnel VPN est activé par défaut dès que le VPN est activé.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN mode global)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN mode de stratégie)</small>

Cliquez sur l'icône d'engrenage à côté du nom du tunnel pour accéder à **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Le Kill Switch de ce tunnel est activé par défaut.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Enhanced Kill Switch

Cette fonction est disponible en **Policy Mode**.

Dans le panneau d'administration Web du routeur, accédez à **VPN** -> **VPN Dashboard**, basculez le mode VPN sur **Policy Mode**, puis recherchez en bas une section nommée **All Other Traffic**. Cette section peut varier légèrement selon la version du firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** (tout le reste du trafic) est un tunnel par défaut qui garantit un accès Internet normal pour le trafic non couvert par les tunnels VPN et les stratégies ci-dessus, ou pour le trafic ayant basculé depuis des connexions VPN. Ce tunnel est activé par défaut et s'exclut mutuellement avec **Enhanced Kill Switch**.

**Remarque** : si vous désactivez **All Other Traffic**, vous ne pourrez accéder à Internet que via le VPN. Tout le reste du trafic non correspondant sera bloqué. Ce réglage ne remplace pas le Kill Switch individuel de chaque tunnel.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

