# GL.iNet ルーターのドメイン / IP フィルタリングルールをオンラインテキストファイルで設定する方法

ファームウェア v4.7.0 以降では、VPN 機能の「VPN Policy Based on the Target Domain or IP」と、Parental Control 機能の「Add a New Ruleset」が、オンラインテキストファイルへのリンクからルールをインポートできるようになっています。この記事では、そのテキストファイルの形式を紹介します。

## URL形式の説明

### 対応および非対応のURL形式

- 対応するテキストファイル形式: `.txt`、`.conf`、`.log` など
- 非対応のファイル形式: `.exe`、`.zip`、`.jpg` などのバイナリファイル

### GitHubを使用したテキストファイルのホスティング

テキストファイルを公開 GitHub リポジトリでホストしている場合は、通常の GitHub URL ではなく raw content URL を使用してください。

例えば、以下のGitHub URLは生のコンテンツではなくWebコンテンツを指しています：

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

ルーターが正しい内容をダウンロードできるようにするには、以下の形式の raw content URL を使用してください:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

これにより、ルーターはファイルのプレーンテキスト内容を取得できるようになります。

## ターゲットドメインまたはIPに基づくVPNポリシーのフィルタ形式

「VPN Policy Based on the Target Domain or IP」機能は、オンラインテキストファイルで以下のフィルタ形式をサポートします：

- ドメイン名形式: `netflix.com` のようなドメイン名を使うと、`netflix.com` のすべてのサブドメインに一致します。
- サブドメイン形式: `www.netflix.com` のように完全なサブドメインを指定すると、その特定のサブドメインのみに一致します。
- CIDR 形式: `192.168.10.0/24` のような CIDR 表記で IP アドレス範囲を指定できます。
- IPv4 アドレス形式: `192.168.10.10` のような個別の IPv4 アドレスを指定できます。

## Parental Control の Add a New Ruleset に対応するフィルタ形式

Parental Control の「Add a New Ruleset」機能では、オンラインテキストファイルで以下のフィルタ形式をサポートします:

- ドメイン名形式: `instagram.com` のようなドメイン名を使うと、`instagram.com` のすべてのサブドメインに一致します。
- サブドメイン形式: `www.instagram.com` のように完全なサブドメインを指定すると、その特定のサブドメインのみに一致します。

オンラインテキストファイルを作成する際は、1 行につき 1 つのフィルタを記述してください。ルーターは各行を指定された形式に従って処理し、対応するルールを VPN または Parental Control 機能に適用します。

## 例

「VPN Policy Based on the Target Domain or IP」の場合：

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

「Parental Control Add a New Ruleset」の場合:

```
instagram.com
facebook
x.com
snapchat
```

これらの形式に従うことで、ルーターの VPN および Parental Control 機能向けのオンラインテキストファイルを簡単に作成し、維持管理できます。

---

まだご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
