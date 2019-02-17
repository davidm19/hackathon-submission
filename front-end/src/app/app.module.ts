import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { SidebarMenuComponent } from './components/sidebar-menu/sidebar-menu.component';
import { TripsComponent } from './components/trips/trips.component';
import { TripsApiService } from './components/trips/trips-api.service';
import { TripFormComponent } from './components/trips/new-trip-form.component';


const appRoutes: Routes = [
  { path: '', component: TripsComponent },
  { path: 'trips', component: TripsComponent },
  { path: 'trips/new', component: TripFormComponent },
  { path: 'new', component: TripFormComponent }

];

@NgModule({
  declarations: [
    AppComponent,
    SidebarMenuComponent,
    TripsComponent,
    TripFormComponent

  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [TripsApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
