import org.junit.Assert;
import org.junit.Test;

public class AppTest {
    private App obj = new App();

    @Test
    public void testLengthODUUID(){
        Assert.assertEquals(221, obj.compareTwoNumbers(21, 221));
    }
}
