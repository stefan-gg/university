package entities;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

@Entity
@Table(name = "role")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Role.findAll", query = "SELECT r FROM Role r")
    , @NamedQuery(name = "Role.findByIdRola", query = "SELECT r FROM Role r WHERE r.idRola = :idRola")
    , @NamedQuery(name = "Role.findByNazivRole", query = "SELECT r FROM Role r WHERE r.nazivRole = :nazivRole")})
public class Role implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "ID_ROLA")
    private Integer idRola;
    @Size(max = 20)
    @Column(name = "NAZIV_ROLE")
    private String nazivRole;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "idRola")
    private List<Korisnik> korisnikList;

    public Role() {
    }

    public Role(Integer idRola) {
        this.idRola = idRola;
    }

    public Integer getIdRola() {
        return idRola;
    }

    public void setIdRola(Integer idRola) {
        this.idRola = idRola;
    }

    public String getNazivRole() {
        return nazivRole;
    }

    public void setNazivRole(String nazivRole) {
        this.nazivRole = nazivRole;
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
        hash += (idRola != null ? idRola.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Role)) {
            return false;
        }
        Role other = (Role) object;
        if ((this.idRola == null && other.idRola != null) || (this.idRola != null && !this.idRola.equals(other.idRola))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entities.Role[ idRola=" + idRola + " ]";
    }
    
}
