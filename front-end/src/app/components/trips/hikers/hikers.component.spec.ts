import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HikersComponent } from './hikers.component';

describe('HikersComponent', () => {
  let component: HikersComponent;
  let fixture: ComponentFixture<HikersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HikersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HikersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
