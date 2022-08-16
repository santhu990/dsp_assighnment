# -*- coding: utf-8 -*-


import folium
world_map= folium.Map()
world_map

nuzvid=folium.Map(location=[16.812951661814868, 80.81202068969367])
nuzvid



amalapuram=folium.Map(location=[16.5787, 82.0061])
amalapuram

coords_1=[[16.791749889941737, 80.84421693241418],[16.768083178923863, 80.87854920403927],[16.731262441000577, 80.90052185787933],[16.707588208823882, 80.92112122085437],[16.678649048657125, 80.94858703815444],[16.67963568306118, 80.94824370835899],[16.684239909752463, 80.96884307133404],[16.686870846648066, 80.97570952565904],[16.686870846648066, 80.98875578887657],[16.686213115818987, 80.99905547036411],[16.684239909752463, 81.00866850641913],[16.686870846648066, 81.02240141506915],
[16.711205295519658, 81.02308806050166],[16.726330551614268, 81.05192716866674],[16.742112148324132, 81.0821395676968],[16.740797065189437, 81.09724576721185],[16.738166871682843, 81.13501126599942],[16.743427222378926, 81.15217740181198],[16.74868742778645, 81.16865689219202],[16.752632486472212, 81.18513638257207],[16.750659967348835, 81.17003018305702],[16.755262480172394, 81.19131619146458],[16.768411904716693, 81.20573575285225],[16.78419001232427, 81.21946866150228],[16.80259614824658, 81.24144131534234],
[16.80654008801268, 81.25380093312737],[16.81048394578203, 81.26478726004738],[16.807854716380728, 81.28058010499494],[16.80654008801268, 81.27714687783244],[16.80916933563739, 81.2737136506699],[16.80456812837816, 81.29980617710498],[16.809826643164946, 81.36641080988927],[16.825601308632482, 81.4611678795745],[16.834802590420235, 81.46803433389952],[16.843346237471874, 81.53051906825719],[16.842031855331825, 81.53257900455469],[16.819685962921593, 81.56691127617977],[16.807854717696934, 81.58133083026229],[16.767097004424592, 81.67814787118931],
[16.682924430168484, 81.80174404903961],[16.726330554056105, 81.83195644806968],[16.69476344200182, 81.84706267409418],[16.70068267307115, 81.87658842769174],[16.70002498978911, 81.8910079817743],[16.688844027524087, 81.89650114523428],[16.67963568503055, 81.91229399018184],[16.657270721786173, 81.93083341685939],[16.65595505432973, 81.93975980748189],[16.646087260345286, 81.96173246132196],[16.640824229091535, 81.96722562478196],[16.623718379765894, 81.96791227021447],[16.607269009648736, 81.97477872453948],[16.58357944232739, 81.99331815121703],[16.577656594535203, 82.00361783270455]]

coords_2=[[16.781416944572747, 80.8575350543379],[16.639364867095082, 80.95915857834815],[16.736708254789477, 81.0662752658184],[16.841888425639223, 81.24480307826883],[16.88920046323589, 81.31896078497901],
          [17.031721844911203, 81.5215211223478],[17.031721844911203, 81.5215211223478],[17.01859076204815, 81.65885020884814],[17.025156418668157, 81.72614146123331],[16.996265807372648, 81.76871347804841],
          [16.950294295607883, 81.78107309583343],[16.820199792587275, 81.84699105735358],[16.825457872525533, 81.84973763908359],[16.78338915072916, 81.86072396600365],[16.791277746462097, 81.86347054773363],
          [16.654495813604967, 81.94724129049884],[16.58211965131749, 82.00354621596398]]

