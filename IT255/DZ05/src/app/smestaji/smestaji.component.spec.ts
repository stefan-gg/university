import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmestajiComponent } from './smestaji.component';

describe('SmestajiComponent', () => {
  let component: SmestajiComponent;
  let fixture: ComponentFixture<SmestajiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SmestajiComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SmestajiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
