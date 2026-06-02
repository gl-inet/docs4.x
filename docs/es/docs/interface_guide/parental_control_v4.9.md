# Control parental (Firmware v4.9)

> Esta guía se aplica al firmware v4.9 y versiones posteriores. Para versiones anteriores, haga clic [aquí](parental_control.md).

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **Parental Control**.

El control parental protege a los menores en Internet bloqueando sitios web inapropiados y limitando el tiempo de pantalla. Filtra contenido perjudicial y fomenta un uso responsable de Internet.

GL.iNet Parental Control ofrece programación flexible para restringir el acceso a Internet en los dispositivos que sus hijos usan con frecuencia. Puede bloquear aplicaciones y sitios web inapropiados con un solo clic. Además, puede introducir dominios manualmente según sea necesario para lograr una protección online completa.

El diseño de la página y el flujo de trabajo de Parental Control se han mejorado en el firmware v4.9, lo que simplifica la configuración y ofrece una vista más intuitiva de las reglas.

---

Siga los pasos que se indican a continuación para configurar el control parental.

1. Inicie sesión en el panel de administración web del router y vaya a **FLOW CONTROL** -> **Parental Control**. Asegúrese de que la hora del router sea correcta.

    ![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/router_time.png){class="glboxshadow"}

    Si no es así, vaya primero a **SYSTEM** -> **Time Zone** para sincronizarla.

2. Active Parental Control y haga clic en **Apply**.

    ![enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/enable.png){class="glboxshadow"}

3. Verá una lista de reglas como la siguiente. Haga clic en **Add a New Rule**.

    ![add a new rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/add_rules.png){class="glboxshadow"}

4. En la ventana emergente, cree una regla, establezca un nombre personalizado y luego haga clic en **Next**.

    ![create a rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/create_rule.png){class="glboxshadow gl-90-desktop"}

5. Seleccione el dispositivo de su hijo y luego haga clic en **Next**.

    Un dispositivo solo aparecerá en esta página si está conectado al router por Wi-Fi o Ethernet. El color cian indica que está en línea, mientras que el gris indica que está desconectado.

    ![select device](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/select_device.png){class="glboxshadow gl-90-desktop"}

    **Consejo**: Si desea distinguir mejor los dispositivos conectados, vaya a la página **CLIENTS** y personalice los nombres de los dispositivos.

6. Establezca la hora de dormir para el dispositivo de su hijo y luego haga clic en **Next**.

    Durante este periodo, Internet no estará disponible en los dispositivos seleccionados. De forma predeterminada, la misma hora de dormir se aplica a todos los días.

    ![bedtime1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/bedtime1.png){class="glboxshadow gl-90-desktop"}

    Si desea configurar distintas horas de dormir para cada día de la semana, seleccione **Customize Days** y establezca diferentes horas de dormir, luego haga clic en **Next**.

    ![bedtime2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/bedtime2.png){class="glboxshadow gl-90-desktop"}

7. Seleccione el filtro de contenido.

    Tres categorías están seleccionadas de forma predeterminada: **Gambling**, **Malicious Content** y **Sexual Content**.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Puede seleccionar otras categorías si lo necesita, como **Games**, **Shopping**, **Social Media**, **Entertainment**, etc.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Si la aplicación que desea bloquear es difícil de localizar, use la búsqueda en la parte superior para encontrarla rápidamente.

    ![search app](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/search_app.png){class="glboxshadow gl-90-desktop"}

8. Si necesita bloquear determinados dominios, haga clic en **Advanced Settings** en la esquina inferior derecha.

    ![block domain1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/block_domain1.png){class="glboxshadow gl-90-desktop"}

    Introduzca los dominios manualmente y luego haga clic en **Finish**.

    ![block domain2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/block_domain2.png){class="glboxshadow gl-90-desktop"}

9. La regla ya está añadida. La lista muestra el nombre de la regla, el número de dispositivos conectados, el horario de descanso, el contenido filtrado y el estado de la regla (activada/desactivada).

    ![rules added](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/rules_added.png){class="glboxshadow"}

    Puede realizar operaciones básicas sobre las reglas existentes: Modify, Copy y Delete.

    ![action](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action.png){class="glboxshadow"}

    - **Modify**: Cambie los dispositivos seleccionados, el horario de descanso y las reglas del filtro de contenido.

        ![action modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action_modify.png){class="glboxshadow"}

    - **Copy**: Cree una copia de una regla existente para no tener que volver a configurarla manualmente.

        ![action copy](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action_copy.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
