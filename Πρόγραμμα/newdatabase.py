#Modules 
import pandas as pd
import csv
import sqlite3
    
def database():
    #Τα url για καθέ αρχείο csv
    urlcases = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    urldeaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    urlvaccine = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/time_series_covid19_vaccine_doses_admin_global.csv"

    print("\nConverting CSV to Dataframe...")
    #Μετατροπή σε dataframe
    dfcases = pd.read_csv(urlcases)
    dfdeaths = pd.read_csv(urldeaths)
    dfvaccine = pd.read_csv(urlvaccine)

    print("\nComplete")

    print("\nMaking corrections")
    #Επιλόγη στηλών με τις βασικές πληροφορίες
    dfcases.drop(dfcases.columns[[2, 3]], axis=1, inplace=True)
    dfdeaths.drop(dfdeaths.columns[[2, 3]], axis=1, inplace=True)
    dfvaccine.drop(dfvaccine.columns[[0, 1, 2, 3, 4, 5, 8, 9, 10 ,11]], axis=1, inplace=True)

    for i in [dfcases,dfdeaths]:
        i.rename(columns={'Province/State': 'State', 'Country/Region': 'Country'}, inplace=True)
    dfvaccine.rename(columns={'Province_State': 'State', 'Country_Region': 'Country'}, inplace=True)
    #Αλλαγή format ημερομηνιών στα ονόματα των στηλών
    for l in [dfcases,dfdeaths]: 
        for col in l.columns: l.rename(columns={col:'D'+col.replace('/','mdy')}, inplace=True)
    for col in dfvaccine.columns: dfvaccine.rename(columns={col:'D'+col.replace('-','ymd')}, inplace=True)

    for i in [dfcases,dfdeaths]:
        i.rename(columns={'DState': 'State', 'DCountry': 'Country'}, inplace=True)
    dfvaccine.rename(columns={'DState': 'State', 'DCountry': 'Country'}, inplace=True)


    print(dfcases, dfdeaths, dfvaccine, sep='\n')
    print("\nComplete")

    connection = sqlite3.connect('covid19.db')
    #Μετατροπή απο dataframe σε sqlite3 dtabase
    print("\nConverting Dataframe to SQLite3 database...")
    #Πρώτος πίνακας(cases)
    dfcases.to_sql(
        name = 'Cases',
        con = connection,
        if_exists = 'replace',
        index= False,
        )
    #Δεύτερος πίνακας(deaths)
    dfdeaths.to_sql(
        name = 'Deaths',
        con = connection,
        if_exists = 'replace',
        index= False,
        )
    #Τρίτος πίνακας(vaccinations)
    dfvaccine.to_sql(
        name = 'Vaccinations',
        con = connection,
        if_exists = 'replace',
        index= False,
        )
    print("\nComplete")
