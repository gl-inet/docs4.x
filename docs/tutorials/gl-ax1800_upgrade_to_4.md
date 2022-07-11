# GL-AX1800(Flint)のファームウェアを4.xにアップグレードするにはどうしたらいいですか？

GL-AX1800は、すでに4.xのベータ版ファームウェアが公開されています。試してみたい方は、以下の手順でGL-AXT1800をファームウェア3.xから4.xにアップグレードすることが可能です。

**注意：ベータ版ファームウェアにはバグがある可能性があります。

## アップグレード

ファームウェア4.xへのアップグレードには2つの方法がありますが、最初の方法が簡単でお勧めです。

- 方法1．

    Web管理画面の「ローカルアップグレード」を利用する。

    1. ファームウェアを3.214（最新の安定版）にバージョンアップしてください。

    2. 4.xベータ版ファームウェアのダウンロードは[こちら](https://dl.gl-inet.com/?model=ax1800&type=beta){target="_blank"}、uboot用のものをダウンロードしてください、ファイル名の拡張子は**.img**です。ここで少し混乱するかもしれませんが、uboot用のファームウェアは通常Local Upgradeでは使用できませんので、これは特別なケースです。

    3. Web管理画面の**Local Upgrade** から、.imgファームウェアファイルを用いてアップグレードしてください。

        ![local upgrade](https://static.gl-inet.com/docs/en/3/setup/share/upgrade/local_upgrade.png){class="glboxshadow"}

- 方法 2:

    1. 4.xベータ版ファームウェアのダウンロードはこちら](https://dl.gl-inet.com/?model=ax1800&type=beta){target="_blank"}、uboot用のものをダウンロードしてください、ファイル名の拡張子は**.img**です。

    2. [Uboot](../debrick/)でファームウェアをフラッシュしてください。

## ダウングレード

1. 最新の3.xリリースファームウェアをダウンロードしてください。 [here](https://dl.gl-inet.com/?model=ax1800){target="_blank"}

2. [Uboot](../debrick/).でファームウェアをフラッシュしてください。
