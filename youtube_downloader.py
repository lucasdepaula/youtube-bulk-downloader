from __future__ import unicode_literals
import youtube_dl

filename = 'playlist.txt'
file = open(filename, "r")
playlist = list()
for line in file:
	playlist.append(str(line[:-1]))
print playlist

class LogHandler(object):
	def debug(self, msg):
		pass

	def warning(self, msg):
		pass

	def error(self, msg):
		print(msg)

def hook(d):
	if d['status'] == 'finished':
		print('\nDone downloading, now converting ...')

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
	'logger': LogHandler(),
	'progress_hooks': [hook],
	'outtmpl': '%(title)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for song in playlist:
		ydl.download([song])