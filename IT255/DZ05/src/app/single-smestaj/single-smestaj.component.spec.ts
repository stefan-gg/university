import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SingleSmestajComponent } from './single-smestaj.component';

describe('SingleSmestajComponent', () => {
  let component: SingleSmestajComponent;
  let fixture: ComponentFixture<SingleSmestajComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SingleSmestajComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SingleSmestajComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
