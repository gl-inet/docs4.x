# Conectar el puerto SFP+ de 10G de Flint 4

Flint 4 (GL‑BE14000) incluye un puerto SFP+ de 10G que puede alternar entre los modos WAN y LAN. Este puerto es compatible con varios tipos de módulos SFP+ y cables para conexiones Ethernet ópticas y de cobre. De este modo, satisface distintas necesidades de red, como el acceso por fibra a larga distancia, el cableado convencional de par trenzado y la terminación avanzada de fibra PON.

A continuación se describen detalladamente las tres soluciones para conectar el puerto SFP+ de Flint 4 (GL-BE14000). La información sobre los casos de uso, las topologías de conexión, las ventajas y desventajas, las precauciones y los modelos compatibles se proporciona únicamente como referencia.

## Solución 1: Transceptor óptico y cable de fibra

### 1.1 Casos de uso

Esta solución es adecuada para redes Ethernet de 10G estables y de larga distancia. Se utiliza principalmente en dos casos:

- Conexión a enlaces ascendentes Ethernet de fibra pura de 10G del proveedor de Internet para ofrecer acceso de banda ancha de muy alta velocidad en hogares y empresas;
- Implementación de interconexiones de red de larga distancia en interiores o exteriores, como la conexión de Flint 4 a un switch 10G remoto, el cableado de una red doméstica entre plantas o el despliegue de la red troncal de una oficina pequeña.

### 1.2 Topología

Puerto SFP+ de 10G de Flint 4 → Transceptor óptico SFP+ de 10G estándar (SR/MR/LR) → Cable de fibra óptica → Switch de red 10G remoto/terminal Ethernet por fibra del proveedor de Internet

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Ventajas y desventajas

La siguiente tabla evalúa aspectos clave del rendimiento y la facilidad de uso de la solución con transceptor óptico y cable de fibra. Las puntuaciones y observaciones se ofrecen como referencia:

|Criterio|Puntuación|Observaciones|
|---|---|---|
|Distancia de transmisión|★★★★★|Admite hasta 300 m (multimodo) o más de 10 km (monomodo), supera los límites de distancia del cable de cobre y resulta adecuado para redes de largo alcance.|
|Resistencia a interferencias|★★★★★|La transmisión de señales ópticas es inmune a las interferencias electromagnéticas, la electricidad estática y la diafonía, lo que garantiza un funcionamiento estable en entornos complejos.|
|Ahorro de energía|★★★★★|Bajo consumo y poca generación de calor; el diseño consolidado del chip permite un funcionamiento estable a plena carga durante periodos prolongados sin riesgo de sobrecalentamiento.|
|Compatibilidad|★★★★★|Cuenta con compatibilidad oficial completa, cumple los protocolos Ethernet de 10G estándar y no presenta riesgos de adaptación del firmware.|
|Facilidad de instalación|★★★☆☆|Requiere conocimientos básicos sobre las especificaciones de conexión de fibra. Una manipulación incorrecta puede atenuar la señal, por lo que exige algo más de experiencia que el cableado de cobre.|
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

El módulo SFP‑10G‑T convierte la ranura óptica SFP+ en una interfaz de par trenzado RJ45 estándar. Es adecuado para redes 10G de corta distancia basadas en cables de red convencionales. Entre sus aplicaciones habituales se incluyen las conexiones de corta distancia entre Flint 4 y switches 10G o dispositivos NAS, la ampliación rápida de puertos de red RJ45 de 10G sin volver a instalar fibra y el cableado de redes locales domésticas o SOHO de alta velocidad que conservan el par trenzado tradicional. Es la mejor alternativa para quienes necesitan Ethernet de 10G pero no disponen de cableado de fibra.

### 2.2 Topología

Puerto SFP+ de 10G de Flint 4 → Módulo SFP+ a RJ45 (SFP‑10G‑T) → Cable de par trenzado CAT6A/CAT7 → Switch 10G/dispositivo terminal 10G por cable

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Ventajas y desventajas

La siguiente tabla evalúa aspectos clave del rendimiento y la facilidad de uso de la solución con módulo SFP+ a RJ45 (SFP‑10G‑T). Las puntuaciones y observaciones se ofrecen como referencia:

