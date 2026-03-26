# Pourquoi est-ce que j'obtiens un message lors du test DDNS ?

Lorsque vous lancez le test DDNS sur la page Dynamic DNS, vous pouvez voir apparaître un message comme ci-dessous.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

Il ne s'agit ni d'un avertissement ni d'une erreur, mais d'un rappel indiquant l'état réseau de votre routeur.

Ce résultat reflète généralement la position de votre routeur dans le réseau. Par exemple, si votre routeur GL.iNet est configuré comme routeur secondaire dans votre réseau domestique, ce message s'affichera.

Il ne disparaîtra pas même si vous avez configuré une redirection de port sur votre routeur principal : cela indique simplement que le routeur se trouve derrière un NAT.

Si vous devez exposer des services à travers le NAT (par exemple pour un accès à distance), des réglages supplémentaires sont nécessaires.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

