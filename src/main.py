from googleapiclient.discovery import build

def playlist_video_links(playlistId):
	nextPageToken=None
	youtube = build('youtube','v3',developerKey='Enter API Key')
	while True:
		pl_request = youtube.playlistItems().list(
			part='snippet',
			playlistId=playlistId,
			maxResults=50,
			pageToken=nextPageToken
			)
		pl_response = pl_request.execute()
		for item in pl_response['items']:
			thumbnails = item['snippet']['thumbnails']
			if 'default' in thumbnails:
				default = thumbnails['default']
				print(default)
			if 'high' in thumbnails:
				high = thumbnails['high']
				print(high)
			if 'maxres' in thumbnails:
				maxres = thumbnails['maxres']
				print(maxres)
			if 'medium' in thumbnails:
				medium = thumbnails['medium']
				print(medium)
			if 'standard' in thumbnails:
				standard = thumbnails['standard']
				print(standard)
			print("\n")
		nextPageToken = pl_response.get('nextPageToken')
		if not nextPageToken:
			break
playlist_video_links('PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau')
