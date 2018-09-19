# engauge
engauge is a project created at HACKMIT 2018. This program was inspired by our ongoing college experiences with our professors' lectures. Sometimes, lectures can inspire students but other times, they can really drown our energy. We created engauge as way for lecturers and public speakers in general to track crowd engagement so that they are able to learn from their own past speeches and find ways to improve their future ones.

# How it is created
The program is written in Python and supported with Microsoft Azure's Video Indexer and Face API's. The Video Indexer API was able to "index" through the whole video and do speech-to-text processing. It gave a fairly good translation of the test video we provided the program. It was then able to pinpoint the faces in the video inputed and track each persons emotions (positive, neutral, or negative). The video indexer API was not able to give exact emotions associated to each person in the video. That is where the FACE API cam into play. I had to manually cut the video into seperate frames using OpenCV and save each frame (~2000+ frames total) to a local folder called "frames". From that I called the CF.face.detect() on each jpg image.

# Other resources used
- Primary test video used at HACKMIT: https://www.youtube.com/watch?v=tiicx0d7yBg

# Milestones to be accomplished
- Refactor all code for cleanliness
- Set up a database to store each uploaded videos' frames
- Provide cleaner website UI
- Provide ways the lecturer can take the data and use it to benefit future lectures (output the buzz words, trim out the parts of the video fo playback, etc)
