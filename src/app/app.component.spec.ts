// // import { TestBed } from '@angular/core/testing';
// // import { RouterTestingModule } from '@angular/router/testing';
// // import { AppComponent } from './app.component';
// //
// // describe('AppComponent', () => {
// //   beforeEach(() => TestBed.configureTestingModule({
// //     imports: [RouterTestingModule],
// //     declarations: [AppComponent]
// //   }));
// //
// //   it('should create the app', () => {
// //     const fixture = TestBed.createComponent(AppComponent);
// //     const app = fixture.componentInstance;
// //     expect(app).toBeTruthy();
// //   });
// //
// //   it(`should have as title 'midnight-ace-1'`, () => {
// //     const fixture = TestBed.createComponent(AppComponent);
// //     const app = fixture.componentInstance;
// //     expect(app.title).toEqual('midnight-ace-1');
// //   });
// //
// //   it('should render title', () => {
// //     const fixture = TestBed.createComponent(AppComponent);
// //     fixture.detectChanges();
// //     const compiled = fixture.nativeElement as HTMLElement;
// //     expect(compiled.querySelector('.content span')?.textContent).toContain('midnight-ace-1 app is running!');
// //   });
// // });
//
//
// import { TestBed } from '@angular/core/testing';
// import { RouterTestingModule } from '@angular/router/testing';
// import { AppComponent } from './app.component';
// import { HttpClientModule } from '@angular/common/http';
// import { HttpClientTestingModule } from '@angular/common/http/testing';
// import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
// describe('AppComponent', () => {
//   beforeEach(() => TestBed.configureTestingModule({
//     imports: [
//       RouterTestingModule,
//       HttpClientModule,
//       HttpClientTestingModule,
//       FontAwesomeModule, // Add FontAwesomeModule here
//     ],
//     declarations: [AppComponent]
//   }));
//
//   it('should create the app', () => {
//     const fixture = TestBed.createComponent(AppComponent);
//     const app = fixture.componentInstance;
//     expect(app).toBeTruthy();
//   });
//
//   it(`should have as title 'midnight-ace-1'`, () => {
//     const fixture = TestBed.createComponent(AppComponent);
//     const app = fixture.componentInstance;
//     expect(app.title).toEqual('midnight-ace-1');
//   });
//
//   it('should render title', () => {
//     const fixture = TestBed.createComponent(AppComponent);
//     fixture.detectChanges();
//     const compiled = fixture.nativeElement as HTMLElement;
//     expect(compiled.querySelector('.content span')?.textContent).toContain('midnight-ace-1 app is running!');
//   });
// });


import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './api.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing'; // Import HttpTestingController
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

describe('AppComponent', () => {
  let httpTestingController: HttpTestingController; // Declare HttpTestingController


  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule,
        HttpClientTestingModule,
        FontAwesomeModule,
      ],
      providers: [AppComponent, ApiService],
    });

    httpTestingController = TestBed.inject(HttpTestingController); // Initialize HttpTestingController
  });

  afterEach(() => {
    httpTestingController.verify(); // Ensure that there are no outstanding HTTP requests
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'midnight-ace-1'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('midnight-ace-1');
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(AppComponent);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('.content span')?.textContent).toContain('midnight-ace-1 app is running!');
  });
});
