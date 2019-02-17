import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../../../env';
import { Trip } from '../trip.model';
import { Hiker } from './hiker.model';

@Injectable()
export class HikersApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  getHiker(HIKER_ID: number): Observable<Hiker> {
  return this.http
  .get<Hiker>(`${API_URL}/hikers/${HIKER_ID}/detail`);
  }

  getHikers():
  Observable<Array<Hiker>> {
    return this.http
    .get<Array<Hiker>>(`${API_URL}/hikers`);
  }

}
