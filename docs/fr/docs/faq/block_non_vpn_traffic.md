# Comment faire passer tout le trafic par le VPN ? {#how-to-let-all-data-go-through-vpn}

Si vous souhaitez que tout le trafic réseau du routeur soit acheminé via le VPN et que toutes les connexions Internet soient bloquées en cas de défaillance du VPN, suivez les étapes ci-dessous pour activer le **VPN Kill Switch**.

**Remarque** : configurez d'abord le client VPN sur votre routeur GL.iNet avant d'activer le **VPN Kill Switch**.

## Pour le firmware v4.7 ou antérieur {#for-firmware-v47-or-earlier}

Connectez-vous au panneau d'administration Web de votre routeur, accédez à **VPN** -> **VPN Dashboard** -> section **VPN Client**, puis cliquez sur **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Activez **Block Non-VPN Traffic** (également appelé Kill Switch dans certaines versions du firmware), puis cliquez sur **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Remarque :** lorsque **Block Non-VPN Traffic** / Kill Switch est activé et que votre VPN est désactivé ou déconnecté, tous les appareils connectés au routeur ne pourront plus accéder à Internet afin d'éviter les fuites DNS.

## Pour le firmware v4.8 {#for-firmware-v48}

Dans le firmware v4.8, le **VPN Kill Switch** a été divisé en deux modes.

- **Tunnel Kill Switch** : il est activé par défaut lorsque le tunnel VPN correspondant est activé.

- **Enhanced Kill Switch (in Policy Mode)** : il est désactivé par défaut afin que tout le trafic non couvert par les tunnels VPN et les stratégies ci-dessus puisse toujours accéder à Internet. En d'autres termes, il maintient un accès Internet normal pour le trafic hors VPN.

### Tunnel Kill Switch {#tunnel-kill-switch}

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

### Enhanced Kill Switch {#enhanced-kill-switch}

Cette fonction est disponible en **Policy Mode**.

Dans le panneau d'administration Web du routeur, accédez à **VPN** -> **VPN Dashboard**, basculez le mode VPN sur **Policy Mode**, puis recherchez en bas une section nommée **All Other Traffic**. Cette section peut varier légèrement selon la version du firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** est le tunnel par défaut. Le trafic qui ne correspond à aucun des tunnels VPN ou politiques ci-dessus, ainsi que le trafic redirigé ici à la suite d’un basculement VPN, conserve un accès normal à Internet. Le tunnel est activé par défaut. Si vous le désactivez, tout ce trafic est bloqué, y compris celui qui serait redirigé après un basculement VPN. Seul le trafic pris en charge par les tunnels VPN configurés peut accéder à Internet. La protection est la même qu’avec **Enhanced Kill Switch**.

**All Other Traffic** Le réglage **All Other Traffic** n’annule pas le Kill Switch propre à chaque tunnel.

## Pour le firmware v4.9 et les versions ultérieures {#for-firmware-v49-and-above}

À partir du firmware v4.9, deux types de Kill Switch VPN sont disponibles, **Tunnel Kill Switch** et **Enhanced Kill Switch**.

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

Dans le panneau d'administration Web du routeur, accédez à **VPN** -> **VPN Dashboard**.

Si vous configurez votre routeur comme client VPN, le Kill Switch de ce tunnel VPN est activé par défaut dès que le VPN est activé.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Cliquez sur l'icône d'engrenage à côté du nom du tunnel pour accéder à **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Le Kill Switch de ce tunnel est activé par défaut.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Enhanced Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

Dans le panneau d'administration Web du routeur, accédez à **VPN** -> **VPN Dashboard**. Cliquez ensuite sur l’icône en forme d’engrenage dans le coin supérieur droit.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

Le réglage de la politique de trafic propose **Allow Non-VPN Traffic** et **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic** : Activé par défaut. Le trafic qui ne correspond à aucun des tunnels VPN ou politiques ci-dessus, ainsi que le trafic redirigé ici à la suite d’un basculement VPN, conserve un accès normal à Internet.

- **Enhanced Kill Switch** : Lorsque cette option est activée, tous les appareils doivent passer par un VPN pour accéder à Internet. Tout trafic qui ne correspond à aucun tunnel VPN est bloqué. Ce réglage n’annule pas le Kill Switch propre à chaque tunnel.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

