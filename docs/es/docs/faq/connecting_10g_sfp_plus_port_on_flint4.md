# Conectar el puerto SFP+ de 10G de Flint 4

Flint 4 (GL-BE14000) incluye un puerto SFP+ de 10G que puede funcionar en modo WAN o LAN. El puerto admite varios tipos de módulos SFP+ y cables para conexiones Ethernet de fibra óptica y cobre, incluidas conexiones de fibra a larga distancia, cableado convencional de par trenzado y terminación avanzada de fibra PON.

Este artículo describe tres opciones para conectar el puerto SFP+ de Flint 4 (GL-BE14000), incluidos sus casos de uso, topologías de conexión, ventajas y desventajas, precauciones y modelos compatibles.

## Solución 1: Transceptor óptico y cable de fibra

### 1.1 Casos de uso

Esta solución está indicada para conexiones Ethernet de 10G fiables y de larga distancia. Entre sus usos habituales se incluyen:

- Conexión al enlace ascendente Ethernet de fibra de 10G de un proveedor de Internet para obtener acceso de banda ancha de alta velocidad en hogares o empresas.
- Implementación de enlaces de red de larga distancia en interiores o exteriores, como la conexión de Flint 4 a un switch 10G remoto, el cableado entre plantas de una vivienda o el despliegue de la red troncal de una oficina pequeña.

### 1.2 Topología

Puerto SFP+ de 10G de Flint 4 → Transceptor óptico SFP+ de 10G estándar (SR/MR/LR) → Cable de fibra óptica → Switch de red 10G remoto/terminal Ethernet por fibra del proveedor de Internet

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Ventajas y desventajas

La siguiente tabla evalúa aspectos clave del rendimiento y la facilidad de uso de la solución con transceptor óptico y cable de fibra. Las puntuaciones y observaciones se ofrecen como referencia:

|Criterio|Puntuación|Observaciones|
|---|---|---|
|Distancia de transmisión|★★★★★|Admite distancias de hasta 300 m mediante fibra multimodo o de más de 10 km mediante fibra monomodo, por lo que resulta adecuado para conexiones de largo alcance.|
|Resistencia a interferencias|★★★★★|La transmisión de señales ópticas es inmune a las interferencias electromagnéticas, la electricidad estática y la diafonía, lo que garantiza un funcionamiento estable en entornos complejos.|
|Ahorro de energía|★★★★★|Ofrece bajo consumo y poca generación de calor. El diseño consolidado del chipset permite un funcionamiento estable a plena carga durante periodos prolongados sin sobrecalentamiento.|
|Compatibilidad|★★★★★|Cuenta con compatibilidad oficial y cumple los protocolos Ethernet de 10G estándar; no requiere adaptar el firmware.|
|Facilidad de instalación|★★★☆☆|Requiere conocimientos básicos sobre las conexiones de fibra. Una manipulación incorrecta puede atenuar la señal, por lo que la instalación es más compleja que con cableado de cobre.|
|Economía|★★★☆☆|Requiere transceptores ópticos y cables de fibra adicionales, por lo que el coste total es superior al de las soluciones tradicionales de par trenzado.|

### 1.4 Precauciones

- Solo se admiten transceptores ópticos Ethernet de 10G estándar. Los módulos ópticos con protocolo PON no son adecuados para esta solución.

- Seleccione módulos ópticos monomodo o multimodo y cables de fibra que se correspondan con la distancia real de transmisión para evitar una reducción de la velocidad o un fallo del enlace.

- Esta solución solo admite servicios Ethernet de 10G sobre fibra del proveedor de Internet. No puede conectarse directamente a líneas de fibra residenciales GPON/XGS-PON convencionales.

### 1.5 Modelos compatibles

Los siguientes transceptores ópticos estándar han sido probados por GL.iNet y usuarios de la comunidad y son compatibles con Flint 4. La lista se proporciona únicamente como referencia.

