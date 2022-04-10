# s = "leonardo        _esta_loco"


#     count = []
#     for charac in char:
#         regex = re.search("[_ - \. - \, - \-]", charac, flags=0)
#         count.append(charac)
#         if charac == "_":
#             count.remove("_")
#             chars = "|"
#             count.append(chars)
#     return count


# def formatin_out(cadena):
#     out = re.sub(r'[^\w\s]', '', cadena)
#     return out

# python = "leonardo\esta"
# print(python)
# newstr= python.maketrans("esta", "esss")
# print(python.translate(newstr).zfill(20))



# class Coordinate(dict):
#     def __missing__(self, key):
#       return key


# print('({x}, {y})'.format_map(Coordinate(x='6')))
# print('({x}, {y})'.format_map(Coordinate(y='5')))
# print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))

# importing arrow module
import arrow
 
# date in string format
s ='2020-02-02 12:30:45'
 
 
# parsing string into date
date = arrow.get(s, 'YYYY-MM-DD HH:mm:ss')
 
# printing the date
print(date)