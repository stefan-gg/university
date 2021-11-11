package entities;

import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;

@Entity
@Table(name = "korisnik")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Korisnik.findAll", query = "SELECT k FROM Korisnik k")
    , @NamedQuery(name = "Korisnik.findById", query = "SELECT k FROM Korisnik k WHERE k.id = :id")
    , @NamedQuery(name = "Korisnik.findByUsername", query = "SELECT k FROM Korisnik k WHERE k.username = :username")
    , @NamedQuery(name = "Korisnik.findByPassword", query = "SELECT k FROM Korisnik k WHERE k.password = :password")
    , @NamedQuery(name = "Korisnik.findByUkupanBrojMinuta", query = "SELECT k FROM Korisnik k WHERE k.ukupanBrojMinuta = :ukupanBrojMinuta")
    , @NamedQuery(name = "Korisnik.findByPreostaloVreme", query = "SELECT k FROM Korisnik k WHERE k.preostaloVreme = :preostaloVreme")
    , @NamedQuery(name = "Korisnik.findByImeSlike", query = "SELECT k FROM Korisnik k WHERE k.imeSlike = :imeSlike")})
public class Korisnik implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "ID")
    private Integer id;
    @Size(max = 50)
    @Column(name = "USERNAME")
    private String username;
    @Size(max = 50)
    @Column(name = "PASSWORD")
    private String password;
    @Column(name = "UKUPAN_BROJ_MINUTA")
    private Integer ukupanBrojMinuta;
    @Column(name = "PREOSTALO_VREME")
    private Integer preostaloVreme;
    @Size(max = 30)
    @Column(name = "ime_slike")
    private String imeSlike;
    @JoinColumn(name = "ID_ROLA", referencedColumnName = "ID_ROLA")
    @ManyToOne(optional = false)
    private Role idRola;
    @JoinColumn(name = "ID_RACUNARA", referencedColumnName = "ID_RACUNARA")
    @ManyToOne(optional = false)
    private Racunar idRacunara;

    public Korisnik() {
    }

    public Korisnik(Integer id) {
        this.id = id;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Integer getUkupanBrojMinuta() {
        return ukupanBrojMinuta;
    }

    public void setUkupanBrojMinuta(Integer ukupanBrojMinuta) {
        this.ukupanBrojMinuta = ukupanBrojMinuta;
    }

    public Integer getPreostaloVreme() {
        return preostaloVreme;
    }

    public void setPreostaloVreme(Integer preostaloVreme) {
        this.preostaloVreme = preostaloVreme;
    }

    public String getImeSlike() {
        return imeSlike;
    }

    public void setImeSlike(String imeSlike) {
        this.imeSlike = imeSlike;
    }

    public Role getIdRola() {
        return idRola;
    }

    public void setIdRola(Role idRola) {
        this.idRola = idRola;
    }

    public Racunar getIdRacunara() {
        return idRacunara;
    }

    public void setIdRacunara(Racunar idRacunara) {
        this.idRacunara = idRacunara;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Korisnik)) {
            return false;
        }
        Korisnik other = (Korisnik) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entities.Korisnik[ id=" + id + " ]";
    }
    
}
