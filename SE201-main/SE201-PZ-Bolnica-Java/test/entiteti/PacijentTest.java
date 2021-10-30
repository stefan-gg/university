package entiteti;

import izuzeci.JMBGException;
import java.util.ArrayList;
import java.util.List;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

public class PacijentTest {

    public PacijentTest() {
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
    public void testGetStepenBolesti() {
        System.out.println("getStepenBolesti");
        Pacijent instance = new Pacijent();
        instance.setStepenBolesti(2);
        int expResult = 2;
        int result = instance.getStepenBolesti();
        assertEquals(expResult, result);

    }

    @Test
    public void testSetStepenBolesti() {
        System.out.println("setStepenBolesti");
        int newStepenBolesti = 3;
        Pacijent instance = new Pacijent();
        instance.setStepenBolesti(newStepenBolesti);
        assertEquals(instance.getStepenBolesti(), newStepenBolesti);
    }

    @Test
    public void testGetIdBrojIzabranogDoktora() {
        System.out.println("getIdBrojIzabranogDoktora");
        Pacijent instance = new Pacijent();
        instance.setIdBrojIzabranogDoktora(12);
        int expResult = 12;
        int result = instance.getIdBrojIzabranogDoktora();
        assertEquals(expResult, result);
    }

    @Test
    public void testSetIdBrojIzabranogDoktora() {
        System.out.println("setIdBrojIzabranogDoktora");
        int newIdBrojIzabranogDoktora = 12;
        Pacijent instance = new Pacijent();
        instance.setIdBrojIzabranogDoktora(newIdBrojIzabranogDoktora);
        assertEquals(instance.getIdBrojIzabranogDoktora(), newIdBrojIzabranogDoktora);
    }

    @Test
    public void testGetJmbg() throws JMBGException {
        System.out.println("getJmbg");
        Pacijent instance = new Pacijent();
        instance.setJmbg("1111111111111");
        String expResult = "1111111111111";
        String result = instance.getJmbg();
        assertEquals(expResult, result);
    }

    @Test
    public void testSetJmbg() throws JMBGException {
        System.out.println("setJmbg");
        String newJmbg = "1111111111111";
        Pacijent instance = new Pacijent();
        instance.setJmbg(newJmbg);
        assertEquals(instance.getJmbg(), newJmbg);
    }

    @Test(expected = JMBGException.class)
    public void testSetJmbg2() throws JMBGException{
        System.out.println("setJmbg2");
        String newJmbg = "1111";
        Pacijent instance = new Pacijent();
        instance.setJmbg(newJmbg);
    }
    
    @Test(expected = JMBGException.class)
    public void testObrisiPacijenta() throws JMBGException {
        System.out.println("obrisiPacijenta");
        String jmbgPacijenta = "1111111111111";
        Pacijent instance = new Pacijent();
        instance.setJmbg("0");
        instance.obrisiPacijenta(jmbgPacijenta);
    }

    @Test
    public void testAzurirajPacijenta() {
        System.out.println("azurirajPacijenta");
        String newIme = "Novo";
        Pacijent pacijent = new Pacijent();
        pacijent.setIme(newIme);
        Pacijent instance = new Pacijent();
        instance.setIme(newIme);
        instance.azurirajPacijenta(pacijent);
        assertEquals(pacijent.getIme(), instance.getIme());
    }

    @Test
    public void testPrikazSvihPacijenata() {
        System.out.println("prikazSvihPacijenata");
        int idBroj = 0;
        Pacijent instance = new Pacijent();
        List<Pacijent> expResult = new ArrayList<>();
        List<Pacijent> result = instance.prikazSvihPacijenata(idBroj);
        assertEquals(expResult, result);
    }

}
