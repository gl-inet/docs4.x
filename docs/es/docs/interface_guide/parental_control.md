# Control parental

El control parental es una forma de mantener a los menores seguros en Internet bloqueando sitios web inapropiados y limitando el tiempo que usan los dispositivos. Ayuda a evitar el acceso a contenido perjudicial, gestionar el tiempo de pantalla y garantizar un uso responsable de Internet.

Esta función está disponible desde el firmware v4.2. **Nota**: Algunos modelos, aunque ejecuten el firmware v4.2 o superior, no admiten Parental Control por memoria insuficiente.

Vea este vídeo o siga los pasos que se indican a continuación para configurar Parental Control en los routers GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Versión local

La versión local es proporcionada por GL.iNet. Actualmente está en fase beta y no tiene coste adicional. En esta versión, si necesita filtrar solicitudes por aplicación, debe introducir manualmente el dominio.

### Modelos compatibles

??? "Modelos compatibles" - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-AX1800 (Flint) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus)

??? "Modelos no compatibles" - GL-SFT1200 (Opal) - GL-MT1300 (Beryl) - GL-E750/E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-XE300 (Puli) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus) - GL-X300B (Collie)

### Pasos de configuración

Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **Parental Control**.

En el firmware v4.8.4 y versiones posteriores, vaya a **Flow Control** -> **Parental Control**.

Asegúrese de que la hora del router sea correcta. Si no es así, vaya primero a **SYSTEM** -> **Time Zone** para sincronizarla.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Active Parental Control y haga clic en **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: se utiliza para bloquear el acceso a Internet de los dispositivos no gestionados.

Después, siga el asistente de configuración para configurar Parental Control.

---

A continuación se muestran dos casos de uso como referencia. Puede ajustar la configuración según sus necesidades.

**Caso 1**

**Escenario**: Los dispositivos del perfil solo pueden acceder a Internet para estudiar de 8:00 a 11:00 de lunes a viernes, y para jugar de 18:00 a 20:00 los fines de semana. En cualquier otro momento, el acceso a Internet queda bloqueado de forma predeterminada.

Siga los pasos que se indican a continuación.

1. Cree un perfil y personalice su nombre.

   ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Seleccione los dispositivos que desea gestionar. Primero debe conectarlos al router. Si aún no se han conectado, añádalos manualmente introduciendo sus direcciones MAC.

   ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Configure el límite de acceso.

   Hay dos conjuntos de reglas predeterminados: **Block Internet Access** y **No Limit**.

   ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

   Cree otros dos conjuntos de reglas para usarlos más adelante: **Learning** y **Play**. Haga clic en **Add a New Ruleset**.

   ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

   Especifique el nombre del conjunto de reglas, por ejemplo Learning, el color e introduzca los sitios que desea bloquear. A continuación, haga clic en **Apply**.

   ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

   **Nota**: Los nombres de dominio introducidos en la lista de bloqueo deben incluir también sus subdominios. Por ejemplo, si se introduce "example.com", también incluirá cualquier subdominio, como "subdomain.example.com".

   Del mismo modo, cree otro conjunto de reglas. Especifique el nombre del conjunto de reglas, por ejemplo Play, el color e introduzca los sitios que desea bloquear. A continuación, haga clic en **Apply**.

   ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

   Una vez aplicado, habrá un total de cuatro conjuntos de reglas, como se muestra a continuación. Asegúrese de seleccionar **Block Internet Access** como **Default Ruleset** y haga clic en **Finish**.

   ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. A continuación, configure la programación de su perfil. Haga clic en **Go to Set**.

   ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

   Añada el conjunto de reglas **Learning** a la programación. Establezca la **Execution Time** de 8:00 a 11:00 de lunes a viernes y haga clic en **Apply**.

   ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. Después se le redirigirá a la página de edición del perfil recién creado.

   ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

   Desplácese hasta la parte inferior y verá que se ha creado una programación. Haga clic en el icono del engranaje en la parte superior derecha y seleccione **Add Schedule**.

   ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Añada otro conjunto de reglas, **Play**, a la programación. Establezca la **Execution Time** de 18:00 a 20:00 los fines de semana y haga clic en **Apply**.

   ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

   El conjunto de reglas **Play** se añadirá entonces a la programación.

   ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

   **Nota**: La línea roja discontinua indica la hora actual.

   También puede modificar la hora de ejecución haciendo clic en un conjunto de reglas concreto dentro de la programación.

   ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Haga clic en **Parental Control** en la parte superior para volver a la página de Parental Control.

   ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

   Verá la configuración final. El control parental ya surte efecto según la programación. Puede modificar los perfiles y conjuntos de reglas existentes o añadir otros nuevos según sea necesario.

   ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

