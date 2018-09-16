import VideoAnalyzer as va
import DataAnalyzer as da

# STEP 1: Set video information as necessary.
data = va.getVideoData()

# STEP 2: Get the information and timestamps for the keywords
keywords = da.getKeywords(data)


print(keywords)
