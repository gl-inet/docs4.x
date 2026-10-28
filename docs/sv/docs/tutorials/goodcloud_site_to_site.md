# GoodCloud Site to Site {#goodcloud-site-to-site}

## Introduktion {#introduction}

GoodCloud Site to Site gör att kontor på flera platser kan upprätta säkra anslutningar till varandra via internet. Företagets nätverk utökas så att datorresurser på en plats blir tillgängliga för medarbetare på andra platser i nätverket.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenario 1**: Flera filialkontor inom samma företag behöver integreras i ett gemensamt privat nätverk för smidig resursdelning mellan alla platser.

**Scenario 2**: När två företag med nära samarbeten behöver arbeta tillsammans kan Site to Site ge dem en delad och säker nätverksmiljö.

**Scenario 3**: För familjer med IP-kameror ger Site to Site fjärråtkomst till enheten när familjemedlemmarna inte är hemma, så att de enkelt kan övervaka hemmet varifrån som helst.

## Villkor {#conditions}

1. Minst två GL.iNet-routrar krävs för att skapa ett Site to Site-nätverk.

2. Minst en router måste ha en offentlig IP-adress så att den kan anges som primär nod. [Kontrollera om internetleverantören tilldelar dig en offentlig IP-adress](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    Välj helst routern med högst prestanda och bäst nätverkshastighet som Main Node.

3. Det rekommenderas **INTE** att köra Site to Site samtidigt som undernoderna kör en VPN-klient/Tailscale/ZeroTier/AstroWarp, eftersom det kan göra nätverkskonfigurationen särskilt komplicerad.

## Skapa ett Site to Site-nätverk {#build-a-site-to-site-network}

1. Koppla routrarna till ditt GoodCloud-konto. Se [Bind Devices to Cloud](../interface_guide/cloud.md#bind-devices-to-cloud).

2. Logga in på [GoodCloud](https://www.goodcloud.xyz/#/login){target="_blank"}, gå till **Site to Site** i det vänstra sidofältet och klicka på **Create Network** i det övre högra hörnet.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Markera kryssrutan till vänster för att välja minst två enheter.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

    De valda enheterna visas på sidans nedre del.

    Standardporten för Site to Site är **51830**. Om du vill använda en annan port klickar du på **Advanced** i det nedre vänstra hörnet och ändrar den. Klicka sedan på **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Ett Site to Site-nätverk kan ha högst 10 enheter för att säkerställa stabila prestanda.

4. Namnge nätverket och klicka på **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing börjar kontrollera om någon enhet kan anges som Main Node.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Om ingen av enheterna kan användas som Main Node kontrollerar du följande:

    - Minst en router har en offentlig IP-adress, antingen statisk eller dynamisk.
    - Porten är öppen. Standardporten för Site to Site är 51830. Du kan även byta port och försöka igen.
    - Om routern som du vill ange som Main Node finns bakom NAT kan du behöva konfigurera portvidarebefordran.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Om flera enheter kan anges som Main Node väljer du en av dem för att fortsätta. Vi rekommenderar att du väljer routern med hög prestanda och bäst nätverkshastighet som Main Node.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Om endast en enhet kan anges som Main Node öppnas informationssidan för Site to Site direkt.

6. Nätverket är inaktiverat som standard. Kontrollera att LAN-IP-adresserna för alla noder inte står i konflikt med varandra. Klicka på kugghjulsikonen för att ändra LAN-IP-adressen vid behov och klicka på **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Vänta i några minuter. När den streckade linjen blir heldragen har Site to Site-nätverket upprättats.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Testa Site to Site-anslutningen {#testing-the-site-to-site-connection}

1. Anslut en dator eller smarttelefon till en av noderna i Site to Site-nätverket.

2. Öppna en webbläsare och gå till en annan nods LAN-IP-adress. Om inloggningssidan öppnas fungerar anslutningen mellan de två noderna.

## Routning och andra alternativ {#route-and-other-options}

Som standard kan varje nod komma åt de andra nodernas LAN. Av säkerhetsskäl rekommenderar vi att du endast öppnar IP-adresserna för särskilda tjänster.

Anta till exempel att det finns en Server A (172.30.97.100) i subnätet för Node 1. Om du vill att andra noder endast ska komma åt Service A på Node 1 kan du konfigurera det enligt följande:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Du kan även lägga till nodens överordnade rutter.

Varje Sub Node skapar ett krypterat tunnelnätverk till Main Node. Om du vill ändra tunnelns subnäts-IP-adress klickar du på **IP Address Range**.

När ett nytt IP-adressintervall tillämpas kopplas nätverket från i några minuter.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
