import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../../env';
import { Trip } from './trip.model';
import { Hiker } from './hiker/hiker.model';

@Injectable()
export class TripsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  deleteTrip(TRIP_ID: number) {
  return this.http
    .delete(`${API_URL}/trips/${TRIP_ID}/delete`);
  }

  getHikersInTrip(TRIP_ID: number) {
    return this.http
    .get<Array<Hiker>>(`${API_URL}/trips/${TRIP_ID}/detail/hikers`)
  }

  getTrip(TRIP_ID: number): Observable<Trip> {
      return this.http
      .get<Trip>(`${API_URL}/trips/${TRIP_ID}/detail`);
  }

  getTrips():
  Observable<Array<Trip>> {
    return this.http
    .get<Array<Trip>>(`${API_URL}/trips`);
  }

  saveTrip(trip: Trip): Observable<any> {
  return this.http
    .post(`${API_URL}/trips/new`, trip);
  }
}
