# GoodCloud経由で技術サポートを受ける

GL.iNetから技術サポートを受けるために、GoodCloud経由でデバイスを共有する必要がある場合があります。このガイドでは、GL.iNet技術サポートへデバイスを共有する方法を紹介します。

## GoodCloudとリモートアクセスを有効にする

GL.iNet技術サポートへデバイスを共有する前に、安定性のためにルーターに追加のインターネット接続があることを確認してください。Ethernet 接続または Repeater 接続をフェイルオーバー用バックアップとして設定し、正常に動作することを確認してください。

その後、ルーターのWeb管理パネルにログインして、GoodCloud とリモートアクセスを有効にします。

- **ファームウェアバージョン 4.7.x 以降**

    **CLOUD SERVICES** -> **GoodCloud** に移動し、**Get Started** をクリックして右上からCloudアカウントへログインしてください。アカウントがない場合は、先に登録してください。

    ![get started log in](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/get_started_v4.7.x.png){class="glboxshadow"}

    ログインすると、デバイスは自動的にCloudアカウントへ紐付けられます。

    **GoodCloud** ページに戻り、**Remote SSH** と **Remote Web Access** を有効にして、**Apply** をクリックします。

    ![enable remote access 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.7.x.png){class="glboxshadow"}

- **ファームウェアバージョン 4.6.x 以前**

    **APPLICATIONS** -> **GoodCloud** に移動し、**GoodCloud**、**Remote SSH**、**Remote Web Access** を有効にします。**Terms of Service & Privacy Policy** を確認してチェックし、**Apply** をクリックします。

    ![enable GoodCloud 4.6](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.6.x.png){class="glboxshadow"}

## Cloudアカウントにログインしてデバイスを紐付ける

ルーターがファームウェア v4.7 以降で動作している場合は、ルーターのWeb管理パネルでアカウントを登録して直接ログインできます。ログインすると、現在のデバイスは自動的にCloudアカウントへ紐付けられます。

ルーターがファームウェア v4.6 以前で動作している場合は、以下の手順でアカウントへログインし、デバイスを紐付けてください。

1. [GoodCloud](https://www.goodcloud.xyz){target="_blank"} にアクセスしてアカウントへログインします。アカウントがない場合は、先に登録してください。

2. デバイスをGoodCloudに紐付けます。詳細は[このリンク](../interface_guide/cloud.md#add-device-in-your-account)を参照してください。

## GL.iNet技術サポートとデバイスを共有する

1. [GoodCloud](https://www.goodcloud.xyz){target="_blank"} にアクセスしてログインします。

2. **Devices** -> **Bound Devices** に移動し、共有したいデバイスをクリックします。

    ![bound devices](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/bound_devices.png){class="glboxshadow"}

3. デバイス詳細ページが表示されたら、**SHARE** タブを開いて **Share Device** をクリックします。

    ![share device](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device.png){class="glboxshadow"}

    その後、GL.iNet Technical Support とデバイスを共有します。個人ネットワークを保護するため、**Auto Expire Sharing** を有効にして有効期限を7日に設定してください。その後、**Confirm** をクリックします。

    ![share device with GL.iNet support](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device_confirm.png){class="glboxshadow"}

**Privacy Protection Statement**

1. GL.iNet Technical Support と共有されたデバイスは、トラブルシューティング目的でのみ使用されます。GL.iNet Support が個人情報を保持、バックアップ、または閲覧することはありません。

2. パスワード保護のため、デバイスをGL.iNet Supportと共有する前に、Web管理パネルのログインパスワードを一時的なものへ変更することを推奨します。トラブルシューティング完了後に元のパスワードへ戻せます。

## GL.iNet技術サポートへ情報を提供する

デバイス共有後、リモートトラブルシューティングのために、ルーターの **MAC address** と **admin password** を、担当のGL.iNet技術サポートスタッフへメールまたはフォーラムPMで送ってください。

**メールとPMの両方へ同時に送信しないでください。**

- **メールで送る場合**: この情報を担当のGL.iNet技術サポートスタッフへ [support@gl-inet.com](mailto:support@gl-inet.com) 宛に送信してください。

- **公式フォーラムのPMで送る場合**: [公式フォーラム](https://forum.gl-inet.com){target="_blank"} で担当のGL.iNet技術サポートスタッフへ PM（プライベートメッセージ）を送信してください。

    フォーラムでプライベートメッセージを送る手順は次のとおりです。

    1. [公式フォーラム](https://forum.gl-inet.com){target="_blank"} にアクセスします。
    2. やり取りしているGL.iNetサポートスタッフのユーザー名をクリックします。
    3. **Message** ボタンをクリックしてプライベートメッセージを送信します。

        ![How to send a private message](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/PM_via_forum.gif){class="glboxshadow"}

フォーラムの新規ユーザーは、GL.iNet技術サポートへプライベートメッセージを送れないことがあります。その場合は、やり取りしている同じスレッドで返信し、先にサポートスタッフからプライベートメッセージを送ってもらうよう依頼してください。

デバイス情報は公開の場で共有せず、必ず PM で GL.iNet技術サポートにのみ共有してください。

問題が解決したら、共有を解除し、ルーターの管理者パスワードを変更してください。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
