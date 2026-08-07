# USB-C OTG とは何か、USB-C OTG でネットワークを共有する方法

## USB OTG
**USB OTG** (On-The-Go) は、ルーターなどの対応デバイスが **Host** と **Device** の役割を切り替えられる USB 規格です。別のホストデバイスなしで、直接データ転送や電源のやり取りを行えます。

**USB OTG** では、次の 2 つのモードを切り替えられます。

- デバイスが USB OTG によって **Host mode** に切り替わると、USB ホストとして動作し、データ転送を開始し、電力を供給し、接続された 2 台のデバイス間の読み書き操作を制御します。

- **Device mode** では、デバイスは周辺機器として動作し、ホストから電力を受け取り、ホストのコマンドに受動的に応答します。自分から通信を開始することはできません。

## Mudi 7 で USB-C OTG 経由のネットワーク共有

Mudi 7 の OTG 対応 USB-C ポートは、外部デバイスとの柔軟なネットワーク共有を行うため、**Device** または **Host** モードで動作します。

### コンピューターに接続する

ほとんどのコンピューターはホストとしてのみ動作し、OTG には対応していません。コンピューターを USB でルーターに接続すると、ルーターにモード選択画面が表示されます。任意のモードを選択すると、Mudi 7 が自動的に役割をネゴシエートします。その後、コンピューターは Mudi 7 を USB アダプターとして認識し、追加ドライバーなしで直接インターネットへアクセスできます。

### スマートフォンに接続する

- **Device Mode**: Mudi 7 が USB デバイスとして動作し、ネットワークをスマートフォンへ共有します。

- **Host Mode**: スマートフォンで USB Tethering を有効にすると、スマートフォンのセルラーネットワークを USB 経由で Mudi 7 に共有できます。この USB 接続は独立した WAN インターフェースとして機能し、Multi-WAN を利用できます。

!!! Note

    1. スマートフォンの OTG 機能で相互接続する場合は、スマートフォンが OTG に対応していることを確認し、データ通信対応の USB ケーブルを使用してください。充電専用ケーブルではネットワーク信号を送信できません。

    2. Device Mode が有効な場合、スマートフォンにはネットワーク接続通知が表示されません。動作を確認するには、スマートフォンの設定でネットワーク状態を確認するか、接続テストを実行してください。

        たとえば、**Device Mode** で Mudi 7 のネットワークをスマートフォン（例: iPhone 17 Pro）に共有する場合は、次の手順で Device Mode が有効であることを確認します。

        1. OTG 対応の USB ケーブルを使用して、Mudi 7 の USB 3.1 ポートを iPhone 17 Pro に接続します。

        2. Mudi 7 で **Device Mode** を選択します。

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. スマートフォンの設定で、以下のスクリーンショットのように Mudi 7 がスマートフォンへネットワークアクセスを提供していることを確認できます。

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} にアクセスするか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
