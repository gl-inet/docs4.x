# GoodCloud を使った技術サポート

GL.iNet の技術サポートを受けるために、GoodCloud 経由でデバイスを共有していただく必要がある場合があります。このガイドでは、デバイスを GL.iNet 技術サポートと共有する方法を説明します。

## GoodCloud とリモートアクセスを有効にする

GL.iNet 技術サポートとデバイスを共有する前に、ルーターに安定性確保のための追加のインターネット接続があることを確認してください。フェイルオーバー用のバックアップとして Ethernet または Repeater 接続を設定し、正常に動作することを確認してください。

次に、ルーターの Web 管理パネルにログインし、GoodCloud とリモートアクセスを有効にします。

- **ファームウェアバージョン 4.7.x 以降の場合**

  **CLOUD SERVICES** -> **GoodCloud** に移動し、右上の **Get Started** をクリックしてクラウドアカウントにログインします。アカウントをお持ちでない場合は、先に登録してください。

  ![get started log in](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/get_started_v4.7.x.png){class="glboxshadow"}

  ログインすると、デバイスは自動的にクラウドアカウントへバインドされます。

  続いて **GoodCloud** ページに移動し、**Remote SSH** と **Remote Web Access** を有効にして、**Apply** をクリックします。

  ![enable remote access 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.7.x.png){class="glboxshadow"}

- **ファームウェアバージョン 4.6.x 以前の場合**

  **APPLICATIONS** -> **GoodCloud** に移動し、**GoodCloud**、**Remote SSH**、**Remote Web Access** を有効にします。次に **Terms of Service & Privacy Policy** にチェックを入れ、**Apply** をクリックします。

  ![enable GoodCloud 4.6](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.6.x.png){class="glboxshadow"}

## クラウドアカウントにログインしてデバイスをバインドする

ルーターがファームウェア v4.7 以降の場合は、ルーターの Web 管理パネルでアカウントを登録し、そのまま直接ログインできます。ログインすると、現在のデバイスは自動的にクラウドアカウントへバインドされます。

ルーターがファームウェア v4.6 以前の場合は、以下の手順に従ってアカウントへログインし、デバイスをバインドしてください。

1. [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} にアクセスしてログインします。アカウントをお持ちでない場合は、先に登録してください。

2. デバイスを GoodCloud にバインドします。詳しくは [こちら](../interface_guide/cloud.md#add-device-in-your-account) を参照してください。

## GL.iNet 技術サポートとデバイスを共有する

1. [GoodCloud](https://www.goodcloud.xyz){target="\_blank"} にアクセスしてログインします。

2. **Devices** -> **Bound Devices** に移動し、共有したいデバイスをクリックします。

   ![bound devices](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/bound_devices.png){class="glboxshadow"}

3. デバイス詳細ページが開いたら、**SHARE** タブをクリックし、**Share Device** を選択します。

   ![share device](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device.png){class="glboxshadow"}

   次に、デバイスを GL.iNet 技術サポートと共有します。個人ネットワークを保護するため、**Auto Expire Sharing** を有効にし、有効期限を 7 日に設定することを推奨します。その後 **Confirm** をクリックします。

   ![share device with GL.iNet support](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device_confirm.png){class="glboxshadow"}

**プライバシー保護に関する声明**

1. GL.iNet 技術サポートと共有されたデバイスは、トラブルシューティング目的にのみ使用されます。GL.iNet サポートは、お客様の個人情報を保持、バックアップ、または閲覧しません。

2. パスワード保護の観点から、デバイスを GL.iNet サポートと共有する前に、Web 管理パネルのログインパスワードを一時的なものへ変更することを推奨します。トラブルシューティング完了後に元のパスワードへ戻してください。

## GL.iNet 技術サポートへ情報を提供する

デバイスを共有した後、リモートでのトラブルシューティングを行えるよう、担当する GL.iNet 技術サポートスタッフへ、ルーターの **MAC アドレス** と **管理者パスワード** をメールまたはフォーラムの PM で送ってください。

**同じ情報をメールと PM の両方で同時に送らないでください。**

- **メールで送る場合**: 担当の GL.iNet 技術サポートスタッフ宛てに、[support@gl-inet.com](mailto:support@gl-inet.com) へ送信してください。

- **公式フォーラムの PM で送る場合**: [公式フォーラム](https://forum.gl-inet.com){target="\_blank"} で、担当の GL.iNet 技術サポートスタッフへ PM（プライベートメッセージ）を送ってください。

  フォーラムでプライベートメッセージを送る手順は以下のとおりです。
  1. [公式フォーラム](https://forum.gl-inet.com){target="\_blank"} にアクセスします。
  2. やり取りしている GL.iNet サポートスタッフのユーザー名をクリックします。
  3. **Message** ボタンをクリックしてプライベートメッセージを送ります。

     ![How to send a private message](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/PM_via_forum.gif){class="glboxshadow"}

新規ユーザーの場合、GL.iNet 技術サポートへプライベートメッセージを送れないことがあります。その場合は、現在やり取りしている同じスレッド内で返信し、先に技術サポートスタッフからプライベートメッセージを送ってもらうよう依頼してください。

デバイス情報を公開の場へ書き込まないでください。共有は必ず PM を通じて、GL.iNet 技術サポートにのみ行ってください。

問題が解決したら、共有を解除し、ルーターの管理者パスワードを変更してください。

---

まだご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
