# Opal (GL-SFT1200) でWi-Fi通話を動作させる方法 {#how-to-make-wi-fi-calling-work-on-opal-gl-sft1200}

## ファームウェアのアップグレード {#upgrade-firmware}

Web管理パネルで、SYSTEM -> Upgradeに移動し、ファームウェアを最新バージョンにアップグレードします。最新バージョンを確認するには、[ファームウェアダウンロードセンター](https://dl.gl-inet.com/){target="_blank"}を参照してください。

![opal4317](https://static.gl-inet.com/docs/router/en/4/faq/wifi_call/opal4317.jpg){class="glboxshadow"}

## ネットワークアクセラレーションを無効にする {#disable-network-acceleration}

私たちの経験とお客様からのフィードバックによると、ネットワーク/ハードウェアアクセラレーションを無効にすると、Wi-Fi通話が正常に動作するようになります。

ファームウェアアップグレード後、Web管理パネルにログインし、**NETWORK** -> **Network Acceleration**に移動し、無効にします。

![networkacc](https://static.gl-inet.com/docs/router/en/4/faq/wifi_call/netacc.jpg){class="glboxshadow"}
