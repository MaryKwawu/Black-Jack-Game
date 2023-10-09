// // import { NgModule } from '@angular/core';
// // import { BrowserModule } from '@angular/platform-browser';
// //
// // import { AppRoutingModule } from './app-routing.module';
// // import { AppComponent } from './app.component';
// // import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// // import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
// // import { HttpClientModule } from '@angular/common/http'
// //
// // // Import the ModalModule from ngx-bootstrap
// // import { ModalModule } from 'ngx-bootstrap/modal';
// //
// //
// // @NgModule({
// //   declarations: [
// //     AppComponent,
// //
// //   ],
// //   imports: [
// //     BrowserModule,
// //     AppRoutingModule,
// //     BrowserAnimationsModule,
// //     FontAwesomeModule,
// //     ModalModule.forRoot(), // Import and initialize the ModalModule
// //     HttpClientModule
// //
// //   ],
// //   providers: [],
// //   bootstrap: [AppComponent]
// // })
// // export class AppModule { }
//
//
// import { NgModule } from '@angular/core';
// import { BrowserModule } from '@angular/platform-browser';
//
// import { AppRoutingModule } from './app-routing.module';
// import { AppComponent } from './app.component';
// import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
// import { HttpClientModule } from '@angular/common/http';
//
// // Import the ModalModule from ngx-bootstrap
// import { ModalModule } from 'ngx-bootstrap/modal';
//
// @NgModule({
//   declarations: [AppComponent],
//   imports: [
//     BrowserModule,
//     AppRoutingModule,
//     BrowserAnimationsModule,
//     FontAwesomeModule,
//     ModalModule.forRoot(),
//     HttpClientModule,
//   ],
//   providers: [],
//   bootstrap: [AppComponent],
// })
// export class AppModule {}

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';


// Import the ModalModule from ngx-bootstrap
import { ModalModule } from 'ngx-bootstrap/modal';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FontAwesomeModule,
    ModalModule.forRoot(),
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}

