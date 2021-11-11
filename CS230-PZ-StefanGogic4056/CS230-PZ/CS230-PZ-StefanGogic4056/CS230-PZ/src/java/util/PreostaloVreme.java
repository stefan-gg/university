package util;

import crud.CrudUser;
import entities.Korisnik;
import java.util.Timer;
import java.util.TimerTask;

public class PreostaloVreme {

    private int userId;
    private int vreme;

    Timer timer = new Timer();

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public int getVreme() {
        return vreme;
    }

    public void setVreme(int vreme) {
        this.vreme = vreme;
    }

    TimerTask task = new TimerTask() {
        public void run() {
            Korisnik k = CrudUser.read(userId);
            
            if (k.getPreostaloVreme() > vreme) {
                k.setPreostaloVreme(k.getPreostaloVreme() - 1);
                CrudUser.update(k);
            } else {
                vreme = 999999;
            }
        }
    };

    public void start() {
        timer.scheduleAtFixedRate(task, 1000, 1000);
    }
}
