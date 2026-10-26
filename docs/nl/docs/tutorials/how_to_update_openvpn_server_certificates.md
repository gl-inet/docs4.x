# How to update OpenVPN server certificates? {#how-to-update-openvpn-server-certificates}

Deze handleiding beschrijft hoe je OpenVPN-servercertificaten op een GL.iNet-router bijwerkt.

**Opmerking**: hierbij wordt het Root CA-certificaat bijgewerkt, waardoor alle bestaande clientcertificaten in configuratiebestanden ongeldig worden. Exporteer alle OpenVPN-clientconfiguraties opnieuw om verbinding met de server te kunnen maken.

1. Meld je aan bij het webbeheerpaneel en ga naar **VPN** -> **OpenVPN Server**.

    Stop de dienst als de OpenVPN-server actief is.

2. Klik op het tabblad Configuration op **Advanced Configuration** om de instellingen uit te vouwen.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Zoek **Server Root Certificate** en verwijder de volledige inhoud van het tekstvak.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Het bijbehorende Server Certificate en de Server Key worden automatisch verwijderd.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Laat alle drie de vakken leeg en klik onderaan op **Apply**. Nieuwe certificaten worden automatisch gegenereerd en ingevuld.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. De OpenVPN Server-certificaten zijn bijgewerkt. Klik onderaan op **Export Client Configuration** om nieuwe configuratiebestanden voor je apparaten te exporteren.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