|Criterio|Puntuación|Observaciones|
|---|---|---|
|Distancia de transmisión|★★☆☆☆|Debido a las limitaciones del chip PHY, la distancia máxima de transmisión estable es de solo 30 metros. No es adecuado para cableado de larga distancia.|
|Resistencia a interferencias|★★★☆☆|La transmisión tradicional por par trenzado es susceptible a las interferencias electromagnéticas y la diafonía en instalaciones de cableado complejas.|
|Ahorro de energía|★★☆☆☆|Alto consumo y generación de calor evidente con cargas elevadas continuas; se requiere una gestión adecuada de la disipación térmica para el funcionamiento prolongado.|
|Compatibilidad|★★★★☆|Compatible con todos los terminales RJ45 de 10G estándar; solo los cables CAT6A/CAT7 admiten una transmisión 10G estable.|
|Facilidad de instalación|★★★★★|Plug-and-play, sin necesidad de ajustar la ruta óptica y compatible con las prácticas habituales de instalación de cables de red; requiere muy poca experiencia.|
|Economía|★★★★☆|Permite reutilizar el cableado RJ45 existente sin coste de conversión a fibra; solo es necesario adquirir por separado un módulo 10G-T.|

### 2.4 Precauciones

- Debe utilizar cables de red CAT6A o de especificaciones superiores para obtener una transmisión 10G estable. Los cables CAT6 o inferiores provocarán una reducción de velocidad y pérdida de paquetes.

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

El módulo PON‑ONU SFP+ integra todas las funciones ONU de un módem óptico, lo que permite que el puerto SFP+ de Flint 4 termine directamente líneas de fibra residenciales GPON/XGS-PON convencionales. Esta solución elimina la necesidad de un módem óptico externo independiente y permite que un solo dispositivo proporcione acceso por fibra y funciones de enrutamiento. Está destinada a configuraciones avanzadas para usuarios experimentados, especialmente a quienes desean simplificar el conjunto de equipos de su red doméstica y acceder directamente a las líneas de fibra PON del operador mediante el router.

### 3.2 Topología

Puerto SFP+ de 10G de Flint 4 → Módulo PON‑ONU SFP+ → Línea de fibra GPON/XGS-PON del proveedor de Internet (incluidos el cable de acometida, el divisor PON y la OLT del proveedor)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Ventajas y desventajas

La siguiente tabla evalúa aspectos clave del rendimiento y la facilidad de uso de la solución con módulo PON‑ONU SFP+. Las puntuaciones y observaciones se ofrecen como referencia:

|Criterio|Puntuación|Observaciones|
|---|---|---|
|Distancia de transmisión|★★★★★|Se adapta a las distancias de transmisión de fibra PON estándar y cubre todos los casos habituales de acceso por fibra doméstico y comercial.|
|Resistencia a interferencias|★★★★★|La transmisión óptica por fibra ofrece una gran resistencia a las interferencias y una señal estable, de acuerdo con los estándares habituales de acceso por fibra PON.|
|Ahorro de energía|★★☆☆☆|Genera mucho calor durante el funcionamiento a alta velocidad; es obligatorio utilizar refrigeración auxiliar para evitar una reducción del rendimiento y desconexiones.|
|Compatibilidad|★★☆☆☆|Solución para usuarios experimentados sin verificación oficial; la compatibilidad depende de la lista de dispositivos permitidos del proveedor y del modelo del módulo, y el funcionamiento estable a largo plazo no está garantizado.|
|Facilidad de instalación|★★☆☆☆|Requiere confirmación previa del proveedor, configurar la autenticación SN/PLOAM y optimizar la disipación térmica; la instalación presenta una complejidad elevada.|
|Economía|★★★☆☆|Elimina el coste de un módem óptico independiente, pero puede ocasionar riesgos de servicio, como la falta de IPTV o servicios de voz y la ausencia de asistencia técnica oficial.|

### 3.4 Precauciones

- **Confirme previamente la autorización del proveedor de Internet**: Consulte al operador si permite conectar hardware ONU de terceros propiedad del cliente a la red PON y obtenga los parámetros de autenticación obligatorios, incluidos el código de registro SN y la contraseña PLOAM.

- **La disipación térmica es obligatoria**: Equipe el módulo PON‑ONU con medidas auxiliares de disipación térmica para evitar reducciones de frecuencia, pérdida de paquetes y desconexiones provocadas por temperaturas elevadas.

- **Sin garantía de servicio**: GL.iNet no proporciona asistencia técnica para esta solución. Los problemas como la inestabilidad de la red, las fluctuaciones de velocidad y el funcionamiento anómalo de servicios de valor añadido no se pueden resolver mediante el firmware oficial ni el servicio posventa.

- Cada operador aplica reglas distintas a la lista de modelos de módulos permitidos. Antes de comprar, confirme qué modelos de módulos PON admite su operador.

### 3.5 Modelos compatibles

Los siguientes módulos PON-ONU SFP+ han sido probados por GL.iNet y usuarios de la comunidad y son compatibles con Flint 4. La lista se proporciona únicamente como referencia.

|Modelo|Responsable de la prueba|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Usuario de la comunidad|

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
