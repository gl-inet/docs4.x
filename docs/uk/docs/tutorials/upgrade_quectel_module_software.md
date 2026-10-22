# Оновлення прошивки модуля Quectel {#upgrade-quectel-module-firmware}

## Підготовка {#preparation}

1. Переконайтеся, що маршрутизатор налаштовано для доступу до інтернету.

2. Підключіть комп’ютер або ноутбук до маршрутизатора через Wi-Fi або кабель Ethernet.

## Кроки оновлення {#upgrade-steps}

### Для GL-X3000/GL-XE3000 {#for-gl-x3000gl-xe3000}

**Спосіб 1. Оновлення через графічний інтерфейс GL.iNet**

1. Завантажте відповідну прошивку модуля за посиланням унизу цього посібника.

2. Увійдіть до вебпанелі адміністрування маршрутизатора, перейдіть до **SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** і завантажте прошивку модуля у форматі .zip.
    
    ![Локальне оновлення модема](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/modem_local_upgrade.png){class="glboxshadow"}

**Спосіб 2. Оновлення через SSH**

Розглянемо оновлення на прикладі модуля RM520N.

1. Увійдіть до маршрутизатора через SSH за [цією інструкцією](ssh_log_in_to_the_router.md).

2. Виконайте наведену нижче команду, щоб завантажити прошивку модуля.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![Завантаження прошивки модуля mtk7981a](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Виконайте наведену нижче команду, щоб розпакувати прошивку модуля.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![Розпакування прошивки модуля mtk7981a](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Оновіть прошивку модуля за допомогою наведеної нижче команди QFirehose.

    **Примітка**: Замініть «/RM520NGLAAR03A03M4G_01.201.01.201» фактичним шляхом до папки з прошивкою модуля.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![Оновлення mtk7981a через QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Зачекайте кілька хвилин. Після завершення оновлення система покаже повідомлення «Upgrade module successfully».

    ![Успішне оновлення mtk7981a](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Перезавантажте маршрутизатор і знову ввійдіть до нього через SSH.

7. Виконайте наведену нижче команду, щоб додатково перевірити, чи успішно оновлено модуль.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![Перевірка версії mtk7981a](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Для GL-MiFi/GL-XE300/GL-X750/GL-E750 {#for-gl-mifigl-xe300gl-x750gl-e750}

Розглянемо оновлення на прикладі модуля EM060K.

1. Підготуйте USB-накопичувач. Завантажте на нього відповідну прошивку модуля за посиланням унизу цього посібника, потім розпакуйте файл .zip і розмістіть його вміст у кореневому каталозі USB-накопичувача.

2. Підключіть USB-накопичувач до маршрутизатора. Потім увійдіть до маршрутизатора через SSH за [цією інструкцією](ssh_log_in_to_the_router.md).

3. Виконайте команду `df -h`, щоб перевірити шлях монтування USB-накопичувача, і запишіть цей шлях.

    ![Перевірка шляху монтування](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Виконайте команду `ls -l`, щоб перевірити папку з прошивкою модуля.

    ![Перевірка папки з прошивкою](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Виконайте наведену нижче команду, щоб завантажити QFirehose із сервера GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Потім надайте йому права на виконання.

    ``` 
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![Завантаження QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Оновіть прошивку модуля за допомогою наведеної нижче команди QFirehose.

    **Примітка**: Замініть «/mnt/sdb1/EM060KGLAAR01A12M2GA» фактичним шляхом до папки з прошивкою модуля.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![Оновлення через QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Зачекайте кілька хвилин. Після завершення оновлення система покаже повідомлення «Upgrade module successfully».

    ![Успішне оновлення](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Перезавантажте маршрутизатор і знову ввійдіть до нього через SSH.

9. Виконайте наведену нижче команду, щоб додатково перевірити, чи успішно оновлено модуль.

    ```
    gl_modem AT AT+QGMR
    ```
    ![Перевірка версії модуля](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## Посилання для завантаження прошивки модуля Quectel {#quectel-module-firmware-download-url}

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
