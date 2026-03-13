# Extensible Authentication Protocol（EAP）ネットワークに接続する方法

## はじめに

GL.iNetルーターを、EAP（Extensible Authentication Protocol）Wi-Fiネットワークに接続できます。このネットワークはGL.iNetルー器でユーザー名とパスワードの認証が必要です。

このガイドでは、GL.iNetルーをEAP Wi-Fiネットワークに接続する2つの方法を説明します：管理パネル経よりとLuCI経よりです。

## 対応モデル

??? "対応モデル"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)
    - ※GL-SFT1200 (Opal)

    **注意:** 
    
    1. GL-MT6000 (Flint 2) と GL-MT3000 (Beryl AX) はデフォルトのファームウェアではEAPネットワークへの接続をサポートしていませんが、GL.iNetはこれらのモデル用のネイティブOpenWrt 24ファームウェアを提供しており、EAPネットワークへの接続をサポートするためにインストールできます。[ダウンロードセンター](https://dl.gl-inet.com/){target="_blank"}でモデルを検索し、詳細についてはOPENWRT 24タブを開いてください。

    2. GL-SFT1200 (Opal) はファームウェアv4.8でEAPネットワークへの接続をサポートしています。

??? "非対応モデル"
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## 管理パネル経よりで接続

1. Web管理パネルにアクセスし、**インターネット** -> **ainless**セクションに移動し、**接続**をクリックします。

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    利用可できるなネットワークをスキャンします。EAP SSIDを見つけて選択し、直接接続できます。

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    または、右上の**彼のネットワークに参加**をクリックして、EAPネットワークに手動で参加します。

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. **SSID**を入力します。

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. **セキュリティ**でWPA/WPA2/WPA3 Enterpriseを選択します。

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. **ユーザー名**と**パスワード**を入力します。次に**適用**をクリックして接続します。

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## LuCI経よりで接続

現に、GL.iNet Web管理パネルは少数のEAPタイプのみをサポートしています。大多数の状況ではLuCIページ経よりで接続する必要があるかもしれません。

1. [LuCI](https://docs.gl-inet.com/router/en/4/faq/what_is_luci/)ページにログインします。

2. LuCIページで、Network -> Wirelessに移動します。

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. 2.4Gセクションまたは5Gセクションで**スキャン**をクリックします。

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. 参加したいネットワークに参加します。

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

---

関連記事：

- [GL.iNetルー器を高度な設定が必要なEAPネットワークに接続する方法](how_to_connect_glinet_router_to_an_eap_network_with_advanced_settings.md)

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
