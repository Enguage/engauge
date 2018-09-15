# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = index_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
from uuid import UUID
import dateutil.parser


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


class Social:
    liked_by_user: bool
    likes: int
    views: int

    def __init__(self, liked_by_user: bool, likes: int, views: int) -> None:
        self.liked_by_user = liked_by_user
        self.likes = likes
        self.views = views

    @staticmethod
    def from_dict(obj: Any) -> 'Social':
        assert isinstance(obj, dict)
        liked_by_user = from_bool(obj.get("likedByUser"))
        likes = from_int(obj.get("likes"))
        views = from_int(obj.get("views"))
        return Social(liked_by_user, likes, views)

    def to_dict(self) -> dict:
        result: dict = {}
        result["likedByUser"] = from_bool(self.liked_by_user)
        result["likes"] = from_int(self.likes)
        result["views"] = from_int(self.views)
        return result


class Duration:
    time: datetime
    seconds: int

    def __init__(self, time: datetime, seconds: int) -> None:
        self.time = time
        self.seconds = seconds

    @staticmethod
    def from_dict(obj: Any) -> 'Duration':
        assert isinstance(obj, dict)
        time = from_datetime(obj.get("time"))
        seconds = from_int(obj.get("seconds"))
        return Duration(time, seconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = self.time.isoformat()
        result["seconds"] = from_int(self.seconds)
        return result


class Appearance:
    start_time: datetime
    end_time: datetime
    start_seconds: int
    end_seconds: int

    def __init__(self, start_time: datetime, end_time: datetime, start_seconds: int, end_seconds: int) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.start_seconds = start_seconds
        self.end_seconds = end_seconds

    @staticmethod
    def from_dict(obj: Any) -> 'Appearance':
        assert isinstance(obj, dict)
        start_time = from_datetime(obj.get("startTime"))
        end_time = from_datetime(obj.get("endTime"))
        start_seconds = from_int(obj.get("startSeconds"))
        end_seconds = from_int(obj.get("endSeconds"))
        return Appearance(start_time, end_time, start_seconds, end_seconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["startTime"] = self.start_time.isoformat()
        result["endTime"] = self.end_time.isoformat()
        result["startSeconds"] = from_int(self.start_seconds)
        result["endSeconds"] = from_int(self.end_seconds)
        return result


class SummarizedInsightsSentiment:
    sentiment_key: str
    appearances: List[Appearance]
    seen_duration_ratio: int

    def __init__(self, sentiment_key: str, appearances: List[Appearance], seen_duration_ratio: int) -> None:
        self.sentiment_key = sentiment_key
        self.appearances = appearances
        self.seen_duration_ratio = seen_duration_ratio

    @staticmethod
    def from_dict(obj: Any) -> 'SummarizedInsightsSentiment':
        assert isinstance(obj, dict)
        sentiment_key = from_str(obj.get("sentimentKey"))
        appearances = from_list(Appearance.from_dict, obj.get("appearances"))
        seen_duration_ratio = from_int(obj.get("seenDurationRatio"))
        return SummarizedInsightsSentiment(sentiment_key, appearances, seen_duration_ratio)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sentimentKey"] = from_str(self.sentiment_key)
        result["appearances"] = from_list(lambda x: to_class(Appearance, x), self.appearances)
        result["seenDurationRatio"] = from_int(self.seen_duration_ratio)
        return result


class Speaker:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Speaker':
        assert isinstance(obj, dict)
        return Speaker()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class Statistics:
    correspondence_count: int
    speaker_talk_to_listen_ratio: Speaker
    speaker_longest_monolog: Speaker
    speaker_number_of_fragments: Speaker
    speaker_word_count: Speaker

    def __init__(self, correspondence_count: int, speaker_talk_to_listen_ratio: Speaker, speaker_longest_monolog: Speaker, speaker_number_of_fragments: Speaker, speaker_word_count: Speaker) -> None:
        self.correspondence_count = correspondence_count
        self.speaker_talk_to_listen_ratio = speaker_talk_to_listen_ratio
        self.speaker_longest_monolog = speaker_longest_monolog
        self.speaker_number_of_fragments = speaker_number_of_fragments
        self.speaker_word_count = speaker_word_count

    @staticmethod
    def from_dict(obj: Any) -> 'Statistics':
        assert isinstance(obj, dict)
        correspondence_count = from_int(obj.get("correspondenceCount"))
        speaker_talk_to_listen_ratio = Speaker.from_dict(obj.get("speakerTalkToListenRatio"))
        speaker_longest_monolog = Speaker.from_dict(obj.get("speakerLongestMonolog"))
        speaker_number_of_fragments = Speaker.from_dict(obj.get("speakerNumberOfFragments"))
        speaker_word_count = Speaker.from_dict(obj.get("speakerWordCount"))
        return Statistics(correspondence_count, speaker_talk_to_listen_ratio, speaker_longest_monolog, speaker_number_of_fragments, speaker_word_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["correspondenceCount"] = from_int(self.correspondence_count)
        result["speakerTalkToListenRatio"] = to_class(Speaker, self.speaker_talk_to_listen_ratio)
        result["speakerLongestMonolog"] = to_class(Speaker, self.speaker_longest_monolog)
        result["speakerNumberOfFragments"] = to_class(Speaker, self.speaker_number_of_fragments)
        result["speakerWordCount"] = to_class(Speaker, self.speaker_word_count)
        return result


class SummarizedInsights:
    name: str
    id: str
    privacy_mode: str
    duration: Duration
    thumbnail_video_id: str
    thumbnail_id: UUID
    faces: List[Any]
    keywords: List[Any]
    sentiments: List[SummarizedInsightsSentiment]
    audio_effects: List[Any]
    labels: List[Any]
    brands: List[Any]
    statistics: Statistics

    def __init__(self, name: str, id: str, privacy_mode: str, duration: Duration, thumbnail_video_id: str, thumbnail_id: UUID, faces: List[Any], keywords: List[Any], sentiments: List[SummarizedInsightsSentiment], audio_effects: List[Any], labels: List[Any], brands: List[Any], statistics: Statistics) -> None:
        self.name = name
        self.id = id
        self.privacy_mode = privacy_mode
        self.duration = duration
        self.thumbnail_video_id = thumbnail_video_id
        self.thumbnail_id = thumbnail_id
        self.faces = faces
        self.keywords = keywords
        self.sentiments = sentiments
        self.audio_effects = audio_effects
        self.labels = labels
        self.brands = brands
        self.statistics = statistics

    @staticmethod
    def from_dict(obj: Any) -> 'SummarizedInsights':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        id = from_str(obj.get("id"))
        privacy_mode = from_str(obj.get("privacyMode"))
        duration = Duration.from_dict(obj.get("duration"))
        thumbnail_video_id = from_str(obj.get("thumbnailVideoId"))
        thumbnail_id = UUID(obj.get("thumbnailId"))
        faces = from_list(lambda x: x, obj.get("faces"))
        keywords = from_list(lambda x: x, obj.get("Keywords"))
        sentiments = from_list(SummarizedInsightsSentiment.from_dict, obj.get("sentiments"))
        audio_effects = from_list(lambda x: x, obj.get("audioEffects"))
        labels = from_list(lambda x: x, obj.get("labels"))
        brands = from_list(lambda x: x, obj.get("brands"))
        statistics = Statistics.from_dict(obj.get("statistics"))
        return SummarizedInsights(name, id, privacy_mode, duration, thumbnail_video_id, thumbnail_id, faces, keywords, sentiments, audio_effects, labels, brands, statistics)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["id"] = from_str(self.id)
        result["privacyMode"] = from_str(self.privacy_mode)
        result["duration"] = to_class(Duration, self.duration)
        result["thumbnailVideoId"] = from_str(self.thumbnail_video_id)
        result["thumbnailId"] = str(self.thumbnail_id)
        result["faces"] = from_list(lambda x: x, self.faces)
        result["Keywords"] = from_list(lambda x: x, self.keywords)
        result["sentiments"] = from_list(lambda x: to_class(SummarizedInsightsSentiment, x), self.sentiments)
        result["audioEffects"] = from_list(lambda x: x, self.audio_effects)
        result["labels"] = from_list(lambda x: x, self.labels)
        result["brands"] = from_list(lambda x: x, self.brands)
        result["statistics"] = to_class(Statistics, self.statistics)
        return result


class Instance:
    adjusted_start: datetime
    adjusted_end: datetime
    start: datetime
    end: datetime

    def __init__(self, adjusted_start: datetime, adjusted_end: datetime, start: datetime, end: datetime) -> None:
        self.adjusted_start = adjusted_start
        self.adjusted_end = adjusted_end
        self.start = start
        self.end = end

    @staticmethod
    def from_dict(obj: Any) -> 'Instance':
        assert isinstance(obj, dict)
        adjusted_start = from_datetime(obj.get("adjustedStart"))
        adjusted_end = from_datetime(obj.get("adjustedEnd"))
        start = from_datetime(obj.get("start"))
        end = from_datetime(obj.get("end"))
        return Instance(adjusted_start, adjusted_end, start, end)

    def to_dict(self) -> dict:
        result: dict = {}
        result["adjustedStart"] = self.adjusted_start.isoformat()
        result["adjustedEnd"] = self.adjusted_end.isoformat()
        result["start"] = self.start.isoformat()
        result["end"] = self.end.isoformat()
        return result


class Block:
    id: int
    instances: List[Instance]

    def __init__(self, id: int, instances: List[Instance]) -> None:
        self.id = id
        self.instances = instances

    @staticmethod
    def from_dict(obj: Any) -> 'Block':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        instances = from_list(Instance.from_dict, obj.get("instances"))
        return Block(id, instances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["instances"] = from_list(lambda x: to_class(Instance, x), self.instances)
        return result


class InsightsSentiment:
    id: int
    score: int
    sentiment_type: int
    instances: List[Instance]

    def __init__(self, id: int, score: int, sentiment_type: int, instances: List[Instance]) -> None:
        self.id = id
        self.score = score
        self.sentiment_type = sentiment_type
        self.instances = instances

    @staticmethod
    def from_dict(obj: Any) -> 'InsightsSentiment':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        score = from_int(obj.get("score"))
        sentiment_type = from_int(obj.get("sentimentType"))
        instances = from_list(Instance.from_dict, obj.get("instances"))
        return InsightsSentiment(id, score, sentiment_type, instances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["score"] = from_int(self.score)
        result["sentimentType"] = from_int(self.sentiment_type)
        result["instances"] = from_list(lambda x: to_class(Instance, x), self.instances)
        return result


class Transcript:
    id: int
    text: str
    confidence: int
    speaker_id: int
    language: str
    instances: List[Instance]

    def __init__(self, id: int, text: str, confidence: int, speaker_id: int, language: str, instances: List[Instance]) -> None:
        self.id = id
        self.text = text
        self.confidence = confidence
        self.speaker_id = speaker_id
        self.language = language
        self.instances = instances

    @staticmethod
    def from_dict(obj: Any) -> 'Transcript':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        text = from_str(obj.get("text"))
        confidence = from_int(obj.get("confidence"))
        speaker_id = from_int(obj.get("speakerId"))
        language = from_str(obj.get("language"))
        instances = from_list(Instance.from_dict, obj.get("instances"))
        return Transcript(id, text, confidence, speaker_id, language, instances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["text"] = from_str(self.text)
        result["confidence"] = from_int(self.confidence)
        result["speakerId"] = from_int(self.speaker_id)
        result["language"] = from_str(self.language)
        result["instances"] = from_list(lambda x: to_class(Instance, x), self.instances)
        return result


class Insights:
    version: str
    source_language: str
    language: str
    transcript: List[Transcript]
    sentiments: List[InsightsSentiment]
    blocks: List[Block]

    def __init__(self, version: str, source_language: str, language: str, transcript: List[Transcript], sentiments: List[InsightsSentiment], blocks: List[Block]) -> None:
        self.version = version
        self.source_language = source_language
        self.language = language
        self.transcript = transcript
        self.sentiments = sentiments
        self.blocks = blocks

    @staticmethod
    def from_dict(obj: Any) -> 'Insights':
        assert isinstance(obj, dict)
        version = from_str(obj.get("version"))
        source_language = from_str(obj.get("sourceLanguage"))
        language = from_str(obj.get("language"))
        transcript = from_list(Transcript.from_dict, obj.get("transcript"))
        sentiments = from_list(InsightsSentiment.from_dict, obj.get("sentiments"))
        blocks = from_list(Block.from_dict, obj.get("blocks"))
        return Insights(version, source_language, language, transcript, sentiments, blocks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["version"] = from_str(self.version)
        result["sourceLanguage"] = from_str(self.source_language)
        result["language"] = from_str(self.language)
        result["transcript"] = from_list(lambda x: to_class(Transcript, x), self.transcript)
        result["sentiments"] = from_list(lambda x: to_class(InsightsSentiment, x), self.sentiments)
        result["blocks"] = from_list(lambda x: to_class(Block, x), self.blocks)
        return result


class Video:
    account_id: str
    id: str
    state: str
    privacy_mode: str
    processing_progress: str
    failure_code: str
    failure_message: str
    external_id: None
    external_url: None
    metadata: None
    insights: Insights
    thumbnail_id: UUID
    published_url: str
    published_proxy_url: None
    view_token: str
    source_language: str
    language: str
    indexing_preset: str
    linguistic_model_id: UUID

    def __init__(self, account_id: str, id: str, state: str, privacy_mode: str, processing_progress: str, failure_code: str, failure_message: str, external_id: None, external_url: None, metadata: None, insights: Insights, thumbnail_id: UUID, published_url: str, published_proxy_url: None, view_token: str, source_language: str, language: str, indexing_preset: str, linguistic_model_id: UUID) -> None:
        self.account_id = account_id
        self.id = id
        self.state = state
        self.privacy_mode = privacy_mode
        self.processing_progress = processing_progress
        self.failure_code = failure_code
        self.failure_message = failure_message
        self.external_id = external_id
        self.external_url = external_url
        self.metadata = metadata
        self.insights = insights
        self.thumbnail_id = thumbnail_id
        self.published_url = published_url
        self.published_proxy_url = published_proxy_url
        self.view_token = view_token
        self.source_language = source_language
        self.language = language
        self.indexing_preset = indexing_preset
        self.linguistic_model_id = linguistic_model_id

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        account_id = from_str(obj.get("accountId"))
        id = from_str(obj.get("id"))
        state = from_str(obj.get("state"))
        privacy_mode = from_str(obj.get("privacyMode"))
        processing_progress = from_str(obj.get("processingProgress"))
        failure_code = from_str(obj.get("failureCode"))
        failure_message = from_str(obj.get("failureMessage"))
        external_id = from_none(obj.get("externalId"))
        external_url = from_none(obj.get("externalUrl"))
        metadata = from_none(obj.get("metadata"))
        insights = Insights.from_dict(obj.get("insights"))
        thumbnail_id = UUID(obj.get("thumbnailId"))
        published_url = from_str(obj.get("publishedUrl"))
        published_proxy_url = from_none(obj.get("publishedProxyUrl"))
        view_token = from_str(obj.get("viewToken"))
        source_language = from_str(obj.get("sourceLanguage"))
        language = from_str(obj.get("language"))
        indexing_preset = from_str(obj.get("indexingPreset"))
        linguistic_model_id = UUID(obj.get("linguisticModelId"))
        return Video(account_id, id, state, privacy_mode, processing_progress, failure_code, failure_message, external_id, external_url, metadata, insights, thumbnail_id, published_url, published_proxy_url, view_token, source_language, language, indexing_preset, linguistic_model_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accountId"] = from_str(self.account_id)
        result["id"] = from_str(self.id)
        result["state"] = from_str(self.state)
        result["privacyMode"] = from_str(self.privacy_mode)
        result["processingProgress"] = from_str(self.processing_progress)
        result["failureCode"] = from_str(self.failure_code)
        result["failureMessage"] = from_str(self.failure_message)
        result["externalId"] = from_none(self.external_id)
        result["externalUrl"] = from_none(self.external_url)
        result["metadata"] = from_none(self.metadata)
        result["insights"] = to_class(Insights, self.insights)
        result["thumbnailId"] = str(self.thumbnail_id)
        result["publishedUrl"] = from_str(self.published_url)
        result["publishedProxyUrl"] = from_none(self.published_proxy_url)
        result["viewToken"] = from_str(self.view_token)
        result["sourceLanguage"] = from_str(self.source_language)
        result["language"] = from_str(self.language)
        result["indexingPreset"] = from_str(self.indexing_preset)
        result["linguisticModelId"] = str(self.linguistic_model_id)
        return result


class Index:
    account_id: str
    id: str
    name: str
    description: None
    user_name: str
    created: datetime
    privacy_mode: str
    state: str
    is_owned: bool
    is_editable: bool
    is_base: bool
    duration_in_seconds: int
    summarized_insights: SummarizedInsights
    videos: List[Video]
    videos_ranges: None
    social: Social

    def __init__(self, account_id: str, id: str, name: str, description: None, user_name: str, created: datetime, privacy_mode: str, state: str, is_owned: bool, is_editable: bool, is_base: bool, duration_in_seconds: int, summarized_insights: SummarizedInsights, videos: List[Video], videos_ranges: None, social: Social) -> None:
        self.account_id = account_id
        self.id = id
        self.name = name
        self.description = description
        self.user_name = user_name
        self.created = created
        self.privacy_mode = privacy_mode
        self.state = state
        self.is_owned = is_owned
        self.is_editable = is_editable
        self.is_base = is_base
        self.duration_in_seconds = duration_in_seconds
        self.summarized_insights = summarized_insights
        self.videos = videos
        self.videos_ranges = videos_ranges
        self.social = social

    @staticmethod
    def from_dict(obj: Any) -> 'Index':
        assert isinstance(obj, dict)
        account_id = from_str(obj.get("accountId"))
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        description = from_none(obj.get("description"))
        user_name = from_str(obj.get("userName"))
        created = from_datetime(obj.get("created"))
        privacy_mode = from_str(obj.get("privacyMode"))
        state = from_str(obj.get("state"))
        is_owned = from_bool(obj.get("isOwned"))
        is_editable = from_bool(obj.get("isEditable"))
        is_base = from_bool(obj.get("isBase"))
        duration_in_seconds = from_int(obj.get("durationInSeconds"))
        summarized_insights = SummarizedInsights.from_dict(obj.get("summarizedInsights"))
        videos = from_list(Video.from_dict, obj.get("videos"))
        videos_ranges = from_none(obj.get("videosRanges"))
        social = Social.from_dict(obj.get("social"))
        return Index(account_id, id, name, description, user_name, created, privacy_mode, state, is_owned, is_editable, is_base, duration_in_seconds, summarized_insights, videos, videos_ranges, social)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accountId"] = from_str(self.account_id)
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["description"] = from_none(self.description)
        result["userName"] = from_str(self.user_name)
        result["created"] = self.created.isoformat()
        result["privacyMode"] = from_str(self.privacy_mode)
        result["state"] = from_str(self.state)
        result["isOwned"] = from_bool(self.is_owned)
        result["isEditable"] = from_bool(self.is_editable)
        result["isBase"] = from_bool(self.is_base)
        result["durationInSeconds"] = from_int(self.duration_in_seconds)
        result["summarizedInsights"] = to_class(SummarizedInsights, self.summarized_insights)
        result["videos"] = from_list(lambda x: to_class(Video, x), self.videos)
        result["videosRanges"] = from_none(self.videos_ranges)
        result["social"] = to_class(Social, self.social)
        return result


def index_from_dict(s: Any) -> Index:
    return Index.from_dict(s)


def index_to_dict(x: Index) -> Any:
    return to_class(Index, x)
