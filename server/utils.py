import pafy
import os

YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')

if YOUTUBE_API_KEY is not None:
    pafy.set_api_key(YOUTUBE_API_KEY)

def download_video(video_id):
    try:
        video = pafy.new(video_id)

    except ValueError:
        error = {
            "error": "Invalid video_id parameter"
        }
        return error

    except Exception as e:
        if "This video is unavailable." in str(e):
            error = {
                "error": "Video not found"
            }
            return error
        else:
            error = {
                "error": "An unknown error has occurred"
            }
            return error

    videos = []
    audios = []
    normals = []
    all_streams = []

    for stream in video.allstreams:

        if stream.url.startswith("https://manifest.googlevideo.com"):
            continue

        if stream.mediatype == "audio":
            streamDict = {
                "url": stream.url,
                "extension": stream.extension,
                "mediatype": f"{stream.mediatype} only", # ex. audio only
                "quality": f"{stream.bitrate}bps" #ex. 128kbps
            }
            audios.append(streamDict)

        elif stream.mediatype == "video":
            streamDict = {
                "url": stream.url,
                "extension": stream.extension,
                "mediatype": f"{stream.mediatype} only", # ex. video only
                "quality": stream.resolution
            }
            videos.append(streamDict)
        else:
            streamDict = {
                "url": stream.url,
                "extension": stream.extension,
                "mediatype": stream.mediatype,
                "quality": stream.resolution
            }
            normals.append(streamDict)

    all_streams.append(normals)
    all_streams.append(audios)
    all_streams.append(videos)

    return all_streams

def info_video(video_id):
    try:
        video = pafy.new(video_id)

    except ValueError:
        error = {
            "error": "Invalid video_id parameter"
        }
        return error

    except Exception as e:
        if "This video is unavailable." in str(e):
            error = {
                "error": "Video not found"
            }
            return error
        else:
            error = {
                "error": "An unknown error has occurred"
            }
            return error

    infoDict = {
        "title" : video.title,
        "duration" : video.duration,
        "author" : video.author,
        "viewcount" : video.viewcount,
        "likes" : video.likes,
        "dislikes" : video.dislikes,
        "description": video.description    
    }

    return infoDict