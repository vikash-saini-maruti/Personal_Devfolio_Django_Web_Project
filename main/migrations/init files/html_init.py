/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
}

.slick-dots {
  bottom: -65px;
}

.slick-dots li {
  margin: 0 13px;
}

.slick-dots li button:hover:before,
.slick-dots li button:focus:before,
.slick-dots li.slick-active button:before {
  opacity: 1;
  color: #3ba0dd;
}

.tm-testimonials-carousel .slick-dots li button:before {
  color: white;
  opacity: 0.5;
}

.tm-testimonials-carousel .slick-dots li button:hover:before,
.tm-testimonials-carousel .slick-dots li button:focus:before,
.tm-testimonials-carousel .slick-dots li.slick-active button:before {
  color: white;
  opacity: 1;
}

.slick-dots li button:before {
  font-size: 18px;
}

/* Hover Effect */
/* Common style */
.grid figure {
  position: relative;
  float: left;
  overflow: hidden;
  background: #3085a3;
  text-align: center;
  cursor: pointer;
}

.grid figure img {
  position: relative;
  display: block;
  min-height: 100%;
  max-width: 100%;
  opacity: 0.8;
}

.grid figure figcaption {
  padding: 2em;
  color: #fff;
  text-transform: uppercase;
  font-size: 1.25em;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.grid figure figcaption::before,
.grid figure figcaption::after {
  pointer-events: none;
}

.grid figure figcaption,
.grid figure figcaption > a {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Anchor will cover the whole item by default */
/* For some effects it will show as a button */
.grid figure figcaption > a {
  z-index: 1000;
  text-indent: 200%;
  white-space: nowrap;
  font-size: 0;
  opacity: 0;
}

.grid figure h2 {
  word-spacing: -0.15em;
  font-size: 0.9em;
  font-weight: 300;
}

.grid figure h2 span {
  font-weight: 600;
}

.grid figure h2,
.grid figure p {
  margin: 0;
}

.grid figure p {
  letter-spacing: 1px;
  font-size: 68.5%;
}

/*---------------*/
/***** Honey *****/
/*---------------*/

figure.effect-honey {
  background: #4a3753;
  max-width: 220px;
}

figure.effect-honey img {
  opacity: 1;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}

figure.effect-honey:hover img {
  opacity: 0.4;
}

figure.effect-honey figcaption::before {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 10px;
  background: #38C;
  content: "";
  -webkit-transform: translate3d(0, 10px, 0);
  transform: translate3d(0, 10px, 0);
}

figure.effect-honey h2 {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1em 1.5em;
  width: 100%;
  text-align: left;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey h2 i {
  font-style: normal;
  opacity: 0;
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey figcaption::before,
figure.effect-honey h2 {
  -webkit-transition: -webkit-transform 0.35s;
  transition: transform 0.35s;
}

figure.effect-honey:hover figcaption::before,
figure.effect-honey:hover h2,
figure.effect-honey:hover h2 i {
  opacity: 1;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}

.tm-container-gallery {
	padding-top: 30px;
	}

/* Contact */

#contact {
  color: white;
  background-color: #001828;
  background-image: url(../img/infinite-loop-03.jpg);
  background-position: center;
  background-repeat: no-repeat;
  min-height: 980px;
  position: relative;

}

.contact-item {
  margin-left: 20px;
  margin-bottom: 50px;
}

.item-link {
  display: flex;
  align-items: center;
}

.item-link i,
.item-link span {
  color: white;
  transition: all 0.3s ease;
}

.item-link:hover i,
.item-link:hover span {
  color: #3496d8;
}

.tm-input {
	margin: 0 0 20px 0;
	width: 90%;
  padding: 8px 20px;
  border-radius: 6px;
  border: 1px solid white;
  background: transparent;
  color: white;
}

.tm-btn-submit {
	font-size: 0.9em;
	color: #fff;
	background-color: #369;
	width: 50%;
	margin-bottom: 60px;
}

.tm-btn-submit:hover {
	color: #fff;
	background-color: #38B;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: white;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: white;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: white;
}

.tm-footer {
  position: absolute;
  bottom: 35px;
  left: 0;
  right: 0;
  padding: 0 15px;
}

.tm-footer a {
	color: #fff;
}

.tm-footer a:hover {
	color: #9CF;
}

.tm-footer-link {
  color: white;
}

.tm-footer-link:hover,
.tm-footer-link:focus {
  color: #38B;
  text-decoration: none;
}

p {
  line-height: 1.9;
}

@media (min-width: 768px) {
  .tm-intro-text-container {
    padding-left: 0px;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    /* padding-right: 30px;
    padding-left: 30px; */
    font-size: 10px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1275px;
  }

  .tm-container-gallery {
    max-width: 1290px;
  }

  .tm-container-contact {
    max-width: 1063px;
  }
}

@media (max-width: 991px) {
  .tm-intro-text-container {
    padding-left: 15px;
    padding-top: 30px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-intro-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-btn-submit {
    margin-left: 0;
    margin-top: 20px;
  }
}

@media (max-width: 767px) {

  .navbar-nav {
    max-width: 200px;
    text-align: right;
  }

  .navbar-collapse {
    background-color: rgb(255, 255, 255);
    padding: 10px;
    border-radius: 3px;
  }

  .navbar-collapse .nav-link {
    color: white;
	padding-right: 20px;
  }
}

@media (max-width: 480px) {
  .tm-gallery-container {
    max-width: 220px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-gallery-container-2 {
    max-width: 350px;
  }

  .slick-dots li {
    margin: 0 8px;
  }

  .tm-gallery-item {
    margin: 0;
  }
}

.h2, h2 {
  font-size: 1.5rem;
}


.h2tagis {
  font-size: 1.5rem;
  font-weight: normal;
  text-align: center;
  border: 2px solid black;
  background-color: goldenrod;
  color: rgb(255, 255, 255);
  width: 20%;
  margin: auto;
  border-radius: 30px;
}

@media screen and (max-width: 768px) {
  .h2tagis {
      font-size: 1.5rem;
      width: 80%;
  }
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio (h / w * 100) */
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
}

.slick-dots {
  bottom: -65px;
}

.slick-dots li {
  margin: 0 13px;
}

.slick-dots li button:hover:before,
.slick-dots li button:focus:before,
.slick-dots li.slick-active button:before {
  opacity: 1;
  color: #3ba0dd;
}

.tm-testimonials-carousel .slick-dots li button:before {
  color: white;
  opacity: 0.5;
}

.tm-testimonials-carousel .slick-dots li button:hover:before,
.tm-testimonials-carousel .slick-dots li button:focus:before,
.tm-testimonials-carousel .slick-dots li.slick-active button:before {
  color: white;
  opacity: 1;
}

.slick-dots li button:before {
  font-size: 18px;
}

/* Hover Effect */
/* Common style */
.grid figure {
  position: relative;
  float: left;
  overflow: hidden;
  background: #3085a3;
  text-align: center;
  cursor: pointer;
}

.grid figure img {
  position: relative;
  display: block;
  min-height: 100%;
  max-width: 100%;
  opacity: 0.8;
}

.grid figure figcaption {
  padding: 2em;
  color: #fff;
  text-transform: uppercase;
  font-size: 1.25em;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.grid figure figcaption::before,
.grid figure figcaption::after {
  pointer-events: none;
}

.grid figure figcaption,
.grid figure figcaption > a {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Anchor will cover the whole item by default */
/* For some effects it will show as a button */
.grid figure figcaption > a {
  z-index: 1000;
  text-indent: 200%;
  white-space: nowrap;
  font-size: 0;
  opacity: 0;
}

.grid figure h2 {
  word-spacing: -0.15em;
  font-size: 0.9em;
  font-weight: 300;
}

.grid figure h2 span {
  font-weight: 600;
}

.grid figure h2,
.grid figure p {
  margin: 0;
}

.grid figure p {
  letter-spacing: 1px;
  font-size: 68.5%;
}

/*---------------*/
/***** Honey *****/
/*---------------*/

figure.effect-honey {
  background: #4a3753;
  max-width: 220px;
}

figure.effect-honey img {
  opacity: 1;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}

figure.effect-honey:hover img {
  opacity: 0.4;
}

figure.effect-honey figcaption::before {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 10px;
  background: #38C;
  content: "";
  -webkit-transform: translate3d(0, 10px, 0);
  transform: translate3d(0, 10px, 0);
}

figure.effect-honey h2 {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1em 1.5em;
  width: 100%;
  text-align: left;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey h2 i {
  font-style: normal;
  opacity: 0;
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey figcaption::before,
figure.effect-honey h2 {
  -webkit-transition: -webkit-transform 0.35s;
  transition: transform 0.35s;
}

figure.effect-honey:hover figcaption::before,
figure.effect-honey:hover h2,
figure.effect-honey:hover h2 i {
  opacity: 1;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}

.tm-container-gallery {
	padding-top: 30px;
	}

/* Contact */

#contact {
  color: white;
  background-color: #001828;
  background-image: url(../img/infinite-loop-03.jpg);
  background-position: center;
  background-repeat: no-repeat;
  min-height: 980px;
  position: relative;

}

.contact-item {
  margin-left: 20px;
  margin-bottom: 50px;
}

.item-link {
  display: flex;
  align-items: center;
}

.item-link i,
.item-link span {
  color: white;
  transition: all 0.3s ease;
}

.item-link:hover i,
.item-link:hover span {
  color: #3496d8;
}

.tm-input {
	margin: 0 0 20px 0;
	width: 90%;
  padding: 8px 20px;
  border-radius: 6px;
  border: 1px solid white;
  background: transparent;
  color: white;
}

.tm-btn-submit {
	font-size: 0.9em;
	color: #fff;
	background-color: #369;
	width: 50%;
	margin-bottom: 60px;
}

.tm-btn-submit:hover {
	color: #fff;
	background-color: #38B;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: white;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: white;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: white;
}

.tm-footer {
  position: absolute;
  bottom: 35px;
  left: 0;
  right: 0;
  padding: 0 15px;
}

.tm-footer a {
	color: #fff;
}

.tm-footer a:hover {
	color: #9CF;
}

.tm-footer-link {
  color: white;
}

.tm-footer-link:hover,
.tm-footer-link:focus {
  color: #38B;
  text-decoration: none;
}

p {
  line-height: 1.9;
}

@media (min-width: 768px) {
  .tm-intro-text-container {
    padding-left: 0px;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    /* padding-right: 30px;
    padding-left: 30px; */
    font-size: 10px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1275px;
  }

  .tm-container-gallery {
    max-width: 1290px;
  }

  .tm-container-contact {
    max-width: 1063px;
  }
}

@media (max-width: 991px) {
  .tm-intro-text-container {
    padding-left: 15px;
    padding-top: 30px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-intro-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-btn-submit {
    margin-left: 0;
    margin-top: 20px;
  }
}

@media (max-width: 767px) {

  .navbar-nav {
    max-width: 200px;
    text-align: right;
  }

  .navbar-collapse {
    background-color: rgb(255, 255, 255);
    padding: 10px;
    border-radius: 3px;
  }

  .navbar-collapse .nav-link {
    color: white;
	padding-right: 20px;
  }
}

@media (max-width: 480px) {
  .tm-gallery-container {
    max-width: 220px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-gallery-container-2 {
    max-width: 350px;
  }

  .slick-dots li {
    margin: 0 8px;
  }

  .tm-gallery-item {
    margin: 0;
  }
}

.h2, h2 {
  font-size: 1.5rem;
}


.h2tagis {
  font-size: 1.5rem;
  font-weight: normal;
  text-align: center;
  border: 2px solid black;
  background-color: goldenrod;
  color: rgb(255, 255, 255);
  width: 20%;
  margin: auto;
  border-radius: 30px;
}

@media screen and (max-width: 768px) {
  .h2tagis {
      font-size: 1.5rem;
      width: 80%;
  }
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio (h / w * 100) */
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
 /*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
}

.slick-dots {
  bottom: -65px;
}

.slick-dots li {
  margin: 0 13px;
}

.slick-dots li button:hover:before,
.slick-dots li button:focus:before,
.slick-dots li.slick-active button:before {
  opacity: 1;
  color: #3ba0dd;
}

.tm-testimonials-carousel .slick-dots li button:before {
  color: white;
  opacity: 0.5;
}

.tm-testimonials-carousel .slick-dots li button:hover:before,
.tm-testimonials-carousel .slick-dots li button:focus:before,
.tm-testimonials-carousel .slick-dots li.slick-active button:before {
  color: white;
  opacity: 1;
}

.slick-dots li button:before {
  font-size: 18px;
}

/* Hover Effect */
/* Common style */
.grid figure {
  position: relative;
  float: left;
  overflow: hidden;
  background: #3085a3;
  text-align: center;
  cursor: pointer;
}

.grid figure img {
  position: relative;
  display: block;
  min-height: 100%;
  max-width: 100%;
  opacity: 0.8;
}

.grid figure figcaption {
  padding: 2em;
  color: #fff;
  text-transform: uppercase;
  font-size: 1.25em;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.grid figure figcaption::before,
.grid figure figcaption::after {
  pointer-events: none;
}

.grid figure figcaption,
.grid figure figcaption > a {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Anchor will cover the whole item by default */
/* For some effects it will show as a button */
.grid figure figcaption > a {
  z-index: 1000;
  text-indent: 200%;
  white-space: nowrap;
  font-size: 0;
  opacity: 0;
}

.grid figure h2 {
  word-spacing: -0.15em;
  font-size: 0.9em;
  font-weight: 300;
}

.grid figure h2 span {
  font-weight: 600;
}

.grid figure h2,
.grid figure p {
  margin: 0;
}

.grid figure p {
  letter-spacing: 1px;
  font-size: 68.5%;
}

/*---------------*/
/***** Honey *****/
/*---------------*/

figure.effect-honey {
  background: #4a3753;
  max-width: 220px;
}

figure.effect-honey img {
  opacity: 1;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}

figure.effect-honey:hover img {
  opacity: 0.4;
}

figure.effect-honey figcaption::before {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 10px;
  background: #38C;
  content: "";
  -webkit-transform: translate3d(0, 10px, 0);
  transform: translate3d(0, 10px, 0);
}

figure.effect-honey h2 {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1em 1.5em;
  width: 100%;
  text-align: left;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey h2 i {
  font-style: normal;
  opacity: 0;
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey figcaption::before,
figure.effect-honey h2 {
  -webkit-transition: -webkit-transform 0.35s;
  transition: transform 0.35s;
}

figure.effect-honey:hover figcaption::before,
figure.effect-honey:hover h2,
figure.effect-honey:hover h2 i {
  opacity: 1;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}

.tm-container-gallery {
	padding-top: 30px;
	}

/* Contact */

#contact {
  color: white;
  background-color: #001828;
  background-image: url(../img/infinite-loop-03.jpg);
  background-position: center;
  background-repeat: no-repeat;
  min-height: 980px;
  position: relative;

}

.contact-item {
  margin-left: 20px;
  margin-bottom: 50px;
}

.item-link {
  display: flex;
  align-items: center;
}

.item-link i,
.item-link span {
  color: white;
  transition: all 0.3s ease;
}

.item-link:hover i,
.item-link:hover span {
  color: #3496d8;
}

.tm-input {
	margin: 0 0 20px 0;
	width: 90%;
  padding: 8px 20px;
  border-radius: 6px;
  border: 1px solid white;
  background: transparent;
  color: white;
}

.tm-btn-submit {
	font-size: 0.9em;
	color: #fff;
	background-color: #369;
	width: 50%;
	margin-bottom: 60px;
}

.tm-btn-submit:hover {
	color: #fff;
	background-color: #38B;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: white;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: white;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: white;
}

.tm-footer {
  position: absolute;
  bottom: 35px;
  left: 0;
  right: 0;
  padding: 0 15px;
}

.tm-footer a {
	color: #fff;
}

.tm-footer a:hover {
	color: #9CF;
}

.tm-footer-link {
  color: white;
}

.tm-footer-link:hover,
.tm-footer-link:focus {
  color: #38B;
  text-decoration: none;
}

p {
  line-height: 1.9;
}

@media (min-width: 768px) {
  .tm-intro-text-container {
    padding-left: 0px;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    /* padding-right: 30px;
    padding-left: 30px; */
    font-size: 10px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1275px;
  }

  .tm-container-gallery {
    max-width: 1290px;
  }

  .tm-container-contact {
    max-width: 1063px;
  }
}

@media (max-width: 991px) {
  .tm-intro-text-container {
    padding-left: 15px;
    padding-top: 30px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-intro-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-btn-submit {
    margin-left: 0;
    margin-top: 20px;
  }
}

@media (max-width: 767px) {

  .navbar-nav {
    max-width: 200px;
    text-align: right;
  }

  .navbar-collapse {
    background-color: rgb(255, 255, 255);
    padding: 10px;
    border-radius: 3px;
  }

  .navbar-collapse .nav-link {
    color: white;
	padding-right: 20px;
  }
}

@media (max-width: 480px) {
  .tm-gallery-container {
    max-width: 220px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-gallery-container-2 {
    max-width: 350px;
  }

  .slick-dots li {
    margin: 0 8px;
  }

  .tm-gallery-item {
    margin: 0;
  }
}

.h2, h2 {
  font-size: 1.5rem;
}


.h2tagis {
  font-size: 1.5rem;
  font-weight: normal;
  text-align: center;
  border: 2px solid black;
  background-color: goldenrod;
  color: rgb(255, 255, 255);
  width: 20%;
  margin: auto;
  border-radius: 30px;
}

@media screen and (max-width: 768px) {
  .h2tagis {
      font-size: 1.5rem;
      width: 80%;
  }
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio (h / w * 100) */
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
}

.slick-dots {
  bottom: -65px;
}

.slick-dots li {
  margin: 0 13px;
}

.slick-dots li button:hover:before,
.slick-dots li button:focus:before,
.slick-dots li.slick-active button:before {
  opacity: 1;
  color: #3ba0dd;
}

.tm-testimonials-carousel .slick-dots li button:before {
  color: white;
  opacity: 0.5;
}

.tm-testimonials-carousel .slick-dots li button:hover:before,
.tm-testimonials-carousel .slick-dots li button:focus:before,
.tm-testimonials-carousel .slick-dots li.slick-active button:before {
  color: white;
  opacity: 1;
}

.slick-dots li button:before {
  font-size: 18px;
}

/* Hover Effect */
/* Common style */
.grid figure {
  position: relative;
  float: left;
  overflow: hidden;
  background: #3085a3;
  text-align: center;
  cursor: pointer;
}

.grid figure img {
  position: relative;
  display: block;
  min-height: 100%;
  max-width: 100%;
  opacity: 0.8;
}

.grid figure figcaption {
  padding: 2em;
  color: #fff;
  text-transform: uppercase;
  font-size: 1.25em;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.grid figure figcaption::before,
.grid figure figcaption::after {
  pointer-events: none;
}

.grid figure figcaption,
.grid figure figcaption > a {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Anchor will cover the whole item by default */
/* For some effects it will show as a button */
.grid figure figcaption > a {
  z-index: 1000;
  text-indent: 200%;
  white-space: nowrap;
  font-size: 0;
  opacity: 0;
}

.grid figure h2 {
  word-spacing: -0.15em;
  font-size: 0.9em;
  font-weight: 300;
}

.grid figure h2 span {
  font-weight: 600;
}

.grid figure h2,
.grid figure p {
  margin: 0;
}

.grid figure p {
  letter-spacing: 1px;
  font-size: 68.5%;
}

/*---------------*/
/***** Honey *****/
/*---------------*/

figure.effect-honey {
  background: #4a3753;
  max-width: 220px;
}

figure.effect-honey img {
  opacity: 1;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}

figure.effect-honey:hover img {
  opacity: 0.4;
}

figure.effect-honey figcaption::before {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 10px;
  background: #38C;
  content: "";
  -webkit-transform: translate3d(0, 10px, 0);
  transform: translate3d(0, 10px, 0);
}

figure.effect-honey h2 {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1em 1.5em;
  width: 100%;
  text-align: left;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey h2 i {
  font-style: normal;
  opacity: 0;
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey figcaption::before,
figure.effect-honey h2 {
  -webkit-transition: -webkit-transform 0.35s;
  transition: transform 0.35s;
}

figure.effect-honey:hover figcaption::before,
figure.effect-honey:hover h2,
figure.effect-honey:hover h2 i {
  opacity: 1;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}

.tm-container-gallery {
	padding-top: 30px;
	}

/* Contact */

#contact {
  color: white;
  background-color: #001828;
  background-image: url(../img/infinite-loop-03.jpg);
  background-position: center;
  background-repeat: no-repeat;
  min-height: 980px;
  position: relative;

}

.contact-item {
  margin-left: 20px;
  margin-bottom: 50px;
}

.item-link {
  display: flex;
  align-items: center;
}

.item-link i,
.item-link span {
  color: white;
  transition: all 0.3s ease;
}

.item-link:hover i,
.item-link:hover span {
  color: #3496d8;
}

.tm-input {
	margin: 0 0 20px 0;
	width: 90%;
  padding: 8px 20px;
  border-radius: 6px;
  border: 1px solid white;
  background: transparent;
  color: white;
}

.tm-btn-submit {
	font-size: 0.9em;
	color: #fff;
	background-color: #369;
	width: 50%;
	margin-bottom: 60px;
}

.tm-btn-submit:hover {
	color: #fff;
	background-color: #38B;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: white;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: white;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: white;
}

.tm-footer {
  position: absolute;
  bottom: 35px;
  left: 0;
  right: 0;
  padding: 0 15px;
}

.tm-footer a {
	color: #fff;
}

.tm-footer a:hover {
	color: #9CF;
}

.tm-footer-link {
  color: white;
}

.tm-footer-link:hover,
.tm-footer-link:focus {
  color: #38B;
  text-decoration: none;
}

p {
  line-height: 1.9;
}

@media (min-width: 768px) {
  .tm-intro-text-container {
    padding-left: 0px;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    /* padding-right: 30px;
    padding-left: 30px; */
    font-size: 10px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1275px;
  }

  .tm-container-gallery {
    max-width: 1290px;
  }

  .tm-container-contact {
    max-width: 1063px;
  }
}

@media (max-width: 991px) {
  .tm-intro-text-container {
    padding-left: 15px;
    padding-top: 30px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-intro-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-btn-submit {
    margin-left: 0;
    margin-top: 20px;
  }
}

@media (max-width: 767px) {

  .navbar-nav {
    max-width: 200px;
    text-align: right;
  }

  .navbar-collapse {
    background-color: rgb(255, 255, 255);
    padding: 10px;
    border-radius: 3px;
  }

  .navbar-collapse .nav-link {
    color: white;
	padding-right: 20px;
  }
}

@media (max-width: 480px) {
  .tm-gallery-container {
    max-width: 220px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-gallery-container-2 {
    max-width: 350px;
  }

  .slick-dots li {
    margin: 0 8px;
  }

  .tm-gallery-item {
    margin: 0;
  }
}

.h2, h2 {
  font-size: 1.5rem;
}


.h2tagis {
  font-size: 1.5rem;
  font-weight: normal;
  text-align: center;
  border: 2px solid black;
  background-color: goldenrod;
  color: rgb(255, 255, 255);
  width: 20%;
  margin: auto;
  border-radius: 30px;
}

@media screen and (max-width: 768px) {
  .h2tagis {
      font-size: 1.5rem;
      width: 80%;
  }
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio (h / w * 100) */
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;
}

a:focus {
  outline: none;
}

.btn {
  padding: 8px 32px;
}

.btn:hover {
  background-color: #ced4da;
}

blockquote {
  font-size: 0.86em;
  line-height: 1.8em;
}

.tm-section-pad-top {
  padding-top: 80px;
  padding-bottom: 128px;
}

.tm-content-box {

  padding-bottom: 40px;
}

.tm-text-primary {
  color: goldenrod;
}

.tm-font-big {
  font-size: 1.25rem;
}

.tm-btn-primary {
  color: white;
  background-color: #369;
  padding: 14px 30px;
}

.tm-btn-primary:hover,
.tm-btn-primary:focus {
  color: white;
  background-color: #38B;
}

/* Navbar */

.tm-navbar {
  position: fixed;
  z-index: 1000;
  background-color: transparent;
  transition: all 0.3s ease;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
  padding: 1px;
  margin-top: 1.5%;
  border-radius: 108px;
  
}



.tm-navbar.scroll {
  background-color: goldenrod;
  border-bottom: 1px solid #e9ecef;
}

.navbar-brand {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
}

.navbar-brand:hover,
.tm-navbar.scroll .navbar-brand:hover {
  color: #38B;
}

.tm-navbar.scroll .navbar-brand {
  color: #369;
}

.nav-item {
  list-style: none;
}

.tm-nav-link {
  color: white;
}

.tm-navbar.scroll .tm-nav-link {
  color: #ffffff;
  font: bold;
}

.tm-navbar.scroll .tm-nav-link:hover,
.tm-navbar.scroll .tm-nav-link.current,
.tm-nav-link:hover {
  color: #FFF;
  background-color: #000;
}

.navbar-toggler {
  border: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.nav-link {
  display: block;
  /* padding: 0.5rem 1rem; */
}

.navbar-toggler-icon {
  color: white;
  padding-top: 6px;
}

.tm-navbar.scroll .navbar-toggler {
  border: 1px solid white;
}

.tm-navbar.scroll .navbar-toggler-icon {
  color: white;
}

/* Hero */

#infinite {
	background-color: #222;
  background-image: url(../img/infinite-loop-01.jpg);
  background-repeat: no-repeat;
  height: 100vh;
  min-height: 375px;
  position: relative;
}

@media (min-height: 600px) and (min-width: 1920px) {
  #infinite {
    background-size: cover;
  }
}

@media (min-height: 830px) {
  #infinite {
    background-position: center -210px;
  }
}

@media (min-height: 680px) and (max-height: 829px) {
  #infinite {
    background-position: center -300px;
  }
}

@media (min-height: 500px) and (max-height: 679px) {
  #infinite {
    background-position: center -400px;
  }
}

@media (max-height: 499px) {
  #infinite {
    background-position: center -450px;
  }
}

.tm-hero-text-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.tm-hero-text-container-inner {
  margin-top: -90px;
}

.tm-hero-title {
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px #333;
}

.tm-hero-subtitle {
  text-shadow: 2px 2px 2px #333;
}

.tm-intro-next {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
}

@media (max-height: 480px) {
  .tm-hero-text-container-inner {
    margin-top: -40px;
  }

  .tm-intro-next {
    bottom: 20px;
  }
}

.tm-down-arrow-link {
  display: block;
  margin-top: 18%;
}

.tm-down-arrow {
  	color: #FFF;
    cursor: pointer;
    background: goldenrod;
    padding: 15px 40px;
    transition: all 0.3s ease;
}

.tm-down-arrow:hover,
.tm-down-arrow:focus {
  color: #FFF;
  background: goldenrod
;
  padding: 20px 50px;
}

/* Introduction */

#introduction {
  padding-bottom: 100px;
}

.tm-section-title {
  font-size: 1.5rem;
  font-weight: normal;
}

.tm-intro-text {
  font-size: 16px;
}

.tm-icon {
  display: block;
  color: goldenrod
;
}

.tm-continue {
	padding: 20px 0 30px 0;
}

/* Testimonials */
#testimonials {
  color: white;
  background-image: url(../img/infinite-loop-02.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-size: 100%;
  position: relative;
}

@media (max-width: 991px) {
  #testimonials {
    background-image: url(../img/infinite-loop-02-mobile.jpg);
  }
}

.tm-testimonials-content {
  position: relative;
  z-index: 100;
}

.tm-bg-overlay {
  width: 100%;
  height: 100%;
  background: rgba(20, 70, 80, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.tm-testimonials-carousel {
  max-width: 1050px;
  margin: 0 auto;
}

.tm-testimonial-item {
  max-width: 290px;
  margin-left: 35px;
  margin-right: 35px;
}

.tm-testimonial-item img {
  border-radius: 50%;
  margin-bottom: 35px;
}

.tm-testimonial-item figcaption {
  text-align: right;
  font-style: italic;
  font-size: 1.1rem;
}

/* Work */

.tm-section-desc {
  max-width: 650px;
  width: 100%;
  font-size: 0.9rem;
}

/* 
.tm-gallery-container {
  padding-top: 51px;
  padding-bottom: 55px;
}
Work */
.tm-gallery-item {
  margin: 0 15px;
}

.slick-dots {
  bottom: -65px;
}

.slick-dots li {
  margin: 0 13px;
}

.slick-dots li button:hover:before,
.slick-dots li button:focus:before,
.slick-dots li.slick-active button:before {
  opacity: 1;
  color: #3ba0dd;
}

.tm-testimonials-carousel .slick-dots li button:before {
  color: white;
  opacity: 0.5;
}

.tm-testimonials-carousel .slick-dots li button:hover:before,
.tm-testimonials-carousel .slick-dots li button:focus:before,
.tm-testimonials-carousel .slick-dots li.slick-active button:before {
  color: white;
  opacity: 1;
}

.slick-dots li button:before {
  font-size: 18px;
}

/* Hover Effect */
/* Common style */
.grid figure {
  position: relative;
  float: left;
  overflow: hidden;
  background: #3085a3;
  text-align: center;
  cursor: pointer;
}

.grid figure img {
  position: relative;
  display: block;
  min-height: 100%;
  max-width: 100%;
  opacity: 0.8;
}

.grid figure figcaption {
  padding: 2em;
  color: #fff;
  text-transform: uppercase;
  font-size: 1.25em;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.grid figure figcaption::before,
.grid figure figcaption::after {
  pointer-events: none;
}

.grid figure figcaption,
.grid figure figcaption > a {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Anchor will cover the whole item by default */
/* For some effects it will show as a button */
.grid figure figcaption > a {
  z-index: 1000;
  text-indent: 200%;
  white-space: nowrap;
  font-size: 0;
  opacity: 0;
}

.grid figure h2 {
  word-spacing: -0.15em;
  font-size: 0.9em;
  font-weight: 300;
}

.grid figure h2 span {
  font-weight: 600;
}

.grid figure h2,
.grid figure p {
  margin: 0;
}

.grid figure p {
  letter-spacing: 1px;
  font-size: 68.5%;
}

/*---------------*/
/***** Honey *****/
/*---------------*/

figure.effect-honey {
  background: #4a3753;
  max-width: 220px;
}

figure.effect-honey img {
  opacity: 1;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}

figure.effect-honey:hover img {
  opacity: 0.4;
}

figure.effect-honey figcaption::before {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 10px;
  background: #38C;
  content: "";
  -webkit-transform: translate3d(0, 10px, 0);
  transform: translate3d(0, 10px, 0);
}

figure.effect-honey h2 {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1em 1.5em;
  width: 100%;
  text-align: left;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey h2 i {
  font-style: normal;
  opacity: 0;
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0, -30px, 0);
  transform: translate3d(0, -30px, 0);
}

figure.effect-honey figcaption::before,
figure.effect-honey h2 {
  -webkit-transition: -webkit-transform 0.35s;
  transition: transform 0.35s;
}

figure.effect-honey:hover figcaption::before,
figure.effect-honey:hover h2,
figure.effect-honey:hover h2 i {
  opacity: 1;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}

.tm-container-gallery {
	padding-top: 30px;
	}

/* Contact */

#contact {
  color: white;
  background-color: #001828;
  background-image: url(../img/infinite-loop-03.jpg);
  background-position: center;
  background-repeat: no-repeat;
  min-height: 980px;
  position: relative;

}

.contact-item {
  margin-left: 20px;
  margin-bottom: 50px;
}

.item-link {
  display: flex;
  align-items: center;
}

.item-link i,
.item-link span {
  color: white;
  transition: all 0.3s ease;
}

.item-link:hover i,
.item-link:hover span {
  color: #3496d8;
}

.tm-input {
	margin: 0 0 20px 0;
	width: 90%;
  padding: 8px 20px;
  border-radius: 6px;
  border: 1px solid white;
  background: transparent;
  color: white;
}

.tm-btn-submit {
	font-size: 0.9em;
	color: #fff;
	background-color: #369;
	width: 50%;
	margin-bottom: 60px;
}

.tm-btn-submit:hover {
	color: #fff;
	background-color: #38B;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: white;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: white;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: white;
}

.tm-footer {
  position: absolute;
  bottom: 35px;
  left: 0;
  right: 0;
  padding: 0 15px;
}

.tm-footer a {
	color: #fff;
}

.tm-footer a:hover {
	color: #9CF;
}

.tm-footer-link {
  color: white;
}

.tm-footer-link:hover,
.tm-footer-link:focus {
  color: #38B;
  text-decoration: none;
}

p {
  line-height: 1.9;
}

@media (min-width: 768px) {
  .tm-intro-text-container {
    padding-left: 0px;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    /* padding-right: 30px;
    padding-left: 30px; */
    font-size: 10px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1275px;
  }

  .tm-container-gallery {
    max-width: 1290px;
  }

  .tm-container-contact {
    max-width: 1063px;
  }
}

@media (max-width: 991px) {
  .tm-intro-text-container {
    padding-left: 15px;
    padding-top: 30px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-intro-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-btn-submit {
    margin-left: 0;
    margin-top: 20px;
  }
}

@media (max-width: 767px) {

  .navbar-nav {
    max-width: 200px;
    text-align: right;
  }

  .navbar-collapse {
    background-color: rgb(255, 255, 255);
    padding: 10px;
    border-radius: 3px;
  }

  .navbar-collapse .nav-link {
    color: white;
	padding-right: 20px;
  }
}

@media (max-width: 480px) {
  .tm-gallery-container {
    max-width: 220px;
    margin-left: auto;
    margin-right: auto;
  }

  .tm-gallery-container-2 {
    max-width: 350px;
  }

  .slick-dots li {
    margin: 0 8px;
  }

  .tm-gallery-item {
    margin: 0;
  }
}

.h2, h2 {
  font-size: 1.5rem;
}


.h2tagis {
  font-size: 1.5rem;
  font-weight: normal;
  text-align: center;
  border: 2px solid black;
  background-color: goldenrod;
  color: rgb(255, 255, 255);
  width: 20%;
  margin: auto;
  border-radius: 30px;
}

@media screen and (max-width: 768px) {
  .h2tagis {
      font-size: 1.5rem;
      width: 80%;
  }
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio (h / w * 100) */
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
/*

Tooplate 2117 Infinite Loop

https://www.tooplate.com/view/2117-infinite-loop

*/

@import url("https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900");

body {
	font-family: "Raleway", sans-serif;
	font-size: 1.2em;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background-color: black;
}
a {
  transition: all 0.3s ease;
  color: #38B;
}

a:hover,
a:focus {
  text-decoration: none;
  color: #D40;

}