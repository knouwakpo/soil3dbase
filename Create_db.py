import sqlite3 as lite

con = lite.connect('Soildb.db')



with con:
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute("CREATE TABLE Sites(SiteId INTEGER PRIMARY KEY, name TEXT, latitude REAL, longitude REAL,\
    labvsfield TEXT, date DATE investigator TEXT)")
    cur.execute("CREATE TABLE Plots(PlotId INTEGER PRIMARY KEY, Plotsite INTEGER REFERENCES Sites(SiteId) \
    ON UPDATE CASCADE ON DELETE CASCADE, plotname TEXT, plotaoc TEXT, width_m REAL, length_m REAL)")
    cur.execute("CREATE TABLE Plot_Properties(PropertyID INTEGER PRIMARY KEY, Property_plot INTEGER REFERENCES Plots(PlotId) \
    ON UPDATE CASCADE ON DELETE CASCADE, property_date DATE, slope REAL, texture TEXT, fao_usda TEXT,\
    sand REAL, silt REAL, clay REAL, rock REAL, treatment TEXT, plantbase REAL, plantlitter REAL,\
    biocrust REAL, bareground REAL, totveg REAL, shrub REAL, angrass REAL,\
    pergrass REAL, forbs REAL, bdensity REAL, carbonpct REAL)")
    cur.execute("CREATE TABLE Reconstructions(ReconID INTTEGER, Reconplot INTEGER REFERENCES Plots(PlotId) \
    ON UPDATE CASCADE ON DELETE CASCADE, raindepth REAL, \
        runondepth REAL, waterdepth REAL, duration REAL, moisture REAL, \
        method TEXT, accuracy_m REAL, precision_m REAL, resolution_m REAL, soillosskg REAL, runoff_mm REAL, recon_ref TEXT, filename TEXT, \
        recon_date DATE, author TEXT, link TEXT)")
con.close()
