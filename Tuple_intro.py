# # tup = '1', '2', '3'
# # print(tup[1])
#
# # x, y = 1, 2
# # data = 1, 2
# # x, y = data
# # print(x,y)
#
# # number = [1,2,3,53,85,96,78,45,21,21,45,]
# # for index, num in enumerate(number):
# #     print(index, num)
# # print()
# # for item in enumerate(number):
# #     index, num = item
# #     print(index, num)
#
# INDEX_SONGS = 3
# SONG_INDEX = 1
#
# albums = [
#     [
#         "JEANS",
#         "ARR",
#         1999,
#         (
#             (1, 'jean1'),
#             (2, 'jeans2'),
#             (3, 'jean3'),
#             (4, 'jean4'),
#             (5, 'jean5'),
#         )
#     ],
#     [
#         "Muthalvan",
#         'ARR',
#         2005,
#         (
#             (1, 'MU1'),
#             (2, 'MU2'),
#             (3, 'MU3'),
#             (4, 'MU4'),
#         )
#     ],
#     [
#         "Paiya",
#         'yuvan',
#         2010,
#         (
#             (1, 'PA1'),
#             (2, 'PA2'),
#             (3, 'PA3'),
#         )
#     ],
# ]
#
# while True:
#     print("The available albums are:")
#     for index, item in enumerate(albums):
#         movie, comp, year, song = item
#         print("ID: {} - Movie: {}, composer: {}, Year: {}"
#               .format(index+1,movie, comp, year))
#     movie = int(input("Select the movie: "))
#     if 0 < movie <= len(albums):
#         print("you available songs in the movie {} are"
#               .format(albums[movie-1][0]))
#         for index, song in albums[movie-1][INDEX_SONGS]:
#             print("ID: {} - Song: {}"
#                 .format(index,song))
#         song = int(input("Which song you want, enter the ID: "))
#         if 0 < song <= len(albums[movie-1][INDEX_SONGS]):
#             print("Playing^-^-^- {}"
#                   .format(albums[movie-1][INDEX_SONGS][song-1][SONG_INDEX]))
#             print("======================================================")
#         else:
#             print("F............... off")
#             break
#     else:
#         print("F............... off")
#         break
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
