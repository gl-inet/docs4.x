# GL-M2 ユーザーガイド {#gl-m2-user-guide}

## ハードウェア情報 {#hardware-info}

GL-M2は、ルーターやモデムを自作したいDIY愛好家向けの5G開発ボードです。GL-M2の5Gモジュールと5Gアンテナにより、高品質な5Gセルラーネットワークを提供します。

![gl-2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/hardware_info/gl-m2_interface.jpg){class="glboxshadow"}

[GL-M2 仕様](https://www.gl-inet.com/products/gl-m2/#specs){target="_blank"}

## パッケージ内容 {#package-contents}

![gl-m2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_unboxing.jpg){class="glboxshadow"}

パッケージには以下が含まれます。

- 1 x GL-M2 開発ボード
- 4 x 5G アンテナ
- 4 x IPEX コネクタ
- 2 x ネジ
- 1 x DC 電源アダプター
- 1 x ユニバーサル変換プラグ（US、EU、UK、AU）
- 1 x 5G モジュール（オプション）
- 1 x Type-C ケーブル

## 初回セットアップ {#first-time-setup}

以下の動画を見るか、次の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/CzhxiAvCIlQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. モジュールとアンテナを取り付けます。

    RF 変換延長ケーブルまたは SMA アンテナ接続ケーブルを使用して、アンテナをモジュールの IPEX インターフェースに接続します。

    ![gl-m2 setup](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_setup_1.jpg){class="glboxshadow"}

2. Nano SIM カードを挿入します。

    ![gl-m2 setup](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_setup_2.jpg){class="glboxshadow"}

3. 電源を入れます。

    DC 電源に接続し、Type-C - USB 3.0 データケーブルを使用して[ルーターに接続](#connect-m2-to-glinet-routers)するか、その他のデバイスに接続します。

    ![gl-m2 setup](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_setup_3.jpg){class="glboxshadow"}

**注意:**

  - 使用中は、安定した電力を供給するためにDC電源に接続する必要があります。

  - 電源インジケーターが赤色に点灯している場合は、電源が正常に供給されていることを示します。

## GL-M2をGL.iNetルーターに接続する {#connect-m2-to-glinet-routers}

GL-M2（5Gモジュール RM520N-GL 搭載）は、以下のモデルと互換性があります。

- Slate 7 Pro (GL-BE10000)
- Brume 3 (GL-MT5000)
- Beryl 7 (GL-MT3600BE)
- Flint 3e (GL-BE6500)
- Flint 3 (GL-BE9300)
- Slate 7 (GL-BE3600)
- Flint 2 (GL-MT6000)
- Flint (GL-AX1800)
- Beryl AX (GL-MT3000)
- Slate AX (GL-AXT1800)
- Brume 2 (GL-MT2500)

**注意**: 上記の互換ルーター一覧は、**RM520N‑GL** 5Gモジュールで検証されたものです。その他のモジュールとの互換性は保証されません。

以下の手順に従って、M2をGL.iNetルーターに接続します。

1. USBケーブルを使用して、M2をGL.iNetルーターに接続します。

2. Ethernetケーブルを使用して、デバイス（コンピューターやノートPCなど）をGL.iNetルーターに接続します。

3. デバイスでWebブラウザーを開き、[http://192.168.8.1](http://192.168.8.1) にアクセスしてWeb管理パネルにログインします。

    ![Connect GL-M2 to GL.iNet Routers](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_with-mt3000_1.png){class="glboxshadow"}

4. **INTERNET** ページで、Cellular セクションの **Auto Setup** をクリックしてインターネットに接続します。

    ![Connect GL-M2 to GL.iNet Routers](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_with-mt3000_2.png){class="glboxshadow"}

5. 接続に成功すると、以下のように接続の詳細がページに表示されます。

    ![Connect GL-M2 to GL.iNet Routers](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-m2/first_time_setup/m2_with-mt3000_3.png){class="glboxshadow"}
