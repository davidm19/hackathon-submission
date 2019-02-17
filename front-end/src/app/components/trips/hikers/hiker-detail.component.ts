import { switchMap } from 'rxjs/operators';
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { Observable } from 'rxjs';

import { TripsApiService } from '../trips-api.service';
import { Trip } from '../trip.model';
import { TripsComponent } from '../trips.component';
import { TripsModule } from '../trips.module';
import { Hiker } from './hiker.model';
import { HikersApiService } from './hikers-api.service';

@Component({
  selector: 'app-hiker-detail',
  templateUrl: './hiker-detail.component.html',
  styleUrls: ['./hikers.component.css']
})

export class HikerDetailComponent implements OnInit {
  hiker: Hiker;


  constructor(private hikersApi: HikersApiService,
              private route: ActivatedRoute
            ) {

            }

  ngOnInit() {
    this.getHiker();
  }

  getHiker(): void {
    const HIKER_ID = +this.route.snapshot.paramMap.get('hiker_id')
    this.hikersApi
    .getHiker(HIKER_ID)
    .subscribe(res => {
        this.hiker = res;
      },
      console.error
    );
  }

}
