# Chloris Full-stack Engineer test

This project is a miniature version of the Chloris Platform which uses React and Bootstrap in the frontend, and AWS Lambda functions written in Python in the backend. The file `sites.geojson` is a set of circles in an area with very high biomass. Our customers manage sites just like these, and we provide estimates for the biomass density in each site. For the purposes of this test, we will allow the user to provide the average biomass density, but then will compute the total biomass for all sites.

This exercise is expected to take 1-2 hours. If you have any suggestions for how we might improve this exercise, please let us know. 

## Setup

You can view index.html in any browser, but we recommend using the provided npm-based local development server. First install Node (v18+), then run `npm install` to install the dependencies. Then you can run `npm run start` to start the local server. You can then access the frontend at `http://localhost:8080`.

## Backend

Write the body of the Lambda function in `get_biomass_stats.py`. While some parameters and code has been provided, you may need to change them to suit your needs. We will be running the Python script using PyOdide in the browser, so please note that you will be unable to access local files, and will need to pass all relevant input data as parameters to the function. Note that PyOdide may take a few seconds to run.

## Frontend

Write the React component (as wireframed below) in `index.html`. It should have an area to enter a new average biomass density, a button to trigger the API request, and an area to display the results. Note that all content should be centered vertically and horizontally in the page. Use the wireframe below as a guide, but feel free to add your own styling and flair.

### UI Wireframe

```text

┌────────────────────────────────┐
│  Avg density of biomass (t/km2)│
│  ┌──────────────────────────┐  │
│  │  73                      │  │
│  └─────────────┬────────────┤  │
│                ├────────────┤  │
│                │  Compute!  │  │
│                ├────────────┤  │
└────────────────┴────────────┴──┘


You have 8 sites, with a total estimated

biomass of **1.11Mt**!

```




## Submission

When you're finished, please zip up `get_biomass_stats.py` and `index.html` and send them to us via email. Please also include roughly how long it took you to complete, and any feedback you have on the exercise. Thank you!
```
