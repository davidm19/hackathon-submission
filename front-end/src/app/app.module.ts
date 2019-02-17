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
import { HikerComponent } from './components/trips/hiker/hiker.component';
import { TripDetailComponent } from './components/trips/trip-detail.component';
import { HikersApiService } from './components/trips/hiker/hikers-api.service';

const appRoutes: Routes = [
  { path: '', component: TripsComponent },
  { path: 'trips', component: TripsComponent },
  { path: 'trips/new', component: TripFormComponent },
  { path: 'new', component: TripFormComponent },
  { path: 'trips/:id/detail', component: TripDetailComponent }

];

@NgModule({
  declarations: [
    AppComponent,
    SidebarMenuComponent,
    TripsComponent,
    TripFormComponent,
    HikerComponent,
    TripDetailComponent,


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
