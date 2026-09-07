# セルラーでインターネットに接続する（v4.10）

このページの内容は、ファームウェア v4.10 以降に基づいています。デバイスで別のファームウェアバージョンを使用している場合は、以下のセレクターで該当するガイドに切り替えてください。

<div class="gl-link-select" data-label="ファームウェアバージョン" data-placeholder="ファームウェア v4.10 以降" markdown="1">

- [ファームウェア v4.8 - v4.9](internet_cellular.md)
- [ファームウェア v4.7 以前](internet_cellular_v4.7.md)

</div>

---

ほとんどの GL.iNet ルーターはセルラー接続に対応しています。このガイドでは、次の2種類のルーターでのセルラー接続について説明します。

1. **セルラールーター**

    GL.iNet セルラールーターには、Spitz AX (GL-X3000) や Mudi 7 (GL-E5800) のように、4G/5G モジュールと1つまたは2つの SIM カードスロットが内蔵されています。Web 管理パネルのセルラー設定は、モデルやファームウェアバージョンによって若干異なる場合があります。これらのモデルでの設定については、[セルラールーター](#cellular-routers) を参照してください。

2. **非セルラールーター**

    非セルラールーターには、ホームルーター、旅行用ルーター、ミニルーター、セキュリティゲートウェイなどがあります。通常は USB ポートを備えており、USB ドングル（別売）を接続してセルラー通信を利用できます。これらのモデルでの設定については、[非セルラールーター](#non-cellular-routers) を参照してください。

**注意:** 一部の SIM カードは初回使用前に有効化が必要です。互換性を確保するため、ルーターへ挿入する前にスマートフォンで SIM カードを有効化してください。

## セルラールーター {#cellular-routers}

このセクションでは、**Mudi 7 (GL-E5800)** を例に、セルラー接続の設定手順と関連機能を説明します。

Mudi 7 は eSIM と2つの Nano-SIM スロットを内蔵し、Dual SIM Dual Standby に対応しています。そのため、Web 管理パネルは他のセルラールーター、特に SIM スロットが1つのモデルとは若干異なる場合があります。

### ネットワーク設定

ルーターの Web 管理パネルにログインし、**INTERNET** -> **Cellular** に移動します。

1. SIM カードが挿入されていない場合、ページには "Your SIM card has not been detected" と表示されます。

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. SIM カードを挿入すると、ルーターは自動的に接続を開始します。接続に成功すると、SIM の通信事業者、信号強度、バンド、データ使用量、その他のオプションが表示されます。

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    SIM カードが検出されない場合は、ルーターに挿し直すか、ルーターを再起動してからもう一度試してください。

3. ネットワークの詳細を表示するには、**Details & Configuration** をクリックします。

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    **Network Information** では、SIM Operator、Phone Number、ICCID、APN、Max Bit Rate、IPv4 Address、IPv4 DNS Server を確認できます。

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Max Bit Rate（AMBR）とは"

        Max Bit Rate（AMBR）は Aggregate Maximum Bit Rate の略です。通信事業者が提供するすべての非 GBR ベアラーを合計した最大ビットレートの上限を定義します。このパラメーターはモバイル通信事業者によって設定されます。

4. ネットワークを手動設定するには、**Details & Configuration** をクリックします。

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    **Network Settings** では、APN などのネットワークパラメーターを設定できます。

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: 通常、APN 設定は SIM カードから自動的に取得されます。一部の SIM カードでは特定の APN が必要です。正しい APN がわからない場合は、通信事業者に確認してください。

    - **IP Type**: 自動検出されます。IPv4、IPv6、またはその両方を選択できます。選択するオプションが SIM カードの対応する IP タイプと一致していることを確認してください。SIM カードが現在の IP タイプに対応していない場合や、ここで IPv6 を選択していてもルーター側で IPv6 が無効になっている場合は、接続に問題が発生することがあります。

    - **International Data Roaming**: 海外旅行中にデータ通信を利用しやすいよう、デフォルトで有効になっています。不要な場合や高額なローミング料金を防ぎたい場合は無効にできます。

    - **TTL**: 通信事業者によっては、TTL 値を読み取って SIM カードがルーターで使われているかどうかを判定します。SIM カードをルーターで使用できない場合は、TTL を 64 と 128 以外の値（例: 65）に設定してみてください。

    - **HL**: IPv6 の HL（Hop Limit）フィールドは、ネットワーク内でデータパケットを転送できるホップ数を制限します。IPv4 の TTL に相当します。

    - **MTU**: 利用環境に合わせて MTU 値を設定します。設定が正しくないとインターネット接続が切断されることがあります。MTU を変更した場合は、設定を反映するためデバイスを再起動してください。

    - **Authentication**: 認証情報が不要な場合は通常 NONE に設定します。PAP、CHAP、PAP/CHAP も選択できます。

### トラフィック統計

トラフィック統計を表示するには、**Data Usage** をクリックします。

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

SIM の Data Cap Amount を設定したり、SIM データを定期的にリセットするスケジュールを設定したりする場合は、**SIM Limit Settings** を有効にします。

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Data Cap Amount、Data Reset Period、Start Day、Start Hour を設定し、**Apply** をクリックします。

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**注意**:

1. Data Used が Data Cap Amount を超えた場合は、Data Cap Amount または Data Used を変更してください。変更しないとネットワークが切断されたり、[SIM フェイルオーバー](#sim-failover) が有効な場合に限り別の SIM に切り替わったりすることがあります。

2. SIM 1 Data Cap Amount を設定し、SIM Auto Switch を有効にしている場合、SIM 1 のデータ使用量が Data Cap Amount を超えると、自動的に SIM 2 へ切り替わり、SIM 1 は無効になります。

3. Start Day で設定できる最大日数は、現在の月の実際の日数です。

### セルラー詳細

セルラー接続の詳細を表示するには、**Details & Configuration** をクリックします。

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

**Cellular Information** では、Network Type、TAC、Cell ID、Band、Signal History を確認できます。

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: 自動検出されます。ネットワークタイプを指定するには、**Cellular Settings** タブに切り替え、ドロップダウンリストから選択します。

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    より高速な通信には 5G（5G 信号が必要）、安定性を重視する場合は 4G を選択します。

    基地局をロックすると、ネットワークタイプが固定され、変更できなくなります。

- **TAC**: Tracking Area Code の略で、セルラーネットワーク内のモビリティ管理に使う追跡エリアを示す、ネットワーク割り当ての識別子です。セルラー基地局から自動検出されます。

- **Cell ID**: セルラー基地局の個々のセルを識別する一意の識別子です。これもセルラー基地局から自動検出されます。

- **Band Information**: クリックすると、セルラーバンドに関する詳細なパラメーターを表示できます。

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: クリックすると、信号強度の履歴を表示できます。セルラー接続の品質監視に利用できます。

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### バンドマスキング

Band Masking を使うと、使用するセルラーバンドを指定してセルラー信号の改善を図れます。

Band Masking を有効にするには、**Details & Configuration** をクリックします。

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

**Cellular Settings** で **Band Masking** を有効にし、使用するバンドを選択して **Apply** をクリックします。

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### 通信事業者ロック

!!! note "対応モデル"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) はファームウェア v4.8 以降でこの機能をサポートします。

特定の通信事業者にロックすると、ルーターはその事業者のネットワークだけを使用します。安定した接続を維持し、特に国境付近でデバイスが国外のネットワークへ接続してしまうことによる意図しないローミング料金を回避できます。

通信事業者をロックするには、**Details & Configuration** をクリックします。

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

**Cellular Settings** で **Lock Operator** をクリックします。

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

ネットワークをスキャンする前に **Lock Mode** を選択できます。

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: 特定の通信事業者に手動でロックします。

- **Manual-Auto**: 手動ロックに失敗した場合、利用可能な通信事業者ネットワークへ自動的に切り替えます。

続いて **Scan Networks** をクリックします。

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

約1分待つと、利用可能な通信事業者が表示されます。1つ選択して **Lock** をクリックします。

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

セルラー信号が選択した通信事業者にロックされます。

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### 基地局ロック

!!! note "対応モデル"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) はファームウェア v4.7 以降でこの機能をサポートします。

より高品質な信号を受信して安定したセルラー接続を確保するには、基地局ロックを試すことができます。ただし、ロックする基地局は通信事業者とデバイスがサポートする周波数帯に一致している必要があります。一致しない場合は接続に失敗することがあります。

基地局をロックするには、**Details & Configuration** をクリックします。

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

**Cellular Settings** で **Lock Tower** をクリックします。

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

ポップアップウィンドウで **Scan Networks** をクリックします。

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

約1分待つと、利用可能な基地局が表示されます。

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

1つ選択して詳細を表示し、**Lock** をクリックします。

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

セルラー信号が選択した基地局にロックされます。

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**注意**:

1. Cellular インターフェースが有効な状態では、すべての基地局をスキャンできない場合があります。

2. ロックした基地局が、有効になっている Band Masking やセルラー設定の APN パラメーターと一致しない場合、ルーターはセルラーネットワークに接続できません。

3. 基地局をロックした後にルーターを別の場所へ移動すると、再起動後も以前ロックした基地局への再接続を試みます。その結果、新しい場所でセルラーネットワークへ自動接続できない場合があります。この場合は、現在の基地局ロックを解除するか、新しい基地局へ手動でロックし直してください。

### SMS

[SMS](../tutorials/sms.md) を参照してください。

### SMS 転送

[SMS 転送](../tutorials/sms_forwarding.md) を参照してください。

### 機内モード

Airplane Mode を有効にするには、右上の歯車アイコンをクリックし、**Airplane Mode** をオンにします。

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### モデム情報

モデムの詳細を表示するには、右上の歯車アイコンをクリックして **Modem Information** を選択します。

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### SIM フェイルオーバー {#sim-failover}

この機能は Dual-SIM に対応するセルラールーターでのみ利用できます。

SIM Failover を使うと、ルーターが SIM 1 と SIM 2 を自動的に切り替えます。優先順位が最も高い SIM のデータ使用量が Data Cap Amount を超えた場合や、その SIM がインターネットに接続できない場合、ルーターはバックアップ SIM に切り替えてネットワーク接続を維持します。

SIM Failover を有効にするには、右上の歯車アイコンをクリックして **SIM Failover** を選択します。

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

ポップアップウィンドウで **Auto Switch** を有効にします。右側のボタンをドラッグして SIM の優先順位を変更できます。

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

毎日の指定時刻に優先 SIM へ戻すには、**Scheduled Switch to Preferred SIM** を有効にして **Daily Execution Time** を設定し、**Apply** をクリックします。

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### AT コマンド

AT コマンドは、セルラーモデムと通信するための標準命令です。この機能を使うと、コマンドを送信してモデムの状態を確認できます。

右上の歯車アイコンをクリックして **AT Command** を選択します。

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: Shortcut が **Manual command** に設定されている場合は、**AT Command** フィールドに任意のコマンドを入力し、下部の **Send** をクリックします。結果は下の出力欄に表示されます。

    ボックスをクリックし、ドロップダウンリストから **preset command** を選択することもできます。

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    たとえば、ショートカットに "Request SIM card status"、SIM スロットに SIM1 を選択し、"Send" をクリックすると、以下の結果が表示されます。

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: コマンドを SIM1 と SIM2 のどちらに適用するかを選択します。

- **AT Command**: Shortcut が "Manual command" の場合に、任意のコマンドを入力します。

## 非セルラールーター {#non-cellular-routers}

このセクションでは、**Flint 3 (GL-BE9300)** と外付け USB ドングル [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} を例に、セルラー接続の設定手順を説明します。

**注意**:

1. SIMPoYo uFi を含む一部の USB セルラードングルは、**ホストレスモード**で動作します。このモードでは、ドングルが内部でセルラー接続を確立し、仮想 USB Ethernet インターフェースをルーターへ提供します。ルーターは制御可能なセルラーモデムではなくテザリング WAN として認識するため、Cellular インターフェースではなく Tethering インターフェースから接続します。

2. ホストレステザリングモードでは、ルーターから信号強度、Cell ID、TAC などの低レベルなセルラー情報を取得したり、APN や SIM 関連パラメーターを制御したりできません。これらの設定は、ドングルに内蔵された Web UI で行ってください。

---

次の手順でセルラー接続を設定します。

1. USB ドングルをルーターの USB ポートに接続します。

2. ルーターの Web 管理パネルにログインし、**INTERNET** -> **Tethering** に移動して **Connect** をクリックします。

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    TTL、HL、MTU などの詳細設定が必要な場合は、**Connect** をクリックする前に **Advanced** をクリックして設定します。

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. 接続に成功すると、ページにはネットワーク情報と緑のドットが表示されます。

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

初回設定後は、USB モデムを接続したままルーターを再起動した場合や、モデムを挿し直した場合でも自動的に認識され、Connect ボタンを再度クリックしなくてもネットワーク接続が確立されます。
