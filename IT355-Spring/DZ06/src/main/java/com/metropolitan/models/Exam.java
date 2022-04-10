package com.metropolitan.models;

import javax.persistence.*;


@Entity
@Table(name = "exams")
public class Exam {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private Integer id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "picked", nullable = false)
    private Boolean picked;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Boolean getPicked() {
        return picked;
    }

    public void setPicked(Boolean picked) {
        this.picked = picked;
    }
}
