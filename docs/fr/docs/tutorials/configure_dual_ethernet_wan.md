# Configurer un double WAN Ethernet filaire via un adaptateur Ethernet vers USB-A

Vous pouvez configurer un double accès WAN Ethernet filaire sur un routeur disposant d'un seul port WAN à l'aide d'un adaptateur Ethernet vers USB-A. 

Les routeurs GL.iNet prennent en charge les adaptateurs Ethernet vers USB-A courants. Vous pouvez ainsi convertir l'accès Ethernet filaire provenant du routeur de votre FAI en connexion USB via le port USB du routeur, afin de lui fournir un accès Ethernet filaire supplémentaire en plus du port WAN.

## Topologie

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Étapes de configuration

1. Branchez l'adaptateur Ethernet vers USB-A sur le port USB de votre routeur GL.iNet, puis connectez l'autre extrémité à votre routeur FAI.

2. Installez le pilote USB. 

    Connectez-vous au panneau d'administration Web du routeur, accédez à **Application** -> **Plug-ins**, puis installez le pilote réseau USB correspondant à votre adaptateur. 

    Par exemple, si vous utilisez un adaptateur Realtek, installez le pilote **kmod-usb-net-rtl8152**. 

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Attendez la fin de l'installation.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Connectez-vous via USB Tethering.

    Une fois le pilote installé, accédez à la section **INTERNET** -> **Tethering**. 
    
    La connexion USB sera détectée et vous pourrez vous connecter à votre routeur FAI.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Cliquez sur **Connect** puis attendez une minute. Lorsqu'un point vert s'allume et que la page affiche des informations telles que l'adresse IP, cela signifie que la connexion USB Tethering est établie avec succès.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
