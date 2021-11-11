package crud;

import entities.Korisnik;
import entities.Racunar;
import entities.Role;
import java.util.ArrayList;
import java.util.List;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.criterion.Restrictions;
import util.HibernateUtil;

public class CrudUser {

    private static Session session;

    public static List<Korisnik> readAll() {
        List<Korisnik> users = new ArrayList<>();
        session = HibernateUtil.getSessionFactory().openSession();
        try {
            users = session.createQuery("from Korisnik").list();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return users;
    }

    public static Racunar readComputerId(int id) {
        session = HibernateUtil.getSessionFactory().openSession();
        Racunar com = null;

        try {
            com = (Racunar) session.createCriteria(Racunar.class)
                    .add(Restrictions.eq("idRacunara", id))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return com;
    }

    public static Role readUserRole(String rola) {
        session = HibernateUtil.getSessionFactory().openSession();
        Role role = null;

        try {
            role = (Role) session.createCriteria(Role.class)
                    .add(Restrictions.eq("nazivRole", rola))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return role;
    }

    public static Role readGuestRole() {
        session = HibernateUtil.getSessionFactory().openSession();
        Role role = null;

        try {
            role = (Role) session.createCriteria(Role.class)
                    .add(Restrictions.eq("nazivRole", "Guest"))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return role;
    }

    public static Korisnik readPictureName(String pictureName) {
        session = HibernateUtil.getSessionFactory().openSession();
        Korisnik user = null;

        try {
            user = (Korisnik) session.createCriteria(Korisnik.class)
                    .add(Restrictions.eq("imeSlike", pictureName))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return user;
    }

    public static Korisnik read(int id) {
        session = HibernateUtil.getSessionFactory().openSession();
        Korisnik user = null;

        try {
            user = (Korisnik) session.createCriteria(Korisnik.class)
                    .add(Restrictions.eq("id", id))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return user;
    }

    public static Korisnik checkData(String username, String password) {
        session = HibernateUtil.getSessionFactory().openSession();
        Korisnik user = null;

        try {
            user = (Korisnik) session.createCriteria(Korisnik.class)
                    .add(Restrictions.eq("username", username))
                    .add(Restrictions.eq("password", password))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return user;
    }

    public static Korisnik checkUsername(String username) {
        session = HibernateUtil.getSessionFactory().openSession();
        Korisnik user = null;

        try {
            user = (Korisnik) session.createCriteria(Korisnik.class)
                    .add(Restrictions.eq("username", username))
                    .uniqueResult();
        } catch (HibernateException ex) {
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return user;
    }

    public static String insert(Korisnik user) {
        String answer = "";
        session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = null;

        try {
            transaction = session.beginTransaction();
            session.persist(user);
            transaction.commit();
            answer = "Success";
        } catch (HibernateException ex) {
            transaction.rollback();
            answer = "Fail";
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return answer;
    }

    public static String update(Korisnik user) {
        String answer = "";
        session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = null;
        try {
            transaction = session.beginTransaction();
            session.update(user);
            transaction.commit();
            answer = "Success";
        } catch (HibernateException ex) {
            transaction.rollback();
            answer = "Fail";
            ex.printStackTrace();
        } finally {
            session.close();
        }
        return answer;
    }

    public static String delete(Korisnik user) {
        session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = null;
        String answer = "";
        try {
            transaction = session.beginTransaction();
            session.delete(user);
            transaction.commit();
            answer = "Success";
        } catch (HibernateException ex) {
            transaction.rollback();
            ex.printStackTrace();
            answer = "Fail";
        } finally {
            session.close();
        }
        return answer;
    }
}