|Modelo|Responsable de la prueba|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Usuario de la comunidad|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Usuario de la comunidad|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Usuario de la comunidad|
|XZSNET SFP10G-SR|GL.iNet|
|10Gtek AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|10Gtek AZS85-192-M1 25G SFP28-SR 850nm 100m|GL.iNet|
|10Gtek ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|10Gtek ASF85-24-X2-D 1.25G SFP-SX 850nm 550m|GL.iNet|
|FS Cisco SFP-10G-SR Compatible 10GBASE-SR|GL.iNet|
|FS Juniper EX-SFP-10GE-SR 10GBASE-SR SFP+|GL.iNet|
|FS Arista SFP-10G-SR 10GBASE-SR SFP+|GL.iNet|
|FS Brocade 10G-SFPP-SR 10GBASE-SR SFP+|GL.iNet|
|HUAWEI 6G-850nm-120m-MM-SFP+ MTRS-6A11-01|GL.iNet|
|HUAWEI 2.5G-1310nm-SM-ESFP MXPD-483II|GL.iNet|
|netLINK 10G/850nm/300m/DDM HTB-10G-SR|GL.iNet|
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100m|GL.iNet|
|H!Fiber ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Usuario de la comunidad|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Usuario de la comunidad|

## Solución 2: Módulo SFP+ a RJ45 (SFP‑10G‑T)

### 2.1 Casos de uso

El módulo SFP-10G-T convierte la ranura SFP+ en una interfaz estándar RJ45 de par trenzado, por lo que resulta adecuado para redes 10G de corta distancia que usan cables Ethernet convencionales. Entre sus aplicaciones habituales se incluyen conectar Flint 4 a un switch 10G o NAS cercano, añadir un puerto RJ45 de 10G sin instalar fibra y crear una LAN doméstica o SOHO de alta velocidad con cableado de par trenzado existente. Esta opción es adecuada para quienes necesitan Ethernet de 10G pero no disponen de cableado de fibra.

### 2.2 Topología

Puerto SFP+ de 10G de Flint 4 → Módulo SFP+ a RJ45 (SFP‑10G‑T) → Cable de par trenzado CAT6A/CAT7 → Switch 10G/dispositivo terminal 10G por cable

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Ventajas y desventajas

La siguiente tabla evalúa aspectos clave del rendimiento y la facilidad de uso de la solución con módulo SFP+ a RJ45 (SFP‑10G‑T). Las puntuaciones y observaciones se ofrecen como referencia:

|Criterio|Puntuación|Observaciones|
|---|---|---|
|Distancia de transmisión|★★☆☆☆|El PHY limita la distancia de transmisión estable a 30 m, por lo que el módulo no es adecuado para cableado de larga distancia.|
|Resistencia a interferencias|★★★☆☆|La transmisión tradicional por par trenzado es susceptible a las interferencias electromagnéticas y la diafonía en instalaciones de cableado complejas.|
|Ahorro de energía|★★☆☆☆|Consume más energía y genera mucho calor con cargas elevadas continuas. Se requiere una disipación térmica adecuada para el funcionamiento prolongado.|
|Compatibilidad|★★★★☆|Compatible con dispositivos RJ45 de 10G estándar. Se requiere cableado CAT6A o CAT7 para una transmisión 10G estable.|
|Facilidad de instalación|★★★★★|Ofrece una instalación plug-and-play sin necesidad de configurar la ruta óptica y funciona con cableado Ethernet convencional.|
|Economía|★★★★☆|Permite reutilizar el cableado RJ45 existente sin instalar fibra, aunque se necesita un módulo 10GBASE-T independiente.|

### 2.4 Precauciones

- Use cables Ethernet CAT6A o de una categoría superior para obtener una transmisión 10G estable. Los cables de categorías inferiores pueden reducir la velocidad o causar pérdida de paquetes.

- Mantenga la longitud del cableado dentro de los 30 metros. Si supera este límite, la conexión puede volverse inestable, reducir la velocidad o desconectarse.

- Deje espacio suficiente alrededor del módulo SFP‑10G‑T para disipar el calor y evitar fallos del equipo debidos al sobrecalentamiento.

