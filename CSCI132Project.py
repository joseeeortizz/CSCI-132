# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 21, 2024
# Course: CSCI-132
# CSCI-132 Project.
# Description: This program will read a CSV file containing subway data and allow users to query the data.
# The program will provide information about subway stations, routes, and portals.

import csv
import math
from collections import defaultdict, namedtuple
from geopy.distance import great_circle

# Define data structures
Portal = namedtuple("Portal", ["station_name", "gps_coordinates", "route_sets"])
SubwayRoute = namedtuple("SubwayRoute", ["route_identifier", "stations"])

def portal_names(row):
    """Generates unique and general names for portals."""
    general_name = f"{row['North South Street']}, {row['East West Street']}, {row['Corner']}"
    gps_coordinates = (float(row['Entrance Latitude']), float(row['Entrance Longitude']))
    return general_name, gps_coordinates

def route_sets(portals, stations):
    """Checks for stations with identical route sets and proximity."""
    connected_stations = set()
    for station1 in stations:
        for station2 in stations:
            if station1 == station2:
                continue
            if (
                set(station1.route_sets) == set(station2.route_sets)
                and great_circle(station1.gps_coordinates, station2.gps_coordinates).kilometers <= 0.28
            ):
                connected_stations.add((station1, station2))
    return connected_stations

def haversine(lat1, lon1, lat2, lon2):
    """Calculates the distance between two points using GPS coordinates."""
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

def list_stations(stations):
    """Lists all station names alphabetically."""
    print("Subway Stations:")
    for station in sorted(stations, key=lambda x: x.station_name):
        print(station.station_name)

def list_route_stations(stations, route_identifier):
    """Lists stations served by a specific route."""
    print(f"Stations on Route {route_identifier}:")
    for station in stations:
        if route_identifier in station.route_sets:
            print(station.station_name)

def list_routes(portals, portal_name):
    """Lists routes accessible at a specific portal."""
    for portal in portals:
        if portal.general_name == portal_name or portal.gps_coordinates == portal_name:
            print(f"Routes at {portal.general_name}: {', '.join(portal.route_sets)}")
            break
    else:
        print(f"No portal found for {portal_name}")

def list_station_portals(portals, station_name):
    """Lists all portals for a given station and their entrance types."""
    print(f"Portals for Station {station_name}:")
    for portal in portals:
        if portal.station_name == station_name:
            print(f"  {portal.general_name} ({portal.entrance_type})")

def nearest_portal(portals, latitude, longitude):
    """Finds the closest portal and its routes."""
    closest_distance = float("inf")
    closest_portal = None
    for portal in portals:
        distance = haversine(latitude, longitude, portal.gps_coordinates[0], portal.gps_coordinates[1])
        if distance < closest_distance:
            closest_distance = distance
            closest_portal = portal
    print(f"Closest portal: {closest_portal.general_name} ({closest_portal.gps_coordinates})")
    print(f"Closest routes: {', '.join(closest_portal.route_sets)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python subway_data.py <data_file>")
        sys.exit(1)

    data_file = sys.argv[1]

    portals = []
    stations = set()
    route_sets_map = defaultdict(set)

    with open(data_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            general_name, gps_coordinates = portal_names(row)
            route_sets = set(route for route in row["Route1"], row["Route2"], row["Route3"], row["Route4"], row["Route5"], row["Route6"], row["Route7"], row["Route8"], row["Route9"], row["Route10"], row["Route11"] if route)
            portal = Portal(row["Station Name"], gps_coordinates, route_sets)
            portals.append(portal)
            stations.add(portal.station_name)
            route_sets_map[portal.station_name].update(route_sets)

    connected_stations = route_sets(portals, stations)

    while True:
        command = input("Enter a command (liststations, listroutestations, listroutes, liststationportals, nearest, help, quit): ")

        if command == "liststations":
            list_stations(stations)
        elif command == "listroutestations":
            route_identifier = input("Enter route identifier: ")
            list_route_stations(stations, route_identifier)
        elif command == "listroutes":
            portal_name = input("Enter portal name or GPS coordinates: ")
            list_routes(portals, portal_name)
        elif command == "liststationportals":
            station_name = input("Enter station name: ")
            list_station_portals(portals, station_name)
        elif command == "nearest":
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            nearest_portal(portals, latitude, longitude)
        elif command == "help":
            print("Available commands:")
            print("  liststations: List all stations")
            print("  listroutestations <route_identifier>: List stations on a route")
            print("  listroutes <portal_name>: List routes at a portal")
            print("  liststationportals <station_name>: List portals for a station")
            print("  nearest <latitude> <longitude>: Find the nearest portal")
            print("  help: Display this help message")
            print("  quit: Exit the program")
        elif command == "quit":
            break
        else:
            print("Invalid command. Type 'help' for the list of valid commands.")

if __name__ == "__main__":
    main()