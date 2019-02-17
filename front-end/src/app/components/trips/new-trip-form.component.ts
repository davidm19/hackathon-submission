import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TripsApiService } from './trips-api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'trip-form',
  templateUrl: './new-trip-form.component.html',
  styles: ['./trips.component.css']
})

export class TripFormComponent {
  trip = {
    trip_name: '',
    trip_description: '',
    trip_start_location: '',
    trip_start_date: Date(),
    trip_end_location: '',
    trip_end_date: Date()
  };

  constructor(private tripsApi: TripsApiService, private router: Router) { }

  updateName(event: any) {
    this.trip.trip_name = event.target.value;
  }

  updateDescription(event: any) {
    this.trip.trip_description = event.target.value;
  }

  updateStartLocation(event:any) {
    this.trip.trip_start_location = event.target.value;
  }

  updateStartDate(event:any) {
    this.trip.trip_start_date = event.target.value;
  }

  updateEndLocation(event:any) {
    this.trip.trip_end_location = event.target.value;
  }

  updateStartDate(event:any) {
    this.trip.trip_end_date = event.target.value;
  }

  saveTrip() {
    this.tripsApi
      .saveTrip(this.trip)
      .subscribe(
        () => this.router.navigate(['/trips']),
        error => alert(error.message)
      );
  }
}
