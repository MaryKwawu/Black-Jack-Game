import { Component } from '@angular/core';
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


  title = 'midnight-ace-1';
}
