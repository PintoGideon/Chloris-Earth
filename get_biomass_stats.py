# This code roughly matches the structure of an AWS Lambda function behind an API Gateway endpoint.
import json
import math

# Approximate conversion factor: 1 degree ≈ 111.1 km
DEG_TO_KM = 111.1

def handler(event):
    # Parse the incoming event (simulate AWS Lambda + API Gateway)
    if isinstance(event, dict) and 'body' in event:
        try:
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        except json.JSONDecodeError:
            return json.dumps({
                'statusCode': 400, 
                'body': {'error': 'Invalid JSON in request body'}
            })
    else:
        return json.dumps({
            'statusCode': 400,
            'body': {'error': 'Missing or invalid request body'}
        })

    # Extract parameters
    density = body.get('density', 0)
    site_data = body.get('siteData', [])

    # Validate density
    if not isinstance(density, (int, float)) or density < 0:
        return json.dumps({
            'statusCode': 400,
            'body': {'error': 'Density must be a non-negative number'}
        })

    # Validate site_data
    if not isinstance(site_data, list):
        return json.dumps({
            'statusCode': 400,
            'body': {'error': 'Site data must be a list'}
        })

    total_area = 0.0
    processed_sites = 0
    skipped = 0

    for site in site_data:
        # Attempt to coerce the radius into a float
        try:
            point_r = float(site.get('pointR'))
        except (TypeError, ValueError):
            skipped += 1
            continue

        # If radius is negative, skip this site
        if point_r < 0:
            skipped += 1
            continue

        # Convert radius from degrees to kilometers
        radius_km = point_r * DEG_TO_KM

        # Area of a circle = π · r²
        area = math.pi * (radius_km ** 2)
        total_area += area
        processed_sites += 1

    # Total biomass = (total area in km²) * (density in t/km²)
    total_biomass = total_area * density

    return json.dumps({
        'statusCode': 200,
        'body': {
            'count': processed_sites,
            'skipped': skipped,
            'area': round(total_area, 2),
            'biomass': round(total_biomass, 2)
        }
    })

# If you have python installed locally, you can test this code by uncommenting the next few line, then running `python get_biomass_stats.py`
print(handler(dict(body='''{"density": 1, "siteData":[{"pointX": 1, "pointY": 2, "pointR": 3}, {"pointX": 4, "pointY": 5, "pointR": -6}, {"pointX": "bad", "pointY": 7, "pointR": 8}]}''')))
