package entiteti;

import izuzeci.BrojTelefonaException;
import izuzeci.JMBGException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

public class PosetilacTest {

    public PosetilacTest() {
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

    @Test(expected = BrojTelefonaException.class)
    public void testGetBrojTelefona() throws BrojTelefonaException {
        System.out.println("getBrojTelefona");
        Posetilac instance = new Posetilac();
        instance.setBrojTelefona("123");
        String expResult = "123";
        String result = instance.getBrojTelefona();
    }

    @Test
    public void testGetBrojTelefona2() throws BrojTelefonaException {
        System.out.println("getBrojTelefona");
        Posetilac instance = new Posetilac();
        instance.setBrojTelefona("0612331");
        String expResult = "0612331";
        String result = instance.getBrojTelefona();
        assertEquals(expResult, result);
    }

    @Test
    public void testSetBrojTelefona() throws BrojTelefonaException {
        System.out.println("setBrojTelefona");
        String newBrojTelefona = "06123312";
        Posetilac instance = new Posetilac();
        instance.setBrojTelefona(newBrojTelefona);
        assertEquals(instance.getBrojTelefona(), newBrojTelefona);
    }

    @Test(expected = BrojTelefonaException.class)
    public void testSetBrojTelefona2() throws BrojTelefonaException {
        System.out.println("setBrojTelefona");
        String newBrojTelefona = "061";
        Posetilac instance = new Posetilac();
        instance.setBrojTelefona(newBrojTelefona);
    }

    @Test
    public void testGetJmbg() throws JMBGException {
        System.out.println("getJmbg");
        Posetilac instance = new Posetilac();
        instance.setJmbg("1111111111111");
        String expResult = "1111111111111";
        String result = instance.getJmbg();
        assertEquals(expResult, result);
    }

    @Test
    public void testSetJmbg() throws JMBGException {
        System.out.println("setJmbg");
        String newJmbg = "1111111111111";
        Posetilac instance = new Posetilac();
        instance.setJmbg(newJmbg);
        assertEquals(instance.getJmbg(), newJmbg);
    }

    @Test(expected = JMBGException.class)
    public void testSetJmbg2() throws JMBGException {
        System.out.println("setJmbg");
        String newJmbg = "132312";
        Posetilac instance = new Posetilac();
        instance.setJmbg(newJmbg);
    }

    @Test
    public void testGetZakazanaPoseta() {
        System.out.println("getZakazanaPoseta");
        Posetilac instance = new Posetilac();
        List<ZakazanaPoseta> expResult = new ArrayList<>();
        List<ZakazanaPoseta> result = instance.getZakazanaPoseta();
        assertEquals(expResult, result);
    }
}
