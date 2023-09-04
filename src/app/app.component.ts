import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { ApiService } from './api.service'


import { faWandMagic, faLightbulb, faRotateLeft } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-root', 
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  faWandMagic = faWandMagic
  faLightbulb = faLightbulb
  faRotateLeft = faRotateLeft

   constructor(private apiService: ApiService) { }

   startGame() {
    const playerName = 'John'; // Your player name data
    this.apiService.startNewGame(playerName)
      .subscribe(response => {
        // Handle the API response here
        console.log('New game started:', response);
      });
  }

  getGameState(gameId: string) {
    this.apiService.getGameState(gameId)
      .subscribe(response => {
        // Handle the API response here
        console.log('Game state retrieved:', response);
      });
  }

  // ...

  
  }


   

  



