import pandas

squirrel_census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sq_clr = squirrel_census_data["Primary Fur Color"].value_counts().to_dict()

sq_clr_data = {"Fur Color": list(sq_clr.keys()), "Count": list(sq_clr.values())}

squirrel_color_data = pandas.DataFrame(sq_clr_data)

squirrel_color_data.to_csv("squirrel_count.csv")
