import pandas as pd

def create_dataframe(csv_file):

    ### This takes is a csv from StreetEasy and turns the date columns into values.
    ### Finally the variable column is changed to a date-time column, which is then
    ### used as the index

    new_data = pandas.melt(csv_file,id_vars=['areaName','Borough', 'areaType'])
    new_data['variable'] = pandas.to_datetime(new_data['variable'], infer_datetime_format=True)
    new_data.set_index('variable', inplace=True)
    return new_data
