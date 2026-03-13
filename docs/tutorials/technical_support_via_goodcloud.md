# GoodCloudを通じた技術サポート

GL.iNetからの技術サポートを受けるために、デバイスをGoodCloudで共有する必要がある場合があります。このガイドでは、デバイスをGL.iNet技術サポートと共有する方法を説明します。

## GoodCloudとリモートアクセスを有効にする

GL.iNet技術サポートとデバイスを共有する前にルー器に安定性のための追加インターネット接続があることを確認してください。フェイルオーバーbackupとしてEthernetまたはRepeater接続を設定し、正しく動作することを確認してください。

次に、ルーターのWeb管理パネルにログインし、GoodCloudとリモートアクセスを有効にします。

- **ファームウェアバージョン4.7.xで上の場合**

    **クラウドサービス** -> **GoodCloud**に移動し、右上の**始める**をクリックしてクラウドアカウントにログインします。アカウントをお持ちでない場合は、まず登録してください。

    ![get started log in](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/get_started_v4.7.x.png){class="glboxshadow"}
    
    ログインすると、デバイスは自動的にクラウドアカウントにバインドされます。
    
    **GoodCloud**ページに移動し、**リモートSSH**と**リモートWebアクセス**を有効にし、**適用**をクリックします。

    ![enable remote access 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.7.x.png){class="glboxshadow"}

- **ファームウェアバージョン4.6.xで前の場合**

    **アプリケーション** -> **GoodCloud**に移動し、**GoodCloud**、**リモートSSH**と**リモートWebアクセス**を有効にし、**利用規約とプライバシーポリシーに同意**し、**適用**をクリックします。

    ![enable GoodCloud 4.6](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/enable_goodcloud_v4.6.x.png){class="glboxshadow"}

## クラウドアカウントにログインしてデバイスをバインド

ルー器がファームウェアv4.7で上を実行している場合は、ルー器のWeb管理パネルでアカウントを登録して直接ログインできます。ログインすると、現にのデバイスは自動的にクラウドアカウントにバインドされます。

ルー器がファームウェアv4.6で前を実行している場合は、以下の手順に従ってアカウントにログインし、デバイスをバインドします。

1. [GoodCloud](https://www.goodcloud.xyz){target="_blank"}にアクセスしてアカウントにログインします。アカウントをお持ちでない場合は、まず登録してください。

2. デバイスをGoodCloudにバインドします。[このリンク](../interface_guide/cloud.md#add-device-in-your-account)を参照してください。

## GL.iNet技術サポートとデバイスを共有

1. [GoodCloud](https://www.goodcloud.xyz){target="_blank"}にアクセスしてログインします。

2. **デバイス** -> **バインド済みデバイス**に移動し、共有したいデバイスをクリックします。

    ![bound devices](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/bound_devices.png){class="glboxshadow"}

3. デバイスの詳細ページに導かれます。下図のようにのように、**共有**タブと**デバイスを共有**をクリックします。

    ![share device](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_device.png){class="glboxshadow"}

4. メールアドレス **support@gl-inet.com** を入力し、**共有**をクリックします。

    ![share support](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_support.png){class="glboxshadow"}

5. 共有が成功すると、下図のようにのようなメッセージが表示されます。

    ![share success](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/share_success.png){class="glboxshadow"}

6. GL.iNet技術サポートがデバイスにアクセスできるようになると、**アクセス権を持つユーザー**リストにsupport@gl-inet.comが表示されます。

    ![shared with support](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/shared_with_support.png){class="glboxshadow"}

## 技術サポート後に共有を取り消す

技術サポートが完たした後、共有を取り消すことができます。

1. **アクセス権を持つユーザー**リストでsupport@gl-inet.comを見つけます。

2. **X**をクリックして共有を取り消します。

    ![revoke access](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/revoke_access.png){class="glboxshadow"}

3. 確認メッセージで**確認**をクリックします。

    ![confirm revoke](https://static.gl-inet.com/docs/router/en/4/tutorials/technical_support_via_goodcloud/confirm_revoke.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
