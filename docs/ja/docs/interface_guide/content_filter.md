# コンテンツフィルター

**注**: この機能はファームウェア v4.9 で導入されました。

Mango 2 (GL-MG1300) など一部のモデルは、メモリ不足のため、ファームウェア v4.9 以降でも Content Filter に対応しません。詳しくは[対応モデル](#supported-models)をご覧ください。

---

コンテンツフィルターは、DPI ベースの分類によって動作するスマートなオンライン保護機能です。有害または悪意のある Web サイトを自動的にブロックしてネットワークを安全でクリーンな状態に保ち、さらに特定のアプリ、ドメイン、IP アドレスをブロックするカスタムルールにも対応しています。

**Note**:

1. コンテンツフィルターは、ルーターが Drop-in Gateway モードのときは動作しません。
2. コンテンツフィルターは **Network Acceleration** と併用できません。有効にすると、安定したパフォーマンスを確保するため **Network Acceleration** は自動的に無効になります。

## 対応モデル {#supported-models}

??? "対応モデル"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "非対応モデル"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## クイックセットアップ

Web Admin Panel の左側で、**FLOW CONTROL** -> **Content Filter** に移動します。

右上のスイッチをオンにし、ブロックしたいコンテンツ（アプリ、ドメイン、IP アドレスなど）を設定して、**Apply** をクリックします。

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

このページは 2 つの部分で構成されています。

- **Blocked Apps List**: このセクションには、Gambling、Adult、Malware の 3 つのカテゴリがあらかじめ選択されています。有効にすると、これら 3 つのカテゴリに関連する Web サイト、サービス、アプリがブロックされます。

    必要に応じて **Edit App** をクリックし、Game や Social Media など、さらに多くのカテゴリを追加することもできます。

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    ポップアップウィンドウでは、ブロックしたいカテゴリを選択します。デフォルトの 3 カテゴリにはアプリ一覧がありませんが、それ以外のカテゴリにはアプリ一覧が含まれています。

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    任意のカテゴリをクリックすると、ブロックしたいアプリを確認して選択できます。右上の **Select All** をクリックすると、そのカテゴリ内のすべてのアプリを一括でブロックできます。選択後、**Confirm** をクリックします。

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

    その後、選択したアプリが Blocked App List に表示されます。

- **Blocked Domain / IP List**: このセクションでは、特定のドメイン（例: google.com）、CIDR 範囲（例: 192.168.8.0/24）、または IP アドレス（例: 192.168.10.10）を手動で入力してブロックできます。リストは最大 10000 件のエントリーに対応しています。

    ブロックしたいドメインまたは IP アドレスを入力し、**Apply** をクリックします。

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## コンテンツフィルターのテスト

たとえば、ここでは **Game** カテゴリを選択しており、その中には Nintendo が含まれています。

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

ルーターに接続したノート PC からは、コンテンツフィルターを有効にする前はアクセスできていた `nintendo.com` に、以後アクセスできなくなります。

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

ルーターの Web Admin Panel では、ブロックされたアクセスリクエスト数も確認できます。

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
