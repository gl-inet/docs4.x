# Notification critique de problème pour GL-MT2500/GL-X3000/GL-XE3000

Chers clients GL.iNet,

Cette annonce concerne les échecs de démarrage et les problèmes de récupération du firmware via U-Boot sur les appareils GL-MT2500/GL-X3000/GL-XE3000. Le problème provenait d'un défaut logiciel dans lequel certains paramètres étaient définis de manière incorrecte, ce qui entraînait un fonctionnement anormal des routeurs. Nous estimons par conséquent que ce problème a pu réduire dans une certaine mesure la durée de vie des routeurs, et nous vous présentons nos sincères excuses.

Pour résoudre complètement ce problème, nous recommandons vivement à tous les utilisateurs des GL-MT2500, GL-X3000 et GL-XE3000 d'effectuer à la fois une mise à niveau du chargeur de démarrage U-Boot et une mise à niveau du firmware. Ces deux procédures sont essentielles et ne doivent pas être omises.

Même si votre appareil a déjà été mis à niveau vers le dernier firmware, la mise à niveau du chargeur de démarrage U-Boot reste obligatoire afin d'éviter tout problème potentiel. Après avoir terminé la mise à niveau du chargeur de démarrage U-Boot, si le dernier firmware est déjà installé, vous pouvez ne pas réinstaller le firmware.

Veuillez effectuer la mise à niveau avec Chrome ou Microsoft Edge. N'utilisez PAS Mozilla/Firefox.

## GL-MT2500

1. Téléchargez et mettez à niveau le chargeur de démarrage U-Boot vers la [version 2025-02-24 15:04:07](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}

2. Téléchargez et mettez à niveau le firmware vers la [version 4.7.4](https://fw.gl-inet.com/firmware/mt2500/release/openwrt-mt2500-4.7.4-0328-1743128340.bin)

## GL-X3000

1. Téléchargez et mettez à niveau le chargeur de démarrage U-Boot vers la [version 2025-02-25 19:05:24](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}

2. Téléchargez et mettez à niveau le firmware vers la [version 4.7.4](https://fw.gl-inet.com/firmware/x3000/release/openwrt-x3000-4.7.4-0317-1742206344.bin)

## GL-XE3000

1. Téléchargez et mettez à niveau le chargeur de démarrage U-Boot vers la [version 2025-02-25 19:07:14](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}

2. Téléchargez et mettez à niveau le firmware vers la [version 4.7.4](https://fw.gl-inet.com/firmware/xe3000/release/openwrt-xe3000-4.7.4-0317-1742206184.bin)

!!! Note

    Pour la méthode de mise à niveau du chargeur de démarrage U-Boot, vous pouvez consulter [ce lien](https://docs.gl-inet.com/router/en/4/faq/upgrade_uboot_version/){target="_blank"}.

    Pour la méthode de mise à niveau du firmware, vous pouvez consulter [ce lien](https://docs.gl-inet.com/router/en/4/tutorials/how_to_upgrade_downgrade_router/){target="_blank"}.

<br>
Nous vous présentons nos sincères excuses pour la gêne occasionnée. À l'avenir, nous nous engageons à améliorer nos produits et nos firmwares avec encore plus de rigueur et de soin.

Pour les personnes qui possèdent actuellement ces routeurs, nous prolongerons la période de garantie d'un an sans frais. Si vous rencontrez le moindre problème, n'hésitez pas à contacter nos équipes d'assistance.

Si le problème persiste malgré la mise à niveau, veuillez contacter nos équipes d'assistance à l'adresse support@gl-inet.com ; nous vous fournirons gratuitement un appareil de remplacement.

Votre confiance et votre soutien comptent énormément pour nous, et nous vous en sommes profondément reconnaissants.

<br>

Cordialement,

Support technique GL.iNet

26 mars 2025

