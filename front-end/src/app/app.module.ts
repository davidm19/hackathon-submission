import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { CreateHikeComponent } from './components/hike/create-hike/create-hike.component';
import { HikeComponent } from './components/hike/hike.component';
import { SidebarMenuComponent } from './components/sidebar-menu/sidebar-menu.component';
import { TripsComponent } from './components/trips/trips.component';


const appRoutes: Routes = [
  { path: '', component: TripsComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    CreateHikeComponent,
    HikeComponent,
    SidebarMenuComponent,
    TripsComponent,

  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
