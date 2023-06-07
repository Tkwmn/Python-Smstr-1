import sys

from kivy.base import runTouchApp
from kivy.lang import Builder

if __name__ == '__main__' and __package__ is None:
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


root = Builder.load_string(
    """
#:import sys sys
#:import MapSource kivy_garden.mapview.MapSource
MapView:
    lat: -40.5731471
    lon: -73.1299819
    zoom: 17
    map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
    MapMarkerPopup:
        lat: -40.5862926
        lon: -73.0905569
        popup_size: dp(230), dp(130)
    MapMarkerPopup:
        lat: -40.576616
        lon: -73.1117204
        popup_size: dp(230), dp(130)
        
"""
)

runTouchApp(root)