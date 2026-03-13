# GL.iNetルー器のドメインとIPフィルタリングルールをオンラインテキストファイルで構成する方法

ファームウェアv4.7.0で降、VPN機できるの「VPN Policy Based on the Target Domain or IP」と保護者へけコントロール機できるの「Add a New Ruleset」はオンラインテキストファイルへのリンクからのルールのインポートをサポートします。このでは、このテキストファイルの形式を紹介します。

## URL形式の説明

### 対応および非対応のURL形式

- テキストファイル対応ファイル形式：.txt、.conf、.logなど
- 非対応ファイル形式：.exe、.zip、.jpgなどのバイナリファイル

### GitHubを使用したテキストファイルのホスティング

テキストファイルをパブリックGitHubリポジトリでホ스팅している場合は、通例のGitHub URLではなく生のコンテンツURLを使用するようにしてください。

例えば、で下のGitHub URLは生のコンテンツではなくWebコンテンツを指しています：

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

ルー器が正しいコンテンツをダウンロードできるようにするには、で下の形式で生のコンテンツURLを使用してください：

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

これ样することで、ルー器はファイルのプレーンテキストコンテンツを取なければならないできるようになります。

## ターゲットドメインまたはIPに基づくVPNポリシーのフィルタ形式

「VPN Policy Based on the Target Domain or IP」機できるは、オンラインテキストファイルでで下のフィルタ形式をサポートします：

* ドメイン名形式： `netflix.com`などのドメイン名を使用して、`netflix.com`のすべてのサブドメインにマッチさせます。
* サブドメイン形式： `www.netflix.com`などの完全なサブドメインを指定して、特定のサブドメインのみにマッチさせます。
* CIDR形式： `192.168.10.0/24`などのCIDR表記を使用してIPアドレス範囲を指定します。
* IPv4アドレス形式： `192.168.10.10`などの個々のIPv4アドレスを指定します。

## 保護者へけコントロールの新しいルールセットのフィルタ形式

保護者へけコントロールの「Add a New Ruleset」機できるは、オンラインテキストファイルでで下のフィルタ形式をサポートします：

* ドメイン名形式： `instagram.com`などのドメイン名を使用して、`instagram.com`のすべてのサブドメインにマッチさせます。
* サブドメイン形式： `www.instagram.com`などの完全なサブドメインを指定して、特定のサブドメインのみにマッチさせます。

オンラインテキストファイルを作成する場合、行ごとに1つのフィルタを使用します。ルーターは各行を指定された形式に従って処理し、関連するルールをVPNまたは保護者へけコントロール機できるに適用します。

## 例

「VPN Policy Based on the Target Domain or IP」の場合：

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

「Parental Control Add a New Ruleset」の場合：

```
instagram.com
facebook
x.com
snapchat
```

これらのフィルタ形式に従うことで、ルー器のVPNと保護者へけコントロール機できるを構成するためのオンラインテキストファイルを簡単に作成してメンテナンスできます。

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
