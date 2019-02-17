import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { SidebarMenuComponent } from './components/sidebar-menu/sidebar-menu.component';
import { TripsComponent } from './components/trips/trips.component';
import { TripsApiService } from './components/trips/trips-api.service';
import { TripFormComponent } from './components/trips/new-trip-form.component';
import { TripDetailComponent } from './components/trips/trip-detail.component';
import { HikersApiService } from './components/trips/hikers/hikers-api.service';
import { HikersComponent } from './components/trips/hikers/hikers.component';
import { HikerDetailComponent } from './components/trips/hikers/hiker-detail.component';

const appRoutes: Routes = [
  { path: '', component: TripsComponent },
  { path: 'trips', component: TripsComponent },
  { path: 'trips/new', component: TripFormComponent },
  { path: 'new', component: TripFormComponent },
  { path: 'trips/:trip_id/detail', component: TripDetailComponent },
  { path: 'trips/:trip_id/detail/hikers/:hiker_id', component: HikerDetailComponent },
  { path: ':trip_id/detail', component: TripDetailComponent },
  { path: 'hikers/:hiker_id', component: HikerDetailComponent },
  { path: 'hikers', component: HikersComponent }


];

@NgModule({
  declarations: [
    AppComponent,
    SidebarMenuComponent,
    TripsComponent,
    TripFormComponent,
    TripDetailComponent,
    HikerDetailComponent,
    HikersComponent



  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    HttpModule
  ],
  providers: [TripsApiService, HikersApiService, HttpModule],
  bootstrap: [AppComponent]
})
export class AppModule { }
