import pandas as pd

def create_dataframe(csv_file):

    ### This takes in a csv from StreetEasy and turns the date columns into values.
    ### Finally the variable column is changed to a date-time column, which is then
    ### used as the index

    new_data = pd.melt(csv_file,id_vars=['areaName','Borough', 'areaType'])
    new_data['variable'] = pd.to_datetime(new_data['variable'], infer_datetime_format=True)
    new_data.set_index('variable', inplace=True)
    return new_data

def select_borough_data(dataframe, borough):
    
    ### Selects data by borough. Acceptable inputs are listed below:
    ### Manhattan, Bronx, Brooklyn, Queens, Staten Island
    
    new_data = dataframe[dataframe['Borough'] == borough]
    new_data = new_data[new_data['areaType']=='borough']
    return new_data

def describe_data(dataframe):
    data_max = dataframe['value'].max()
    data_min = dataframe['value'].min()
    data_min_year = str(dataframe[dataframe['value']==data_min].index[0]).split(" ")[0][:4]
    data_max_year = str(dataframe[dataframe['value']==data_max].index[0]).split(" ")[0][:4]
    time_from_min_max = int(data_max_year) - int(data_min_year)
    percentage_increase = (((data_max - data_min) / data_min))
    

    st1 = 'The lowest median asking price was ${:0,.0f}' ' which was in the year {}.'.format(data_min, data_min_year)
    st2 = 'The highest median asking price was ${:0,.0f}' ' which was in the year {}.'.format(data_max, data_max_year)
    st3 = 'Over the course of {} years (between {} and {}), the asking price has increased by {:.1%}.'.format(time_from_min_max, data_min_year, data_max_year,percentage_increase)   
    final_str = st1 + ' ' +  st2 + ' ' + st3
    
    return final_str
    
def calculate_asking_price_change(dataframe, starting_year_and_month, ending_year_and_month):
    if starting_year_and_month > ending_year_and_month:
        return 'Starting Year needs to be before the ending year. Try switching the numbers.'
    
    starting_data = int(dataframe.loc[starting_year_and_month]['value'])
    ending_data = int(dataframe.loc[ending_year_and_month]['value'])
    ret = ((ending_data - starting_data) / starting_data)
    st1 = 'The median asking price from {} to {} went from {:0,.0f} to {:0,.0f}.'.format(starting_year_and_month, ending_year_and_month, starting_data, ending_data )
    st2 = 'This represented a percentage change of {:.1%}.'.format(ret)
    final_str = st1 + ' ' + st2
    
    return final_str
    
   
    
    
    
    
    
    
    
    
        
        