**Caso 2**

**Escenario**: Los dispositivos del perfil solo pueden acceder a Internet para juegos y vídeos cortos entre las 18:00 y las 20:00 durante las noches del fin de semana. En cualquier otro momento, incluido el horario de descanso desde las 21:00 hasta las 7:00 de la mañana siguiente, el acceso a Internet queda bloqueado de forma predeterminada.

Consulte el siguiente videotutorial.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Solución de problemas

Si la configuración que ha establecido no surte efecto, compruebe las siguientes posibles causas.

1. Caché DNS.

   Los navegadores y los sistemas operativos mantienen cachés DNS, por lo que los cambios pueden tardar en surtir efecto. Puede borrar la caché para aplicar los cambios de inmediato.
   - [Borrar la caché en Chrome para escritorio](https://support.google.com/accounts/answer/32050){target="\_blank"}
   - [Borrar la caché en Edge para escritorio](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="\_blank"}

2. La programación del perfil aún no ha comenzado.

3. Es posible que el nombre de dominio introducido sea incorrecto.

   El dominio de un sitio web es público, pero el dominio de la API que utiliza una aplicación muchas veces no lo es. Para resolverlo, use una herramienta como Wireshark para capturar paquetes o busque el dominio correspondiente.

   Por ejemplo, para bloquear "www.google.com", usar "google.com" es más eficaz que usar "www.google.com".

4. El dispositivo de destino utiliza una dirección MAC aleatoria para cada conexión, lo que impide que las reglas surtan efecto.

## Versión Bark

La versión [Bark](https://www.bark.us/){target="\_blank"}, proporcionada y gestionada por Bark en su propia plataforma, ofrece la opción de filtrar aplicaciones y sitios web con un solo clic y supervisar el historial de solicitudes.

Ofrece funciones de supervisión para más de 24 aplicaciones populares y plataformas de redes sociales, incluidas en la lista preestablecida de nuestra función local de control parental.

Con su función de registros, anota qué cliente ha accedido a qué sitio web y en qué momento. Esto permite a los padres ver fácilmente los registros, identificar sitios web que no están en la lista negra y añadirlos rápidamente al ámbito de gestión.

La función Bark Parental Control está disponible desde el firmware v4.5 y solo es compatible con determinados routers GL.iNet.

**Nota**:

1. El servicio Bark está disponible **solo en Estados Unidos, Australia y Sudáfrica**. Haga clic [aquí](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="\_blank"} para ver los detalles.

2. El servicio Bark normalmente requiere una suscripción de pago. Sin embargo, como parte de nuestra colaboración con Bark, GL.iNet ofrece el plan Bark Home de forma gratuita en determinados modelos de router, con supervisión avanzada y alertas sin coste adicional.

3. Las dos versiones de Parental Control no pueden habilitarse al mismo tiempo. Al cambiar entre versiones, la otra se desactivará automáticamente.

### Modelos compatibles

??? "Modelos compatibles" - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-B3000 (Marble) - GL-MT6000 (Flint2)

??? "Modelos no compatibles" - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-AX1800 (Flint) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus) - GL-SFT1200 (Opal) - GL-MT1300 (Beryl) - GL-E750/E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-XE300 (Puli) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus) - GL-X300B (Collie)

### Pasos de configuración

Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **Parental Control**.

Seleccione la versión Bark, active el interruptor y haga clic en **Apply**.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Nota:** Es posible que el servicio Bark no esté disponible en determinados países. Como GL.iNet no es el proveedor de este servicio, si encuentra algún problema al usar Bark, póngase en contacto directamente con el [soporte técnico de Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet) para obtener ayuda.

El servicio Bark está habilitado, pero este dispositivo todavía no está vinculado a ninguna cuenta. Utilice el [enlace de vinculación del dispositivo](https://www.bark.us/app/signup/?ref=glinet&home=glinet) para vincular este dispositivo con su cuenta de Bark.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Una vez vinculado, la página se mostrará como se indica a continuación.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Su dispositivo ahora está conectado a Bark Cloud Services y vinculado a su cuenta. [Vaya a Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) e inicie sesión en su cuenta para crear un perfil de control de red.

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
