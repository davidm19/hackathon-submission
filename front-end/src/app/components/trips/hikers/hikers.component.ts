import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { Trip } from '../trip.model';
import { TripsApiService } from '../trips-api.service';
import { Observable } from 'rxjs/Observable';
import { HikersApiService } from './hikers-api.service';

@Component({
  selector: 'app-hikers',
  templateUrl: './hikers.component.html',
  styleUrls: ['./hikers.component.css']
})
export class HikersComponent implements OnInit {
  hikersListSubs: Subscription;
  hikersList: Array<Hiker>;
  hikers: Array<Hiker>;

  constructor(private hikersApi: HikersApiService) { }

  ngOnInit() {
    this.hikersListSubs = this.hikersApi
    .getHikers()
    .subscribe(res => {
      this.hikersList = res;
    },
  console.error
);
  }

  ngOnDestroy() {
  this.hikersListSubs.unsubscribe();
}

}
