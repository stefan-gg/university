package entiteti;

import izuzeci.JMBGException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

public class ZakazanaPosetaTest {

    public ZakazanaPosetaTest() {
    }

    @BeforeClass
    public static void setUpClass() {
    }

    @AfterClass
    public static void tearDownClass() {
    }

    @Before
    public void setUp() {
    }

    @After
    public void tearDown() {
    }

    @Test
    public void testGetJmbgPacijenta() throws JMBGException {
        System.out.println("getJmbgPacijenta");
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setJmbgPacijenta("1231231231231");
        String expResult = "1231231231231";
        assertEquals(instance.getJmbgPacijenta(), expResult);
    }

    @Test(expected = JMBGException.class)
    public void testGetJmbgPacijenta2() throws JMBGException {
        System.out.println("getJmbgPacijenta");
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setJmbgPacijenta("12");

    }

    @Test
    public void testSetJmbgPacijenta() throws JMBGException {
        System.out.println("setJmbgPacijenta");
        String newJmbgPacijenta = "1231231231233";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setJmbgPacijenta(newJmbgPacijenta);
        assertEquals(instance.getJmbgPacijenta(), "1231231231233");
    }

    @Test
    public void testGetJmbgPosetioca() throws JMBGException {
        System.out.println("getJmbgPosetioca");
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setJmbgPosetioca("1231231231231");
        String expResult = "1231231231231";
        assertEquals(instance.getJmbgPosetioca(), expResult);
    }

    @Test
    public void testSetJmbgPosetioca() throws JMBGException {
        System.out.println("setJmbgPosetioca");
        String newJmbgPosetioca = "1231231231231";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setJmbgPosetioca(newJmbgPosetioca);
        assertEquals(instance.getJmbgPosetioca(), "1231231231231");
    }

    @Test(expected = JMBGException.class)
    public void testSetJmbgPosetioca2() throws JMBGException {
        System.out.println("setJmbgPosetioca");
        String newJmbgPosetioca = "1";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setJmbgPosetioca(newJmbgPosetioca);
        assertEquals(instance.getJmbgPosetioca(), "1231231231231");
    }

    @Test
    public void testGetDatumPosete() {
        System.out.println("getDatumPosete");
        ZakazanaPoseta instance = new ZakazanaPoseta();
        Date expResult = new Date(12, 3, 20);
        instance.setDatumPosete(expResult);
        Date result = instance.getDatumPosete();
        assertEquals(expResult, result);

    }

    @Test
    public void testSetDatumPosete() {
        System.out.println("setDatumPosete");
        Date newDatumPosete = new Date(12, 3, 20);
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.setDatumPosete(newDatumPosete);
        assertEquals(instance.getDatumPosete(), newDatumPosete);
    }

    @Test
    public void testMogucnostZakazivanjaPosete() {
        System.out.println("mogucnostZakazivanjaPosete");
        String jmbgPacijenta = "11111111111111";
        String jmbgPosetioca = "1231231231231";
        Date datumPosete = null;
        ZakazanaPoseta instance = new ZakazanaPoseta();
        boolean expResult = false;
        boolean result = instance.mogucnostZakazivanjaPosete(jmbgPacijenta, jmbgPosetioca, datumPosete);
        assertEquals(expResult, result);
    }

    @Test
    public void testMogucnostZakazivanjaPosete2() {
        System.out.println("mogucnostZakazivanjaPosete");
        String jmbgPacijenta = "123";
        String jmbgPosetioca = "1231231231231";
        Date datumPosete = null;
        ZakazanaPoseta instance = new ZakazanaPoseta();
        boolean expResult = false;
        boolean result = instance.mogucnostZakazivanjaPosete(jmbgPacijenta, jmbgPosetioca, datumPosete);
        assertEquals(expResult, result);
    }

    @Test
    public void testProveraValidnostiJMBG() {
        System.out.println("proveraValidnostiJMBG");
        String jmbgPacijenta = "1231231231231";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        boolean expResult = false;
        boolean result = instance.proveraValidnostiJMBG(jmbgPacijenta);
        assertEquals(expResult, result);
    }

    @Test
    public void testObrisanaPoseta() {
        System.out.println("obrisanaPoseta");
        String jmbgPacijenta = "1231231231231";
        String jmbgPosetioca = "1231231231231";
        Date datumPosete = null;
        ZakazanaPoseta instance = new ZakazanaPoseta();
        boolean expResult = true;
        boolean result = instance.obrisanaPoseta(jmbgPacijenta, jmbgPosetioca, datumPosete);
        assertEquals(expResult, result);
    }

    @Test
    public void testZakazanePosete() {
        System.out.println("zakazanePosete");
        String jmbgPosetioca = "11111111111111";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        List<ZakazanaPoseta> expResult = new ArrayList<>();
        List<ZakazanaPoseta> result = instance.zakazanePosete(jmbgPosetioca);
        assertEquals(expResult, result);
    }

    @Test
    public void testPrikazZakazanihPoseta() {
        System.out.println("prikazZakazanihPoseta");
        String jmbg = "111111111111";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        List<ZakazanaPoseta> expResult = new ArrayList<>();
        List<ZakazanaPoseta> result = instance.prikazZakazanihPoseta(jmbg);
        assertEquals(expResult, result);
    }

    @Test
    public void testPregledZakazanePosete() {
        System.out.println("pregledZakazanePosete");
        ZakazanaPoseta instance = new ZakazanaPoseta();
        instance.pregledZakazanePosete(instance);
        assertEquals(instance, instance);
    }

    @Test
    public void testPotvrdaBrisanjaPosete() {
        System.out.println("potvrdaBrisanjaPosete");
        String odgovor = "Da";
        ZakazanaPoseta instance = new ZakazanaPoseta();
        boolean expResult = true;
        boolean result = instance.potvrdaBrisanjaPosete(odgovor);
        assertEquals(expResult, result);
    }

    @Test
    public void testProveraStepenaBolesti() {
        System.out.println("proveraStepenaBolesti");
        Pacijent pacijent = new Pacijent();
        pacijent.setStepenBolesti(4);
        ZakazanaPoseta instance = new ZakazanaPoseta();
        boolean expResult = false;
        boolean result = instance.proveraStepenaBolesti(pacijent);
        assertEquals(expResult, result);
    }

}
