# デバイスID、MACアドレス、シリアルナンバーはどこで確認できますか？

## 方法1:

ほとんどの機種では、ルーターの背面に記載されています。

新しい機種の場合、ルーター背面のラベルは以下の画像のようになっています。例えば、下の写真では、そのMACは **E4:95:6E:40:DB:A1**, デバイスIDは **hh0dba1** シリアルナンバーは **7c0be4bb45d96057**.

![label of gl-x750](https://static.gl-inet.com/docs/en/4/tutorials/where_to_find_the_device_id_mac_sn/back_label_new.png){class="glboxshadow"}

古い機種の場合、デバイスIDは分かりませんが、DDNSは分かります。実は、そのDDNSの最初の7文字がデバイスIDなのです。 次の写真を例にとると、そのMACは次のとおりです。**E4:95:6E:40:DB:A1**, デバイスIDは　 **hh0dba1**, シリアルナンバーは **7c0be4bb45d96057**.

![label of gl-ar150](https://static.gl-inet.com/docs/en/4/tutorials/where_to_find_the_device_id_mac_sn/back_label_old.png){class="glboxshadow"}

## 方法2:

ウェブ管理パネルにログインしてください。 -> APPLICATION -> GoodCloud.

![goodcloud page](https://static.gl-inet.com/docs/en/4/tutorials/where_to_find_the_device_id_mac_sn/goodcloud_page_device_id.png){class="glboxshadow"}
