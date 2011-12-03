# Copyright 2011 Omniscale (http://omniscale.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from imposm.mapping import (
    Options,
    Points, LineStrings, Polygons,
    String, Bool, Integer, OneOfInt,
    WayZOrder, ZOrder, Direction,
    GeneralizedTable, UnionView,
)

# # internal configuration options
# # uncomment to make changes to the default values
# import imposm.config
# 
# # import relations with missing rings
# imposm.config.import_partial_relations = False
# 
# # select relation builder: union or contains
# imposm.config.relation_builder = 'contains'
# 
# # log relation that take longer than x seconds
# imposm.config.imposm_multipolygon_report = 60
# 
# # skip relations with more rings (0 skip nothing)
# imposm.config.imposm_multipolygon_max_ring = 0


db_conf = Options(
    # db='osm',
    host='localhost',
    port=5984,
    user='osm',
    password='osm',
    sslmode='allow',
    prefix='osm_new_',
    proj='epsg:900913',
    name='geocouch', #make sure to add this line if you want to use couchdb
)

class Highway(LineStrings):
    fields = (
        ('tunnel', Bool()),
        ('bridge', Bool()),
        ('oneway', Direction()),
        ('ref', String()),
        ('z_order', WayZOrder()),
    )
    field_filter = (
        ('area', Bool()),
    )

places = Points(
    name = 'places',
    mapping = {
        'place': (
            'country',
            'state',
            'region',
            'county',
            'city',
            'town',
            'village',
            'hamlet',
            'suburb',
            'locality',
        ),
    },
    fields = (
        ('z_order', ZOrder([
            'country',
            'state',
            'region',
            'county',
            'city',
            'town',
            'village',
            'hamlet',
            'suburb',
            'locality',
        ])),
        ('population', Integer()),
    ),
)

admin = Polygons(
    name = 'admin',
    mapping = {
        'boundary': (
            'administrative',
        ),
    },
    fields = (
        ('admin_level', OneOfInt('1 2 3 4 5 6'.split())),
    ),
)

motorways = Highway(
    name = 'motorways',
    mapping = {
        'highway': (
            'motorway',
            'motorway_link',
            'trunk',
            'trunk_link',
        ),
    }
)

mainroads = Highway(
    name = 'mainroads',
    mapping = {
        'highway': (
            'primary',
            'primary_link',
            'secondary',
            'secondary_link',
            'tertiary',
    )}
)

buildings = Polygons(
    name = 'buildings',
    mapping = {
        'building': (
            '__any__',
    )}
)

minorroads = Highway(
    name = 'minorroads',
    mapping = {
        'highway': (
            'road',
            'path',
            'track',
            'service',
            'footway',
            'bridleway',
            'cycleway',
            'steps',
            'pedestrian',
            'living_street',
            'unclassified',
            'residential',
    )}
)

transport_points = Points(
    name = 'transport_points',
    fields = (
        ('ref', String()),
    ),
    mapping = {
        'highway': (
            'motorway_junction',
            'turning_circle',
            'bus_stop',
        ),
        'railway': (
            'station',
            'halt',
            'tram_stop',
            'crossing',
            'level_crossing',
            'subway_entrance',
        ),
        'aeroway': (
            'aerodome',
            'terminal',
            'helipad',
            'gate',
    )}
)

railways = LineStrings(
    name = 'railways',
    fields = (
        ('tunnel', Bool()),
        ('bridge', Bool()),
        # ('ref', String()),
        ('z_order', WayZOrder()),
    ),
    mapping = {
        'railway': (
            'rail',
            'tram',
            'light_rail',
            'subway',
            'narrow_gauge',
            'preserved',
            'funicular',
            'monorail',
    )}
)

waterways = LineStrings(
    name = 'waterways',
    mapping = {
        'waterway': (
            'stream',
            'river',
            'canal',
            'drain',
    )},
    field_filter = (
        ('tunnel', Bool()),
    ),
)

waterareas = Polygons(
    name = 'waterareas',
    mapping = {
        'waterway': ('riverbank',),
        'natural': ('water',),
        'landuse': ('basin', 'reservoir'),
})

