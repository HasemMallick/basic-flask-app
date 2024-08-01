from flask import Flask, render_template_string
import leafmap.foliumap as leafmap
from database import connect_db, get_nyc
from layers import get_us_states


app = Flask(__name__)

@app.route('/')
def index():
    # Create a Leafmap map
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_basemap("HYBRID")  # Set the initial basemap

    m.add_gdf(get_nyc(), layer_name="NYC Map")

    m.add_gdf(get_us_states(), layer_name="US States")

    map_html = m.to_html()  # Convert map to HTML

    # Render the map with dropdown functionality
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Leafmap with Flask</title>
        <style>
            #map { height: 600px; }
        </style>
    </head>
    <body>
        <div>
            <h2>This is a Flask application</h2>
            <label for="layer-select">Select Basemap:</label>
            <select id="layer-select">
                <option value="HYBRID" selected>Hybrid</option>
                <option value="SATELLITE">Satellite</option>
                <option value="ROADMAP">Roadmap</option>
                <option value="TERRAIN">Terrain</option>
                <option value="TONER">Toner</option>
                <option value="WATERCOLOR">Watercolor</option>
            </select>
        </div>
        <div id="map" style="margin: 100px 50px">{{ map_html|safe }}</div>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                var map = document.querySelector('#map iframe').contentWindow;
                var select = document.getElementById('layer-select');
                
                select.addEventListener('change', function() {
                    var basemap = select.value;
                    map.postMessage({ type: 'change-basemap', basemap: basemap }, '*');
                });

                window.addEventListener('message', function(event) {
                    if (event.data.type === 'change-basemap') {
                        var basemap = event.data.basemap;
                        map.eval(`map.setBasemap('${basemap}');`);
                    }
                });
            });
        </script>
    </body>
    </html>
    ''', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
