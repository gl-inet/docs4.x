# Ethernet Port（ファームウェアv4.10）

**注**：このページの内容は現在Flint 4（GL-BE14000）で利用できます。他のモデルにもファームウェアv4.10で順次提供されます。

デバイスで別のファームウェアバージョンを使用している場合は、次の選択メニューから対応するガイドへ切り替えてください。

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [ファームウェアv4.9以前](ethernet_port.md)

</div>

---

Web管理パネルの左側で、**NETWORK** -> **Ethernet Port** の順に移動します。

このページには、ルーターのすべてのインターフェースが表示されます。各インターフェースの接続状態を確認し、Ethernetポートの役割（WANまたはLAN）を管理できるほか、MACアドレス、ネゴシエート速度、現在のリンク状態など、ポートの詳細を確認できます。また、作成済みの任意のサブネットに物理インターフェースを割り当てることもできます。

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**：ポートアイコンが青色で強調表示されている場合、物理リンクは有効です。

- **Link Down**：ポートアイコンがグレーの場合、物理リンクは無効です。

- **Speed**：Ethernetポートのネゴシエートされた伝送速度です。

- **MAC**：ポートのMACアドレスです。

- **VLAN Mode**：LANポートの動作モードをStandardまたはMultiple VLANsに設定できます。

- **Native Network**：LANポートに割り当てられる、タグなしのデフォルトサブネットです。

- **Allowed VLANs**：Multiple VLANsモードで、このポートの通過を許可するタグ付きVLANを指定します。

- **Settings**：クリックすると、各ポートの設定ページが開きます。

## WAN

このセクションには、ポートモード（WANまたはLAN）、MACアドレス、ネゴシエート速度が表示されます。

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**：物理WANポートの現在の動作モードです。必要に応じてLANに設定できます。

- **MAC Mode**：デフォルトはFactory Modeです。Clone ModeまたはRandom Modeに切り替えることができます。

- **MAC Address**：WANインターフェースのMACアドレスです。

- **Negotiated Network Port Rate**：WANインターフェースのネゴシエート速度です。有効なリンクが検出された場合にのみ表示されます。

## LAN

このセクションにはLANポートの設定が表示されます。必要に応じてEthernet Modeを**Standard**または**Multiple VLANs**に設定できます。

### Standardモード

Standardモードでは、端末の接続に使用する1つのVLAN（Untagged）のみを設定できます。

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**：LANインターフェースのネゴシエート速度です。有効なリンクが検出された場合にのみ表示されます。

- **Ethernet Mode**：デフォルトはStandard Modeです。
  
- **Access Network**：LANポートを異なるサブネットへ割り当てることで、ネットワークを分離できます。

設定後、Ethernet Portページに戻って設定内容を確認できます。

### Multiple VLANsモード

Multiple VLANsモードでは、1つのポートで複数のVLAN（Tagged）を使用できます。通常はAPや他のスイッチを接続する場合に使用します。

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**：LANインターフェースのネゴシエート速度です。有効なリンクが検出された場合にのみ表示されます。

- **VLAN Mode**：Multiple VLANsモードへ切り替えるには、Multiple VLANsタブをクリックします。

- **Untagged Traffic Handling**：ポートでのタグなしパケットの処理方法を設定します。パケットを直接破棄するか、ネイティブPVIDネットワークとして別のサブネットへ転送するかを選択できます。

- **Allowed Tagged Networks**：タグ付きモードでこのポートの通過を許可するVLANを指定します。リストからVLANネットワークを選択でき、一致するトラフィックのみが転送されます。

設定後、Ethernet Portページに戻って設定内容を確認できます。

一部のモデルでは、デュアルEthernet WAN構成でLAN 1をWANポートに切り替えることができます。詳細は[Dual-Ethernet WAN](#dual-ethernet-wan)を参照してください。

## Dual-Ethernet WAN

Dual-Ethernet WAN機能では、デフォルトのLAN Ethernetポートを2つ目のWANポートへ切り替えて、2本のEthernet回線でインターネットに接続できます。信頼性の高いバックアップ接続を提供し、対応する構成では、帯域幅を多く使用する処理向けに帯域幅の集約もサポートします。また、仕事用と個人用など、独立した2つのネットワークへ同時に接続できるため、追加のハードウェアを使用せずに柔軟性を高められます。

??? "対応モデル"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **注**：GL-E5800（Mudi 7）は、1つのEthernetポート（デフォルトはLAN、WANへ切り替え可能）と**OTG対応USB-Cポート**を搭載しています。Dual-Ethernet WAN用の2つ目のEthernetポートを追加するには、別売りのUSB‑C - EthernetアダプターをUSB‑Cポートに接続してください。

??? "非対応モデル"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

以下では、Flint 3（GL-BE9300）を例に、LANポートをWANポートへ切り替える手順を説明します。

1. **Ethernet Port**ページで**LAN1**の設定をクリックし、Configurationページを開きます。ポートの役割をWANへ切り替え、**Apply**をクリックします。
   
    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Ethernet Portページに戻り、ポートの役割がWANへ切り替わったことを確認します。
   
    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. 選択したポートがWANポートとして動作します。続いて、[こちら](multi-wan.md)からMulti-WANを設定できます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
