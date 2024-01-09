from pystac_client import Client
from shapely.geometry import Point

point_location = Point(-79.75, 32.57)
point_location = Point(4.89, 52.37)  # AMS coordinates


api_url = "https://earth-search.aws.element84.com/v0"
client = Client.open(api_url)

collection = "sentinel-s2-l2a-cogs"  # Sentinel-2, Level 2A, COGs
search = client.search(
    collections=[collection],
    intersects=point_location,
    max_items=10,
)
items = search.get_all_items()
print(len(items))
