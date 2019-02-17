import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { Trip } from './trip.model';
import { TripsApiService } from './trips-api.service';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-trips',
  templateUrl: './trips.component.html',
  styleUrls: ['./trips.component.css']
})
export class TripsComponent implements OnInit {
  tripsListSubs: Subscription;
  tripsList: Array<Trip>;
  trips: Array<Trip>;

  constructor(private tripsApi: TripsApiService) { }

  ngOnInit() {
    this.tripsListSubs = this.tripsApi
      .getTrips()
      .subscribe(res => {
          this.tripsList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
  this.tripsListSubs.unsubscribe();
}


}
