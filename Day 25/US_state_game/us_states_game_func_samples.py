##################################################
# onscreenclick handler

# import turtle
#
# def get_cor(x, y):
#     print(x, y)
#
# screen = turtle.Screen()
#
# turtle.onscreenclick(get_cor)
# screen.mainloop()


##################################################
# looping through pandas DataFrame rows

# for row in flights.head().itertuples():
#     print(row)
# Pandas(Index=0, date=Timestamp('2001-01-14 21:55:00'), delay=0, destination='SMF', distance=480, origin='SAN')
# Pandas(Index=1, date=Timestamp('2001-03-26 20:15:00'), delay=-11, destination='SLC', distance=507, origin='PHX')
# Pandas(Index=2, date=Timestamp('2001-03-05 14:55:00'), delay=-3, destination='LAX', distance=714, origin='ELP')
# Pandas(Index=3, date=Timestamp('2001-01-07 12:30:00'), delay=12, destination='SNA', distance=342, origin='SJC')
# Pandas(Index=4, date=Timestamp('2001-01-18 12:00:00'), delay=2, destination='LAX', distance=373, origin='SMF')

# We can see that itertuples simply returns the content of row as named tuple with associated column names.
# Therefore, we can simply access the data with column names and Index, like:

# for row in flights.head().itertuples():
#     print(row.Index, row.date, row.delay)

# We will get each row as

# 0 2001-01-14 21:55:00 0
# 1 2001-03-26 20:15:00 -11
# 2 2001-03-05 14:55:00 -3
# 3 2001-01-07 12:30:00 12
# 4 2001-01-18 12:00:00 2
# Another benefit of itertuples is that it is generally faster than iterrows().


#############################################
# Find the nearest state that user clicks on

# Process of indexing list of cors and doing NNS will look something like this
# idx.insert(id = 0, (x1, y1, x2, y2))
# idx.insert(id = 1, (x1, y1, x2, y2))
# idx.insert(id = 2, (x1, y1, x2, y2))
# idx.insert(id = 3, (x1, y1, x2, y2))
# idx.insert(id = 4, (x1, y1, x2, y2))
# hits = idx.nearest((0, 0, 0, 0), 1, objects=True)
# for i in hits:
#     print(i.id)
#     print(i.bbox)
# With the example above I think we are done with most uses of this package
# That is to find the nearest coordinate from a list toward an input point
