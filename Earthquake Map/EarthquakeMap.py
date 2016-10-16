import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import feedparser


# class for map
class map:


    # method for extracting rss file
    
    RSS="http://earthquake.usgs.gov/earthquakes/shakemap/rss.xml"
    increment = 0

    feed = feedparser.parse(RSS)
    event = []

    # update date
    Update_date = feed['channel']['published']
   
    print("Reading data from the RSS link...")
    # prints all the entries
        
    
    # Data extraction and manipulation
    def magnitude(entry):
        magnitude_end = entry.title.find('-')
        return float(entry.title[0:magnitude_end-1])

    def location(entry):
        return entry.title[6:]

    def longitude(entry):
        return float(entry.geo_lat)

    def latitude(entry):
        return float(entry.geo_long)

    def depth(entry):
        return float(entry.eq_depth)

    def datetime(entry):
        return entry.published 


    increment = 0
    while increment < len(feed.entries):
        entry = feed['entries'][increment]
        event.append([])
        event[increment].append(datetime(entry))
        event[increment].append(location(entry))
        event[increment].append(magnitude(entry))
        event[increment].append(latitude(entry))
        event[increment].append(longitude(entry))
        event[increment].append(depth(entry))
        count = 0
        while count < len(event[increment]):
            print(event[increment][count])
            count += 1
        print()
        increment += 1
      
        
                          
##
##    for entry in feed.entries:
##        event.append([])
##        event[increment].append(datetime(entry))
##        event[increment].append(location(entry))
##        event[increment].append(magnitude(entry))
##        event[increment].append(latitude(entry))
##        event[increment].append(longitude(entry))
##        event[increment].append(depth(entry))


##        for element in range(len(event[increment])):
##            if element == 1:
##                print("Location : {0}".format(event[increment][element]))
##            else:
##                print(event[increment][element])
##        print( )

    print("Earthquakes in the last 30 days: {0}".format(increment))

    

    # Design the map
    map = Basemap(projection ='robin',lat_0=0,lon_0=0,resolution='l')

    # draw coastline, country boardlines,fill continents

    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)
    map.fillcontinents(color='grey',lake_color='aqua')

    # color of oceans
    map.drawmapboundary(fill_color='aqua')

    # draw lat/lon grid lines every 30 degrees

    map.drawmeridians(np.arange(0,360,10))
    map.drawparallels(np.arange(-90,90,10))

    plt.suptitle("Earthquakes in the past 30 Days \n",size=17,weight='bold')
    plt.title("Last updated : {0}".format(Update_date), size=7,color='red')

    count2 = 0
    index = 0
    while count2 < len(event):
        x,y = map(event[index][3],event[index][4])
        map.plot(x,y,'ro',markersize=(event[index][2]**2)/5)
        plt.text(x,y,event[index][1],fontsize=7,color='red')
        count2 += 1
        index += 1
                
##    for earthquake in event:
##        
##        x,y = map(earthquake[3],earthquake[4])
##        map.plot (x, y, 'ro',markersize=(earthquake[2]**2)/5)
##        plt.text(x,y,earthquake[1],fontsize=7,color='red')
##
    plt.show()


     





            
        
        