aeroways = LineStrings(
    name = 'aeroways',
    mapping = {
        'aeroway': (
            'runway',
            'taxiway',
    )}
)

transport_areas = Polygons(
    name = 'transport_areas',
    mapping = {
        'railway': (
            'station',
        ),
        'aeroway': (
            'aerodome',
            'terminal',
            'helipad',
            'apron',
        ),
})

landusages = Polygons(
    name = 'landusages',
    fields = (
        ('z_order', ZOrder([
            'pedestrian',
            'footway',
            'playground',
            'park',
            'forest',
            'cemetery',
            'farmyard',
            'farm',
            'farmland',
            'wood',
            'meadow',
            'grass',
            'village_green',
            'recreation_ground',
            'garden',
            'sports_centre',
            'pitch',
            'common',
            'allotments',
            'golf_course',
            'university',
            'school',
            'college',
            'library',
            'fuel',
            'parking',
            'nature_reserve',
            'cinema',
            'theatre',
            'place_of_worship',
            'hospital',
            'scrub',
            'quarry',
            'residential',
            'retail',
            'commercial',
            'industrial',
            'railway',
            'land',
        ])),
    ),
    mapping = {
        'landuse': (
            'park',
            'forest',
            'residential',
            'retail',
            'commercial',
            'industrial',
            'railway',
            'cemetery',
            'grass',
            'farmyard',
            'farm',
            'farmland',
            'wood',
            'meadow',
            'village_green',
            'recreation_ground',
            'allotments',
            'quarry',
        ),
        'leisure': (
            'park',
            'garden',
            'playground',
            'golf_course',
            'sports_centre',
            'pitch',
            'stadium',
            'common',
            'nature_reserve',
        ),
        'natural': (
            'wood',
            'land',
            'scrub',
        ),
        'highway': (
            'pedestrian',
            'footway',
        ),
        'amenity': (
            'university',
            'school',
            'college',
            'library',
            'fuel',
            'parking',
            'cinema',
            'theatre',
            'place_of_worship',
            'hospital',
        ),
})

amenities = Points(
    name='amenities',
    mapping = {
        'amenity': (
            'university',
            'school',
            'library',
            'fuel',
            'hospital',
            'fire_station',
            'police',
            'townhall',
        ),
})

motorways_gen1 = GeneralizedTable(
    name = 'motorways_gen1',
    tolerance = 50.0,
    origin = motorways,
)

mainroads_gen1 = GeneralizedTable(
    name = 'mainroads_gen1',
    tolerance = 50.0,
    origin = mainroads,
)

railways_gen1 = GeneralizedTable(
    name = 'railways_gen1',
    tolerance = 50.0,
    origin = railways,
)

motorways_gen0 = GeneralizedTable(
    name = 'motorways_gen0',
    tolerance = 200.0,
    origin = motorways_gen1,
)

mainroads_gen0 = GeneralizedTable(
    name = 'mainroads_gen0',
    tolerance = 200.0,
    origin = mainroads_gen1,
)

railways_gen0 = GeneralizedTable(
    name = 'railways_gen0',
    tolerance = 200.0,
    origin = railways_gen1,
)

roads = UnionView(
    name = 'roads',
    fields = (
        ('bridge', 0),
        ('ref', None),
        ('tunnel', 0),
        ('oneway', 0),
        ('z_order', 0),
    ),
    mappings = [motorways, mainroads, minorroads, railways],
)

roads_gen1 = UnionView(
    name = 'roads_gen1',
    fields = (
        ('bridge', 0),
        ('ref', None),
        ('tunnel', 0),
        ('oneway', 0),
        ('z_order', 0),
    ),
    mappings = [railways_gen1, mainroads_gen1, motorways_gen1],
)

roads_gen0 = UnionView(
    name = 'roads_gen0',
    fields = (
        ('bridge', 0),
        ('ref', None),
        ('tunnel', 0),
        ('oneway', 0),
        ('z_order', 0),
    ),
    mappings = [railways_gen0, mainroads_gen0, motorways_gen0],
)
