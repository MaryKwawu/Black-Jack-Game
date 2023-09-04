import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://localhost:4200/api';

  constructor(private http: HttpClient) { }

  startNewGame(playerName: string): Observable<any> {
    const url = `${this.baseUrl}/blackjack/start`;
    const body = { playerName };
    return this.http.post(url, body);
  }

  getGameState(gameId: string): Observable<any> {
    const url = `${this.baseUrl}/blackjack/game/${gameId}`;
    return this.http.get(url);
  }

  // Define other methods for your API requests
}
