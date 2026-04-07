# GL.iNetルーターでオンラインテキストファイルを使ってドメインおよびIPフィルタリングルールを設定する方法

ファームウェア v4.7.0 以降では、VPN 機能の「VPN Policy Based on the Target Domain or IP」と、Parental Control 機能の「Add a New Ruleset」で、オンラインテキストファイルへのリンクからルールをインポートできるようになりました。この記事では、このテキストファイルの形式を紹介します。

## URL形式の説明

### 対応しているURL形式と対応していないURL形式

* テキストファイルで対応しているファイル形式: .txt、.conf、.log など
* 対応していないファイル形式: .exe、.zip、.jpg などのバイナリファイル

### GitHubを使ってテキストファイルをホストする

テキストファイルを公開 GitHub リポジトリでホストする場合は、通常の GitHub URL ではなく raw content URL を使用してください。

たとえば、以下の GitHub URL は raw content ではなく Web コンテンツを指しています。

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

ルーターが正しい内容をダウンロードできるようにするには、以下の形式の raw content URL を使用してください。

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

このようにすることで、ルーターはファイルのプレーンテキストを取得できます。

## ターゲットドメインまたはIPに基づくVPNポリシーのフィルタ形式

「VPN Policy Based on the Target Domain or IP」機能は、オンラインテキストファイルで次のフィルタ形式をサポートしています。

* ドメイン名形式: `netflix.com` のようなドメイン名を使用すると、`netflix.com` のすべてのサブドメインに一致します。
* サブドメイン形式: `www.netflix.com` のように完全なサブドメインを指定すると、その特定のサブドメインのみに一致します。
* CIDR形式: `192.168.10.0/24` のように CIDR 表記を使って IP アドレス範囲を指定できます。
* IPv4アドレス形式: `192.168.10.10` のように個別の IPv4 アドレスを指定できます。

## Parental Control Add a New Rulesetのフィルタ形式

Parental Control の「Add a New Ruleset」機能は、オンラインテキストファイルで次のフィルタ形式をサポートしています。

* ドメイン名形式: `instagram.com` のようなドメイン名を使用すると、`instagram.com` のすべてのサブドメインに一致します。
* サブドメイン形式: `www.instagram.com` のように完全なサブドメインを指定すると、その特定のサブドメインのみに一致します。

オンラインテキストファイルを作成する際は、1 行につき 1 つのフィルタを記述してください。ルーターは各行を指定された形式に従って処理し、対応するルールを VPN または Parental Control 機能に適用します。

## 例

「VPN Policy Based on the Target Domain or IP」の例:

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

「Parental Control Add a New Ruleset」の例:

```
instagram.com
facebook
x.com
snapchat
```

これらのフィルタ形式に従えば、ルーターの VPN 機能と Parental Control 機能向けのオンラインテキストファイルを簡単に作成して管理できます。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
