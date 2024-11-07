#!/usr/bin/env python3
# subway.py -- an interactive subway program
# Usage : subway.py - CSCI-132 Project.
# Author : Jose Ortiz
# Created on : November 5, 2024.
# Description : This program will read a CSV file containing subway data and allow users to query the data. The program will provide information about subway stations, routes, and portals.
#
#*************************************************************


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
                connected_stations.add((station1.station_name, station2.station_name))  # Store names instead
    return connected_stations


def haversine(lat1, lon1, lat2, lon2):
    """Calculates the distance between two points using GPS coordinates."""
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r


def list_stations(stations, output_file):
    """Lists all station names alphabetically."""
    output = "Subway Stations:\n"
    for station in sorted(stations, key=lambda x: x.station_name):
        output += station.station_name + "\n"
    print(output)
    output_file.write(output)


def list_route_stations(stations, route_identifier, output_file):
    """Lists stations served by a specific route."""
    output = f"Stations on Route {route_identifier}:\n"
    for station in stations:
        if route_identifier in station.route_sets:
            output += station.station_name + "\n"
    print(output)
    output_file.write(output)


def list_routes(portals, portal_name, output_file):
    """Lists routes accessible at a specific portal."""
    output = ""
    for portal in portals:
        if portal.station_name == portal_name:  # Ensure comparison is correct
            output = f"Routes at {portal.station_name}: {', '.join(portal.route_sets)}\n"
            break
    else:
        output = f"No portal found for {portal_name}\n"
    print(output)
    output_file.write(output)


def list_station_portals(portals, station_name, output_file):
    """Lists all portals for a given station and their entrance types."""
    output = f"Portals for Station {station_name}:\n"
    for portal in portals:
        if portal.station_name == station_name:
            output += f"  {portal.station_name} ({portal.route_sets})\n"
    print(output)
    output_file.write(output)


def nearest_portal(portals, latitude, longitude, output_file):
    """Finds the closest portal and its routes."""
    closest_distance = float("inf")
    closest_portal = None
    for portal in portals:
        distance = haversine(latitude, longitude, portal.gps_coordinates[0], portal.gps_coordinates[1])
        if distance < closest_distance:
            closest_distance = distance
            closest_portal = portal
    output = (f"Closest portal: {closest_portal.station_name} ({closest_portal.gps_coordinates})\n"
              f"Closest routes: {', '.join(closest_portal.route_sets)}\n")
    print(output)
    output_file.write(output)


def main():
    data_file = '/Users/jortiz/Desktop/nyc_subway_stations.csv'

    # Open the output file for writing
    output_file = open('/Users/jortiz/Desktop/subway_output.txt', 'w')

    portals = []
    station_list = []
    route_sets_map = defaultdict(set)

    with open(data_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            general_name, gps_coordinates = portal_names(row)

            # Create a set of routes from the Route columns
            route_columns = ["Route1", "Route2", "Route3", "Route4", "Route5", "Route6",
                             "Route7", "Route8", "Route9", "Route10", "Route11"]
            route_set = set(row[route] for route in route_columns if row[route])  # Renamed this variable

            portal = Portal(row["Station Name"], gps_coordinates, route_set)
            portals.append(portal)
            station_list.append(portal)
            route_sets_map[portal.station_name].update(route_set)

    connected_stations = route_sets(portals, station_list)  # This should now work without conflict

    while True:
        command = input(
            "Enter a command (liststations, listroutestations, listroutes, liststationportals, nearest, help, quit): ")

        if command == "liststations":
            list_stations(station_list, output_file)
        elif command == "listroutestations":
            route_identifier = input("Enter route identifier: ")
            list_route_stations(station_list, route_identifier, output_file)
        elif command == "listroutes":
            portal_name = input("Enter portal name or GPS coordinates: ")
            list_routes(portals, portal_name, output_file)
        elif command == "liststationportals":
            station_name = input("Enter station name: ")
            list_station_portals(portals, station_name, output_file)
        elif command == "nearest":
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            nearest_portal(portals, latitude, longitude, output_file)
        elif command == "help":
            help_text = ("Available commands:\n"
                         "  liststations: List all stations\n"
                         "  listroutestations <route_identifier>: List stations on a route\n"
                         "  listroutes <portal_name>: List routes at a portal\n"
                         "  liststationportals <station_name>: List portals for a station\n"
                         "  nearest <latitude> <longitude>: Find the nearest portal\n"
                         "  help: Display this help message\n"
                         "  quit: Exit the program")
            print(help_text)
            output_file.write(help_text + "\n")
        elif command == "quit":
            break
        else:
            error_message = "Invalid command. Type 'help' for the list of valid commands.\n"
            print(error_message)
            output_file.write(error_message)

    # Close the output file when done
    output_file.close()


if __name__ == "__main__":
    main()