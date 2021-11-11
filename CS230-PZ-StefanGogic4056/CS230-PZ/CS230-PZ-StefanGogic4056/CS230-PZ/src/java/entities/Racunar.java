package entities;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

@Entity
@Table(name = "racunar")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Racunar.findAll", query = "SELECT r FROM Racunar r")
    , @NamedQuery(name = "Racunar.findByIdRacunara", query = "SELECT r FROM Racunar r WHERE r.idRacunara = :idRacunara")})
public class Racunar implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "ID_RACUNARA")
    private Integer idRacunara;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "idRacunara")
    private List<Korisnik> korisnikList;

    public Racunar() {
    }

    public Racunar(Integer idRacunara) {
        this.idRacunara = idRacunara;
    }

    public Integer getIdRacunara() {
        return idRacunara;
    }

    public void setIdRacunara(Integer idRacunara) {
        this.idRacunara = idRacunara;
    }

    @XmlTransient
    public List<Korisnik> getKorisnikList() {
        return korisnikList;
    }

    public void setKorisnikList(List<Korisnik> korisnikList) {
        this.korisnikList = korisnikList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idRacunara != null ? idRacunara.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Racunar)) {
            return false;
        }
        Racunar other = (Racunar) object;
        if ((this.idRacunara == null && other.idRacunara != null) || (this.idRacunara != null && !this.idRacunara.equals(other.idRacunara))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "" + idRacunara;
    }
    
}
