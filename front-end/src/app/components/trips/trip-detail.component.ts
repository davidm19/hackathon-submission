import { switchMap } from 'rxjs/operators';
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { Observable } from 'rxjs';

import { TripsApiService } from './trips-api.service';
import { Trip } from './trip.model';
import { TripsComponent } from './trips.component';
import { TripsModule } from './trips.module';
import { Hiker } from './hiker/hiker.model';
import { HikersApiService } from './hiker/hikers-api.service';

@Component({
  selector: 'app-trip-detail',
  templateUrl: './trip-detail.component.html'
  // styleUrls: ['./trip-detail.component.css']
})
export class TripDetailComponent implements OnInit {
  tripHikerList: Array<Hiker>;
  trip: Trip;

  constructor(
    private tripsApi: TripsApiService,
    private route: ActivatedRoute,
    private hikersApi: HikersApiService
  ) {

  }
    ngOnInit() {
      this.getTrip();
      this.getHikersInTrip();

    }

  getTrip(): void {
    const TRIP_ID = +this.route.snapshot.paramMap.get('id');
    this.tripsApi
    .getTrip(TRIP_ID)
    .subscribe(res => {
        this.trip = res;
      },
      console.error
    );
  }

  getHikersInTrip(): void {
    const TRIP_ID = +this.route.snapshot.paramMap.get('id');
    this.tripsApi
    .getHikersInTrip(TRIP_ID)
    .subscribe(
      res => {
      this.tripHikerList = res;
    }
  );
}
}
