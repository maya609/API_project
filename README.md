# API_project

Hosted on: Google Cloud Platform (VM instance)

Public IP: http://34.57.146.240:5000

Framework: Flask (Python)


This project is a token-protected Flask API hosted on a Google Cloud VM. It takes the name of a capital city and returns the current local time and UTC offset in JSON format.

---

## API Endpoint

**GET** `/api/time?city=<CapitalCityName>`

Example: http://34.57.146.240:5000/api/time?city=London

This API requires a Bearer Token to access.
Authorization: Bearer supersecrettoken123


## Example Request
curl -H "Authorization: Bearer supersecrettoken123" "http://34.57.146.240:5000/api/time?city=London"

Supported Capital Cities
Washington
London
Tokyo
Paris
New Delhi
Canberra
Ottawa
Beijing

