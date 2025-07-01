This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.
The content has been processed where security check has been disabled.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: docs/*
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Security check has been disabled - content may contain sensitive information
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
docs/
  AbridgedVideoView.md
  Asset.md
  AssetErrors.md
  AssetGeneratedSubtitleSettings.md
  AssetMaster.md
  AssetMetadata.md
  AssetNonStandardInputReasons.md
  AssetRecordingTimes.md
  AssetResponse.md
  AssetsApi.md
  AssetStaticRenditions.md
  BreakdownValue.md
  CreateAssetRequest.md
  CreateLiveStreamRequest.md
  CreatePlaybackIDRequest.md
  CreatePlaybackIDResponse.md
  CreatePlaybackRestrictionRequest.md
  CreateSimulcastTargetRequest.md
  CreateStaticRenditionRequest.md
  CreateStaticRenditionResponse.md
  CreateTrackRequest.md
  CreateTrackResponse.md
  CreateTranscriptionVocabularyRequest.md
  CreateUploadRequest.md
  CreateWebInputRequest.md
  DeliveryReport.md
  DeliveryReportDeliveredSecondsByResolution.md
  DeliveryUsageApi.md
  DimensionsApi.md
  DimensionValue.md
  DirectUploadsApi.md
  DisableLiveStreamResponse.md
  DRMConfiguration.md
  DRMConfigurationResponse.md
  DRMConfigurationsApi.md
  EnableLiveStreamResponse.md
  Error.md
  ErrorsApi.md
  ExportDate.md
  ExportFile.md
  ExportsApi.md
  FiltersApi.md
  FilterValue.md
  GenerateTrackSubtitlesRequest.md
  GenerateTrackSubtitlesResponse.md
  GetAssetInputInfoResponse.md
  GetAssetOrLiveStreamIdResponse.md
  GetAssetOrLiveStreamIdResponseData.md
  GetAssetOrLiveStreamIdResponseDataObject.md
  GetAssetPlaybackIDResponse.md
  GetLiveStreamPlaybackIDResponse.md
  GetMetricTimeseriesDataResponse.md
  GetMonitoringBreakdownResponse.md
  GetMonitoringBreakdownTimeseriesResponse.md
  GetMonitoringHistogramTimeseriesResponse.md
  GetMonitoringHistogramTimeseriesResponseMeta.md
  GetMonitoringTimeseriesResponse.md
  GetOverallValuesResponse.md
  GetRealTimeBreakdownResponse.md
  GetRealTimeHistogramTimeseriesResponse.md
  GetRealTimeHistogramTimeseriesResponseMeta.md
  GetRealTimeTimeseriesResponse.md
  Incident.md
  IncidentBreakdown.md
  IncidentNotification.md
  IncidentNotificationRule.md
  IncidentResponse.md
  IncidentsApi.md
  InputFile.md
  InputInfo.md
  InputSettings.md
  InputSettingsOverlaySettings.md
  InputTrack.md
  Insight.md
  LaunchWebInputResponse.md
  ListAllMetricValuesResponse.md
  ListAssetsResponse.md
  ListBreakdownValuesResponse.md
  ListBreakdownValuesResponseMeta.md
  ListDeliveryUsageResponse.md
  ListDimensionsResponse.md
  ListDimensionValuesResponse.md
  ListDRMConfigurationsResponse.md
  ListErrorsResponse.md
  ListExportsResponse.md
  ListFiltersResponse.md
  ListFiltersResponseData.md
  ListFilterValuesResponse.md
  ListIncidentsResponse.md
  ListInsightsResponse.md
  ListLiveStreamsResponse.md
  ListMonitoringDimensionsResponse.md
  ListMonitoringDimensionsResponseData.md
  ListMonitoringMetricsResponse.md
  ListPlaybackRestrictionsResponse.md
  ListRealTimeDimensionsResponse.md
  ListRealTimeMetricsResponse.md
  ListRelatedIncidentsResponse.md
  ListSigningKeysResponse.md
  ListTranscriptionVocabulariesResponse.md
  ListUploadsResponse.md
  ListVideoViewExportsResponse.md
  ListVideoViewsResponse.md
  ListWebInputsResponse.md
  LiveStream.md
  LiveStreamEmbeddedSubtitleSettings.md
  LiveStreamGeneratedSubtitleSettings.md
  LiveStreamResponse.md
  LiveStreamsApi.md
  LiveStreamStatus.md
  Metric.md
  MetricsApi.md
  MonitoringApi.md
  MonitoringBreakdownTimeseriesDatapoint.md
  MonitoringBreakdownTimeseriesValues.md
  MonitoringBreakdownValue.md
  MonitoringHistogramTimeseriesBucket.md
  MonitoringHistogramTimeseriesBucketValues.md
  MonitoringHistogramTimeseriesDatapoint.md
  MonitoringTimeseriesDatapoint.md
  NotificationRule.md
  OverallValues.md
  PlaybackID.md
  PlaybackIDApi.md
  PlaybackPolicy.md
  PlaybackRestriction.md
  PlaybackRestrictionResponse.md
  PlaybackRestrictionsApi.md
  RealTimeApi.md
  RealTimeBreakdownValue.md
  RealTimeHistogramTimeseriesBucket.md
  RealTimeHistogramTimeseriesBucketValues.md
  RealTimeHistogramTimeseriesDatapoint.md
  RealTimeTimeseriesDatapoint.md
  ReferrerDomainRestriction.md
  ReloadWebInputResponse.md
  Score.md
  ShutdownWebInputResponse.md
  SignalLiveStreamCompleteResponse.md
  SigningKey.md
  SigningKeyResponse.md
  SigningKeysApi.md
  SimulcastTarget.md
  SimulcastTargetResponse.md
  StaticRendition.md
  Track.md
  TranscriptionVocabulariesApi.md
  TranscriptionVocabulary.md
  TranscriptionVocabularyResponse.md
  UpdateAssetMasterAccessRequest.md
  UpdateAssetMP4SupportRequest.md
  UpdateAssetRequest.md
  UpdateLiveStreamEmbeddedSubtitlesRequest.md
  UpdateLiveStreamGeneratedSubtitlesRequest.md
  UpdateLiveStreamNewAssetSettings.md
  UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest.md
  UpdateLiveStreamRequest.md
  UpdateReferrerDomainRestrictionRequest.md
  UpdateTranscriptionVocabularyRequest.md
  UpdateUserAgentRestrictionRequest.md
  UpdateWebInputUrlRequest.md
  Upload.md
  UploadError.md
  UploadResponse.md
  URLSigningKeysApi.md
  UserAgentRestrictionRequest.md
  UserAgentRestrictionSettings.md
  VideoView.md
  VideoViewEvent.md
  VideoViewResponse.md
  VideoViewsApi.md
  WebInput.md
  WebInputResponse.md
  WebInputsApi.md
```

# Files

## File: docs/AbridgedVideoView.md
````markdown
# AbridgedVideoView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**viewer_os_family** | **str** |  | [optional]
**viewer_application_name** | **str** |  | [optional]
**video_title** | **str** |  | [optional]
**total_row_count** | **int** |  | [optional]
**player_error_message** | **str** |  | [optional]
**player_error_code** | **str** |  | [optional]
**error_type_id** | **int** |  | [optional]
**country_code** | **str** |  | [optional]
**view_start** | **str** |  | [optional]
**view_end** | **str** |  | [optional]
**viewer_experience_score** | **float** |  | [optional]
**watch_time** | **int** |  | [optional]
**playback_failure** | **bool** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Asset.md
````markdown
# Asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Asset. Max 255 characters. | [optional]
**created_at** | **str** | Time the Asset was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**status** | **str** | The status of the asset. | [optional]
**duration** | **float** | The duration of the asset in seconds (max duration for a single asset is 12 hours). | [optional]
**max_stored_resolution** | **str** | This field is deprecated. Please use &#x60;resolution_tier&#x60; instead. The maximum resolution that has been stored for the asset. The asset may be delivered at lower resolutions depending on the device and bandwidth, however it cannot be delivered at a higher value than is stored. | [optional]
**resolution_tier** | **str** | The resolution tier that the asset was ingested at, affecting billing for ingest &amp; storage. This field also represents the highest resolution tier that the content can be delivered at, however the actual resolution may be lower depending on the device, bandwidth, and exact resolution of the uploaded asset. | [optional]
**max_resolution_tier** | **str** | Max resolution tier can be used to control the maximum &#x60;resolution_tier&#x60; your asset is encoded, stored, and streamed at. If not set, this defaults to &#x60;1080p&#x60;. | [optional]
**encoding_tier** | **str** | This field is deprecated. Please use &#x60;video_quality&#x60; instead. The encoding tier informs the cost, quality, and available platform features for the asset. The default encoding tier for an account can be set in the Mux Dashboard. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**video_quality** | **str** | The video quality controls the cost, quality, and available platform features for the asset. The default video quality for an account can be set in the Mux Dashboard. This field replaces the deprecated &#x60;encoding_tier&#x60; value. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**max_stored_frame_rate** | **float** | The maximum frame rate that has been stored for the asset. The asset may be delivered at lower frame rates depending on the device and bandwidth, however it cannot be delivered at a higher value than is stored. This field may return -1 if the frame rate of the input cannot be reliably determined. | [optional]
**aspect_ratio** | **str** | The aspect ratio of the asset in the form of &#x60;width:height&#x60;, for example &#x60;16:9&#x60;. | [optional]
**playback_ids** | [**list[PlaybackID]**](PlaybackID.md) | An array of Playback ID objects. Use these to create HLS playback URLs. See [Play your videos](https://docs.mux.com/guides/play-your-videos) for more details. | [optional]
**tracks** | [**list[Track]**](Track.md) | The individual media tracks that make up an asset. | [optional]
**errors** | [**AssetErrors**](AssetErrors.md) |  | [optional]
**per_title_encode** | **bool** |  | [optional]
**upload_id** | **str** | Unique identifier for the Direct Upload. This is an optional parameter added when the asset is created from a direct upload. | [optional]
**is_live** | **bool** | Indicates whether the live stream that created this asset is currently &#x60;active&#x60; and not in &#x60;idle&#x60; state. This is an optional parameter added when the asset is created from a live stream. | [optional]
**passthrough** | **str** | You can set this field to anything you want. It will be included in the asset details and related webhooks. If you&#39;re looking for more structured metadata, such as &#x60;title&#x60; or &#x60;external_id&#x60; , you can use the &#x60;meta&#x60; object instead. **Max: 255 characters**. | [optional]
**live_stream_id** | **str** | Unique identifier for the live stream. This is an optional parameter added when the asset is created from a live stream. | [optional]
**master** | [**AssetMaster**](AssetMaster.md) |  | [optional]
**master_access** | **str** |  | [optional] [default to 'none']
**mp4_support** | **str** |  | [optional] [default to 'none']
**source_asset_id** | **str** | Asset Identifier of the video used as the source for creating the clip. | [optional]
**normalize_audio** | **bool** | Normalize the audio track loudness level. This parameter is only applicable to on-demand (not live) assets. | [optional] [default to False]
**static_renditions** | [**AssetStaticRenditions**](AssetStaticRenditions.md) |  | [optional]
**recording_times** | [**list[AssetRecordingTimes]**](AssetRecordingTimes.md) | An array of individual live stream recording sessions. A recording session is created on each encoder connection during the live stream. Additionally any time slate media is inserted during brief interruptions in the live stream media or times when the live streaming software disconnects, a recording session representing the slate media will be added with a \&quot;slate\&quot; type. | [optional]
**non_standard_input_reasons** | [**AssetNonStandardInputReasons**](AssetNonStandardInputReasons.md) |  | [optional]
**test** | **bool** | True means this live stream is a test asset. A test asset can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test assets created. Test assets are watermarked with the Mux logo, limited to 10 seconds, and deleted after 24 hrs. | [optional]
**ingest_type** | **str** | The type of ingest used to create the asset. | [optional]
**meta** | [**AssetMetadata**](AssetMetadata.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetErrors.md
````markdown
# AssetErrors

Object that describes any errors that happened when processing this asset.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of error that occurred for this asset. | [optional]
**messages** | **list[str]** | Error messages with more details. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetGeneratedSubtitleSettings.md
````markdown
# AssetGeneratedSubtitleSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for this subtitle track. | [optional]
**passthrough** | **str** | Arbitrary metadata set for the subtitle track. Max 255 characters. | [optional]
**language_code** | **str** | The language to generate subtitles in. | [optional] [default to 'en']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetMaster.md
````markdown
# AssetMaster

An object containing the current status of Master Access and the link to the Master MP4 file when ready. This object does not exist if `master_access` is set to `none` and when the temporary URL expires.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional]
**url** | **str** | The temporary URL to the master version of the video, as an MP4 file. This URL will expire after 24 hours. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetMetadata.md
````markdown
# AssetMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The asset title. Max 512 code points. | [optional]
**creator_id** | **str** | This is an identifier you provide to keep track of the creator of the asset. Max 128 code points. | [optional]
**external_id** | **str** | This is an identifier you provide to link the asset to your own data. Max 128 code points. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetNonStandardInputReasons.md
````markdown
# AssetNonStandardInputReasons

An object containing one or more reasons the input file is non-standard. See [the guide on minimizing processing time](https://docs.mux.com/guides/minimize-processing-time) for more information on what a standard input is defined as. This object only exists on on-demand assets that have non-standard inputs, so if missing you can assume the input qualifies as standard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_codec** | **str** | The video codec used on the input file. For example, the input file encoded with &#x60;hevc&#x60; video codec is non-standard and the value of this parameter is &#x60;hevc&#x60;. | [optional]
**audio_codec** | **str** | The audio codec used on the input file. Non-AAC audio codecs are non-standard. | [optional]
**video_gop_size** | **str** | The video key frame Interval (also called as Group of Picture or GOP) of the input file is &#x60;high&#x60;. This parameter is present when the gop is greater than 20 seconds. | [optional]
**video_frame_rate** | **str** | The video frame rate of the input file. Video with average frames per second (fps) less than 5 or greater than 120 is non-standard. A &#x60;-1&#x60; frame rate value indicates Mux could not determine the frame rate of the video track. | [optional]
**video_resolution** | **str** | The video resolution of the input file. Video resolution higher than 2048 pixels on any one dimension (height or width) is considered non-standard, The resolution value is presented as &#x60;width&#x60; x &#x60;height&#x60; in pixels. | [optional]
**video_bitrate** | **str** | The video bitrate of the input file is &#x60;high&#x60;. This parameter is present when the average bitrate of any key frame interval (also known as Group of Pictures or GOP) is higher than what&#39;s considered standard which typically is 16 Mbps. | [optional]
**pixel_aspect_ratio** | **str** | The video pixel aspect ratio of the input file. | [optional]
**video_edit_list** | **str** | Video Edit List reason indicates that the input file&#39;s video track contains a complex Edit Decision List. | [optional]
**audio_edit_list** | **str** | Audio Edit List reason indicates that the input file&#39;s audio track contains a complex Edit Decision List. | [optional]
**unexpected_media_file_parameters** | **str** | A catch-all reason when the input file in created with non-standard encoding parameters. | [optional]
**unsupported_pixel_format** | **str** | The video pixel format, as a string, returned by libav. Considered non-standard if not one of yuv420p or yuvj420p. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetRecordingTimes.md
````markdown
# AssetRecordingTimes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **datetime** | The time at which the recording for the live stream started. The time value is Unix epoch time represented in ISO 8601 format. | [optional]
**duration** | **float** | The duration of the live stream recorded. The time value is in seconds. | [optional]
**type** | **str** | The type of media represented by the recording session, either &#x60;content&#x60; for normal stream content or &#x60;slate&#x60; for slate media inserted during stream interruptions. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetResponse.md
````markdown
# AssetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Asset**](Asset.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/AssetsApi.md
````markdown
# mux_python.AssetsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetsApi.md#create_asset) | **POST** /video/v1/assets | Create an asset
[**create_asset_playback_id**](AssetsApi.md#create_asset_playback_id) | **POST** /video/v1/assets/{ASSET_ID}/playback-ids | Create a playback ID
[**create_asset_static_rendition**](AssetsApi.md#create_asset_static_rendition) | **POST** /video/v1/assets/{ASSET_ID}/static-renditions | Create a static rendition for an asset
[**create_asset_track**](AssetsApi.md#create_asset_track) | **POST** /video/v1/assets/{ASSET_ID}/tracks | Create an asset track
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /video/v1/assets/{ASSET_ID} | Delete an asset
[**delete_asset_playback_id**](AssetsApi.md#delete_asset_playback_id) | **DELETE** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Delete a playback ID
[**delete_asset_static_rendition**](AssetsApi.md#delete_asset_static_rendition) | **DELETE** /video/v1/assets/{ASSET_ID}/static-renditions/{STATIC_RENDITION_ID} | Delete a single static rendition for an asset
[**delete_asset_track**](AssetsApi.md#delete_asset_track) | **DELETE** /video/v1/assets/{ASSET_ID}/tracks/{TRACK_ID} | Delete an asset track
[**generate_asset_track_subtitles**](AssetsApi.md#generate_asset_track_subtitles) | **POST** /video/v1/assets/{ASSET_ID}/tracks/{TRACK_ID}/generate-subtitles | Generate track subtitles
[**get_asset**](AssetsApi.md#get_asset) | **GET** /video/v1/assets/{ASSET_ID} | Retrieve an asset
[**get_asset_input_info**](AssetsApi.md#get_asset_input_info) | **GET** /video/v1/assets/{ASSET_ID}/input-info | Retrieve asset input info
[**get_asset_playback_id**](AssetsApi.md#get_asset_playback_id) | **GET** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a playback ID
[**list_assets**](AssetsApi.md#list_assets) | **GET** /video/v1/assets | List assets
[**update_asset**](AssetsApi.md#update_asset) | **PATCH** /video/v1/assets/{ASSET_ID} | Update an asset
[**update_asset_master_access**](AssetsApi.md#update_asset_master_access) | **PUT** /video/v1/assets/{ASSET_ID}/master-access | Update master access
[**update_asset_mp4_support**](AssetsApi.md#update_asset_mp4_support) | **PUT** /video/v1/assets/{ASSET_ID}/mp4-support | Update MP4 support


# **create_asset**
> AssetResponse create_asset(create_asset_request)

Create an asset

Create a new Mux Video asset.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    create_asset_request = {"inputs":[{"url":"https://muxed.s3.amazonaws.com/leds.mp4"}],"playback_policies":["public"],"video_quality":"basic"} # CreateAssetRequest | 

    try:
        # Create an asset
        api_response = api_instance.create_asset(create_asset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_asset_request** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_playback_id**
> CreatePlaybackIDResponse create_asset_playback_id(asset_id, create_playback_id_request)

Create a playback ID

Creates a playback ID that can be used to stream the asset to a viewer.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
create_playback_id_request = {"policy":"public"} # CreatePlaybackIDRequest | 

    try:
        # Create a playback ID
        api_response = api_instance.create_asset_playback_id(asset_id, create_playback_id_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **create_playback_id_request** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_static_rendition**
> CreateStaticRenditionResponse create_asset_static_rendition(asset_id, create_static_rendition_request)

Create a static rendition for an asset

Creates a static rendition (i.e. MP4) for an asset

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
create_static_rendition_request = {"resolution":"highest"} # CreateStaticRenditionRequest | 

    try:
        # Create a static rendition for an asset
        api_response = api_instance.create_asset_static_rendition(asset_id, create_static_rendition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset_static_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **create_static_rendition_request** | [**CreateStaticRenditionRequest**](CreateStaticRenditionRequest.md)|  | 

### Return type

[**CreateStaticRenditionResponse**](CreateStaticRenditionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_track**
> CreateTrackResponse create_asset_track(asset_id, create_track_request)

Create an asset track

Adds an asset track (for example, subtitles, or an alternate audio track) to an asset. Assets must be in the `ready` state before tracks can be added.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
create_track_request = {"url":"https://example.com/myVideo_en.srt","type":"text","text_type":"subtitles","language_code":"en-US","name":"English","closed_captions":true,"passthrough":"English"} # CreateTrackRequest | 

    try:
        # Create an asset track
        api_response = api_instance.create_asset_track(asset_id, create_track_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **create_track_request** | [**CreateTrackRequest**](CreateTrackRequest.md)|  | 

### Return type

[**CreateTrackResponse**](CreateTrackResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> delete_asset(asset_id)

Delete an asset

Deletes a video asset and all its data.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.

    try:
        # Delete an asset
        api_instance.delete_asset(asset_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_playback_id**
> delete_asset_playback_id(asset_id, playback_id)

Delete a playback ID

Deletes a playback ID, rendering it nonfunctional for viewing an asset's video content. Please note that deleting the playback ID removes access to the underlying asset; a viewer who started playback before the playback ID was deleted may be able to watch the entire video for a limited duration.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Delete a playback ID
        api_instance.delete_asset_playback_id(asset_id, playback_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_static_rendition**
> delete_asset_static_rendition(asset_id, static_rendition_id)

Delete a single static rendition for an asset

Deletes a single static rendition for an asset

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
static_rendition_id = 'static_rendition_id_example' # str | The static rendition ID.

    try:
        # Delete a single static rendition for an asset
        api_instance.delete_asset_static_rendition(asset_id, static_rendition_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_static_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **static_rendition_id** | **str**| The static rendition ID. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_track**
> delete_asset_track(asset_id, track_id)

Delete an asset track

Removes a text track from an asset. Audio and video tracks on assets cannot be removed.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
track_id = 'track_id_example' # str | The track ID.

    try:
        # Delete an asset track
        api_instance.delete_asset_track(asset_id, track_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **track_id** | **str**| The track ID. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_asset_track_subtitles**
> GenerateTrackSubtitlesResponse generate_asset_track_subtitles(asset_id, track_id, generate_track_subtitles_request)

Generate track subtitles

Generates subtitles (captions) for a given audio track. This API can be used for up to 7 days after an asset is created.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
track_id = 'track_id_example' # str | The track ID.
generate_track_subtitles_request = {"generated_subtitles":[{"language_code":"en","name":"English (generated)","passthrough":"English (generated)"}]} # GenerateTrackSubtitlesRequest | 

    try:
        # Generate track subtitles
        api_response = api_instance.generate_asset_track_subtitles(asset_id, track_id, generate_track_subtitles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->generate_asset_track_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **track_id** | **str**| The track ID. | 
 **generate_track_subtitles_request** | [**GenerateTrackSubtitlesRequest**](GenerateTrackSubtitlesRequest.md)|  | 

### Return type

[**GenerateTrackSubtitlesResponse**](GenerateTrackSubtitlesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetResponse get_asset(asset_id)

Retrieve an asset

Retrieves the details of an asset that has previously been created. Supply the unique asset ID that was returned from your previous request, and Mux will return the corresponding asset information. The same information is returned when creating an asset.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.

    try:
        # Retrieve an asset
        api_response = api_instance.get_asset(asset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_input_info**
> GetAssetInputInfoResponse get_asset_input_info(asset_id)

Retrieve asset input info

Returns a list of the input objects that were used to create the asset along with any settings that were applied to each input.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.

    try:
        # Retrieve asset input info
        api_response = api_instance.get_asset_input_info(asset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset_input_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

### Return type

[**GetAssetInputInfoResponse**](GetAssetInputInfoResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_playback_id**
> GetAssetPlaybackIDResponse get_asset_playback_id(asset_id, playback_id)

Retrieve a playback ID

Retrieves information about the specified playback ID.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Retrieve a playback ID
        api_response = api_instance.get_asset_playback_id(asset_id, playback_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

[**GetAssetPlaybackIDResponse**](GetAssetPlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> ListAssetsResponse list_assets(limit=limit, page=page, live_stream_id=live_stream_id, upload_id=upload_id)

List assets

List all Mux assets.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
live_stream_id = 'live_stream_id_example' # str | Filter response to return all the assets for this live stream only (optional)
upload_id = 'upload_id_example' # str | Filter response to return an asset created from this direct upload only (optional)

    try:
        # List assets
        api_response = api_instance.list_assets(limit=limit, page=page, live_stream_id=live_stream_id, upload_id=upload_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->list_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **live_stream_id** | **str**| Filter response to return all the assets for this live stream only | [optional] 
 **upload_id** | **str**| Filter response to return an asset created from this direct upload only | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> AssetResponse update_asset(asset_id, update_asset_request)

Update an asset

Updates the details of an already-created Asset with the provided Asset ID. This currently supports only the `passthrough` field.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
update_asset_request = {"passthrough":"Example"} # UpdateAssetRequest | 

    try:
        # Update an asset
        api_response = api_instance.update_asset(asset_id, update_asset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->update_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **update_asset_request** | [**UpdateAssetRequest**](UpdateAssetRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_master_access**
> AssetResponse update_asset_master_access(asset_id, update_asset_master_access_request)

Update master access

Allows you to add temporary access to the master (highest-quality) version of the asset in MP4 format. A URL will be created that can be used to download the master version for 24 hours. After 24 hours Master Access will revert to \"none\". This master version is not optimized for web and not meant to be streamed, only downloaded for purposes like archiving or editing the video offline.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
update_asset_master_access_request = {"master_access":"temporary"} # UpdateAssetMasterAccessRequest | 

    try:
        # Update master access
        api_response = api_instance.update_asset_master_access(asset_id, update_asset_master_access_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->update_asset_master_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **update_asset_master_access_request** | [**UpdateAssetMasterAccessRequest**](UpdateAssetMasterAccessRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_mp4_support**
> AssetResponse update_asset_mp4_support(asset_id, update_asset_mp4_support_request)

Update MP4 support

This method has been deprecated. Please see the [Static Rendition API](https://www.mux.com/docs/guides/enable-static-mp4-renditions#after-asset-creation). Allows you to add or remove mp4 support for assets that were created without it. The values supported are `capped-1080p`, `audio-only`, `audio-only,capped-1080p`, `standard`(deprecated),  and `none`. `none` means that an asset *does not* have mp4 support, so submitting a request with `mp4_support` set to `none` will delete the mp4 assets from the asset in question. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
update_asset_mp4_support_request = {"mp4_support":"capped-1080p"} # UpdateAssetMP4SupportRequest | 

    try:
        # Update MP4 support
        api_response = api_instance.update_asset_mp4_support(asset_id, update_asset_mp4_support_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->update_asset_mp4_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **update_asset_mp4_support_request** | [**UpdateAssetMP4SupportRequest**](UpdateAssetMP4SupportRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/AssetStaticRenditions.md
````markdown
# AssetStaticRenditions

An object containing the current status of any static renditions (mp4s). The object does not exist if no static renditions have been requested. See [Download your videos](https://docs.mux.com/guides/enable-static-mp4-renditions) for more information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates the status of downloadable MP4 versions of this asset. This field is only valid when &#x60;mp4_support&#x60; is enabled | [optional] [default to 'disabled']
**files** | [**list[StaticRendition]**](StaticRendition.md) | Array of file objects. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/BreakdownValue.md
````markdown
# BreakdownValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**views** | **int** |  | [optional]
**value** | **float** |  | [optional]
**total_watch_time** | **int** |  | [optional]
**total_playing_time** | **int** |  | [optional]
**negative_impact** | **int** |  | [optional]
**field** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateAssetRequest.md
````markdown
# CreateAssetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**list[InputSettings]**](InputSettings.md) | Deprecated. Use &#x60;inputs&#x60; instead, which accepts an identical type. | [optional]
**inputs** | [**list[InputSettings]**](InputSettings.md) | An array of objects that each describe an input file to be used to create the asset. As a shortcut, input can also be a string URL for a file when only one input file is used. See &#x60;input[].url&#x60; for requirements. | [optional]
**playback_policy** | [**list[PlaybackPolicy]**](PlaybackPolicy.md) | Deprecated. Use &#x60;playback_policies&#x60; instead, which accepts an identical type. | [optional]
**playback_policies** | [**list[PlaybackPolicy]**](PlaybackPolicy.md) | An array of playback policy names that you want applied to this asset and available through &#x60;playback_ids&#x60;. Options include:  * &#x60;\&quot;public\&quot;&#x60; (anyone with the playback URL can stream the asset). * &#x60;\&quot;signed\&quot;&#x60; (an additional access token is required to play the asset).  If no &#x60;playback_policies&#x60; are set, the asset will have no playback IDs and will therefore not be playable. For simplicity, a single string name can be used in place of the array in the case of only one playback policy.  | [optional]
**advanced_playback_policies** | [**list[CreatePlaybackIDRequest]**](CreatePlaybackIDRequest.md) | An array of playback policy objects that you want applied to this asset and available through &#x60;playback_ids&#x60;. &#x60;advanced_playback_policies&#x60; must be used instead of &#x60;playback_policies&#x60; when creating a DRM playback ID.  | [optional]
**per_title_encode** | **bool** |  | [optional]
**passthrough** | **str** | You can set this field to anything you want. It will be included in the asset details and related webhooks. If you&#39;re looking for more structured metadata, such as &#x60;title&#x60; or &#x60;external_id&#x60;, you can use the &#x60;meta&#x60; object instead. **Max: 255 characters**. | [optional]
**mp4_support** | **str** | Deprecated. See the [Static Renditions API](https://www.mux.com/docs/guides/enable-static-mp4-renditions) for the updated API.  Specify what level of support for mp4 playback. You may not enable both &#x60;mp4_support&#x60; and  &#x60;static_renditions&#x60;.  * The &#x60;capped-1080p&#x60; option produces a single MP4 file, called &#x60;capped-1080p.mp4&#x60;, with the video resolution capped at 1080p. This option produces an &#x60;audio.m4a&#x60; file for an audio-only asset. * The &#x60;audio-only&#x60; option produces a single M4A file, called &#x60;audio.m4a&#x60; for a video or an audio-only asset. MP4 generation will error when this option is specified for a video-only asset. * The &#x60;audio-only,capped-1080p&#x60; option produces both the &#x60;audio.m4a&#x60; and &#x60;capped-1080p.mp4&#x60; files. Only the &#x60;capped-1080p.mp4&#x60; file is produced for a video-only asset, while only the &#x60;audio.m4a&#x60; file is produced for an audio-only asset.  The &#x60;standard&#x60;(deprecated) option produces up to three MP4 files with different levels of resolution (&#x60;high.mp4&#x60;, &#x60;medium.mp4&#x60;, &#x60;low.mp4&#x60;, or &#x60;audio.m4a&#x60; for an audio-only asset).  MP4 files are not produced for &#x60;none&#x60; (default).  In most cases you should use our default HLS-based streaming playback (&#x60;{playback_id}.m3u8&#x60;) which can automatically adjust to viewers&#39; connection speeds, but an mp4 can be useful for some legacy devices or downloading for offline playback. See the [Download your videos guide](https://docs.mux.com/guides/enable-static-mp4-renditions) for more information.  | [optional]
**normalize_audio** | **bool** | Normalize the audio track loudness level. This parameter is only applicable to on-demand (not live) assets. | [optional] [default to False]
**master_access** | **str** | Specify what level (if any) of support for master access. Master access can be enabled temporarily for your asset to be downloaded. See the [Download your videos guide](https://docs.mux.com/guides/enable-static-mp4-renditions) for more information. | [optional]
**test** | **bool** | Marks the asset as a test asset when the value is set to true. A Test asset can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test assets created. Test asset are watermarked with the Mux logo, limited to 10 seconds, deleted after 24 hrs. | [optional]
**max_resolution_tier** | **str** | Max resolution tier can be used to control the maximum &#x60;resolution_tier&#x60; your asset is encoded, stored, and streamed at. If not set, this defaults to &#x60;1080p&#x60;. | [optional]
**encoding_tier** | **str** | This field is deprecated. Please use &#x60;video_quality&#x60; instead. The encoding tier informs the cost, quality, and available platform features for the asset. The default encoding tier for an account can be set in the Mux Dashboard. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**video_quality** | **str** | The video quality controls the cost, quality, and available platform features for the asset. The default video quality for an account can be set in the Mux Dashboard. This field replaces the deprecated &#x60;encoding_tier&#x60; value. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**static_renditions** | [**list[CreateStaticRenditionRequest]**](CreateStaticRenditionRequest.md) | An array of static renditions to create for this asset. You may not enable both &#x60;static_renditions&#x60; and &#x60;mp4_support (the latter being deprecated)&#x60; | [optional]
**meta** | [**AssetMetadata**](AssetMetadata.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateLiveStreamRequest.md
````markdown
# CreateLiveStreamRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playback_policy** | [**list[PlaybackPolicy]**](PlaybackPolicy.md) | Deprecated. Use &#x60;playback_policies&#x60; instead, which accepts an identical type. | [optional]
**playback_policies** | [**list[PlaybackPolicy]**](PlaybackPolicy.md) | An array of playback policy names that you want applied to this live stream and available through &#x60;playback_ids&#x60;. Options include:  * &#x60;\&quot;public\&quot;&#x60; (anyone with the playback URL can stream the live stream). * &#x60;\&quot;signed\&quot;&#x60; (an additional access token is required to play the live stream).  If no &#x60;playback_policies&#x60; is set, the live stream will have no playback IDs and will therefore not be playable. For simplicity, a single string name can be used in place of the array in the case of only one playback policy.  | [optional]
**advanced_playback_policies** | [**list[CreatePlaybackIDRequest]**](CreatePlaybackIDRequest.md) | An array of playback policy objects that you want applied on this live stream and available through &#x60;playback_ids&#x60;. &#x60;advanced_playback_policies&#x60; must be used instead of &#x60;playback_policies&#x60; when creating a DRM playback ID.  | [optional]
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional]
**reconnect_window** | **float** | When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Defaults to 60 seconds on the API if not specified.  If not specified directly, Standard Latency streams have a Reconnect Window of 60 seconds; Reduced and Low Latency streams have a default of 0 seconds, or no Reconnect Window. For that reason, we suggest specifying a value other than zero for Reduced and Low Latency streams.  Reduced and Low Latency streams with a Reconnect Window greater than zero will insert slate media into the recorded asset while waiting for the streaming software to reconnect or when there are brief interruptions in the live stream media. When using a Reconnect Window setting higher than 60 seconds with a Standard Latency stream, we highly recommend enabling slate with the &#x60;use_slate_for_standard_latency&#x60; option.  | [optional] [default to 60]
**use_slate_for_standard_latency** | **bool** | By default, Standard Latency live streams do not have slate media inserted while waiting for live streaming software to reconnect to Mux. Setting this to true enables slate insertion on a Standard Latency stream. | [optional] [default to False]
**reconnect_slate_url** | **str** | The URL of the image file that Mux should download and use as slate media during interruptions of the live stream media. This file will be downloaded each time a new recorded asset is created from the live stream. If this is not set, the default slate media will be used. | [optional]
**passthrough** | **str** |  | [optional]
**audio_only** | **bool** | Force the live stream to only process the audio track when the value is set to true. Mux drops the video track if broadcasted. | [optional]
**embedded_subtitles** | [**list[LiveStreamEmbeddedSubtitleSettings]**](LiveStreamEmbeddedSubtitleSettings.md) | Describe the embedded closed caption contents of the incoming live stream. | [optional]
**generated_subtitles** | [**list[LiveStreamGeneratedSubtitleSettings]**](LiveStreamGeneratedSubtitleSettings.md) | Configure the incoming live stream to include subtitles created with automatic speech recognition. Each Asset created from a live stream with &#x60;generated_subtitles&#x60; configured will automatically receive two text tracks. The first of these will have a &#x60;text_source&#x60; value of &#x60;generated_live&#x60;, and will be available with &#x60;ready&#x60; status as soon as the stream is live. The second text track will have a &#x60;text_source&#x60; value of &#x60;generated_live_final&#x60; and will contain subtitles with improved accuracy, timing, and formatting. However, &#x60;generated_live_final&#x60; tracks will not be available in &#x60;ready&#x60; status until the live stream ends. If an Asset has both &#x60;generated_live&#x60; and &#x60;generated_live_final&#x60; tracks that are &#x60;ready&#x60;, then only the &#x60;generated_live_final&#x60; track will be included during playback. | [optional]
**reduced_latency** | **bool** | This field is deprecated. Please use &#x60;latency_mode&#x60; instead. Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this if you want lower latency for your live stream. Read more here: https://mux.com/blog/reduced-latency-for-mux-live-streaming-now-available/ | [optional]
**low_latency** | **bool** | This field is deprecated. Please use &#x60;latency_mode&#x60; instead. Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Setting this option will enable compatibility with the LL-HLS specification for low-latency streaming. This typically has lower latency than Reduced Latency streams, and cannot be combined with Reduced Latency. | [optional]
**latency_mode** | **str** | Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this as an alternative to setting low latency or reduced latency flags. | [optional]
**test** | **bool** | Marks the live stream as a test live stream when the value is set to true. A test live stream can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test live streams created. Test live streams are watermarked with the Mux logo and limited to 5 minutes. The test live stream is disabled after the stream is active for 5 mins and the recorded asset also deleted after 24 hours. | [optional]
**simulcast_targets** | [**list[CreateSimulcastTargetRequest]**](CreateSimulcastTargetRequest.md) |  | [optional]
**max_continuous_duration** | **int** | The time in seconds a live stream may be continuously active before being disconnected. Defaults to 12 hours. | [optional] [default to 43200]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreatePlaybackIDRequest.md
````markdown
# CreatePlaybackIDRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**PlaybackPolicy**](PlaybackPolicy.md) |  | [optional]
**drm_configuration_id** | **str** | The DRM configuration used by this playback ID. Must only be set when &#x60;policy&#x60; is set to &#x60;drm&#x60;. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreatePlaybackIDResponse.md
````markdown
# CreatePlaybackIDResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaybackID**](PlaybackID.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreatePlaybackRestrictionRequest.md
````markdown
# CreatePlaybackRestrictionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referrer** | [**ReferrerDomainRestriction**](ReferrerDomainRestriction.md) |  | [optional]
**user_agent** | [**UserAgentRestrictionRequest**](UserAgentRestrictionRequest.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateSimulcastTargetRequest.md
````markdown
# CreateSimulcastTargetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passthrough** | **str** | Arbitrary user-supplied metadata set by you when creating a simulcast target. | [optional]
**stream_key** | **str** | Stream Key represents a stream identifier on the third party live streaming service to send the parent live stream to. Only used for RTMP(s) simulcast destinations. | [optional]
**url** | **str** | The RTMP(s) or SRT endpoint for a simulcast destination. * For RTMP(s) destinations, this should include the application name for the third party live streaming service, for example: &#x60;rtmp://live.example.com/app&#x60;. * For SRT destinations, this should be a fully formed SRT connection string, for example: &#x60;srt://srt-live.example.com:1234?streamid&#x3D;{stream_key}&amp;passphrase&#x3D;{srt_passphrase}&#x60;.  Note: SRT simulcast targets can only be used when an source is connected over SRT.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateStaticRenditionRequest.md
````markdown
# CreateStaticRenditionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **str** |  | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the static rendition. Max 255 characters. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateStaticRenditionResponse.md
````markdown
# CreateStaticRenditionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StaticRendition**](StaticRendition.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateTrackRequest.md
````markdown
# CreateTrackRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the file that Mux should download and use. * For &#x60;audio&#x60; tracks, the URL is the location of the audio file for Mux to download, for example an M4A, WAV, or MP3 file. Mux supports most audio file formats and codecs, but for fastest processing, you should [use standard inputs wherever possible](https://docs.mux.com/guides/video/minimize-processing-time). * For &#x60;text&#x60; tracks, the URL is the location of subtitle/captions file. Mux supports [SubRip Text (SRT)](https://en.wikipedia.org/wiki/SubRip) and [Web Video Text Tracks](https://www.w3.org/TR/webvtt1/) formats for ingesting Subtitles and Closed Captions.  |
**type** | **str** |  |
**text_type** | **str** |  |
**language_code** | **str** | The language code value must be a valid BCP 47 specification compliant value. For example, en for English or en-US for the US version of English. |
**name** | **str** | The name of the track containing a human-readable description. This value must be unique within each group of &#x60;text&#x60; or &#x60;audio&#x60; track types. The HLS manifest will associate the &#x60;text&#x60; or &#x60;audio&#x60; track with this value. For example, set the value to \&quot;English\&quot; for subtitles text track with &#x60;language_code&#x60; as en-US. If this parameter is not included, Mux will auto-populate a value based on the &#x60;language_code&#x60; value. | [optional]
**closed_captions** | **bool** | Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the track either when creating the asset or track. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateTrackResponse.md
````markdown
# CreateTrackResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Track**](Track.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateTranscriptionVocabularyRequest.md
````markdown
# CreateTranscriptionVocabularyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-supplied name of the Transcription Vocabulary. | [optional]
**phrases** | **list[str]** | Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream&#39;s &#x60;generated_subtitles&#x60;, the probability of successful speech recognition for these words or phrases is boosted. |
**passthrough** | **str** | Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateUploadRequest.md
````markdown
# CreateUploadRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked &#x60;timed_out&#x60; | [optional] [default to 3600]
**cors_origin** | **str** | If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers. | [optional]
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional]
**test** | **bool** | Indicates if this is a test Direct Upload, in which case the Asset that gets created will be a &#x60;test&#x60; Asset. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/CreateWebInputRequest.md
````markdown
# CreateWebInputRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Web Input. | [optional]
**created_at** | **str** | Time the Web Input was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**url** | **str** | The URL for the Web Input to load. | [optional]
**auto_launch** | **bool** | When set to &#x60;true&#x60; the Web Input will automatically launch and start streaming immediately after creation | [optional]
**live_stream_id** | **str** | The Live Stream ID to broadcast this Web Input to | [optional]
**status** | **str** |  | [optional]
**passthrough** | **str** | Arbitrary metadata that will be included in the Web Input details and related webhooks. Can be used to store your own ID for the Web Input. **Max: 255 characters**. | [optional]
**resolution** | **str** | The resolution of the viewport of the Web Input&#39;s browser instance. Defaults to 1920x1080 if not set. | [optional] [default to '1920x1080']
**timeout** | **int** | The number of seconds that the Web Input should stream for before automatically shutting down. | [optional] [default to 3600]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DeliveryReport.md
````markdown
# DeliveryReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_stream_id** | **str** | Unique identifier for the live stream that created the asset. | [optional]
**asset_id** | **str** | Unique identifier for the asset. | [optional]
**passthrough** | **str** | The &#x60;passthrough&#x60; value for the asset. | [optional]
**created_at** | **str** | Time at which the asset was created. Measured in seconds since the Unix epoch. | [optional]
**deleted_at** | **str** | If exists, time at which the asset was deleted. Measured in seconds since the Unix epoch. | [optional]
**asset_state** | **str** | The state of the asset. | [optional]
**asset_duration** | **float** | The duration of the asset in seconds. | [optional]
**asset_resolution_tier** | **str** | The resolution tier that the asset was ingested at, affecting billing for ingest &amp; storage | [optional]
**asset_encoding_tier** | **str** | This field is deprecated. Please use &#x60;asset_video_quality&#x60; instead. The encoding tier that the asset was ingested at. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**asset_video_quality** | **str** | The video quality that the asset was ingested at. This field replaces &#x60;asset_encoding_tier&#x60;. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**delivered_seconds** | **float** | Total number of delivered seconds during this time window. | [optional]
**delivered_seconds_by_resolution** | [**DeliveryReportDeliveredSecondsByResolution**](DeliveryReportDeliveredSecondsByResolution.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DeliveryReportDeliveredSecondsByResolution.md
````markdown
# DeliveryReportDeliveredSecondsByResolution

Seconds delivered broken into resolution tiers. Each tier will only be displayed if there was content delivered in the tier.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_2160p** | **float** | Total number of delivered seconds during this time window that had a resolution larger than the 1440p tier (over 4,194,304 pixels total). | [optional]
**tier_1440p** | **float** | Total number of delivered seconds during this time window that had a resolution larger than the 1080p tier but less than or equal to the 2160p tier (over 2,073,600 and &lt;&#x3D; 4,194,304 pixels total). | [optional]
**tier_1080p** | **float** | Total number of delivered seconds during this time window that had a resolution larger than the 720p tier but less than or equal to the 1440p tier (over 921,600 and &lt;&#x3D; 2,073,600 pixels total). | [optional]
**tier_720p** | **float** | Total number of delivered seconds during this time window that had a resolution within the 720p tier (up to 921,600 pixels total, based on typical 1280x720). | [optional]
**tier_audio_only** | **float** | Total number of delivered seconds during this time window that had a resolution of audio only. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DeliveryUsageApi.md
````markdown
# mux_python.DeliveryUsageApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_delivery_usage**](DeliveryUsageApi.md#list_delivery_usage) | **GET** /video/v1/delivery-usage | List Usage


# **list_delivery_usage**
> ListDeliveryUsageResponse list_delivery_usage(page=page, limit=limit, asset_id=asset_id, live_stream_id=live_stream_id, timeframe=timeframe)

List Usage

Returns a list of delivery usage records and their associated Asset IDs or Live Stream IDs.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DeliveryUsageApi(api_client)
    page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
limit = 100 # int | Number of items to include in the response (optional) (default to 100)
asset_id = 'asset_id_example' # str | Filter response to return delivery usage for this asset only. You cannot specify both the `asset_id` and `live_stream_id` parameters together. (optional)
live_stream_id = 'live_stream_id_example' # str | Filter response to return delivery usage for assets for this live stream. You cannot specify both the `asset_id` and `live_stream_id` parameters together. (optional)
timeframe = ['timeframe_example'] # list[str] | Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made. (optional)

    try:
        # List Usage
        api_response = api_instance.list_delivery_usage(page=page, limit=limit, asset_id=asset_id, live_stream_id=live_stream_id, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveryUsageApi->list_delivery_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **int**| Number of items to include in the response | [optional] [default to 100]
 **asset_id** | **str**| Filter response to return delivery usage for this asset only. You cannot specify both the &#x60;asset_id&#x60; and &#x60;live_stream_id&#x60; parameters together. | [optional] 
 **live_stream_id** | **str**| Filter response to return delivery usage for assets for this live stream. You cannot specify both the &#x60;asset_id&#x60; and &#x60;live_stream_id&#x60; parameters together. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made. | [optional] 

### Return type

[**ListDeliveryUsageResponse**](ListDeliveryUsageResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/DimensionsApi.md
````markdown
# mux_python.DimensionsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dimension_values**](DimensionsApi.md#list_dimension_values) | **GET** /data/v1/dimensions/{DIMENSION_ID} | Lists the values for a specific dimension
[**list_dimensions**](DimensionsApi.md#list_dimensions) | **GET** /data/v1/dimensions | List Dimensions


# **list_dimension_values**
> ListDimensionValuesResponse list_dimension_values(dimension_id, limit=limit, page=page, filters=filters, metric_filters=metric_filters, timeframe=timeframe)

Lists the values for a specific dimension

Lists the values for a dimension along with a total count of related views.  Note: This API replaces the list-filter-values API call. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DimensionsApi(api_client)
    dimension_id = 'abcd1234' # str | ID of the Dimension
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # Lists the values for a specific dimension
        api_response = api_instance.list_dimension_values(dimension_id, limit=limit, page=page, filters=filters, metric_filters=metric_filters, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DimensionsApi->list_dimension_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dimension_id** | **str**| ID of the Dimension | 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListDimensionValuesResponse**](ListDimensionValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dimensions**
> ListDimensionsResponse list_dimensions()

List Dimensions

List all available dimensions.  Note: This API replaces the list-filters API call. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DimensionsApi(api_client)
    
    try:
        # List Dimensions
        api_response = api_instance.list_dimensions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DimensionsApi->list_dimensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDimensionsResponse**](ListDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/DimensionValue.md
````markdown
# DimensionValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**total_count** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DirectUploadsApi.md
````markdown
# mux_python.DirectUploadsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_direct_upload**](DirectUploadsApi.md#cancel_direct_upload) | **PUT** /video/v1/uploads/{UPLOAD_ID}/cancel | Cancel a direct upload
[**create_direct_upload**](DirectUploadsApi.md#create_direct_upload) | **POST** /video/v1/uploads | Create a new direct upload URL
[**get_direct_upload**](DirectUploadsApi.md#get_direct_upload) | **GET** /video/v1/uploads/{UPLOAD_ID} | Retrieve a single direct upload&#39;s info
[**list_direct_uploads**](DirectUploadsApi.md#list_direct_uploads) | **GET** /video/v1/uploads | List direct uploads


# **cancel_direct_upload**
> UploadResponse cancel_direct_upload(upload_id)

Cancel a direct upload

Cancels a direct upload and marks it as cancelled. If a pending upload finishes after this request, no asset will be created. This request will only succeed if the upload is still in the `waiting` state. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DirectUploadsApi(api_client)
    upload_id = 'abcd1234' # str | ID of the Upload

    try:
        # Cancel a direct upload
        api_response = api_instance.cancel_direct_upload(upload_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectUploadsApi->cancel_direct_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| ID of the Upload | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Cancellation no longer possible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_direct_upload**
> UploadResponse create_direct_upload(create_upload_request)

Create a new direct upload URL

Creates a new direct upload, through which video content can be uploaded for ingest to Mux.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DirectUploadsApi(api_client)
    create_upload_request = {"cors_origin":"https://example.com/","new_asset_settings":{"playback_policies":["public"]}} # CreateUploadRequest | 

    try:
        # Create a new direct upload URL
        api_response = api_instance.create_direct_upload(create_upload_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectUploadsApi->create_direct_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_upload_request** | [**CreateUploadRequest**](CreateUploadRequest.md)|  | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_upload**
> UploadResponse get_direct_upload(upload_id)

Retrieve a single direct upload's info

Fetches information about a single direct upload in the current environment.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DirectUploadsApi(api_client)
    upload_id = 'abcd1234' # str | ID of the Upload

    try:
        # Retrieve a single direct upload's info
        api_response = api_instance.get_direct_upload(upload_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectUploadsApi->get_direct_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| ID of the Upload | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_direct_uploads**
> ListUploadsResponse list_direct_uploads(limit=limit, page=page)

List direct uploads

Lists direct uploads in the current environment.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DirectUploadsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

    try:
        # List direct uploads
        api_response = api_instance.list_direct_uploads(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectUploadsApi->list_direct_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListUploadsResponse**](ListUploadsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/DisableLiveStreamResponse.md
````markdown
# DisableLiveStreamResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DRMConfiguration.md
````markdown
# DRMConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the DRM Configuration. Max 255 characters. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DRMConfigurationResponse.md
````markdown
# DRMConfigurationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DRMConfiguration**](DRMConfiguration.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/DRMConfigurationsApi.md
````markdown
# mux_python.DRMConfigurationsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drm_configuration**](DRMConfigurationsApi.md#get_drm_configuration) | **GET** /video/v1/drm-configurations/{DRM_CONFIGURATION_ID} | Retrieve a DRM Configuration
[**list_drm_configurations**](DRMConfigurationsApi.md#list_drm_configurations) | **GET** /video/v1/drm-configurations | List DRM Configurations


# **get_drm_configuration**
> DRMConfigurationResponse get_drm_configuration(drm_configuration_id)

Retrieve a DRM Configuration

Retrieves a single DRM Configuration.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DRMConfigurationsApi(api_client)
    drm_configuration_id = 'drm_configuration_id_example' # str | The DRM Configuration ID.

    try:
        # Retrieve a DRM Configuration
        api_response = api_instance.get_drm_configuration(drm_configuration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DRMConfigurationsApi->get_drm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drm_configuration_id** | **str**| The DRM Configuration ID. | 

### Return type

[**DRMConfigurationResponse**](DRMConfigurationResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drm_configurations**
> ListDRMConfigurationsResponse list_drm_configurations(page=page, limit=limit)

List DRM Configurations

Returns a list of DRM Configurations

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.DRMConfigurationsApi(api_client)
    page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)

    try:
        # List DRM Configurations
        api_response = api_instance.list_drm_configurations(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DRMConfigurationsApi->list_drm_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]

### Return type

[**ListDRMConfigurationsResponse**](ListDRMConfigurationsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/EnableLiveStreamResponse.md
````markdown
# EnableLiveStreamResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Error.md
````markdown
# Error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for this error. | [optional]
**percentage** | **float** | The percentage of views that experienced this error. | [optional]
**notes** | **str** | Notes that are attached to this error. | [optional]
**message** | **str** | The error message. | [optional]
**last_seen** | **str** | The last time this error was seen (ISO 8601 timestamp). | [optional]
**description** | **str** | Description of the error. | [optional]
**count** | **int** | The total number of views that experienced this error. | [optional]
**code** | **int** | The error code | [optional]
**player_error_code** | **str** | The string version of the error code | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ErrorsApi.md
````markdown
# mux_python.ErrorsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_errors**](ErrorsApi.md#list_errors) | **GET** /data/v1/errors | List Errors


# **list_errors**
> ListErrorsResponse list_errors(filters=filters, metric_filters=metric_filters, timeframe=timeframe)

List Errors

Returns a list of errors.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.ErrorsApi(api_client)
    filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # List Errors
        api_response = api_instance.list_errors(filters=filters, metric_filters=metric_filters, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ErrorsApi->list_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListErrorsResponse**](ListErrorsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/ExportDate.md
````markdown
# ExportDate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_date** | **date** |  | [optional]
**files** | [**list[ExportFile]**](ExportFile.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ExportFile.md
````markdown
# ExportFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional]
**type** | **str** |  | [optional]
**path** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ExportsApi.md
````markdown
# mux_python.ExportsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_exports**](ExportsApi.md#list_exports) | **GET** /data/v1/exports | List property video view export links
[**list_exports_views**](ExportsApi.md#list_exports_views) | **GET** /data/v1/exports/views | List available property view exports


# **list_exports**
> ListExportsResponse list_exports()

List property video view export links

The API has been replaced by the list-exports-views API call.  Lists the available video view exports along with URLs to retrieve them. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.ExportsApi(api_client)
    
    try:
        # List property video view export links
        api_response = api_instance.list_exports()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportsApi->list_exports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListExportsResponse**](ListExportsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exports_views**
> ListVideoViewExportsResponse list_exports_views()

List available property view exports

Lists the available video view exports along with URLs to retrieve them.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.ExportsApi(api_client)
    
    try:
        # List available property view exports
        api_response = api_instance.list_exports_views()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportsApi->list_exports_views: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVideoViewExportsResponse**](ListVideoViewExportsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/FiltersApi.md
````markdown
# mux_python.FiltersApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_filter_values**](FiltersApi.md#list_filter_values) | **GET** /data/v1/filters/{FILTER_ID} | Lists values for a specific filter
[**list_filters**](FiltersApi.md#list_filters) | **GET** /data/v1/filters | List Filters


# **list_filter_values**
> ListFilterValuesResponse list_filter_values(filter_id, limit=limit, page=page, filters=filters, timeframe=timeframe)

Lists values for a specific filter

The API has been replaced by the list-dimension-values API call.  Lists the values for a filter along with a total count of related views. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.FiltersApi(api_client)
    filter_id = 'abcd1234' # str | ID of the Filter
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # Lists values for a specific filter
        api_response = api_instance.list_filter_values(filter_id, limit=limit, page=page, filters=filters, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FiltersApi->list_filter_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| ID of the Filter | 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListFilterValuesResponse**](ListFilterValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_filters**
> ListFiltersResponse list_filters()

List Filters

The API has been replaced by the list-dimensions API call.  Lists all the filters broken out into basic and advanced. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.FiltersApi(api_client)
    
    try:
        # List Filters
        api_response = api_instance.list_filters()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FiltersApi->list_filters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListFiltersResponse**](ListFiltersResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/FilterValue.md
````markdown
# FilterValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**total_count** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GenerateTrackSubtitlesRequest.md
````markdown
# GenerateTrackSubtitlesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_subtitles** | [**list[AssetGeneratedSubtitleSettings]**](AssetGeneratedSubtitleSettings.md) | Generate subtitle tracks using automatic speech recognition with this configuration. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GenerateTrackSubtitlesResponse.md
````markdown
# GenerateTrackSubtitlesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Track]**](Track.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetAssetInputInfoResponse.md
````markdown
# GetAssetInputInfoResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[InputInfo]**](InputInfo.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetAssetOrLiveStreamIdResponse.md
````markdown
# GetAssetOrLiveStreamIdResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetAssetOrLiveStreamIdResponseData**](GetAssetOrLiveStreamIdResponseData.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetAssetOrLiveStreamIdResponseData.md
````markdown
# GetAssetOrLiveStreamIdResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Playback ID used to retrieve the corresponding asset or the live stream ID | [optional]
**policy** | [**PlaybackPolicy**](PlaybackPolicy.md) |  | [optional]
**object** | [**GetAssetOrLiveStreamIdResponseDataObject**](GetAssetOrLiveStreamIdResponseDataObject.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetAssetOrLiveStreamIdResponseDataObject.md
````markdown
# GetAssetOrLiveStreamIdResponseDataObject

Describes the Asset or LiveStream object associated with the playback ID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the object. | [optional]
**type** | **str** | Identifies the object type associated with the playback ID. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetAssetPlaybackIDResponse.md
````markdown
# GetAssetPlaybackIDResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaybackID**](PlaybackID.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetLiveStreamPlaybackIDResponse.md
````markdown
# GetLiveStreamPlaybackIDResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaybackID**](PlaybackID.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetMetricTimeseriesDataResponse.md
````markdown
# GetMetricTimeseriesDataResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **list[list[str]]** |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]
**meta** | [**ListBreakdownValuesResponseMeta**](ListBreakdownValuesResponseMeta.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetMonitoringBreakdownResponse.md
````markdown
# GetMonitoringBreakdownResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[MonitoringBreakdownValue]**](MonitoringBreakdownValue.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetMonitoringBreakdownTimeseriesResponse.md
````markdown
# GetMonitoringBreakdownTimeseriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[MonitoringBreakdownTimeseriesValues]**](MonitoringBreakdownTimeseriesValues.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetMonitoringHistogramTimeseriesResponse.md
````markdown
# GetMonitoringHistogramTimeseriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetMonitoringHistogramTimeseriesResponseMeta**](GetMonitoringHistogramTimeseriesResponseMeta.md) |  | [optional]
**data** | [**list[MonitoringHistogramTimeseriesDatapoint]**](MonitoringHistogramTimeseriesDatapoint.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetMonitoringHistogramTimeseriesResponseMeta.md
````markdown
# GetMonitoringHistogramTimeseriesResponseMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_unit** | **str** |  | [optional]
**buckets** | [**list[MonitoringHistogramTimeseriesBucket]**](MonitoringHistogramTimeseriesBucket.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetMonitoringTimeseriesResponse.md
````markdown
# GetMonitoringTimeseriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[MonitoringTimeseriesDatapoint]**](MonitoringTimeseriesDatapoint.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetOverallValuesResponse.md
````markdown
# GetOverallValuesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OverallValues**](OverallValues.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]
**meta** | [**ListBreakdownValuesResponseMeta**](ListBreakdownValuesResponseMeta.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetRealTimeBreakdownResponse.md
````markdown
# GetRealTimeBreakdownResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[RealTimeBreakdownValue]**](RealTimeBreakdownValue.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetRealTimeHistogramTimeseriesResponse.md
````markdown
# GetRealTimeHistogramTimeseriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetRealTimeHistogramTimeseriesResponseMeta**](GetRealTimeHistogramTimeseriesResponseMeta.md) |  | [optional]
**data** | [**list[RealTimeHistogramTimeseriesDatapoint]**](RealTimeHistogramTimeseriesDatapoint.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetRealTimeHistogramTimeseriesResponseMeta.md
````markdown
# GetRealTimeHistogramTimeseriesResponseMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_unit** | **str** |  | [optional]
**buckets** | [**list[RealTimeHistogramTimeseriesBucket]**](RealTimeHistogramTimeseriesBucket.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/GetRealTimeTimeseriesResponse.md
````markdown
# GetRealTimeTimeseriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[RealTimeTimeseriesDatapoint]**](RealTimeTimeseriesDatapoint.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Incident.md
````markdown
# Incident

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** |  | [optional]
**status** | **str** |  | [optional]
**started_at** | **str** |  | [optional]
**severity** | **str** |  | [optional]
**sample_size_unit** | **str** |  | [optional]
**sample_size** | **int** |  | [optional]
**resolved_at** | **str** |  | [optional]
**notifications** | [**list[IncidentNotification]**](IncidentNotification.md) |  | [optional]
**notification_rules** | [**list[IncidentNotificationRule]**](IncidentNotificationRule.md) |  | [optional]
**measurement** | **str** |  | [optional]
**measured_value_on_close** | **float** |  | [optional]
**measured_value** | **float** |  | [optional]
**incident_key** | **str** |  | [optional]
**impact** | **str** |  | [optional]
**id** | **str** |  | [optional]
**error_description** | **str** |  | [optional]
**description** | **str** |  | [optional]
**breakdowns** | [**list[IncidentBreakdown]**](IncidentBreakdown.md) |  | [optional]
**affected_views_per_hour_on_open** | **int** |  | [optional]
**affected_views_per_hour** | **int** |  | [optional]
**affected_views** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/IncidentBreakdown.md
````markdown
# IncidentBreakdown

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**name** | **str** |  | [optional]
**id** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/IncidentNotification.md
````markdown
# IncidentNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queued_at** | **str** |  | [optional]
**id** | **int** |  | [optional]
**attempted_at** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/IncidentNotificationRule.md
````markdown
# IncidentNotificationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional]
**rules** | [**list[NotificationRule]**](NotificationRule.md) |  | [optional]
**property_id** | **str** |  | [optional]
**id** | **str** |  | [optional]
**action** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/IncidentResponse.md
````markdown
# IncidentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Incident**](Incident.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/IncidentsApi.md
````markdown
# mux_python.IncidentsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_incident**](IncidentsApi.md#get_incident) | **GET** /data/v1/incidents/{INCIDENT_ID} | Get an Incident
[**list_incidents**](IncidentsApi.md#list_incidents) | **GET** /data/v1/incidents | List Incidents
[**list_related_incidents**](IncidentsApi.md#list_related_incidents) | **GET** /data/v1/incidents/{INCIDENT_ID}/related | List Related Incidents


# **get_incident**
> IncidentResponse get_incident(incident_id)

Get an Incident

Returns the details of an incident.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.IncidentsApi(api_client)
    incident_id = 'abcd1234' # str | ID of the Incident

    try:
        # Get an Incident
        api_response = api_instance.get_incident(incident_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->get_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**| ID of the Incident | 

### Return type

[**IncidentResponse**](IncidentResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incidents**
> ListIncidentsResponse list_incidents(limit=limit, page=page, order_by=order_by, order_direction=order_direction, status=status, severity=severity)

List Incidents

Returns a list of incidents.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.IncidentsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
status = 'status_example' # str | Status to filter incidents by (optional)
severity = 'severity_example' # str | Severity to filter incidents by (optional)

    try:
        # List Incidents
        api_response = api_instance.list_incidents(limit=limit, page=page, order_by=order_by, order_direction=order_direction, status=status, severity=severity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->list_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **status** | **str**| Status to filter incidents by | [optional] 
 **severity** | **str**| Severity to filter incidents by | [optional] 

### Return type

[**ListIncidentsResponse**](ListIncidentsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_related_incidents**
> ListRelatedIncidentsResponse list_related_incidents(incident_id, limit=limit, page=page, order_by=order_by, order_direction=order_direction)

List Related Incidents

Returns all the incidents that seem related to a specific incident.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.IncidentsApi(api_client)
    incident_id = 'abcd1234' # str | ID of the Incident
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)

    try:
        # List Related Incidents
        api_response = api_instance.list_related_incidents(incident_id, limit=limit, page=page, order_by=order_by, order_direction=order_direction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->list_related_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**| ID of the Incident | 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 

### Return type

[**ListRelatedIncidentsResponse**](ListRelatedIncidentsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/InputFile.md
````markdown
# InputFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_format** | **str** |  | [optional]
**tracks** | [**list[InputTrack]**](InputTrack.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/InputInfo.md
````markdown
# InputInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**InputSettings**](InputSettings.md) |  | [optional]
**file** | [**InputFile**](InputFile.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/InputSettings.md
````markdown
# InputSettings

An array of objects that each describe an input file to be used to create the asset. As a shortcut, `input` can also be a string URL for a file when only one input file is used. See `input[].url` for requirements.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the file that Mux should download and use. * For the main input file, this should be the URL to the muxed file for Mux to download, for example an MP4, MOV, MKV, or TS file. Mux supports most audio/video file formats and codecs, but for fastest processing, you should [use standard inputs wherever possible](https://docs.mux.com/guides/minimize-processing-time). * For &#x60;audio&#x60; tracks, the URL is the location of the audio file for Mux to download, for example an M4A, WAV, or MP3 file. Mux supports most audio file formats and codecs, but for fastest processing, you should [use standard inputs wherever possible](https://docs.mux.com/guides/minimize-processing-time). * For &#x60;text&#x60; tracks, the URL is the location of subtitle/captions file. Mux supports [SubRip Text (SRT)](https://en.wikipedia.org/wiki/SubRip) and [Web Video Text Tracks](https://www.w3.org/TR/webvtt1/) formats for ingesting Subtitles and Closed Captions. * For Watermarking or Overlay, the URL is the location of the watermark image. The maximum size is 4096x4096. * When creating clips from existing Mux assets, the URL is defined with &#x60;mux://assets/{asset_id}&#x60; template where &#x60;asset_id&#x60; is the Asset Identifier for creating the clip from. The url property may be omitted on the first input object when providing asset settings for LiveStream and Upload objects, in order to configure settings related to the primary (live stream or direct upload) input.  | [optional]
**overlay_settings** | [**InputSettingsOverlaySettings**](InputSettingsOverlaySettings.md) |  | [optional]
**generated_subtitles** | [**list[AssetGeneratedSubtitleSettings]**](AssetGeneratedSubtitleSettings.md) | Generate subtitle tracks using automatic speech recognition with this configuration. This may only be provided for the first input object (the main input file). For direct uploads, this first input should omit the url parameter, as the main input file is provided via the direct upload. This will create subtitles based on the audio track ingested from that main input file. Note that subtitle generation happens after initial ingest, so the generated tracks will be in the &#x60;preparing&#x60; state when the asset transitions to &#x60;ready&#x60;. | [optional]
**start_time** | **float** | The time offset in seconds from the beginning of the video indicating the clip&#39;s starting marker. The default value is 0 when not included. This parameter is only applicable for creating clips when &#x60;input.url&#x60; has &#x60;mux://assets/{asset_id}&#x60; format. | [optional]
**end_time** | **float** | The time offset in seconds from the beginning of the video, indicating the clip&#39;s ending marker. The default value is the duration of the video when not included. This parameter is only applicable for creating clips when &#x60;input.url&#x60; has &#x60;mux://assets/{asset_id}&#x60; format. | [optional]
**type** | **str** | This parameter is required for &#x60;text&#x60; type tracks. | [optional]
**text_type** | **str** | Type of text track. This parameter only supports subtitles value. For more information on Subtitles / Closed Captions, [see this blog post](https://mux.com/blog/subtitles-captions-webvtt-hls-and-those-magic-flags/). This parameter is required for &#x60;text&#x60; type tracks. | [optional]
**language_code** | **str** | The language code value must be a valid [BCP 47](https://tools.ietf.org/html/bcp47) specification compliant value. For example, &#x60;en&#x60; for English or &#x60;en-US&#x60; for the US version of English. This parameter is required for &#x60;text&#x60; and &#x60;audio&#x60; track types. | [optional]
**name** | **str** | The name of the track containing a human-readable description. This value must be unique within each group of &#x60;text&#x60; or &#x60;audio&#x60; track types. The HLS manifest will associate a subtitle text track with this value. For example, the value should be \&quot;English\&quot; for a subtitle text track with &#x60;language_code&#x60; set to &#x60;en&#x60;. This optional parameter should be used only for &#x60;text&#x60; and &#x60;audio&#x60; type tracks. This parameter can be optionally provided for the first video input to denote the name of the muxed audio track if present. If this parameter is not included, Mux will auto-populate based on the &#x60;input[].language_code&#x60; value. | [optional]
**closed_captions** | **bool** | Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). This optional parameter should be used for tracks with &#x60;type&#x60; of &#x60;text&#x60; and &#x60;text_type&#x60; set to &#x60;subtitles&#x60;. | [optional]
**passthrough** | **str** | This optional parameter should be used for tracks with &#x60;type&#x60; of &#x60;text&#x60; and &#x60;text_type&#x60; set to &#x60;subtitles&#x60;. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/InputSettingsOverlaySettings.md
````markdown
# InputSettingsOverlaySettings

An object that describes how the image file referenced in URL should be placed over the video (i.e. watermarking). Ensure that the URL is active and persists the entire lifespan of the video object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vertical_align** | **str** | Where the vertical positioning of the overlay/watermark should begin from. Defaults to &#x60;\&quot;top\&quot;&#x60; | [optional]
**vertical_margin** | **str** | The distance from the vertical_align starting point and the image&#39;s closest edge. Can be expressed as a percent (\&quot;10%\&quot;) or as a pixel value (\&quot;100px\&quot;). Negative values will move the overlay offscreen. In the case of &#39;middle&#39;, a positive value will shift the overlay towards the bottom and and a negative value will shift it towards the top. | [optional]
**horizontal_align** | **str** | Where the horizontal positioning of the overlay/watermark should begin from. | [optional]
**horizontal_margin** | **str** | The distance from the horizontal_align starting point and the image&#39;s closest edge. Can be expressed as a percent (\&quot;10%\&quot;) or as a pixel value (\&quot;100px\&quot;). Negative values will move the overlay offscreen. In the case of &#39;center&#39;, a positive value will shift the image towards the right and and a negative value will shift it towards the left. | [optional]
**width** | **str** | How wide the overlay should appear. Can be expressed as a percent (\&quot;10%\&quot;) or as a pixel value (\&quot;100px\&quot;). If both width and height are left blank the width will be the true pixels of the image, applied as if the video has been scaled to fit a 1920x1080 frame. If height is supplied with no width, the width will scale proportionally to the height. | [optional]
**height** | **str** | How tall the overlay should appear. Can be expressed as a percent (\&quot;10%\&quot;) or as a pixel value (\&quot;100px\&quot;). If both width and height are left blank the height will be the true pixels of the image, applied as if the video has been scaled to fit a 1920x1080 frame. If width is supplied with no height, the height will scale proportionally to the width. | [optional]
**opacity** | **str** | How opaque the overlay should appear, expressed as a percent. (Default 100%) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/InputTrack.md
````markdown
# InputTrack

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional]
**duration** | **float** |  | [optional]
**encoding** | **str** |  | [optional]
**width** | **int** |  | [optional]
**height** | **int** |  | [optional]
**frame_rate** | **float** |  | [optional]
**sample_rate** | **int** |  | [optional]
**sample_size** | **int** |  | [optional]
**channels** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Insight.md
````markdown
# Insight

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_watch_time** | **int** |  | [optional]
**total_playing_time** | **int** |  | [optional]
**total_views** | **int** |  | [optional]
**negative_impact_score** | **float** |  | [optional]
**metric** | **float** |  | [optional]
**filter_value** | **str** |  | [optional]
**filter_column** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/LaunchWebInputResponse.md
````markdown
# LaunchWebInputResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListAllMetricValuesResponse.md
````markdown
# ListAllMetricValuesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Score]**](Score.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListAssetsResponse.md
````markdown
# ListAssetsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Asset]**](Asset.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListBreakdownValuesResponse.md
````markdown
# ListBreakdownValuesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[BreakdownValue]**](BreakdownValue.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]
**meta** | [**ListBreakdownValuesResponseMeta**](ListBreakdownValuesResponseMeta.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListBreakdownValuesResponseMeta.md
````markdown
# ListBreakdownValuesResponseMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granularity** | **str** |  | [optional]
**aggregation** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListDeliveryUsageResponse.md
````markdown
# ListDeliveryUsageResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[DeliveryReport]**](DeliveryReport.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]
**limit** | **int** | Number of assets returned in this response. Default value is 100. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListDimensionsResponse.md
````markdown
# ListDimensionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListFiltersResponseData**](ListFiltersResponseData.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListDimensionValuesResponse.md
````markdown
# ListDimensionValuesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[DimensionValue]**](DimensionValue.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListDRMConfigurationsResponse.md
````markdown
# ListDRMConfigurationsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[DRMConfiguration]**](DRMConfiguration.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListErrorsResponse.md
````markdown
# ListErrorsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Error]**](Error.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListExportsResponse.md
````markdown
# ListExportsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **list[str]** |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListFiltersResponse.md
````markdown
# ListFiltersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListFiltersResponseData**](ListFiltersResponseData.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListFiltersResponseData.md
````markdown
# ListFiltersResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **list[str]** |  | [optional]
**advanced** | **list[str]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListFilterValuesResponse.md
````markdown
# ListFilterValuesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[FilterValue]**](FilterValue.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListIncidentsResponse.md
````markdown
# ListIncidentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Incident]**](Incident.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListInsightsResponse.md
````markdown
# ListInsightsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Insight]**](Insight.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]
**meta** | [**ListBreakdownValuesResponseMeta**](ListBreakdownValuesResponseMeta.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListLiveStreamsResponse.md
````markdown
# ListLiveStreamsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[LiveStream]**](LiveStream.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListMonitoringDimensionsResponse.md
````markdown
# ListMonitoringDimensionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[ListMonitoringDimensionsResponseData]**](ListMonitoringDimensionsResponseData.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListMonitoringDimensionsResponseData.md
````markdown
# ListMonitoringDimensionsResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**display_name** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListMonitoringMetricsResponse.md
````markdown
# ListMonitoringMetricsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[ListMonitoringDimensionsResponseData]**](ListMonitoringDimensionsResponseData.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListPlaybackRestrictionsResponse.md
````markdown
# ListPlaybackRestrictionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[PlaybackRestriction]**](PlaybackRestriction.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListRealTimeDimensionsResponse.md
````markdown
# ListRealTimeDimensionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[ListMonitoringDimensionsResponseData]**](ListMonitoringDimensionsResponseData.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListRealTimeMetricsResponse.md
````markdown
# ListRealTimeMetricsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[ListMonitoringDimensionsResponseData]**](ListMonitoringDimensionsResponseData.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListRelatedIncidentsResponse.md
````markdown
# ListRelatedIncidentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Incident]**](Incident.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListSigningKeysResponse.md
````markdown
# ListSigningKeysResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[SigningKey]**](SigningKey.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListTranscriptionVocabulariesResponse.md
````markdown
# ListTranscriptionVocabulariesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[TranscriptionVocabulary]**](TranscriptionVocabulary.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListUploadsResponse.md
````markdown
# ListUploadsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[Upload]**](Upload.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListVideoViewExportsResponse.md
````markdown
# ListVideoViewExportsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[ExportDate]**](ExportDate.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListVideoViewsResponse.md
````markdown
# ListVideoViewsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[AbridgedVideoView]**](AbridgedVideoView.md) |  | [optional]
**total_row_count** | **int** |  | [optional]
**timeframe** | **list[int]** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ListWebInputsResponse.md
````markdown
# ListWebInputsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[WebInput]**](WebInput.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/LiveStream.md
````markdown
# LiveStream

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Live Stream. Max 255 characters. | [optional]
**created_at** | **str** | Time the Live Stream was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**stream_key** | **str** | Unique key used for streaming to a Mux RTMP endpoint. This should be considered as sensitive as credentials, anyone with this stream key can begin streaming. | [optional]
**active_asset_id** | **str** | The Asset that is currently being created if there is an active broadcast. | [optional]
**recent_asset_ids** | **list[str]** | An array of strings with the most recent Asset IDs that were created from this Live Stream. The most recently generated Asset ID is the last entry in the list. | [optional]
**status** | [**LiveStreamStatus**](LiveStreamStatus.md) |  | [optional]
**playback_ids** | [**list[PlaybackID]**](PlaybackID.md) | An array of Playback ID objects. Use these to create HLS playback URLs. See [Play your videos](https://docs.mux.com/guides/play-your-videos) for more details. | [optional]
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the asset. Max 255 characters. | [optional]
**audio_only** | **bool** | The live stream only processes the audio track if the value is set to true. Mux drops the video track if broadcasted. | [optional]
**embedded_subtitles** | [**list[LiveStreamEmbeddedSubtitleSettings]**](LiveStreamEmbeddedSubtitleSettings.md) | Describes the embedded closed caption configuration of the incoming live stream. | [optional]
**generated_subtitles** | [**list[LiveStreamGeneratedSubtitleSettings]**](LiveStreamGeneratedSubtitleSettings.md) | Configure the incoming live stream to include subtitles created with automatic speech recognition. Each Asset created from a live stream with &#x60;generated_subtitles&#x60; configured will automatically receive two text tracks. The first of these will have a &#x60;text_source&#x60; value of &#x60;generated_live&#x60;, and will be available with &#x60;ready&#x60; status as soon as the stream is live. The second text track will have a &#x60;text_source&#x60; value of &#x60;generated_live_final&#x60; and will contain subtitles with improved accuracy, timing, and formatting. However, &#x60;generated_live_final&#x60; tracks will not be available in &#x60;ready&#x60; status until the live stream ends. If an Asset has both &#x60;generated_live&#x60; and &#x60;generated_live_final&#x60; tracks that are &#x60;ready&#x60;, then only the &#x60;generated_live_final&#x60; track will be included during playback. | [optional]
**reconnect_window** | **float** | When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. **Max**: 1800s (30 minutes).  If not specified directly, Standard Latency streams have a Reconnect Window of 60 seconds; Reduced and Low Latency streams have a default of 0 seconds, or no Reconnect Window. For that reason, we suggest specifying a value other than zero for Reduced and Low Latency streams.  Reduced and Low Latency streams with a Reconnect Window greater than zero will insert slate media into the recorded asset while waiting for the streaming software to reconnect or when there are brief interruptions in the live stream media. When using a Reconnect Window setting higher than 60 seconds with a Standard Latency stream, we highly recommend enabling slate with the &#x60;use_slate_for_standard_latency&#x60; option.  | [optional] [default to 60]
**use_slate_for_standard_latency** | **bool** | By default, Standard Latency live streams do not have slate media inserted while waiting for live streaming software to reconnect to Mux. Setting this to true enables slate insertion on a Standard Latency stream. | [optional] [default to False]
**reconnect_slate_url** | **str** | The URL of the image file that Mux should download and use as slate media during interruptions of the live stream media. This file will be downloaded each time a new recorded asset is created from the live stream. If this is not set, the default slate media will be used. | [optional]
**reduced_latency** | **bool** | This field is deprecated. Please use &#x60;latency_mode&#x60; instead. Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this if you want lower latency for your live stream. See the [Reduce live stream latency guide](https://docs.mux.com/guides/reduce-live-stream-latency) to understand the tradeoffs. | [optional]
**low_latency** | **bool** | This field is deprecated. Please use &#x60;latency_mode&#x60; instead. Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Setting this option will enable compatibility with the LL-HLS specification for low-latency streaming. This typically has lower latency than Reduced Latency streams, and cannot be combined with Reduced Latency. | [optional]
**simulcast_targets** | [**list[SimulcastTarget]**](SimulcastTarget.md) | Each Simulcast Target contains configuration details to broadcast (or \&quot;restream\&quot;) a live stream to a third-party streaming service. [See the Stream live to 3rd party platforms guide](https://docs.mux.com/guides/stream-live-to-3rd-party-platforms). | [optional]
**latency_mode** | **str** | Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this as an alternative to setting low latency or reduced latency flags. | [optional]
**test** | **bool** | True means this live stream is a test live stream. Test live streams can be used to help evaluate the Mux Video APIs for free. There is no limit on the number of test live streams, but they are watermarked with the Mux logo, and limited to 5 minutes. The test live stream is disabled after the stream is active for 5 mins and the recorded asset also deleted after 24 hours. | [optional]
**max_continuous_duration** | **int** | The time in seconds a live stream may be continuously active before being disconnected. Defaults to 12 hours. | [optional] [default to 43200]
**srt_passphrase** | **str** | Unique key used for encrypting a stream to a Mux SRT endpoint. | [optional]
**active_ingest_protocol** | **str** | The protocol used for the active ingest stream. This is only set when the live stream is active. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/LiveStreamEmbeddedSubtitleSettings.md
````markdown
# LiveStreamEmbeddedSubtitleSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for this live stream closed caption track. | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the live stream closed caption track. Max 255 characters. | [optional]
**language_code** | **str** | The language of the closed caption stream. Value must be BCP 47 compliant. | [optional] [default to 'en']
**language_channel** | **str** | CEA-608 caption channel to read data from. | [optional] [default to 'cc1']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/LiveStreamGeneratedSubtitleSettings.md
````markdown
# LiveStreamGeneratedSubtitleSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for this live stream subtitle track. | [optional]
**passthrough** | **str** | Arbitrary metadata set for the live stream subtitle track. Max 255 characters. | [optional]
**language_code** | **str** | The language to generate subtitles in. | [optional] [default to 'en']
**transcription_vocabulary_ids** | **list[str]** | Unique identifiers for existing Transcription Vocabularies to use while generating subtitles for the live stream. If the Transcription Vocabularies provided collectively have more than 1000 phrases, only the first 1000 phrases will be included. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/LiveStreamResponse.md
````markdown
# LiveStreamResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LiveStream**](LiveStream.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/LiveStreamsApi.md
````markdown
# mux_python.LiveStreamsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_live_stream**](LiveStreamsApi.md#create_live_stream) | **POST** /video/v1/live-streams | Create a live stream
[**create_live_stream_playback_id**](LiveStreamsApi.md#create_live_stream_playback_id) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids | Create a live stream playback ID
[**create_live_stream_simulcast_target**](LiveStreamsApi.md#create_live_stream_simulcast_target) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets | Create a live stream simulcast target
[**delete_live_stream**](LiveStreamsApi.md#delete_live_stream) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID} | Delete a live stream
[**delete_live_stream_new_asset_settings_static_renditions**](LiveStreamsApi.md#delete_live_stream_new_asset_settings_static_renditions) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/new-asset-settings/static-renditions | Delete a live stream&#39;s static renditions setting for new assets
[**delete_live_stream_playback_id**](LiveStreamsApi.md#delete_live_stream_playback_id) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID} | Delete a live stream playback ID
[**delete_live_stream_simulcast_target**](LiveStreamsApi.md#delete_live_stream_simulcast_target) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID} | Delete a live stream simulcast target
[**disable_live_stream**](LiveStreamsApi.md#disable_live_stream) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/disable | Disable a live stream
[**enable_live_stream**](LiveStreamsApi.md#enable_live_stream) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/enable | Enable a live stream
[**get_live_stream**](LiveStreamsApi.md#get_live_stream) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID} | Retrieve a live stream
[**get_live_stream_playback_id**](LiveStreamsApi.md#get_live_stream_playback_id) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a live stream playback ID
[**get_live_stream_simulcast_target**](LiveStreamsApi.md#get_live_stream_simulcast_target) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID} | Retrieve a live stream simulcast target
[**list_live_streams**](LiveStreamsApi.md#list_live_streams) | **GET** /video/v1/live-streams | List live streams
[**reset_stream_key**](LiveStreamsApi.md#reset_stream_key) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/reset-stream-key | Reset a live stream&#39;s stream key
[**signal_live_stream_complete**](LiveStreamsApi.md#signal_live_stream_complete) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/complete | Signal a live stream is finished
[**update_live_stream**](LiveStreamsApi.md#update_live_stream) | **PATCH** /video/v1/live-streams/{LIVE_STREAM_ID} | Update a live stream
[**update_live_stream_embedded_subtitles**](LiveStreamsApi.md#update_live_stream_embedded_subtitles) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/embedded-subtitles | Update a live stream&#39;s embedded subtitles
[**update_live_stream_generated_subtitles**](LiveStreamsApi.md#update_live_stream_generated_subtitles) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/generated-subtitles | Update a live stream&#39;s generated subtitles
[**update_live_stream_new_asset_settings_static_renditions**](LiveStreamsApi.md#update_live_stream_new_asset_settings_static_renditions) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/new-asset-settings/static-renditions | Update live stream static renditions for new assets


# **create_live_stream**
> LiveStreamResponse create_live_stream(create_live_stream_request)

Create a live stream

Creates a new live stream. Once created, an encoder can connect to Mux via the specified stream key and begin streaming to an audience.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    create_live_stream_request = {"playback_policies":["public"],"new_asset_settings":{"playback_policies":["public"]}} # CreateLiveStreamRequest | 

    try:
        # Create a live stream
        api_response = api_instance.create_live_stream(create_live_stream_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->create_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_live_stream_request** | [**CreateLiveStreamRequest**](CreateLiveStreamRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_live_stream_playback_id**
> CreatePlaybackIDResponse create_live_stream_playback_id(live_stream_id, create_playback_id_request)

Create a live stream playback ID

Create a new playback ID for this live stream, through which a viewer can watch the streamed content of the live stream.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
create_playback_id_request = {"policy":"signed"} # CreatePlaybackIDRequest | 

    try:
        # Create a live stream playback ID
        api_response = api_instance.create_live_stream_playback_id(live_stream_id, create_playback_id_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->create_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **create_playback_id_request** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_live_stream_simulcast_target**
> SimulcastTargetResponse create_live_stream_simulcast_target(live_stream_id, create_simulcast_target_request)

Create a live stream simulcast target

Create a simulcast target for the parent live stream. Simulcast target can only be created when the parent live stream is in idle state. Only one simulcast target can be created at a time with this API.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
create_simulcast_target_request = {"url":"rtmp://live.example.com/app","stream_key":"abcdefgh","passthrough":"Example"} # CreateSimulcastTargetRequest | 

    try:
        # Create a live stream simulcast target
        api_response = api_instance.create_live_stream_simulcast_target(live_stream_id, create_simulcast_target_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->create_live_stream_simulcast_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **create_simulcast_target_request** | [**CreateSimulcastTargetRequest**](CreateSimulcastTargetRequest.md)|  | 

### Return type

[**SimulcastTargetResponse**](SimulcastTargetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream**
> delete_live_stream(live_stream_id)

Delete a live stream

Deletes a live stream from the current environment. If the live stream is currently active and being streamed to, ingest will be terminated and the encoder will be disconnected.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Delete a live stream
        api_instance.delete_live_stream(live_stream_id)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_new_asset_settings_static_renditions**
> delete_live_stream_new_asset_settings_static_renditions(live_stream_id)

Delete a live stream's static renditions setting for new assets

Deletes a live stream's static renditions settings for new assets. Further assets made via this live stream will not create static renditions unless re-added.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Delete a live stream's static renditions setting for new assets
        api_instance.delete_live_stream_new_asset_settings_static_renditions(live_stream_id)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_live_stream_new_asset_settings_static_renditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_playback_id**
> delete_live_stream_playback_id(live_stream_id, playback_id)

Delete a live stream playback ID

Deletes the playback ID for the live stream. This will not disable ingest (as the live stream still exists). New attempts to play back the live stream will fail immediately. However, current viewers will be able to continue watching the stream for some period of time.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Delete a live stream playback ID
        api_instance.delete_live_stream_playback_id(live_stream_id, playback_id)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_simulcast_target**
> delete_live_stream_simulcast_target(live_stream_id, simulcast_target_id)

Delete a live stream simulcast target

Delete the simulcast target using the simulcast target ID returned when creating the simulcast target. Simulcast Target can only be deleted when the parent live stream is in idle state.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
simulcast_target_id = 'simulcast_target_id_example' # str | The ID of the simulcast target.

    try:
        # Delete a live stream simulcast target
        api_instance.delete_live_stream_simulcast_target(live_stream_id, simulcast_target_id)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_live_stream_simulcast_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **simulcast_target_id** | **str**| The ID of the simulcast target. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_live_stream**
> DisableLiveStreamResponse disable_live_stream(live_stream_id)

Disable a live stream

Disables a live stream, making it reject incoming RTMP streams until re-enabled. The API also ends the live stream recording immediately when active. Ending the live stream recording adds the `EXT-X-ENDLIST` tag to the HLS manifest which notifies the player that this live stream is over.  Mux also closes the encoder connection immediately. Any attempt from the encoder to re-establish connection will fail till the live stream is re-enabled. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Disable a live stream
        api_response = api_instance.disable_live_stream(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->disable_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**DisableLiveStreamResponse**](DisableLiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_live_stream**
> EnableLiveStreamResponse enable_live_stream(live_stream_id)

Enable a live stream

Enables a live stream, allowing it to accept an incoming RTMP stream.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Enable a live stream
        api_response = api_instance.enable_live_stream(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->enable_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**EnableLiveStreamResponse**](EnableLiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_stream**
> LiveStreamResponse get_live_stream(live_stream_id)

Retrieve a live stream

Retrieves the details of a live stream that has previously been created. Supply the unique live stream ID that was returned from your previous request, and Mux will return the corresponding live stream information. The same information is returned when creating a live stream.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Retrieve a live stream
        api_response = api_instance.get_live_stream(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->get_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_stream_playback_id**
> GetLiveStreamPlaybackIDResponse get_live_stream_playback_id(live_stream_id, playback_id)

Retrieve a live stream playback ID

Fetches information about a live stream's playback ID, through which a viewer can watch the streamed content from this live stream.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Retrieve a live stream playback ID
        api_response = api_instance.get_live_stream_playback_id(live_stream_id, playback_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->get_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

[**GetLiveStreamPlaybackIDResponse**](GetLiveStreamPlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_stream_simulcast_target**
> SimulcastTargetResponse get_live_stream_simulcast_target(live_stream_id, simulcast_target_id)

Retrieve a live stream simulcast target

Retrieves the details of the simulcast target created for the parent live stream. Supply the unique live stream ID and simulcast target ID that was returned in the response of create simulcast target request, and Mux will return the corresponding information.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
simulcast_target_id = 'simulcast_target_id_example' # str | The ID of the simulcast target.

    try:
        # Retrieve a live stream simulcast target
        api_response = api_instance.get_live_stream_simulcast_target(live_stream_id, simulcast_target_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->get_live_stream_simulcast_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **simulcast_target_id** | **str**| The ID of the simulcast target. | 

### Return type

[**SimulcastTargetResponse**](SimulcastTargetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_live_streams**
> ListLiveStreamsResponse list_live_streams(limit=limit, page=page, stream_key=stream_key, status=status)

List live streams

Lists the live streams that currently exist in the current environment.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
stream_key = 'stream_key_example' # str | Filter response to return live stream for this stream key only (optional)
status = mux_python.LiveStreamStatus() # LiveStreamStatus | Filter response to return live streams with the specified status only (optional)

    try:
        # List live streams
        api_response = api_instance.list_live_streams(limit=limit, page=page, stream_key=stream_key, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->list_live_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **stream_key** | **str**| Filter response to return live stream for this stream key only | [optional] 
 **status** | [**LiveStreamStatus**](.md)| Filter response to return live streams with the specified status only | [optional] 

### Return type

[**ListLiveStreamsResponse**](ListLiveStreamsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_stream_key**
> LiveStreamResponse reset_stream_key(live_stream_id)

Reset a live stream's stream key

Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Reset a live stream's stream key
        api_response = api_instance.reset_stream_key(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->reset_stream_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_live_stream_complete**
> SignalLiveStreamCompleteResponse signal_live_stream_complete(live_stream_id)

Signal a live stream is finished

(Optional) End the live stream recording immediately instead of waiting for the reconnect_window. `EXT-X-ENDLIST` tag is added to the HLS manifest which notifies the player that this live stream is over.  Mux does not close the encoder connection immediately. Encoders are often configured to re-establish connections immediately which would result in a new recorded asset. For this reason, Mux waits for 60s before closing the connection with the encoder. This 60s timeframe is meant to give encoder operators a chance to disconnect from their end. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Signal a live stream is finished
        api_response = api_instance.signal_live_stream_complete(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->signal_live_stream_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**SignalLiveStreamCompleteResponse**](SignalLiveStreamCompleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream**
> LiveStreamResponse update_live_stream(live_stream_id, update_live_stream_request)

Update a live stream

Updates the parameters of a previously-created live stream. This currently supports a subset of variables. Supply the live stream ID and the updated parameters and Mux will return the corresponding live stream information. The information returned will be the same after update as for subsequent get live stream requests.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_request = {"latency_mode":"standard","reconnect_window":30,"max_continuous_duration":1200} # UpdateLiveStreamRequest | 

    try:
        # Update a live stream
        api_response = api_instance.update_live_stream(live_stream_id, update_live_stream_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_request** | [**UpdateLiveStreamRequest**](UpdateLiveStreamRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_embedded_subtitles**
> LiveStreamResponse update_live_stream_embedded_subtitles(live_stream_id, update_live_stream_embedded_subtitles_request)

Update a live stream's embedded subtitles

Configures a live stream to receive embedded closed captions. The resulting Asset's subtitle text track will have `closed_captions: true` set. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_embedded_subtitles_request = {"embedded_subtitles":[{"passthrough":"Example"}]} # UpdateLiveStreamEmbeddedSubtitlesRequest | 

    try:
        # Update a live stream's embedded subtitles
        api_response = api_instance.update_live_stream_embedded_subtitles(live_stream_id, update_live_stream_embedded_subtitles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream_embedded_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_embedded_subtitles_request** | [**UpdateLiveStreamEmbeddedSubtitlesRequest**](UpdateLiveStreamEmbeddedSubtitlesRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_generated_subtitles**
> LiveStreamResponse update_live_stream_generated_subtitles(live_stream_id, update_live_stream_generated_subtitles_request)

Update a live stream's generated subtitles

Updates a live stream's automatic-speech-recognition-generated subtitle configuration. Automatic speech recognition subtitles can be removed by sending an empty array in the request payload. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_generated_subtitles_request = {"generated_subtitles":[{"name":"English CC (ASR)","language_code":"en","passthrough":"Example"}]} # UpdateLiveStreamGeneratedSubtitlesRequest | 

    try:
        # Update a live stream's generated subtitles
        api_response = api_instance.update_live_stream_generated_subtitles(live_stream_id, update_live_stream_generated_subtitles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream_generated_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_generated_subtitles_request** | [**UpdateLiveStreamGeneratedSubtitlesRequest**](UpdateLiveStreamGeneratedSubtitlesRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_new_asset_settings_static_renditions**
> LiveStreamResponse update_live_stream_new_asset_settings_static_renditions(live_stream_id, update_live_stream_new_asset_settings_static_renditions_request)

Update live stream static renditions for new assets

Updates a live stream's static renditions settings for new assets. Further assets made via this live stream will create static renditions per the settings provided. You must provide all static renditions desired.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_new_asset_settings_static_renditions_request = {"static_renditions":[{"resolution":"audio-only"},{"resolution":"highest"}]} # UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest | 

    try:
        # Update live stream static renditions for new assets
        api_response = api_instance.update_live_stream_new_asset_settings_static_renditions(live_stream_id, update_live_stream_new_asset_settings_static_renditions_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream_new_asset_settings_static_renditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_new_asset_settings_static_renditions_request** | [**UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest**](UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/LiveStreamStatus.md
````markdown
# LiveStreamStatus

`idle` indicates that there is no active broadcast. `active` indicates that there is an active broadcast and `disabled` status indicates that no future RTMP streams can be published.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Metric.md
````markdown
# Metric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional]
**type** | **str** |  | [optional]
**name** | **str** |  | [optional]
**metric** | **str** |  | [optional]
**measurement** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MetricsApi.md
````markdown
# mux_python.MetricsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_timeseries_data**](MetricsApi.md#get_metric_timeseries_data) | **GET** /data/v1/metrics/{METRIC_ID}/timeseries | Get metric timeseries data
[**get_overall_values**](MetricsApi.md#get_overall_values) | **GET** /data/v1/metrics/{METRIC_ID}/overall | Get Overall values
[**list_all_metric_values**](MetricsApi.md#list_all_metric_values) | **GET** /data/v1/metrics/comparison | List all metric values
[**list_breakdown_values**](MetricsApi.md#list_breakdown_values) | **GET** /data/v1/metrics/{METRIC_ID}/breakdown | List breakdown values
[**list_insights**](MetricsApi.md#list_insights) | **GET** /data/v1/metrics/{METRIC_ID}/insights | List Insights


# **get_metric_timeseries_data**
> GetMetricTimeseriesDataResponse get_metric_timeseries_data(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement, order_direction=order_direction, group_by=group_by)

Get metric timeseries data

Returns timeseries data for a specific metric.  Each interval represented in the data array contains an array with the following values:   * the first element is the interval time   * the second element is the calculated metric value   * the third element is the number of views in the interval that have a valid metric value 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
group_by = 'group_by_example' # str | Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the timeframe.  For timeframes of less than 90 minutes, the default granularity is `minute`. Between 90 minutes and 6 hours, the default granularity is `ten_minutes`. Between 6 hours and 15 days inclusive, the default granularity is `hour`. The granularity of timeframes that exceed 15 days is `day`. This default behavior is subject to change; it is strongly suggested that you explicitly specify the granularity.  (optional)

    try:
        # Get metric timeseries data
        api_response = api_instance.get_metric_timeseries_data(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement, order_direction=order_direction, group_by=group_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_metric_timeseries_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **group_by** | **str**| Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the timeframe.  For timeframes of less than 90 minutes, the default granularity is &#x60;minute&#x60;. Between 90 minutes and 6 hours, the default granularity is &#x60;ten_minutes&#x60;. Between 6 hours and 15 days inclusive, the default granularity is &#x60;hour&#x60;. The granularity of timeframes that exceed 15 days is &#x60;day&#x60;. This default behavior is subject to change; it is strongly suggested that you explicitly specify the granularity.  | [optional] 

### Return type

[**GetMetricTimeseriesDataResponse**](GetMetricTimeseriesDataResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overall_values**
> GetOverallValuesResponse get_overall_values(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement)

Get Overall values

Returns the overall value for a specific metric, as well as the total view count, watch time, and the Mux Global metric value for the metric.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)

    try:
        # Get Overall values
        api_response = api_instance.get_overall_values(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_overall_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 

### Return type

[**GetOverallValuesResponse**](GetOverallValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_metric_values**
> ListAllMetricValuesResponse list_all_metric_values(timeframe=timeframe, filters=filters, metric_filters=metric_filters, dimension=dimension, value=value)

List all metric values

List all of the values across every breakdown for a specific metric.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MetricsApi(api_client)
    timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
dimension = 'dimension_example' # str | Dimension the specified value belongs to (optional)
value = 'value_example' # str | Value to show all available metrics for (optional)

    try:
        # List all metric values
        api_response = api_instance.list_all_metric_values(timeframe=timeframe, filters=filters, metric_filters=metric_filters, dimension=dimension, value=value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_all_metric_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **dimension** | **str**| Dimension the specified value belongs to | [optional] 
 **value** | **str**| Value to show all available metrics for | [optional] 

### Return type

[**ListAllMetricValuesResponse**](ListAllMetricValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_breakdown_values**
> ListBreakdownValuesResponse list_breakdown_values(metric_id, group_by=group_by, measurement=measurement, filters=filters, metric_filters=metric_filters, limit=limit, page=page, order_by=order_by, order_direction=order_direction, timeframe=timeframe)

List breakdown values

List the breakdown values for a specific metric.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
group_by = 'group_by_example' # str | Breakdown value to group the results by (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # List breakdown values
        api_response = api_instance.list_breakdown_values(metric_id, group_by=group_by, measurement=measurement, filters=filters, metric_filters=metric_filters, limit=limit, page=page, order_by=order_by, order_direction=order_direction, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_breakdown_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **group_by** | **str**| Breakdown value to group the results by | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListBreakdownValuesResponse**](ListBreakdownValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_insights**
> ListInsightsResponse list_insights(metric_id, measurement=measurement, order_direction=order_direction, timeframe=timeframe, filters=filters, metric_filters=metric_filters)

List Insights

Returns a list of insights for a metric. These are the worst performing values across all breakdowns sorted by how much they negatively impact a specific metric.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)

    try:
        # List Insights
        api_response = api_instance.list_insights(metric_id, measurement=measurement, order_direction=order_direction, timeframe=timeframe, filters=filters, metric_filters=metric_filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 

### Return type

[**ListInsightsResponse**](ListInsightsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/MonitoringApi.md
````markdown
# mux_python.MonitoringApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_monitoring_breakdown**](MonitoringApi.md#get_monitoring_breakdown) | **GET** /data/v1/monitoring/metrics/{MONITORING_METRIC_ID}/breakdown | Get Monitoring Breakdown
[**get_monitoring_breakdown_timeseries**](MonitoringApi.md#get_monitoring_breakdown_timeseries) | **GET** /data/v1/monitoring/metrics/{MONITORING_METRIC_ID}/breakdown-timeseries | Get Monitoring Breakdown Timeseries
[**get_monitoring_histogram_timeseries**](MonitoringApi.md#get_monitoring_histogram_timeseries) | **GET** /data/v1/monitoring/metrics/{MONITORING_HISTOGRAM_METRIC_ID}/histogram-timeseries | Get Monitoring Histogram Timeseries
[**get_monitoring_timeseries**](MonitoringApi.md#get_monitoring_timeseries) | **GET** /data/v1/monitoring/metrics/{MONITORING_METRIC_ID}/timeseries | Get Monitoring Timeseries
[**list_monitoring_dimensions**](MonitoringApi.md#list_monitoring_dimensions) | **GET** /data/v1/monitoring/dimensions | List Monitoring Dimensions
[**list_monitoring_metrics**](MonitoringApi.md#list_monitoring_metrics) | **GET** /data/v1/monitoring/metrics | List Monitoring Metrics


# **get_monitoring_breakdown**
> GetMonitoringBreakdownResponse get_monitoring_breakdown(monitoring_metric_id, dimension=dimension, timestamp=timestamp, filters=filters, order_by=order_by, order_direction=order_direction)

Get Monitoring Breakdown

Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MonitoringApi(api_client)
    monitoring_metric_id = 'current-concurrent-viewers' # str | ID of the Monitoring Metric
dimension = 'dimension_example' # str | Dimension the specified value belongs to (optional)
timestamp = 56 # int | Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)

    try:
        # Get Monitoring Breakdown
        api_response = api_instance.get_monitoring_breakdown(monitoring_metric_id, dimension=dimension, timestamp=timestamp, filters=filters, order_by=order_by, order_direction=order_direction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_monitoring_breakdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_metric_id** | **str**| ID of the Monitoring Metric | 
 **dimension** | **str**| Dimension the specified value belongs to | [optional] 
 **timestamp** | **int**| Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 

### Return type

[**GetMonitoringBreakdownResponse**](GetMonitoringBreakdownResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_breakdown_timeseries**
> GetMonitoringBreakdownTimeseriesResponse get_monitoring_breakdown_timeseries(monitoring_metric_id, dimension=dimension, timeframe=timeframe, filters=filters, limit=limit, order_by=order_by, order_direction=order_direction)

Get Monitoring Breakdown Timeseries

Gets timeseries of breakdown information for a specific dimension and metric. Each datapoint in the response represents 5 seconds worth of data.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MonitoringApi(api_client)
    monitoring_metric_id = 'current-concurrent-viewers' # str | ID of the Monitoring Metric
dimension = 'dimension_example' # str | Dimension the specified value belongs to (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  The default for this is the last 60 seconds of available data. Timeframes larger than 10 minutes are not allowed, and must be within the last 24 hours.  (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
limit = 10 # int | Number of items to include in each timestamp's `value` list.  The default is 10, and the maximum is 100.  (optional) (default to 10)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)

    try:
        # Get Monitoring Breakdown Timeseries
        api_response = api_instance.get_monitoring_breakdown_timeseries(monitoring_metric_id, dimension=dimension, timeframe=timeframe, filters=filters, limit=limit, order_by=order_by, order_direction=order_direction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_monitoring_breakdown_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_metric_id** | **str**| ID of the Monitoring Metric | 
 **dimension** | **str**| Dimension the specified value belongs to | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  The default for this is the last 60 seconds of available data. Timeframes larger than 10 minutes are not allowed, and must be within the last 24 hours.  | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **limit** | **int**| Number of items to include in each timestamp&#39;s &#x60;value&#x60; list.  The default is 10, and the maximum is 100.  | [optional] [default to 10]
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 

### Return type

[**GetMonitoringBreakdownTimeseriesResponse**](GetMonitoringBreakdownTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_histogram_timeseries**
> GetMonitoringHistogramTimeseriesResponse get_monitoring_histogram_timeseries(monitoring_histogram_metric_id, filters=filters)

Get Monitoring Histogram Timeseries

Gets histogram timeseries information for a specific metric.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MonitoringApi(api_client)
    monitoring_histogram_metric_id = 'video-startup-time' # str | ID of the Monitoring Histogram Metric
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)

    try:
        # Get Monitoring Histogram Timeseries
        api_response = api_instance.get_monitoring_histogram_timeseries(monitoring_histogram_metric_id, filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_monitoring_histogram_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_histogram_metric_id** | **str**| ID of the Monitoring Histogram Metric | 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 

### Return type

[**GetMonitoringHistogramTimeseriesResponse**](GetMonitoringHistogramTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_timeseries**
> GetMonitoringTimeseriesResponse get_monitoring_timeseries(monitoring_metric_id, filters=filters, timestamp=timestamp)

Get Monitoring Timeseries

Gets Time series information for a specific metric along with the number of concurrent viewers.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MonitoringApi(api_client)
    monitoring_metric_id = 'current-concurrent-viewers' # str | ID of the Monitoring Metric
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
timestamp = 56 # int | Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. (optional)

    try:
        # Get Monitoring Timeseries
        api_response = api_instance.get_monitoring_timeseries(monitoring_metric_id, filters=filters, timestamp=timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_monitoring_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitoring_metric_id** | **str**| ID of the Monitoring Metric | 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timestamp** | **int**| Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. | [optional] 

### Return type

[**GetMonitoringTimeseriesResponse**](GetMonitoringTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitoring_dimensions**
> ListMonitoringDimensionsResponse list_monitoring_dimensions()

List Monitoring Dimensions

Lists available monitoring dimensions.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MonitoringApi(api_client)
    
    try:
        # List Monitoring Dimensions
        api_response = api_instance.list_monitoring_dimensions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->list_monitoring_dimensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListMonitoringDimensionsResponse**](ListMonitoringDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitoring_metrics**
> ListMonitoringMetricsResponse list_monitoring_metrics()

List Monitoring Metrics

Lists available monitoring metrics.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.MonitoringApi(api_client)
    
    try:
        # List Monitoring Metrics
        api_response = api_instance.list_monitoring_metrics()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->list_monitoring_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListMonitoringMetricsResponse**](ListMonitoringMetricsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/MonitoringBreakdownTimeseriesDatapoint.md
````markdown
# MonitoringBreakdownTimeseriesDatapoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**metric_value** | **float** |  | [optional]
**concurrent_viewers** | **int** |  | [optional]
**starting_up_viewers** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MonitoringBreakdownTimeseriesValues.md
````markdown
# MonitoringBreakdownTimeseriesValues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**list[MonitoringBreakdownTimeseriesDatapoint]**](MonitoringBreakdownTimeseriesDatapoint.md) |  | [optional]
**date** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MonitoringBreakdownValue.md
````markdown
# MonitoringBreakdownValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**negative_impact** | **int** |  | [optional]
**metric_value** | **float** |  | [optional]
**display_value** | **str** |  | [optional]
**concurrent_viewers** | **int** |  | [optional]
**starting_up_viewers** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MonitoringHistogramTimeseriesBucket.md
````markdown
# MonitoringHistogramTimeseriesBucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | [optional]
**end** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MonitoringHistogramTimeseriesBucketValues.md
````markdown
# MonitoringHistogramTimeseriesBucketValues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** |  | [optional]
**count** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MonitoringHistogramTimeseriesDatapoint.md
````markdown
# MonitoringHistogramTimeseriesDatapoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional]
**sum** | **int** |  | [optional]
**p95** | **float** |  | [optional]
**median** | **float** |  | [optional]
**max_percentage** | **float** |  | [optional]
**bucket_values** | [**list[MonitoringHistogramTimeseriesBucketValues]**](MonitoringHistogramTimeseriesBucketValues.md) |  | [optional]
**average** | **float** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/MonitoringTimeseriesDatapoint.md
````markdown
# MonitoringTimeseriesDatapoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional]
**date** | **str** |  | [optional]
**concurrent_viewers** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/NotificationRule.md
````markdown
# NotificationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**name** | **str** |  | [optional]
**id** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/OverallValues.md
````markdown
# OverallValues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional]
**total_watch_time** | **int** |  | [optional]
**total_views** | **int** |  | [optional]
**total_playing_time** | **int** |  | [optional]
**global_value** | **float** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/PlaybackID.md
````markdown
# PlaybackID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the PlaybackID | [optional]
**policy** | [**PlaybackPolicy**](PlaybackPolicy.md) |  | [optional]
**drm_configuration_id** | **str** | The DRM configuration used by this playback ID. Must only be set when &#x60;policy&#x60; is set to &#x60;drm&#x60;. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/PlaybackIDApi.md
````markdown
# mux_python.PlaybackIDApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_or_livestream_id**](PlaybackIDApi.md#get_asset_or_livestream_id) | **GET** /video/v1/playback-ids/{PLAYBACK_ID} | Retrieve an asset or live stream ID


# **get_asset_or_livestream_id**
> GetAssetOrLiveStreamIdResponse get_asset_or_livestream_id(playback_id)

Retrieve an asset or live stream ID

Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackIDApi(api_client)
    playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Retrieve an asset or live stream ID
        api_response = api_instance.get_asset_or_livestream_id(playback_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackIDApi->get_asset_or_livestream_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

[**GetAssetOrLiveStreamIdResponse**](GetAssetOrLiveStreamIdResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/PlaybackPolicy.md
````markdown
# PlaybackPolicy

* `public` playback IDs are accessible by constructing an HLS URL like `https://stream.mux.com/${PLAYBACK_ID}`  * `signed` playback IDs should be used with tokens `https://stream.mux.com/${PLAYBACK_ID}?token={TOKEN}`. See [Secure video playback](https://docs.mux.com/guides/secure-video-playback) for details about creating tokens.  * `drm` playback IDs are protected with DRM technologies. [See DRM documentation for more details](https://docs.mux.com/guides/protect-videos-with-drm). 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/PlaybackRestriction.md
````markdown
# PlaybackRestriction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Playback Restriction. Max 255 characters. | [optional]
**created_at** | **str** | Time the Playback Restriction was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**updated_at** | **str** | Time the Playback Restriction was last updated, defined as a Unix timestamp (seconds since epoch). | [optional]
**referrer** | [**ReferrerDomainRestriction**](ReferrerDomainRestriction.md) |  | [optional]
**user_agent** | [**UserAgentRestrictionSettings**](UserAgentRestrictionSettings.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/PlaybackRestrictionResponse.md
````markdown
# PlaybackRestrictionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaybackRestriction**](PlaybackRestriction.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/PlaybackRestrictionsApi.md
````markdown
# mux_python.PlaybackRestrictionsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_playback_restriction**](PlaybackRestrictionsApi.md#create_playback_restriction) | **POST** /video/v1/playback-restrictions | Create a Playback Restriction
[**delete_playback_restriction**](PlaybackRestrictionsApi.md#delete_playback_restriction) | **DELETE** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID} | Delete a Playback Restriction
[**get_playback_restriction**](PlaybackRestrictionsApi.md#get_playback_restriction) | **GET** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID} | Retrieve a Playback Restriction
[**list_playback_restrictions**](PlaybackRestrictionsApi.md#list_playback_restrictions) | **GET** /video/v1/playback-restrictions | List Playback Restrictions
[**update_referrer_domain_restriction**](PlaybackRestrictionsApi.md#update_referrer_domain_restriction) | **PUT** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID}/referrer | Update the Referrer Playback Restriction
[**update_user_agent_restriction**](PlaybackRestrictionsApi.md#update_user_agent_restriction) | **PUT** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID}/user_agent | Update the User Agent Restriction


# **create_playback_restriction**
> PlaybackRestrictionResponse create_playback_restriction(create_playback_restriction_request)

Create a Playback Restriction

Create a new Playback Restriction.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    create_playback_restriction_request = {"referrer":{"allowed_domains":["*.example.com"],"allow_no_referrer":true},"user_agent":{"allow_no_user_agent":false,"allow_high_risk_user_agent":false}} # CreatePlaybackRestrictionRequest | 

    try:
        # Create a Playback Restriction
        api_response = api_instance.create_playback_restriction(create_playback_restriction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->create_playback_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_playback_restriction_request** | [**CreatePlaybackRestrictionRequest**](CreatePlaybackRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_playback_restriction**
> delete_playback_restriction(playback_restriction_id)

Delete a Playback Restriction

Deletes a single Playback Restriction.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.

    try:
        # Delete a Playback Restriction
        api_instance.delete_playback_restriction(playback_restriction_id)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->delete_playback_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playback_restriction**
> PlaybackRestrictionResponse get_playback_restriction(playback_restriction_id)

Retrieve a Playback Restriction

Retrieves a Playback Restriction associated with the unique identifier.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.

    try:
        # Retrieve a Playback Restriction
        api_response = api_instance.get_playback_restriction(playback_restriction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->get_playback_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_playback_restrictions**
> ListPlaybackRestrictionsResponse list_playback_restrictions(page=page, limit=limit)

List Playback Restrictions

Returns a list of all Playback Restrictions.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)

    try:
        # List Playback Restrictions
        api_response = api_instance.list_playback_restrictions(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->list_playback_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]

### Return type

[**ListPlaybackRestrictionsResponse**](ListPlaybackRestrictionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_referrer_domain_restriction**
> PlaybackRestrictionResponse update_referrer_domain_restriction(playback_restriction_id, update_referrer_domain_restriction_request)

Update the Referrer Playback Restriction

Allows you to modify the list of domains or change how Mux validates playback requests without the `Referer` HTTP header. The Referrer restriction fully replaces the old list with this new list of domains.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.
update_referrer_domain_restriction_request = {"allowed_domains":["*.example.com"],"allow_no_referrer":true} # UpdateReferrerDomainRestrictionRequest | 

    try:
        # Update the Referrer Playback Restriction
        api_response = api_instance.update_referrer_domain_restriction(playback_restriction_id, update_referrer_domain_restriction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->update_referrer_domain_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 
 **update_referrer_domain_restriction_request** | [**UpdateReferrerDomainRestrictionRequest**](UpdateReferrerDomainRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_agent_restriction**
> PlaybackRestrictionResponse update_user_agent_restriction(playback_restriction_id, update_user_agent_restriction_request)

Update the User Agent Restriction

Allows you to modify how Mux validates playback requests with different user agents.  Please see [Using User-Agent HTTP header for validation](https://docs.mux.com/guides/secure-video-playback#using-user-agent-http-header-for-validation) for more details on this feature.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.
update_user_agent_restriction_request = {"allow_no_user_agent":false,"allow_high_risk_user_agent":false} # UpdateUserAgentRestrictionRequest | 

    try:
        # Update the User Agent Restriction
        api_response = api_instance.update_user_agent_restriction(playback_restriction_id, update_user_agent_restriction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->update_user_agent_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 
 **update_user_agent_restriction_request** | [**UpdateUserAgentRestrictionRequest**](UpdateUserAgentRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/RealTimeApi.md
````markdown
# mux_python.RealTimeApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_realtime_breakdown**](RealTimeApi.md#get_realtime_breakdown) | **GET** /data/v1/realtime/metrics/{REALTIME_METRIC_ID}/breakdown | Get Real-Time Breakdown
[**get_realtime_histogram_timeseries**](RealTimeApi.md#get_realtime_histogram_timeseries) | **GET** /data/v1/realtime/metrics/{REALTIME_HISTOGRAM_METRIC_ID}/histogram-timeseries | Get Real-Time Histogram Timeseries
[**get_realtime_timeseries**](RealTimeApi.md#get_realtime_timeseries) | **GET** /data/v1/realtime/metrics/{REALTIME_METRIC_ID}/timeseries | Get Real-Time Timeseries
[**list_realtime_dimensions**](RealTimeApi.md#list_realtime_dimensions) | **GET** /data/v1/realtime/dimensions | List Real-Time Dimensions
[**list_realtime_metrics**](RealTimeApi.md#list_realtime_metrics) | **GET** /data/v1/realtime/metrics | List Real-Time Metrics


# **get_realtime_breakdown**
> GetRealTimeBreakdownResponse get_realtime_breakdown(realtime_metric_id, dimension=dimension, timestamp=timestamp, filters=filters, order_by=order_by, order_direction=order_direction)

Get Real-Time Breakdown

Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score. This API is now deprecated, please use the `Get Monitoring Breakdown` API.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.RealTimeApi(api_client)
    realtime_metric_id = 'current-concurrent-viewers' # str | ID of the Realtime Metric
dimension = 'dimension_example' # str | Dimension the specified value belongs to (optional)
timestamp = 56 # int | Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)

    try:
        # Get Real-Time Breakdown
        api_response = api_instance.get_realtime_breakdown(realtime_metric_id, dimension=dimension, timestamp=timestamp, filters=filters, order_by=order_by, order_direction=order_direction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->get_realtime_breakdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realtime_metric_id** | **str**| ID of the Realtime Metric | 
 **dimension** | **str**| Dimension the specified value belongs to | [optional] 
 **timestamp** | **int**| Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 

### Return type

[**GetRealTimeBreakdownResponse**](GetRealTimeBreakdownResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_realtime_histogram_timeseries**
> GetRealTimeHistogramTimeseriesResponse get_realtime_histogram_timeseries(realtime_histogram_metric_id, filters=filters)

Get Real-Time Histogram Timeseries

Gets histogram timeseries information for a specific metric. This API is now deprecated, please use the `Get Monitoring Histogram Timeseries` API.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.RealTimeApi(api_client)
    realtime_histogram_metric_id = 'video-startup-time' # str | ID of the Realtime Histogram Metric
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)

    try:
        # Get Real-Time Histogram Timeseries
        api_response = api_instance.get_realtime_histogram_timeseries(realtime_histogram_metric_id, filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->get_realtime_histogram_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realtime_histogram_metric_id** | **str**| ID of the Realtime Histogram Metric | 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 

### Return type

[**GetRealTimeHistogramTimeseriesResponse**](GetRealTimeHistogramTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_realtime_timeseries**
> GetRealTimeTimeseriesResponse get_realtime_timeseries(realtime_metric_id, filters=filters, timestamp=timestamp)

Get Real-Time Timeseries

Gets Time series information for a specific metric along with the number of concurrent viewers. This API is now deprecated, please use the `Get Monitoring Timeseries` API.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.RealTimeApi(api_client)
    realtime_metric_id = 'current-concurrent-viewers' # str | ID of the Realtime Metric
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
timestamp = 56 # int | Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. (optional)

    try:
        # Get Real-Time Timeseries
        api_response = api_instance.get_realtime_timeseries(realtime_metric_id, filters=filters, timestamp=timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->get_realtime_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realtime_metric_id** | **str**| ID of the Realtime Metric | 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timestamp** | **int**| Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. | [optional] 

### Return type

[**GetRealTimeTimeseriesResponse**](GetRealTimeTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_realtime_dimensions**
> ListRealTimeDimensionsResponse list_realtime_dimensions()

List Real-Time Dimensions

Lists available real-time dimensions. This API is now deprecated, please use the `List Monitoring Dimensions` API.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.RealTimeApi(api_client)
    
    try:
        # List Real-Time Dimensions
        api_response = api_instance.list_realtime_dimensions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->list_realtime_dimensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRealTimeDimensionsResponse**](ListRealTimeDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_realtime_metrics**
> ListRealTimeMetricsResponse list_realtime_metrics()

List Real-Time Metrics

Lists available real-time metrics. This API is now deprecated, please use the `List Monitoring Metrics` API.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.RealTimeApi(api_client)
    
    try:
        # List Real-Time Metrics
        api_response = api_instance.list_realtime_metrics()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->list_realtime_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRealTimeMetricsResponse**](ListRealTimeMetricsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/RealTimeBreakdownValue.md
````markdown
# RealTimeBreakdownValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional]
**negative_impact** | **int** |  | [optional]
**metric_value** | **float** |  | [optional]
**display_value** | **str** |  | [optional]
**concurrent_viewers** | **int** |  | [optional]
**starting_up_viewers** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/RealTimeHistogramTimeseriesBucket.md
````markdown
# RealTimeHistogramTimeseriesBucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | [optional]
**end** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/RealTimeHistogramTimeseriesBucketValues.md
````markdown
# RealTimeHistogramTimeseriesBucketValues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** |  | [optional]
**count** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/RealTimeHistogramTimeseriesDatapoint.md
````markdown
# RealTimeHistogramTimeseriesDatapoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional]
**sum** | **int** |  | [optional]
**p95** | **float** |  | [optional]
**median** | **float** |  | [optional]
**max_percentage** | **float** |  | [optional]
**bucket_values** | [**list[RealTimeHistogramTimeseriesBucketValues]**](RealTimeHistogramTimeseriesBucketValues.md) |  | [optional]
**average** | **float** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/RealTimeTimeseriesDatapoint.md
````markdown
# RealTimeTimeseriesDatapoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional]
**date** | **str** |  | [optional]
**concurrent_viewers** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ReferrerDomainRestriction.md
````markdown
# ReferrerDomainRestriction

A list of domains allowed to play your videos.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_domains** | **list[str]** | List of domains allowed to play videos. Possible values are   * &#x60;[]&#x60; Empty Array indicates deny video playback requests for all domains   * &#x60;[\&quot;*\&quot;]&#x60; A Single Wildcard &#x60;*&#x60; entry means allow video playback requests from any domain   * &#x60;[\&quot;*.example.com\&quot;, \&quot;foo.com\&quot;]&#x60; A list of up to 10 domains or valid dns-style wildcards  | [optional]
**allow_no_referrer** | **bool** | A boolean to determine whether to allow or deny HTTP requests without &#x60;Referer&#x60; HTTP request header. Playback requests coming from non-web/native applications like iOS, Android or smart TVs will not have a &#x60;Referer&#x60; HTTP header. Set this value to &#x60;true&#x60; to allow these playback requests. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ReloadWebInputResponse.md
````markdown
# ReloadWebInputResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Score.md
````markdown
# Score

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watch_time** | **int** |  | [optional]
**view_count** | **int** |  | [optional]
**unique_viewers** | **int** |  | [optional]
**started_views** | **int** |  | [optional]
**total_playing_time** | **int** |  | [optional]
**name** | **str** |  | [optional]
**ended_views** | **int** |  | [optional]
**value** | **float** |  | [optional]
**type** | **str** |  | [optional]
**metric** | **str** |  | [optional]
**items** | [**list[Metric]**](Metric.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/ShutdownWebInputResponse.md
````markdown
# ShutdownWebInputResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/SignalLiveStreamCompleteResponse.md
````markdown
# SignalLiveStreamCompleteResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/SigningKey.md
````markdown
# SigningKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Signing Key. | [optional]
**created_at** | **str** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional]
**private_key** | **str** | A Base64 encoded private key that can be used with the RS256 algorithm when creating a [JWT](https://jwt.io/). **Note that this value is only returned once when creating a URL signing key.** | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/SigningKeyResponse.md
````markdown
# SigningKeyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SigningKey**](SigningKey.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/SigningKeysApi.md
````markdown
# mux_python.SigningKeysApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signing_key**](SigningKeysApi.md#create_signing_key) | **POST** /system/v1/signing-keys | Create a signing key
[**delete_signing_key**](SigningKeysApi.md#delete_signing_key) | **DELETE** /system/v1/signing-keys/{SIGNING_KEY_ID} | Delete a signing key
[**get_signing_key**](SigningKeysApi.md#get_signing_key) | **GET** /system/v1/signing-keys/{SIGNING_KEY_ID} | Retrieve a signing key
[**list_signing_keys**](SigningKeysApi.md#list_signing_keys) | **GET** /system/v1/signing-keys | List signing keys


# **create_signing_key**
> SigningKeyResponse create_signing_key()

Create a signing key

Creates a new signing key pair. When creating a new signing key, the API will generate a 2048-bit RSA key-pair and return the private key and a generated key-id; the public key will be stored at Mux to validate signed tokens.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.SigningKeysApi(api_client)
    
    try:
        # Create a signing key
        api_response = api_instance.create_signing_key()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigningKeysApi->create_signing_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SigningKeyResponse**](SigningKeyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_signing_key**
> delete_signing_key(signing_key_id)

Delete a signing key

Deletes an existing signing key. Use with caution, as this will invalidate any existing signatures and no JWTs can be signed using the key again.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.SigningKeysApi(api_client)
    signing_key_id = 'signing_key_id_example' # str | The ID of the signing key.

    try:
        # Delete a signing key
        api_instance.delete_signing_key(signing_key_id)
    except ApiException as e:
        print("Exception when calling SigningKeysApi->delete_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signing_key_id** | **str**| The ID of the signing key. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_key**
> SigningKeyResponse get_signing_key(signing_key_id)

Retrieve a signing key

Retrieves the details of a signing key that has previously been created. Supply the unique signing key ID that was returned from your previous request, and Mux will return the corresponding signing key information. **The private key is not returned in this response.** 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.SigningKeysApi(api_client)
    signing_key_id = 'signing_key_id_example' # str | The ID of the signing key.

    try:
        # Retrieve a signing key
        api_response = api_instance.get_signing_key(signing_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigningKeysApi->get_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signing_key_id** | **str**| The ID of the signing key. | 

### Return type

[**SigningKeyResponse**](SigningKeyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signing_keys**
> ListSigningKeysResponse list_signing_keys(limit=limit, page=page)

List signing keys

Returns a list of signing keys.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.SigningKeysApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

    try:
        # List signing keys
        api_response = api_instance.list_signing_keys(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigningKeysApi->list_signing_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListSigningKeysResponse**](ListSigningKeysResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/SimulcastTarget.md
````markdown
# SimulcastTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Simulcast Target | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set when creating a simulcast target. | [optional]
**status** | **str** | The current status of the simulcast target. See Statuses below for detailed description.   * &#x60;idle&#x60;: Default status. When the parent live stream is in disconnected status, simulcast targets will be idle state.   * &#x60;starting&#x60;: The simulcast target transitions into this state when the parent live stream transition into connected state.   * &#x60;broadcasting&#x60;: The simulcast target has successfully connected to the third party live streaming service and is pushing video to that service.   * &#x60;errored&#x60;: The simulcast target encountered an error either while attempting to connect to the third party live streaming service, or mid-broadcasting. When a simulcast target has this status it will have an &#x60;error_severity&#x60; field with more details about the error.  | [optional]
**stream_key** | **str** | Stream Key represents a stream identifier on the third party live streaming service to send the parent live stream to. Only used for RTMP(s) simulcast destinations. | [optional]
**url** | **str** | The RTMP(s) or SRT endpoint for a simulcast destination. * For RTMP(s) destinations, this should include the application name for the third party live streaming service, for example: &#x60;rtmp://live.example.com/app&#x60;. * For SRT destinations, this should be a fully formed SRT connection string, for example: &#x60;srt://srt-live.example.com:1234?streamid&#x3D;{stream_key}&amp;passphrase&#x3D;{srt_passphrase}&#x60;.  Note: SRT simulcast targets can only be used when an source is connected over SRT.  | [optional]
**error_severity** | **str** | The severity of the error encountered by the simulcast target. This field is only set when the simulcast target is in the &#x60;errored&#x60; status. See the values of severities below and their descriptions.   * &#x60;normal&#x60;: The simulcast target encountered an error either while attempting to connect to the third party live streaming service, or mid-broadcasting. A simulcast may transition back into the broadcasting state if a connection with the service can be re-established.   * &#x60;fatal&#x60;: The simulcast target is incompatible with the current input to the parent live stream. No further attempts to this simulcast target will be made for the current live stream asset.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/SimulcastTargetResponse.md
````markdown
# SimulcastTargetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SimulcastTarget**](SimulcastTarget.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/StaticRendition.md
````markdown
# StaticRendition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the static rendition file | [optional]
**ext** | **str** | Extension of the static rendition file | [optional]
**height** | **int** | The height of the static rendition&#39;s file in pixels | [optional]
**width** | **int** | The width of the static rendition&#39;s file in pixels | [optional]
**bitrate** | **int** | The bitrate in bits per second | [optional]
**filesize** | **str** | The file size in bytes | [optional]
**type** | **str** | Indicates the static rendition type of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**status** | **str** | Indicates the status of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. * &#x60;ready&#x60; indicates the MP4 has been generated and is ready for download * &#x60;preparing&#x60; indicates the asset has not been ingested or the static rendition is still being generated after an asset is ready * &#x60;skipped&#x60; indicates the static rendition will not be generated because the requested resolution conflicts with the asset attributes after the asset has been ingested * &#x60;errored&#x60; indicates the static rendition cannot be generated. For example, an asset could not be ingested  | [optional]
**resolution_tier** | **str** | Indicates the resolution tier of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**resolution** | **str** | Indicates the resolution of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**id** | **str** | The ID of this static rendition, used in managing this static rendition. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the static rendition. Max 255 characters. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Track.md
````markdown
# Track

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Track | [optional]
**type** | **str** | The type of track | [optional]
**duration** | **float** | The duration in seconds of the track media. This parameter is not set for &#x60;text&#x60; type tracks. This field is optional and may not be set. The top level &#x60;duration&#x60; field of an asset will always be set. | [optional]
**max_width** | **int** | The maximum width in pixels available for the track. Only set for the &#x60;video&#x60; type track. | [optional]
**max_height** | **int** | The maximum height in pixels available for the track. Only set for the &#x60;video&#x60; type track. | [optional]
**max_frame_rate** | **float** | The maximum frame rate available for the track. Only set for the &#x60;video&#x60; type track. This field may return &#x60;-1&#x60; if the frame rate of the input cannot be reliably determined. | [optional]
**max_channels** | **int** | The maximum number of audio channels the track supports. Only set for the &#x60;audio&#x60; type track. | [optional]
**max_channel_layout** | **str** | Only set for the &#x60;audio&#x60; type track. | [optional]
**text_type** | **str** | This parameter is only set for &#x60;text&#x60; type tracks. | [optional]
**text_source** | **str** | The source of the text contained in a Track of type &#x60;text&#x60;. Valid &#x60;text_source&#x60; values are listed below. * &#x60;uploaded&#x60;: Tracks uploaded to Mux as caption or subtitle files using the Create Asset Track API. * &#x60;embedded&#x60;: Tracks extracted from an embedded stream of CEA-608 closed captions. * &#x60;generated_vod&#x60;: Tracks generated by automatic speech recognition on an on-demand asset. * &#x60;generated_live&#x60;: Tracks generated by automatic speech recognition on a live stream configured with &#x60;generated_subtitles&#x60;. If an Asset has both &#x60;generated_live&#x60; and &#x60;generated_live_final&#x60; tracks that are &#x60;ready&#x60;, then only the &#x60;generated_live_final&#x60; track will be included during playback. * &#x60;generated_live_final&#x60;: Tracks generated by automatic speech recognition on a live stream using &#x60;generated_subtitles&#x60;. The accuracy, timing, and formatting of these subtitles is improved compared to the corresponding &#x60;generated_live&#x60; tracks. However, &#x60;generated_live_final&#x60; tracks will not be available in &#x60;ready&#x60; status until the live stream ends. If an Asset has both &#x60;generated_live&#x60; and &#x60;generated_live_final&#x60; tracks that are &#x60;ready&#x60;, then only the &#x60;generated_live_final&#x60; track will be included during playback.  | [optional]
**language_code** | **str** | The language code value represents [BCP 47](https://tools.ietf.org/html/bcp47) specification compliant value. For example, &#x60;en&#x60; for English or &#x60;en-US&#x60; for the US version of English. This parameter is only set for &#x60;text&#x60; and &#x60;audio&#x60; track types. | [optional]
**name** | **str** | The name of the track containing a human-readable description. The HLS manifest will associate a subtitle &#x60;text&#x60; or &#x60;audio&#x60; track with this value. For example, the value should be \&quot;English\&quot; for a subtitle text track for the &#x60;language_code&#x60; value of &#x60;en-US&#x60;. This parameter is only set for &#x60;text&#x60; and &#x60;audio&#x60; track types. | [optional]
**closed_captions** | **bool** | Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). This parameter is only set tracks where &#x60;type&#x60; is &#x60;text&#x60; and &#x60;text_type&#x60; is &#x60;subtitles&#x60;. | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the track either when creating the asset or track. This parameter is only set for &#x60;text&#x60; type tracks. Max 255 characters. | [optional]
**status** | **str** | The status of the track. This parameter is only set for &#x60;text&#x60; type tracks. | [optional]
**primary** | **bool** | For an audio track, indicates that this is the primary audio track, ingested from the main input for this asset. The primary audio track cannot be deleted. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/TranscriptionVocabulariesApi.md
````markdown
# mux_python.TranscriptionVocabulariesApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transcription_vocabulary**](TranscriptionVocabulariesApi.md#create_transcription_vocabulary) | **POST** /video/v1/transcription-vocabularies | Create a Transcription Vocabulary
[**delete_transcription_vocabulary**](TranscriptionVocabulariesApi.md#delete_transcription_vocabulary) | **DELETE** /video/v1/transcription-vocabularies/{TRANSCRIPTION_VOCABULARY_ID} | Delete a Transcription Vocabulary
[**get_transcription_vocabulary**](TranscriptionVocabulariesApi.md#get_transcription_vocabulary) | **GET** /video/v1/transcription-vocabularies/{TRANSCRIPTION_VOCABULARY_ID} | Retrieve a Transcription Vocabulary
[**list_transcription_vocabularies**](TranscriptionVocabulariesApi.md#list_transcription_vocabularies) | **GET** /video/v1/transcription-vocabularies | List Transcription Vocabularies
[**update_transcription_vocabulary**](TranscriptionVocabulariesApi.md#update_transcription_vocabulary) | **PUT** /video/v1/transcription-vocabularies/{TRANSCRIPTION_VOCABULARY_ID} | Update a Transcription Vocabulary


# **create_transcription_vocabulary**
> TranscriptionVocabularyResponse create_transcription_vocabulary(create_transcription_vocabulary_request)

Create a Transcription Vocabulary

Create a new Transcription Vocabulary.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.TranscriptionVocabulariesApi(api_client)
    create_transcription_vocabulary_request = {"name":"Mux API Vocabulary","phrases":["Mux","Live Stream","Playback ID","video encoding"]} # CreateTranscriptionVocabularyRequest | 

    try:
        # Create a Transcription Vocabulary
        api_response = api_instance.create_transcription_vocabulary(create_transcription_vocabulary_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranscriptionVocabulariesApi->create_transcription_vocabulary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transcription_vocabulary_request** | [**CreateTranscriptionVocabularyRequest**](CreateTranscriptionVocabularyRequest.md)|  | 

### Return type

[**TranscriptionVocabularyResponse**](TranscriptionVocabularyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transcription Vocabulary Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transcription_vocabulary**
> delete_transcription_vocabulary(transcription_vocabulary_id)

Delete a Transcription Vocabulary

Deletes a Transcription Vocabulary. The Transcription Vocabulary's ID will be disassociated from any live streams using it. Transcription Vocabularies can be deleted while associated live streams are active. However, the words and phrases in the deleted Transcription Vocabulary will remain attached to those streams while they are active.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.TranscriptionVocabulariesApi(api_client)
    transcription_vocabulary_id = 'transcription_vocabulary_id_example' # str | The ID of the Transcription Vocabulary.

    try:
        # Delete a Transcription Vocabulary
        api_instance.delete_transcription_vocabulary(transcription_vocabulary_id)
    except ApiException as e:
        print("Exception when calling TranscriptionVocabulariesApi->delete_transcription_vocabulary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription_vocabulary_id** | **str**| The ID of the Transcription Vocabulary. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcription_vocabulary**
> TranscriptionVocabularyResponse get_transcription_vocabulary(transcription_vocabulary_id)

Retrieve a Transcription Vocabulary

Retrieves the details of a Transcription Vocabulary that has previously been created. Supply the unique Transcription Vocabulary ID and Mux will return the corresponding Transcription Vocabulary information. The same information is returned when creating a Transcription Vocabulary.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.TranscriptionVocabulariesApi(api_client)
    transcription_vocabulary_id = 'transcription_vocabulary_id_example' # str | The ID of the Transcription Vocabulary.

    try:
        # Retrieve a Transcription Vocabulary
        api_response = api_instance.get_transcription_vocabulary(transcription_vocabulary_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranscriptionVocabulariesApi->get_transcription_vocabulary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription_vocabulary_id** | **str**| The ID of the Transcription Vocabulary. | 

### Return type

[**TranscriptionVocabularyResponse**](TranscriptionVocabularyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transcription_vocabularies**
> ListTranscriptionVocabulariesResponse list_transcription_vocabularies(limit=limit, page=page)

List Transcription Vocabularies

List all Transcription Vocabularies.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.TranscriptionVocabulariesApi(api_client)
    limit = 10 # int | Number of items to include in the response (optional) (default to 10)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

    try:
        # List Transcription Vocabularies
        api_response = api_instance.list_transcription_vocabularies(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranscriptionVocabulariesApi->list_transcription_vocabularies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 10]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListTranscriptionVocabulariesResponse**](ListTranscriptionVocabulariesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transcription_vocabulary**
> TranscriptionVocabularyResponse update_transcription_vocabulary(transcription_vocabulary_id, update_transcription_vocabulary_request)

Update a Transcription Vocabulary

Updates the details of a previously-created Transcription Vocabulary. Updates to Transcription Vocabularies are allowed while associated live streams are active. However, updates will not be applied to those streams while they are active.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.TranscriptionVocabulariesApi(api_client)
    transcription_vocabulary_id = 'transcription_vocabulary_id_example' # str | The ID of the Transcription Vocabulary.
update_transcription_vocabulary_request = {"name":"Mux API Vocabulary - Updated","phrases":["Mux","Live Stream","RTMP","Stream Key"]} # UpdateTranscriptionVocabularyRequest | 

    try:
        # Update a Transcription Vocabulary
        api_response = api_instance.update_transcription_vocabulary(transcription_vocabulary_id, update_transcription_vocabulary_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranscriptionVocabulariesApi->update_transcription_vocabulary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription_vocabulary_id** | **str**| The ID of the Transcription Vocabulary. | 
 **update_transcription_vocabulary_request** | [**UpdateTranscriptionVocabularyRequest**](UpdateTranscriptionVocabularyRequest.md)|  | 

### Return type

[**TranscriptionVocabularyResponse**](TranscriptionVocabularyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/TranscriptionVocabulary.md
````markdown
# TranscriptionVocabulary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Transcription Vocabulary | [optional]
**name** | **str** | The user-supplied name of the Transcription Vocabulary. | [optional]
**phrases** | **list[str]** | Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream&#39;s &#x60;generated_subtitles&#x60; configuration, the probability of successful speech recognition for these words or phrases is boosted. | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters. | [optional]
**created_at** | **str** | Time the Transcription Vocabulary was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**updated_at** | **str** | Time the Transcription Vocabulary was updated, defined as a Unix timestamp (seconds since epoch). | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/TranscriptionVocabularyResponse.md
````markdown
# TranscriptionVocabularyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TranscriptionVocabulary**](TranscriptionVocabulary.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateAssetMasterAccessRequest.md
````markdown
# UpdateAssetMasterAccessRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_access** | **str** | Add or remove access to the master version of the video. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateAssetMP4SupportRequest.md
````markdown
# UpdateAssetMP4SupportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mp4_support** | **str** | Specify what level of support for mp4 playback.  * The &#x60;capped-1080p&#x60; option produces a single MP4 file, called &#x60;capped-1080p.mp4&#x60;, with the video resolution capped at 1080p. This option produces an &#x60;audio.m4a&#x60; file for an audio-only asset. * The &#x60;audio-only&#x60; option produces a single M4A file, called &#x60;audio.m4a&#x60; for a video or an audio-only asset. MP4 generation will error when this option is specified for a video-only asset. * The &#x60;audio-only,capped-1080p&#x60; option produces both the &#x60;audio.m4a&#x60; and &#x60;capped-1080p.mp4&#x60; files. Only the &#x60;capped-1080p.mp4&#x60; file is produced for a video-only asset, while only the &#x60;audio.m4a&#x60; file is produced for an audio-only asset.  The &#x60;standard&#x60;(deprecated) option produces up to three MP4 files with different levels of resolution (&#x60;high.mp4&#x60;, &#x60;medium.mp4&#x60;, &#x60;low.mp4&#x60;, or &#x60;audio.m4a&#x60; for an audio-only asset).  &#x60;none&#x60; will delete the MP4s from the asset in question.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateAssetRequest.md
````markdown
# UpdateAssetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passthrough** | **str** | You can set this field to anything you want. It will be included in the asset details and related webhooks. If you&#39;re looking for more structured metadata, such as &#x60;title&#x60; or &#x60;external_id&#x60; , you can use the &#x60;meta&#x60; object instead. **Max: 255 characters**. In order to clear this value, the field should be included with an empty string value. | [optional]
**meta** | [**AssetMetadata**](AssetMetadata.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateLiveStreamEmbeddedSubtitlesRequest.md
````markdown
# UpdateLiveStreamEmbeddedSubtitlesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded_subtitles** | [**list[LiveStreamEmbeddedSubtitleSettings]**](LiveStreamEmbeddedSubtitleSettings.md) | Describe the embedded closed caption contents of the incoming live stream. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateLiveStreamGeneratedSubtitlesRequest.md
````markdown
# UpdateLiveStreamGeneratedSubtitlesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_subtitles** | [**list[LiveStreamGeneratedSubtitleSettings]**](LiveStreamGeneratedSubtitleSettings.md) | Update automated speech recognition subtitle configuration for a live stream. At most one subtitle track is allowed. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateLiveStreamNewAssetSettings.md
````markdown
# UpdateLiveStreamNewAssetSettings

Updates the new asset settings to use to generate a new asset for this live stream. Only the `mp4_support`, `master_access`, and `video_quality` settings may be updated. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mp4_support** | **str** | Deprecated. See the [Static Renditions API](https://www.mux.com/docs/guides/enable-static-mp4-renditions#during-live-stream-creation) for the updated API. Specify what level of support for mp4 playback should be added to new assets generated from this live stream. * The &#x60;none&#x60; option disables MP4 support for new assets. MP4 files will not be produced for an asset generated from this live stream. * The &#x60;capped-1080p&#x60; option produces a single MP4 file, called &#x60;capped-1080p.mp4&#x60;, with the video resolution capped at 1080p. This option produces an &#x60;audio.m4a&#x60; file for an audio-only asset. * The &#x60;audio-only&#x60; option produces a single M4A file, called &#x60;audio.m4a&#x60; for a video or an audio-only asset. MP4 generation will error when this option is specified for a video-only asset. * The &#x60;audio-only,capped-1080p&#x60; option produces both the &#x60;audio.m4a&#x60; and &#x60;capped-1080p.mp4&#x60; files. Only the &#x60;capped-1080p.mp4&#x60; file is produced for a video-only asset, while only the &#x60;audio.m4a&#x60; file is produced for an audio-only asset. * The &#x60;standard&#x60;(deprecated) option produces up to three MP4 files with different levels of resolution (&#x60;high.mp4&#x60;, &#x60;medium.mp4&#x60;, &#x60;low.mp4&#x60;, or &#x60;audio.m4a&#x60; for an audio-only asset).  | [optional]
**master_access** | **str** | Add or remove access to the master version of the video. | [optional]
**video_quality** | **str** | The video quality controls the cost, quality, and available platform features for the asset. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**meta** | [**AssetMetadata**](AssetMetadata.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest.md
````markdown
# UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_renditions** | [**list[CreateStaticRenditionRequest]**](CreateStaticRenditionRequest.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateLiveStreamRequest.md
````markdown
# UpdateLiveStreamRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passthrough** | **str** | Arbitrary user-supplied metadata set for the live stream. Max 255 characters. In order to clear this value, the field should be included with an empty-string value. | [optional]
**latency_mode** | **str** | Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this as an alternative to setting low latency or reduced latency flags. | [optional]
**reconnect_window** | **float** | When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset.  If not specified directly, Standard Latency streams have a Reconnect Window of 60 seconds; Reduced and Low Latency streams have a default of 0 seconds, or no Reconnect Window. For that reason, we suggest specifying a value other than zero for Reduced and Low Latency streams.  Reduced and Low Latency streams with a Reconnect Window greater than zero will insert slate media into the recorded asset while waiting for the streaming software to reconnect or when there are brief interruptions in the live stream media. When using a Reconnect Window setting higher than 60 seconds with a Standard Latency stream, we highly recommend enabling slate with the &#x60;use_slate_for_standard_latency&#x60; option.  | [optional] [default to 60]
**use_slate_for_standard_latency** | **bool** | By default, Standard Latency live streams do not have slate media inserted while waiting for live streaming software to reconnect to Mux. Setting this to true enables slate insertion on a Standard Latency stream. | [optional] [default to False]
**reconnect_slate_url** | **str** | The URL of the image file that Mux should download and use as slate media during interruptions of the live stream media. This file will be downloaded each time a new recorded asset is created from the live stream. Set this to a blank string to clear the value so that the default slate media will be used. | [optional]
**max_continuous_duration** | **int** | The time in seconds a live stream may be continuously active before being disconnected. Defaults to 12 hours. | [optional] [default to 43200]
**new_asset_settings** | [**UpdateLiveStreamNewAssetSettings**](UpdateLiveStreamNewAssetSettings.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateReferrerDomainRestrictionRequest.md
````markdown
# UpdateReferrerDomainRestrictionRequest

A list of domains allowed to play your videos.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_domains** | **list[str]** | List of domains allowed to play videos. Possible values are   * &#x60;[]&#x60; Empty Array indicates deny video playback requests for all domains   * &#x60;[\&quot;*\&quot;]&#x60; A Single Wildcard &#x60;*&#x60; entry means allow video playback requests from any domain   * &#x60;[\&quot;*.example.com\&quot;, \&quot;foo.com\&quot;]&#x60; A list of up to 10 domains or valid dns-style wildcards  | [optional]
**allow_no_referrer** | **bool** | A boolean to determine whether to allow or deny HTTP requests without &#x60;Referer&#x60; HTTP request header. Playback requests coming from non-web/native applications like iOS, Android or smart TVs will not have a &#x60;Referer&#x60; HTTP header. Set this value to &#x60;true&#x60; to allow these playback requests. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateTranscriptionVocabularyRequest.md
````markdown
# UpdateTranscriptionVocabularyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-supplied name of the Transcription Vocabulary. | [optional]
**phrases** | **list[str]** | Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream&#39;s &#x60;generated_subtitles&#x60;, the probability of successful speech recognition for these words or phrases is boosted. |
**passthrough** | **str** | Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateUserAgentRestrictionRequest.md
````markdown
# UpdateUserAgentRestrictionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_no_user_agent** | **bool** | Whether or not to allow views without a &#x60;User-Agent&#x60; HTTP request header. | [optional] [default to True]
**allow_high_risk_user_agent** | **bool** | Whether or not to allow high risk user agents. The high risk user agents are defined by Mux. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UpdateWebInputUrlRequest.md
````markdown
# UpdateWebInputUrlRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL for the Web Input to load. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/Upload.md
````markdown
# Upload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Direct Upload. | [optional]
**timeout** | **int** | Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked &#x60;timed_out&#x60; | [optional] [default to 3600]
**status** | **str** |  | [optional]
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional]
**asset_id** | **str** | Only set once the upload is in the &#x60;asset_created&#x60; state. | [optional]
**error** | [**UploadError**](UploadError.md) |  | [optional]
**cors_origin** | **str** | If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers. | [optional]
**url** | **str** | The URL to upload the associated source media to. | [optional]
**test** | **bool** | Indicates if this is a test Direct Upload, in which case the Asset that gets created will be a &#x60;test&#x60; Asset. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UploadError.md
````markdown
# UploadError

Only set if an error occurred during asset creation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Label for the specific error | [optional]
**message** | **str** | Human readable error message | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UploadResponse.md
````markdown
# UploadResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Upload**](Upload.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/URLSigningKeysApi.md
````markdown
# mux_python.URLSigningKeysApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_url_signing_key**](URLSigningKeysApi.md#create_url_signing_key) | **POST** /video/v1/signing-keys | Create a URL signing key
[**delete_url_signing_key**](URLSigningKeysApi.md#delete_url_signing_key) | **DELETE** /video/v1/signing-keys/{SIGNING_KEY_ID} | Delete a URL signing key
[**get_url_signing_key**](URLSigningKeysApi.md#get_url_signing_key) | **GET** /video/v1/signing-keys/{SIGNING_KEY_ID} | Retrieve a URL signing key
[**list_url_signing_keys**](URLSigningKeysApi.md#list_url_signing_keys) | **GET** /video/v1/signing-keys | List URL signing keys


# **create_url_signing_key**
> SigningKeyResponse create_url_signing_key()

Create a URL signing key

This route is now deprecated, please use the `Signing Keys` API. Creates a new signing key pair. When creating a new signing key, the API will generate a 2048-bit RSA key-pair and return the private key and a generated key-id; the public key will be stored at Mux to validate signed tokens.  Note: Any new access tokens authenticating this route will be required to have `System` level permissions. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.URLSigningKeysApi(api_client)
    
    try:
        # Create a URL signing key
        api_response = api_instance.create_url_signing_key()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling URLSigningKeysApi->create_url_signing_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SigningKeyResponse**](SigningKeyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_url_signing_key**
> delete_url_signing_key(signing_key_id)

Delete a URL signing key

This route is now deprecated, please use the `Signing Keys` API. Deletes an existing signing key. Use with caution, as this will invalidate any existing signatures and no URLs can be signed using the key again.  Note: Any new access tokens authenticating this route will be required to have `System` level permissions. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.URLSigningKeysApi(api_client)
    signing_key_id = 'signing_key_id_example' # str | The ID of the signing key.

    try:
        # Delete a URL signing key
        api_instance.delete_url_signing_key(signing_key_id)
    except ApiException as e:
        print("Exception when calling URLSigningKeysApi->delete_url_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signing_key_id** | **str**| The ID of the signing key. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_url_signing_key**
> SigningKeyResponse get_url_signing_key(signing_key_id)

Retrieve a URL signing key

This route is now deprecated, please use the `Signing Keys` API. Retrieves the details of a URL signing key that has previously been created. Supply the unique signing key ID that was returned from your previous request, and Mux will return the corresponding signing key information. **The private key is not returned in this response.**  Note: Any new access tokens authenticating this route will be required to have `System` level permissions. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.URLSigningKeysApi(api_client)
    signing_key_id = 'signing_key_id_example' # str | The ID of the signing key.

    try:
        # Retrieve a URL signing key
        api_response = api_instance.get_url_signing_key(signing_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling URLSigningKeysApi->get_url_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signing_key_id** | **str**| The ID of the signing key. | 

### Return type

[**SigningKeyResponse**](SigningKeyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_url_signing_keys**
> ListSigningKeysResponse list_url_signing_keys(limit=limit, page=page)

List URL signing keys

This route is now deprecated, please use the `Signing Keys` API. Returns a list of URL signing keys.  Note: Any new access tokens authenticating this route will be required to have `System` level permissions. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.URLSigningKeysApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

    try:
        # List URL signing keys
        api_response = api_instance.list_url_signing_keys(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling URLSigningKeysApi->list_url_signing_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListSigningKeysResponse**](ListSigningKeysResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/UserAgentRestrictionRequest.md
````markdown
# UserAgentRestrictionRequest

Rules that control what user agents are allowed to play your videos. Please see [Using User-Agent HTTP header for validation](https://docs.mux.com/guides/secure-video-playback#using-user-agent-http-header-for-validation) for more details on this feature.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_no_user_agent** | **bool** | Whether or not to allow views without a &#x60;User-Agent&#x60; HTTP request header. | [optional] [default to True]
**allow_high_risk_user_agent** | **bool** | Whether or not to allow high risk user agents. The high risk user agents are defined by Mux. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/UserAgentRestrictionSettings.md
````markdown
# UserAgentRestrictionSettings

Rules that control what user agents are allowed to play your videos. Please see [Using User-Agent HTTP header for validation](https://docs.mux.com/guides/secure-video-playback#using-user-agent-http-header-for-validation) for more details on this feature.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_no_user_agent** | **bool** | Whether or not to allow views without a &#x60;User-Agent&#x60; HTTP request header. | [optional] [default to True]
**allow_high_risk_user_agent** | **bool** | Whether or not to allow high risk user agents. The high risk user agents are defined by Mux. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/VideoView.md
````markdown
# VideoView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_total_upscaling** | **str** |  | [optional]
**preroll_ad_asset_hostname** | **str** |  | [optional]
**player_source_domain** | **str** |  | [optional]
**region** | **str** |  | [optional]
**viewer_user_agent** | **str** |  | [optional]
**preroll_requested** | **bool** |  | [optional]
**page_type** | **str** |  | [optional]
**startup_score** | **str** |  | [optional]
**view_seek_duration** | **int** |  | [optional]
**country_name** | **str** |  | [optional]
**player_source_height** | **int** |  | [optional]
**longitude** | **str** |  | [optional]
**buffering_count** | **int** |  | [optional]
**video_duration** | **int** |  | [optional]
**player_source_type** | **str** |  | [optional]
**city** | **str** |  | [optional]
**view_id** | **str** |  | [optional]
**platform_description** | **str** |  | [optional]
**video_startup_preroll_request_time** | **int** |  | [optional]
**viewer_device_name** | **str** |  | [optional]
**video_series** | **str** |  | [optional]
**viewer_application_name** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]
**view_total_content_playback_time** | **int** |  | [optional]
**cdn** | **str** |  | [optional]
**player_instance_id** | **str** |  | [optional]
**video_language** | **str** |  | [optional]
**player_source_width** | **int** |  | [optional]
**player_error_message** | **str** |  | [optional]
**player_mux_plugin_version** | **str** |  | [optional]
**watched** | **bool** |  | [optional]
**playback_score** | **str** |  | [optional]
**page_url** | **str** |  | [optional]
**metro** | **str** |  | [optional]
**view_max_request_latency** | **int** |  | [optional]
**requests_for_first_preroll** | **int** |  | [optional]
**view_total_downscaling** | **str** |  | [optional]
**latitude** | **str** |  | [optional]
**player_source_host_name** | **str** |  | [optional]
**inserted_at** | **str** |  | [optional]
**view_end** | **str** |  | [optional]
**mux_embed_version** | **str** |  | [optional]
**player_language** | **str** |  | [optional]
**page_load_time** | **int** |  | [optional]
**viewer_device_category** | **str** |  | [optional]
**video_startup_preroll_load_time** | **int** |  | [optional]
**player_version** | **str** |  | [optional]
**watch_time** | **int** |  | [optional]
**player_source_stream_type** | **str** |  | [optional]
**preroll_ad_tag_hostname** | **str** |  | [optional]
**viewer_device_manufacturer** | **str** |  | [optional]
**rebuffering_score** | **str** |  | [optional]
**experiment_name** | **str** |  | [optional]
**viewer_os_version** | **str** |  | [optional]
**player_preload** | **bool** |  | [optional]
**buffering_duration** | **int** |  | [optional]
**player_view_count** | **int** |  | [optional]
**player_software** | **str** |  | [optional]
**player_load_time** | **int** |  | [optional]
**platform_summary** | **str** |  | [optional]
**video_encoding_variant** | **str** |  | [optional]
**player_width** | **int** |  | [optional]
**view_seek_count** | **int** |  | [optional]
**viewer_experience_score** | **str** |  | [optional]
**view_error_id** | **int** |  | [optional]
**video_variant_name** | **str** |  | [optional]
**preroll_played** | **bool** |  | [optional]
**viewer_application_engine** | **str** |  | [optional]
**viewer_os_architecture** | **str** |  | [optional]
**player_error_code** | **str** |  | [optional]
**buffering_rate** | **str** |  | [optional]
**events** | [**list[VideoViewEvent]**](VideoViewEvent.md) |  | [optional]
**player_name** | **str** |  | [optional]
**view_start** | **str** |  | [optional]
**view_average_request_throughput** | **int** |  | [optional]
**video_producer** | **str** |  | [optional]
**error_type_id** | **int** |  | [optional]
**mux_viewer_id** | **str** |  | [optional]
**video_id** | **str** |  | [optional]
**continent_code** | **str** |  | [optional]
**session_id** | **str** |  | [optional]
**exit_before_video_start** | **bool** |  | [optional]
**video_content_type** | **str** |  | [optional]
**viewer_os_family** | **str** |  | [optional]
**player_poster** | **str** |  | [optional]
**view_average_request_latency** | **int** |  | [optional]
**video_variant_id** | **str** |  | [optional]
**player_source_duration** | **int** |  | [optional]
**player_source_url** | **str** |  | [optional]
**mux_api_version** | **str** |  | [optional]
**video_title** | **str** |  | [optional]
**id** | **str** |  | [optional]
**short_time** | **str** |  | [optional]
**rebuffer_percentage** | **str** |  | [optional]
**time_to_first_frame** | **int** |  | [optional]
**viewer_user_id** | **str** |  | [optional]
**video_stream_type** | **str** |  | [optional]
**player_startup_time** | **int** |  | [optional]
**viewer_application_version** | **str** |  | [optional]
**view_max_downscale_percentage** | **str** |  | [optional]
**view_max_upscale_percentage** | **str** |  | [optional]
**country_code** | **str** |  | [optional]
**used_fullscreen** | **bool** |  | [optional]
**isp** | **str** |  | [optional]
**property_id** | **int** |  | [optional]
**player_autoplay** | **bool** |  | [optional]
**player_height** | **int** |  | [optional]
**asn** | **int** |  | [optional]
**asn_name** | **str** |  | [optional]
**quality_score** | **str** |  | [optional]
**player_software_version** | **str** |  | [optional]
**player_mux_plugin_name** | **str** |  | [optional]
**sub_property_id** | **str** |  | [optional]
**player_remote_played** | **bool** |  | [optional]
**view_max_playhead_position** | **str** |  | [optional]
**view_playing_time** | **str** |  | [optional]
**view_session_id** | **str** |  | [optional]
**viewer_connection_type** | **str** |  | [optional]
**viewer_device_model** | **str** |  | [optional]
**weighted_average_bitrate** | **float** |  | [optional]
**custom_1** | **str** |  | [optional]
**custom_2** | **str** |  | [optional]
**custom_3** | **str** |  | [optional]
**custom_4** | **str** |  | [optional]
**custom_5** | **str** |  | [optional]
**custom_6** | **str** |  | [optional]
**custom_7** | **str** |  | [optional]
**custom_8** | **str** |  | [optional]
**custom_9** | **str** |  | [optional]
**custom_10** | **str** |  | [optional]
**live_stream_latency** | **int** |  | [optional]
**asset_id** | **str** |  | [optional]
**environment_id** | **str** |  | [optional]
**live_stream_id** | **str** |  | [optional]
**mux_embed** | **str** |  | [optional]
**playback_id** | **str** |  | [optional]
**player_error_context** | **str** |  | [optional]
**view_drm_type** | **str** |  | [optional]
**view_dropped_frame_count** | **int** |  | [optional]
**view_has_ad** | **bool** |  | [optional]
**video_startup_failure** | **bool** |  | [optional]
**ad_attempt_count** | **int** |  | [optional]
**ad_break_count** | **int** |  | [optional]
**ad_break_error_count** | **int** |  | [optional]
**ad_break_error_percentage** | **str** |  | [optional]
**ad_error_count** | **int** |  | [optional]
**ad_error_percentage** | **str** |  | [optional]
**ad_impression_count** | **int** |  | [optional]
**ad_startup_error_count** | **int** |  | [optional]
**ad_startup_error_percentage** | **str** |  | [optional]
**ad_exit_before_start_count** | **int** |  | [optional]
**ad_exit_before_start_percentage** | **str** |  | [optional]
**long_resume** | **bool** |  | [optional]
**long_rebuffering** | **bool** |  | [optional]
**playback_failure_error_type_id** | **int** |  | [optional]
**playback_business_exception_error_type_id** | **int** |  | [optional]
**video_startup_business_exception_error_type_id** | **int** |  | [optional]
**playback_failure** | **bool** |  | [optional]
**ad_playback_failure_error_type_id** | **int** |  | [optional]
**view_content_startup_time** | **int** |  | [optional]
**ad_preroll_startup_time** | **int** |  | [optional]
**view_dropped** | **bool** |  | [optional]
**client_application_name** | **str** |  | [optional]
**client_application_version** | **str** |  | [optional]
**video_affiliate** | **str** |  | [optional]
**viewer_plan** | **str** |  | [optional]
**viewer_plan_status** | **str** |  | [optional]
**viewer_plan_category** | **str** |  | [optional]
**view_drm_level** | **str** |  | [optional]
**video_brand** | **str** |  | [optional]
**used_pip** | **bool** |  | [optional]
**time_shift_enabled** | **bool** |  | [optional]
**used_captions** | **bool** |  | [optional]
**video_codec** | **str** |  | [optional]
**audio_codec** | **str** |  | [optional]
**video_dynamic_range_type** | **str** |  | [optional]
**view_cdn_edge_pop** | **str** |  | [optional]
**view_cdn_origin** | **str** |  | [optional]
**video_creator_id** | **str** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/VideoViewEvent.md
````markdown
# VideoViewEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer_time** | **int** |  | [optional]
**playback_time** | **int** |  | [optional]
**name** | **str** |  | [optional]
**event_time** | **int** |  | [optional]
**details** | **dict(str, object)** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/VideoViewResponse.md
````markdown
# VideoViewResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VideoView**](VideoView.md) |  | [optional]
**timeframe** | **list[int]** |  | [optional]
**total_row_count** | **int** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/VideoViewsApi.md
````markdown
# mux_python.VideoViewsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_view**](VideoViewsApi.md#get_video_view) | **GET** /data/v1/video-views/{VIDEO_VIEW_ID} | Get a Video View
[**list_video_views**](VideoViewsApi.md#list_video_views) | **GET** /data/v1/video-views | List Video Views


# **get_video_view**
> VideoViewResponse get_video_view(video_view_id)

Get a Video View

Returns the details of a video view.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.VideoViewsApi(api_client)
    video_view_id = 'abcd1234' # str | ID of the Video View

    try:
        # Get a Video View
        api_response = api_instance.get_video_view(video_view_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideoViewsApi->get_video_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_view_id** | **str**| ID of the Video View | 

### Return type

[**VideoViewResponse**](VideoViewResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_video_views**
> ListVideoViewsResponse list_video_views(limit=limit, page=page, viewer_id=viewer_id, error_id=error_id, order_direction=order_direction, filters=filters, metric_filters=metric_filters, timeframe=timeframe)

List Video Views

Returns a list of video views which match the filters and have a `view_end` within the specified timeframe.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.VideoViewsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
viewer_id = 'viewer_id_example' # str | Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux. (optional)
error_id = 56 # int | Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error. (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # List Video Views
        api_response = api_instance.list_video_views(limit=limit, page=page, viewer_id=viewer_id, error_id=error_id, order_direction=order_direction, filters=filters, metric_filters=metric_filters, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VideoViewsApi->list_video_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **viewer_id** | **str**| Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux. | [optional] 
 **error_id** | **int**| Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error. | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListVideoViewsResponse**](ListVideoViewsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````

## File: docs/WebInput.md
````markdown
# WebInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Web Input. | [optional]
**created_at** | **str** | Time the Web Input was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**url** | **str** | The URL for the Web Input to load. | [optional]
**auto_launch** | **bool** | When set to &#x60;true&#x60; the Web Input will automatically launch and start streaming immediately after creation | [optional]
**live_stream_id** | **str** | The Live Stream ID to broadcast this Web Input to | [optional]
**status** | **str** |  | [optional]
**passthrough** | **str** | Arbitrary metadata that will be included in the Web Input details and related webhooks. Can be used to store your own ID for the Web Input. **Max: 255 characters**. | [optional]
**resolution** | **str** | The resolution of the viewport of the Web Input&#39;s browser instance. Defaults to 1920x1080 if not set. | [optional] [default to '1920x1080']
**timeout** | **int** | The number of seconds that the Web Input should stream for before automatically shutting down. | [optional] [default to 3600]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/WebInputResponse.md
````markdown
# WebInputResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebInput**](WebInput.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
````

## File: docs/WebInputsApi.md
````markdown
# mux_python.WebInputsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_input**](WebInputsApi.md#create_web_input) | **POST** /video/v1/web-inputs | Create a new Web Input
[**delete_web_input**](WebInputsApi.md#delete_web_input) | **DELETE** /video/v1/web-inputs/{WEB_INPUT_ID} | Delete a Web Input
[**get_web_input**](WebInputsApi.md#get_web_input) | **GET** /video/v1/web-inputs/{WEB_INPUT_ID} | Retrieve a Web Input
[**launch_web_input**](WebInputsApi.md#launch_web_input) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/launch | Launch a Web Input
[**list_web_inputs**](WebInputsApi.md#list_web_inputs) | **GET** /video/v1/web-inputs | List Web Inputs
[**reload_web_input**](WebInputsApi.md#reload_web_input) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/reload | Reload a Web Input
[**shutdown_web_input**](WebInputsApi.md#shutdown_web_input) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/shutdown | Shut down a Web Input
[**update_web_input_url**](WebInputsApi.md#update_web_input_url) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/url | Update Web Input URL


# **create_web_input**
> WebInputResponse create_web_input(create_web_input_request)

Create a new Web Input

Create a new Web Input

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    create_web_input_request = {"url":"https://example.com/hello.html","live_stream_id":"ZEBrNTpHC02iUah025KM3te6ylM7W4S4silsrFtUkn3Ag"} # CreateWebInputRequest | 

    try:
        # Create a new Web Input
        api_response = api_instance.create_web_input(create_web_input_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->create_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_web_input_request** | [**CreateWebInputRequest**](CreateWebInputRequest.md)|  | 

### Return type

[**WebInputResponse**](WebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Web Input Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_input**
> delete_web_input(web_input_id)

Delete a Web Input

Deletes a Web Input and all its data

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Delete a Web Input
        api_instance.delete_web_input(web_input_id)
    except ApiException as e:
        print("Exception when calling WebInputsApi->delete_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_input**
> WebInputResponse get_web_input(web_input_id)

Retrieve a Web Input

Retrieve a single Web Input's info

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Retrieve a Web Input
        api_response = api_instance.get_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->get_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**WebInputResponse**](WebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_web_input**
> LaunchWebInputResponse launch_web_input(web_input_id)

Launch a Web Input

Launches the browsers instance, loads the URL specified, and then starts streaming to the specified Live Stream.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Launch a Web Input
        api_response = api_instance.launch_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->launch_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**LaunchWebInputResponse**](LaunchWebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_web_inputs**
> ListWebInputsResponse list_web_inputs(limit=limit, page=page)

List Web Inputs

List Web Inputs

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

    try:
        # List Web Inputs
        api_response = api_instance.list_web_inputs(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->list_web_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListWebInputsResponse**](ListWebInputsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_web_input**
> ReloadWebInputResponse reload_web_input(web_input_id)

Reload a Web Input

Reloads the page that a Web Input is displaying.  Note: Using this when the Web Input is streaming will display the page reloading. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Reload a Web Input
        api_response = api_instance.reload_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->reload_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**ReloadWebInputResponse**](ReloadWebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_web_input**
> ShutdownWebInputResponse shutdown_web_input(web_input_id)

Shut down a Web Input

Ends streaming to the specified Live Stream, and then shuts down the Web Input browser instance.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Shut down a Web Input
        api_response = api_instance.shutdown_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->shutdown_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**ShutdownWebInputResponse**](ShutdownWebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_input_url**
> WebInputResponse update_web_input_url(web_input_id, update_web_input_url_request)

Update Web Input URL

Changes the URL that a Web Input loads when it launches.  Note: This can only be called when the Web Input is idle. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID
update_web_input_url_request = {"url":"https://example.com/hello-there.html"} # UpdateWebInputUrlRequest | 

    try:
        # Update Web Input URL
        api_response = api_instance.update_web_input_url(web_input_id, update_web_input_url_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->update_web_input_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 
 **update_web_input_url_request** | [**UpdateWebInputUrlRequest**](UpdateWebInputUrlRequest.md)|  | 

### Return type

[**WebInputResponse**](WebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
````