from branca.element import Figure
fig5=Figure(height=550,width=750)
map=folium.Map(location=[16.5787,80.81202068969367],tiles="openstreetmap",zoom_start=14)
fig5.add_child(map)
f1=folium.FeatureGroup("1st Way toNuzvid to Amalapuram")
f2=folium.FeatureGroup("2nd Way to Nuzvid to amalapuram")
line_1=folium.vector_layers.PolyLine(coords_1,popup='<b>Path of Vehicle_1</b>',tooltip='Vehicle_1',color='red',weight=10).add_to(f1)
line_2=folium.vector_layers.PolyLine(coords_2,popup='<b>Path of Vehicle_2</b>',tooltip='Vehicle_2',color='black',weight=10).add_to(f2)
folium.Marker(location=[16.591476284686536, 82.0008711759649],popup='Destination',tooltip='Amalpuram',icon=folium.Icon(color='red',prefix='fa',icon='map-marker',weigth=10)).add_to(map)
folium.Marker(location=[16.79153401962576, 80.83798308995817],popup='Source',tooltip='Nuzvid',icon=folium.Icon(color='red',prefix='fa',icon='circle',weigth=10)).add_to(map)
folium.Marker(location=[16.672896064752575, 80.94217879365388],popup='Jawahar Navodaya Vidyalaya',tooltip='college',icon=folium.Icon(color='blue',prefix='fa',icon='university',weigth=5)).add_to(map)
folium.Marker(location=[16.686192898560233, 81.02314527163307],popup='Sri Vidyanidhi Junoir college',tooltip='clg',icon=folium.Icon(color='blue',prefix='fa',icon='university',weigth=10)).add_to(map)
folium.Marker(location=[16.73535204012236, 81.06777722799359],popup='Raja dhaba resturant',tooltip='Food court',icon=folium.Icon(color='blue',prefix='fa',icon='hotel',weigth=10)).add_to(map)
folium.Marker(location=[16.836137895637442, 81.49560028724459],popup='Sri vasavi Eniginerring college',tooltip='University',icon=folium.Icon(color='blue',prefix='fa',icon='university',weigth=10)).add_to(map)
folium.Marker(location=[16.763337489758264, 81.6578203059186],popup='Bharat petrloum petrol pump',tooltip='Petrol Source',icon=folium.Icon(color='blue',prefix='fa',icon='circle',weigth=10)).add_to(map)
folium.Marker(location=[16.6916602153082, 81.78690964722891],popup='Children parks',tooltip='parks',icon=folium.Icon(color='green',prefix='fa',icon='tree',weigth=10)).add_to(map)
folium.Marker(location=[16.836630801824402, 81.44530354455932],popup='Garuda Food Court',tooltip='High class resturant',icon=folium.Icon(color='blue',prefix='fa',icon='hotel',weigth=10)).add_to(map)
folium.Marker(location=[16.810340493520417, 81.24754965999884],popup='Dwaraka Tirumala',tooltip='Famous Temple',icon=folium.Icon(color='blue',prefix='fa',icon='circle',weigth=10)).add_to(map)
folium.Marker(location=[16.994459999912472, 81.77300502182969],popup='D-Mart',tooltip='shopping mall',icon=folium.Icon(color='blue',prefix='fa',icon='shopping-cart',weigth=10)).add_to(map)
folium.Marker(location=[17.00025638665711, 81.50967991646478],popup='Bus stop',tooltip='main-center',icon=folium.Icon(color='blue',prefix='fa',icon='hotel',weigth=10)).add_to(map)
folium.Marker(location=[16.929325707785555, 81.36411108477444],popup='Godavari Gas Private Limited CNG Filling Station',tooltip='Petrol Bank',icon=folium.Icon(color='blue',prefix='fa',icon='circle',weigth=10)).add_to(map)
folium.Marker(location=[16.724265008969976, 81.88046845724548],popup='HP Gas Private Limited CNG Filling Station',tooltip='Petrol Bank',icon=folium.Icon(color='blue',prefix='fa',icon='circle',weigth=10)).add_to(map)
f1.add_to(map)
f2.add_to(map)
folium.LayerControl().add_to(map)
map