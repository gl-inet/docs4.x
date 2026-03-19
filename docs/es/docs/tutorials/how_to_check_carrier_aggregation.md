# Cómo comprobar el estado de agregación de portadoras en su router celular

La agregación de portadoras combina varias bandas de red para proporcionar mayor ancho de banda y velocidades más rápidas en su conexión celular.
Esta función no puede habilitarse desde el panel de administración web del router, ya que depende de que su operador SIM la admita.
Sin embargo, puede comprobar el estado de la agregación de portadoras mediante comandos AT en el panel de administración web del router.

!!! note "Modelos compatibles"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Siga los pasos que se indican a continuación para comprobar el estado de la agregación de portadoras.

1. Inserte una tarjeta SIM en el router.
2. Abra un navegador web, escriba `192.168.8.1` en la barra de direcciones e inicie sesión.
3. Vaya a **INTERNET** -> **Cellular**, haga clic en el icono de tres puntos de la esquina superior derecha y luego en **Modem AT Command**.
    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}
4. En la ventana emergente, introduzca **AT+QCAINFO** y haga clic en **Send**.

    Si la agregación de portadoras está activa, verá varias bandas de red en la lista.
    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
