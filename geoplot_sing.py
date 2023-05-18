import os
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from scipy.spatial import ConvexHull
import branca.colormap as cmp
import re


def load_geodata(dir='./', load_fname='result.csv'):
    # 운송지 경로 할당 정보
    optm_location = pd.read_csv(os.path.join(dir, load_fname))
    optm_location = optm_location[['CAR_NUM', 'VISIT_ORDER',  'Y',	'X', 'LOCATION_NM']]
    return optm_location

#
def marker(m, coords_y, coords_x, marker_nm='name', color= 'red', min_width=200, max_width=200):

    # Add  markers to the map
    folium.Marker(
        location=[coords_y, coords_x],
        popup=folium.Popup(marker_nm, min_width=min_width, max_width=max_width),
        icon=folium.Icon(color=color)
        ).add_to(m)
    return m


def marker2(m, coords_y, coords_x, car_nm='car', marker_nm='name', loc_nm='LOCATION_NM', color='blue' ,
            min_width=200, max_width=200):
    import folium.plugins as plugins

    mc = MarkerCluster()

    # BASE MAP
    html=f"""
            <h2>  Information </h2>
            <p> car: {car_nm}  </p>
            <p> order: {marker_nm}  </p>
            <p> address: {loc_nm}  </p>
            """
    iframe = folium.IFrame(html=html, width=200, height=150)
    popup = folium.Popup(iframe, max_width=650)
    folium.Marker(
        location=[coords_y, coords_x],
        popup=popup,\
        icon=plugins.BeautifyIcon(
                            icon="arrow-down", icon_shape="marker",
                            number=marker_nm,
                            border_color=color,
                            background_color=color
                         )
    ).add_to(m)

    # Show the map again
    return


def pointer(m, coords_y, coords_x, color='red', marker_nm='marker_nm',min_width=200, max_width=200):
    # Add  points to the map
    folium.CircleMarker(location = [coords_y, coords_x],
                        radius = 5,
                        fill=True,
                        fill_opacity=1,
                        color = color,
                        popup=folium.Popup(marker_nm, min_width=min_width, max_width=max_width)
    ).add_to(m)
    return m

def PolyLine(m, lines, color='red'):
    folium.PolyLine(
        locations=lines,
        tooltip='PolyLine',
        color = color
    ).add_to(m)
    return m


def ploygons(m, coords_y, coords_x, marker_nm='name', color='red'):
    loc_lines = [[lat, log] for lat, log in zip(coords_y, coords_x)]
    ConvexHull_loc_lines = [loc_lines[i] for i in ConvexHull(loc_lines).vertices]
    # outlines for location point    
    folium.Polygon(
        locations=ConvexHull_loc_lines,
        fill=True,
        tooltip=marker_nm,
        color = color
    ).add_to(m)
    return m



def optmplot(car_result, dir='./', carnum = 'CA07'):
    init_xy = [1.3521, 103.8198]  # N(Y), E(X)

   # map 설정 (google map)
    m = folium.Map(
        location=init_xy,
        tiles="http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}",
        attr='Google',
        zoom_start=12
    )
    # optm center
    marker_colors = [
    'blue','gray','darkred', 'purple','orange',
    'green','darkgreen','darkblue','lightblue','cadetblue','lightred','darkpurple',
    'pink','lightgreen','lightgray','black','beige']

    points = []
    for optm_cntr_lat, optm_cntr_lon, optm_order, loc_nm in zip(car_result['Y'], car_result['X'],
                                                                car_result['VISIT_ORDER'], car_result['LOCATION_NM']):
        marker2(m, coords_y=optm_cntr_lat, coords_x=optm_cntr_lon,
                car_nm=carnum, marker_nm=optm_order, loc_nm=loc_nm, \
                color='cadetblue')
        if optm_order == (len(car_result) - 1):
            marker2(m, coords_y=optm_cntr_lat, coords_x=optm_cntr_lon,
                    car_nm=carnum, marker_nm='0', loc_nm=loc_nm, \
                    color='lightgray')
        points.append([optm_cntr_lat, optm_cntr_lon])
    PolyLine(m, lines=points)
    final_name = carnum + ".html"
    m.save(os.path.join(dir, final_name))


def optm_carPlot(input_dir="./input", output_dir="./output", fdate='230222',
                 load_fname='result_20230222.csv'):
    # 데이터 전처리
    optm_location= load_geodata(dir=input_dir, load_fname=load_fname) #최적화 엔진 결과로 떨어질 것

    import os

    dir_fdate = os.path.join(output_dir, fdate)
    if not os.path.exists(dir_fdate):
        os.makedirs(dir_fdate)

    CAR_NUM = list(set(optm_location['CAR_NUM']))
    for carnum in CAR_NUM:
        car_result = optm_location[optm_location['CAR_NUM'] == carnum].reset_index(drop=True)
        optmplot(car_result, dir= dir_fdate, carnum=carnum)


def get_files_to_json(output_dir='./web-data', file_path = './folders.json'):
    import os
    import json
    import glob

    filedict = {}
    filedict['rootFolder'] = output_dir
    filedict['folders'] = []

    dateDirlist= sorted(glob.glob(os.path.join(output_dir,'*')), reverse=True) #최신날짜가 가장먼저
    for datedir in dateDirlist:
        redatedir = datedir.replace(output_dir, "").replace('/', '')
        file_lists = sorted([f for f in os.listdir(datedir)])
        filedict['folders'].append({
            "id": redatedir,
            "files": file_lists
        })
    with open(file_path, 'w') as outfile:
        json.dump(filedict, outfile, indent=4)

if __name__=='__main__':
    import os
    input_dir = os.path.join('./', 'input-data')
    output_dir = os.path.join('./', 'web-data')
    optm_carPlot(input_dir=input_dir, output_dir=output_dir, fdate='230223')
    get_files_to_json(output_dir='./web-data')