### 2.5 Modelos compatibles

Los siguientes módulos SFP+ a RJ45 han sido probados por GL.iNet y usuarios de la comunidad y son compatibles con Flint 4. La lista se proporciona únicamente como referencia.

|Modelo|Responsable de la prueba|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Usuario de la comunidad|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Usuario de la comunidad|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Usuario de la comunidad|

## Solución 3: Módulo PON‑ONU SFP+

### 3.1 Casos de uso

El módulo PON-ONU SFP+ proporciona las funciones de un módem óptico ONU, lo que permite que el puerto SFP+ de Flint 4 termine directamente líneas de fibra residenciales GPON/XGS-PON convencionales. Esta opción combina el acceso por fibra y el enrutamiento en un solo dispositivo, por lo que elimina la necesidad de un módem óptico externo independiente. Está destinada a instalaciones avanzadas para usuarios experimentados, en particular a quienes desean reducir el número de dispositivos de su red doméstica y conectar el router directamente a una línea de fibra PON del operador.

### 3.2 Topología

Puerto SFP+ de 10G de Flint 4 → Módulo PON‑ONU SFP+ → Línea de fibra GPON/XGS-PON del proveedor de Internet (incluidos el cable de acometida, el divisor PON y la OLT del proveedor)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Ventajas y desventajas

La siguiente tabla evalúa aspectos clave del rendimiento y la facilidad de uso de la solución con módulo PON‑ONU SFP+. Las puntuaciones y observaciones se ofrecen como referencia:

|Criterio|Puntuación|Observaciones|
|---|---|---|
|Distancia de transmisión|★★★★★|Admite las distancias de transmisión PON estándar para el acceso por fibra residencial y comercial habitual.|
|Resistencia a interferencias|★★★★★|La transmisión óptica por fibra ofrece una gran resistencia a las interferencias y una señal estable, de acuerdo con los estándares habituales de acceso por fibra PON.|
|Ahorro de energía|★★☆☆☆|Genera mucho calor durante el funcionamiento a alta velocidad; es obligatorio utilizar refrigeración auxiliar para evitar una reducción del rendimiento y desconexiones.|
|Compatibilidad|★★☆☆☆|Es una solución no oficial destinada a usuarios experimentados. La compatibilidad depende de la lista de dispositivos permitidos del proveedor y del modelo del módulo, y el funcionamiento a largo plazo puede ser inestable.|
|Facilidad de instalación|★★☆☆☆|Requiere confirmación previa del proveedor, configurar la autenticación SN/PLOAM y proporcionar refrigeración adecuada. La instalación es relativamente compleja.|
|Economía|★★★☆☆|Elimina el coste de un módem óptico independiente, pero puede afectar a servicios como IPTV y voz y no incluye asistencia técnica oficial.|

### 3.4 Precauciones

- **Confirme previamente la autorización del proveedor de Internet**: Consulte al operador si permite conectar hardware ONU de terceros propiedad del cliente a la red PON y obtenga los parámetros de autenticación obligatorios, incluidos el código de registro SN y la contraseña PLOAM.

- **La disipación térmica es obligatoria**: Equipe el módulo PON‑ONU con medidas auxiliares de disipación térmica para evitar reducciones de frecuencia, pérdida de paquetes y desconexiones provocadas por temperaturas elevadas.

- **Sin garantía de servicio**: GL.iNet no proporciona asistencia técnica para esta opción. Los problemas como la inestabilidad de la red, las fluctuaciones de velocidad o las incidencias en servicios de valor añadido no están cubiertos por el firmware oficial ni por el servicio posventa.

- Cada operador aplica reglas distintas a la lista de modelos de módulos permitidos. Antes de comprar, confirme qué modelos de módulos PON admite su operador.

### 3.5 Modelos compatibles

Los siguientes módulos PON-ONU SFP+ han sido probados por GL.iNet y usuarios de la comunidad y son compatibles con Flint 4. La lista se proporciona únicamente como referencia.

|Modelo|Responsable de la prueba|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Usuario de la comunidad|

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
