import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TripDetailComponent } from './trip-detail.component';
import { HikersComponent } from './hikers/hikers.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [TripDetailComponent, HikersComponent]
})
export class TripsModule { }
