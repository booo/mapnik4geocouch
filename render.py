#!/usr/bin/env python
import mapnik2

mapfile = 'style.xml'
map_output = 'hello_world_geocouch.png'
m = mapnik2.Map(2048, 2048)
mapnik2.load_map(m, mapfile)
bbox = mapnik2.Envelope(mapnik2.Coord(13.42529296875, 52.48278022207821), mapnik2.Coord(13.436279296875, 52.48947038534305))
m.zoom_to_box(bbox)
mapnik2.render_to_file(m, map_output)
