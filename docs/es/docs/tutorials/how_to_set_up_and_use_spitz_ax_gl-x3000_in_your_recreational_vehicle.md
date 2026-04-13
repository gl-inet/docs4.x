# Cómo configurar y usar Spitz AX (GL-X3000) en su vehículo recreativo

Esta guía le muestra cómo configurar y usar Spitz AX en su vehículo recreativo. Antes de empezar, es posible que necesite preparar el siguiente equipo y servicios adicionales:

- Tarjeta(s) SIM o un cable USB para tethering, según el método de conexión a Internet que vaya a utilizar. Si usa tarjeta(s) SIM, solicite a su operador el APN.
- Una antena de techo si desea una mejor cobertura.
- [Una suscripción a Starlink](https://www.starlink.com/roam), si va a desplazarse a zonas sin cobertura celular.

---

## 1. Instale su Spitz AX y otros equipos

Antes de iniciar su viaje, configure su Spitz AX siguiendo estos pasos.

### Paso 1: Elija una ubicación para su Spitz AX

Se recomienda elegir una ubicación central y sin obstrucciones para obtener la máxima cobertura. Asegúrese de que el lugar esté a menos de 1 metro de la fuente de alimentación, que es la longitud del cable del adaptador de corriente.

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Puede colocar su Spitz AX sobre una superficie plana o montarlo en la pared. Si decide montarlo en la pared, siga el paso siguiente.

### (Opcional) Paso 2: Instale su Spitz AX en la pared

Hay dos formas de instalar su Spitz AX en la pared:

- Use la almohadilla adhesiva incluida.
- Use los soportes de pared.

Los soportes de pared se incluyen en el paquete. Para montar su Spitz AX en la pared, siga estos pasos:

1. Fije el soporte a la pared con tornillos.
2. Encaje su Spitz AX en el soporte.

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Opcional) Paso 3: Instale la antena de techo del vehículo recreativo

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

Para obtener una mejor señal, use una antena de techo para su Spitz AX. Se recomienda utilizar [la antena multibanda LTMG942 de MobileMark](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/), que ofrece una señal de red óptima. Si desea usar antenas de techo de otras marcas, asegúrese de que cumplan los siguientes requisitos:

- 4 antenas celulares, con rango de frecuencia de recepción de 600M~6GHz.
- 2 antenas Wi-Fi, con rango de frecuencia de recepción de 2.4G~2.5GHz y 5.15~5.84GHz.

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Nota:** Puede usar una antena 7 en 1, que incluye una antena GPS, pero solo necesitará conectar las seis antenas de su Spitz AX. La interfaz DIV/GNSS del Spitz AX admite señales GPS porque la antena celular, con rango de recepción de 600M~6GHz, cubre la frecuencia de GPS. Spitz AX permite ver su ubicación GPS mediante la línea de comandos, pero actualmente no admite mostrar su ubicación en el mapa.

Para evitar la atenuación de la señal, el cable de radiofrecuencia entre la antena de techo y su Spitz AX no debe superar los 5 metros. Por ejemplo, cuando el cable de radiofrecuencia de MobileMark tiene una longitud de 5 metros, la recepción de la señal a 3000MHz se reduce en 3dB, lo que equivale a la mitad de la intensidad. Cuanto mayor sea la frecuencia de la señal, mayor será la atenuación.

[Aprenda a instalar o cambiar las antenas externas de routers celulares.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_install_or_change_antennas/)

---

## 2. Configure Internet en su Spitz AX

Para asegurarse de tener acceso a Internet durante el viaje, configure la conexión mediante tarjetas SIM.

Spitz AX incorpora un módulo 5GNR y admite doble SIM. Los distintos operadores móviles ofrecen diferentes planes celulares para las tarjetas SIM y utilizan distintos APN. Deberá introducir el APN en la configuración, así que confirme con su operador cuál es el APN correcto.

Para configurar sus tarjetas SIM, siga estos pasos:

1. Inserte su(s) tarjeta(s) SIM.
   ![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Conecte el adaptador de corriente y encienda el router.

Para introducir su APN, siga estos pasos:

1. Escriba `192.168.8.1` en un navegador web e inicie sesión.
2. Debería ver el nombre de su operador en la esquina superior izquierda. Haga clic en **Manual Setup**.
3. Junto a **APN**, introduzca el APN.
4. Haga clic en **Apply**.

Si utiliza dos tarjetas SIM, tenga en cuenta que solo una de ellas funciona cada vez. Puede seleccionar manualmente qué tarjeta SIM usar en cada momento. También puede activar la función [Auto Switch](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models). Si el router detecta que una de las tarjetas SIM no puede acceder correctamente a Internet, cambiará automáticamente a la otra tarjeta. El cambio tarda aproximadamente 1 minuto en completarse.

---

## 3. Use Spitz AX en distintos escenarios

### En la carretera

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Mientras conduce por carretera, debería poder conectarse a Internet mediante la(s) tarjeta(s) SIM que configuró en el paso anterior.

### En un camping

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Si hace una parada en un camping durante su viaje, puede usar la red Wi-Fi pública que ofrezca el lugar y ahorrar datos móviles. [Aprenda a conectarse a una red Wi-Fi existente.](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/)

Después de conectarse una vez a la red Wi-Fi, Spitz AX podrá recordar el nombre de la red y la contraseña. Se conectará automáticamente la próxima vez que se encuentre cerca.

### En zonas sin cobertura celular

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Si va a desplazarse a una zona sin cobertura celular, como un área desértica con poca población, use Starlink, un servicio de Internet por satélite. De esta forma, en zonas con buena cobertura celular podrá usar la señal 5G recibida por Spitz AX, y en zonas sin cobertura celular podrá usar Starlink.

Cuando instale la antena de Starlink, asegúrese de que no haya obstrucciones. Los obstáculos a ambos lados de la carretera, como árboles, afectarán a la recepción, así que procure aparcar lejos de cualquier obstrucción.

---

## 4. Establezca las prioridades de failover

Spitz AX admite multi-WAN, incluyendo failover y balanceo de carga. Puede establecer prioridades de failover para diferentes redes según su escenario.

| Escenario                                                  | Prioridad                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| En el camping, conectado a su red Wi-Fi mediante repetidor | <p>Asigne al repetidor una prioridad superior a la conexión celular.</p> <p>En cuanto salga del camping, su router cambiará automáticamente a la conexión celular.</p>                                                                                                    |
| Starlink (ethernet) + celular                              | <p>Asigne a la conexión celular una prioridad superior a ethernet.</p> <p>En las zonas con cobertura celular, su router usará la red celular.</p> <p>Cuando llegue a zonas sin cobertura celular, su router cambiará automáticamente a Starlink a través de ethernet.</p> |

Para configurar el failover, consulte la sección [Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/).

---

¿Aún tiene preguntas? Visite nuestro [Community Forum](https://forum.gl-inet.com){target="\_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="\_blank"}.
