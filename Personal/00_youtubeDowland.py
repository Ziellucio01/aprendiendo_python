import pytube

url = input("Ingresa la url del video: ")

path = "C:"

pytube.Yotube(url).streams.get_highest_resolution().dowloand(path)