# Weather API
> A simple API project based on [https://roadmap.sh/projects/weather-api-wrapper-service] built with FastAPI.
>
> The API manages:
> - Request air temperature at time range at input coordinates from SMHI SNOW REST API
> - Caches retrieved temperatures at Redis Cache database for 10 minutes

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Contact](#contact)

## General Information
RESTful API wrapper around the SMHI SNOW Forecast API for retrieving air temperature forecasts.

Data is fetched from:

https://opendata.smhi.se/metfcst/snow1gv1

Responses are cached in Redis for 10 minutes to improve performance.


## Technologies Used
- **Programming Language:** Python 3.11+
- **Backend Framework:** FastAPI
- **In-Memory Cache:** Redis
- **Testing:** Pytest, FastAPI TestClient

## Contact
Emelie Wärmlund - @emeliewarmlund@gmail.com  
<br>  
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/emelie-wärmlund-4b33bb98
