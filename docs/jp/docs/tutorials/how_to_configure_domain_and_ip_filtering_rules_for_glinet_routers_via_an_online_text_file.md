# GL.iNetルーターでオンラインテキストファイルを使ってドメインおよびIPフィルタリングルールを設定する方法

ファームウェア v4.7 以降では、次の機能でオンラインテキストファイル URL からルールをインポートできます。

- ターゲットドメインまたは IP アドレスに基づく VPN ポリシー（VPN 配下）
- Add a New Ruleset（Parental Control 配下）

このチュートリアルでは、GL.iNet ルーターでオンラインテキストファイルを使ってドメインおよび IP フィルタリングルールをインポートする方法を説明します。

## 対応するURL形式とファイル形式

対応する URL 形式は次のとおりです。

- プレーンテキストファイルの URL（HTTP/HTTPS）
- GitHub Raw content URL

対応するファイル形式は `.txt`、`.conf`、`.log` などのプレーンテキスト形式です。

**Note**: `.exe`、`.zip`、`.jpg`、`.png` などのバイナリファイルには対応していません。

## GitHubを使ってテキストファイルをホストする

テキストファイルを公開 GitHub リポジトリでホストする場合は、通常の GitHub URL ではなく raw content URL を使用してください。

たとえば、次の GitHub URL は raw content ではなく Web ページのコンテンツを指しています。

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

ルーターが正しい内容をダウンロードできるようにするには、次の形式の raw content URL を使用してください。

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

このようにすることで、ルーターはファイルのプレーンテキスト内容を正しく取得できます。

## VPNポリシー（ドメイン / IP）のフィルタ形式

「VPN Policy Based on Target Domain or IP Address」機能は、オンラインテキストファイルで次のフィルタ形式をサポートしています。

* ドメイン名: `netflix.com` のようなドメイン名を指定します（すべてのサブドメインに一致）。
* サブドメイン: `www.netflix.com` のように完全なサブドメインを指定します（このサブドメインのみに一致）。
* CIDR 範囲: `192.168.10.0/24` のように CIDR 表記で IP アドレス範囲を指定します。
* IPv4 アドレス: `192.168.10.10` のように個別の IPv4 アドレスを指定します。

## Parental Control（Ruleset）のフィルタ形式

Parental Control の「Add a New Ruleset」機能は、オンラインテキストファイルで次のフィルタ形式をサポートしています。

* ドメイン名: `instagram.com` のようなドメイン名を指定します（すべてのサブドメインに一致）。
* サブドメイン: `www.instagram.com` のように完全なサブドメインを指定します（このサブドメインのみに一致）。

オンラインテキストファイルを作成する際は、1 行につき 1 つのフィルタを記述してください。ルーターは各行を指定された形式に従って処理し、対応するルールを VPN または Parental Control 機能に適用します。

これらのフィルタ形式に従えば、ルーターの VPN 機能および Parental Control 機能向けのオンラインテキストファイルを簡単に作成して管理できます。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
