import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TripsApiService } from './trips-api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'trip-form',
  templateUrl: './new-trip-form.component.html',
  styles: [`
    .w3-container {
    }

    .button2 {
      background-color: #888;
      border: none;
      color: white;
      padding: 10px;
      text-align: center;
      font-size: 16px;
      cursor: pointer;
      border-radius: 8px;
      margin-left: 330px;
    }

    /* .button2: hover {
        background-color: #8886 ;
    } */

    .button3 {
      background-color: #888;
      border: none;
      color: white;
      padding: 10px;
      text-align: center;
      font-size: 16px;
      cursor: pointer;
      border-radius: 8px;
      margin-left: 155px;
    }

    .button2:hover {
        background-color: #418e86;
        color: white;
    }

    .delete {
      background-color: #888;
      border: none;
      color: white;
      padding: 10px;
      text-align: center;
      font-size: 16px;
      cursor: pointer;
      border-radius: 8px;
      position: relative;
      float: right;
      bottom: 20px;
      right: 20px;
    }
    .delete:hover {
      background-color: #cb6969;
      color: white;
    }

    .input-element.description{
    height: 100px !important;
    width: 400px;
    }
`]
})

export class TripFormComponent {
  trip = {
    trip_name: '',
    trip_description: '',
  };

  constructor(private tripsApi: TripsApiService, private router: Router) { }

  updateName(event: any) {
    this.trip.trip_name = event.target.value;
  }

  updateDescription(event: any) {
    this.trip.trip_description = event.target.value;
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
