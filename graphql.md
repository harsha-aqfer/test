---
title: Example1
---

***Import Trade Desk Impressions and Clicks***

This YAML example ingests two types of event data, impressions and clicks, from The Trade Desk to aMDP’s impression_event and click_event schemas, respectively.

This is the beginning of job pipelines to incorporate data The Trade Desk into an entity graph or into datamarts useful for user segmentation and customer journey analysis.
### mappings.yaml

```
schemas:
  ttd_impression:
    columns:
      - LogEntryTime
      - ImpressionId
      - PartnerId
      - AdvertiserId
      - CampaignId
      - AdGroupId
      - PrivateContractID
      - AudienceID
      - CreativeId
      - AdFormat
      - Frequency
      - SupplyVendor
      - SupplyVendorPublisherID
      - DealID
      - Site
      - ReferrerCategoriesList
      - FoldPosition
      - UserHourOfWeek
      - UserAgent
      - IPAddress
      - TDID
      - Country
      - Region
      - Metro
      - City
      - DeviceType
      - OSFamily
      - OS
      - Browser
      - Recency
      - LanguageCode
      - MediaCost
      - FeeFeatureCost
      - DataUsageTotalCost
      - TTDCostInUSD
      - PartnerCostInUSD
      - AdvertiserCostInUSD
      - Latitude
      - Longitude
      - DeviceID
      - ZipCode
      - ProcessedTime
      - DeviceMake
      - DeviceModel
      - RenderingContext
      - CarrierID
      - TemperatrueInCelsiusName
      - TemperatureBucketStartInCelsiusName
      - TemperatureBucketEndInCelsiusName
  ttd_click:
    columns:
      - LogEntryTime
      - ClickId
      - IPAddress
      - ReferrerURL
      - RedirectURL
      - CampaignId
      - ChannelId
      - AdvertiserId
      - DisplayImpressionId
      - Keyword
      - KeywordId
      - MatchType
      - DistributionNetwork
      - TDID
      - RawUrl
      - ProcessedTime
      - DeviceID
  http_schema:
    columns:
      - name: status_code
        required: false
      - name: tag_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: cookie
        data_type: map
      - name: ip_info
        required: false
        data_type:
          type: custom
          schema: ip_struct
      - name: user_agent_info
        data_type: map
      - name: headers
        data_type: map
  ip_struct:
    columns:
      - name: ip_type
        required: false
      - name: ip_domain
        required: false
      - name: ip
        required: false
  url_struct:
    columns:
      - name: scheme
        required: false
      - name: host
        required: false
      - name: path
        required: false
      - name: query
        data_type: map
  entity_struct:
    columns:
      - name: entity_type
        required: false
      - name: entity_domain
        required: false
      - name: entity_id
        required: false
  aqfer_click_subevent:
    columns:
      - name: event_timestamp
        data_type: long
      - agency_id
      - click_id
      - name: page_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: page_referer_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: destination_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: cpc_paid
        required: false
        data_type: int
      - name: cpc_cost
        required: false
        data_type: int
      - name: other_event_ids
        data_type: map
      - name: metrics
        data_type: map
      - name: others
        data_type: map
  aqfer_click_subevent_ext:
    columns:
      - entity_id
      - name: event_timestamp
        data_type: long
      - event_type
      - event_id
      - name: source
        required: false
      - name: country_code
        required: false
      - name: region_code
        required: false
      - name: parent_event_id
        required: false
      - name: agency_id
        required: false
      - name: advertiser_id
        required: false
      - name: page_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: ad_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: page_referer_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: destination_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: campaign_id
        required: false
      - name: ad_group_id
        required: false
      - name: creative_id
        required: false
      - name: placement_id
        required: false
      - name: other_marketing_program_levels
        data_type: map
      - name: media_partner
        required: false
      - name: inventory_partner
        required: false
      - name: supply_vendor_publisher_id
        required: false
      - name: site_id
        required: false
      - name: other_media_group_levels
        data_type: map
      - name: has_click_conversion
        data_type: boolean
        required: false
      - name: cpm_currency
        required: false
      - name: cpm_paid
        required: false
        data_type: int
      - name: cpm_cost
        required: false
        data_type: int
      - name: cpc_paid
        required: false
        data_type: int
      - name: cpc_cost
        required: false
        data_type: int
      - name: keywords
        required: false
      - name: search_terms
        required: false
      - name: search_phrase
        required: false
      - name: other_entity_ids
        data_type:
          type: list
          element:
            type: custom
            schema: entity_struct
      - name: other_event_ids
        data_type: map
      - name: http_info
        data_type:
          type: custom
          schema: http_schema
      - name: geo
        data_type: map
      - name: metrics
        data_type: map
      - name: others
        data_type: map
    partitions:
      - entity_type
      - entity_domain
      - event_date
      - event_hour
      - batch_id
  aqfer_engagement_subevent:
    columns:
      - engagement_type
      - name: engagement_sub_type
        required: false
      - name: event_timestamp
        data_type: long
      - name: cpc_paid
        required: false
        data_type: int
      - name: cpc_cost
        required: false
        data_type: int
      - name: cpe_paid
        required: false
        data_type: int
      - name: cpe_cost
        required: false
        data_type: int
      - name: engagement_actions
        data_type: list
      - name: metrics
        data_type: map
      - name: others
        data_type: map
  aqfer_impression:
    columns:
      - entity_id
      - name: event_timestamp
        data_type: long
      - event_type
      - event_id
      - name: source
        required: false
      - name: country_code
        required: false
      - name: region_code
        required: false
      - name: parent_event_id
        required: false
      - name: agency_id
        required: false
      - name: advertiser_id
        required: false
      - name: page_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: ad_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: page_referer_url
        required: false
        data_type:
          type: custom
          schema: url_struct
      - name: campaign_id
        required: false
      - name: ad_group_id
        required: false
      - name: creative_id
        required: false
      - name: placement_id
        required: false
      - name: other_marketing_program_levels
        data_type: map
      - name: media_partner
        required: false
      - name: inventory_partner
        required: false
      - name: supply_vendor_publisher_id
        required: false
      - name: site_id
        required: false
      - name: other_media_group_levels
        data_type: map
      - name: has_click_conversion
        data_type: boolean
        required: false
      - name: has_click
        data_type: boolean
        required: false
      - name: viewable
        data_type: boolean
        required: false
      - name: cpm_currency
        required: false
      - name: cpm_paid
        required: false
        data_type: int
      - name: cpm_cost
        required: false
        data_type: int
      - name: keywords
        required: false
      - name: search_terms
        required: false
      - name: search_phrase
        required: false
      - name: other_entity_ids
        data_type:
          type: list
          element:
            type: custom
            schema: entity_struct
      - name: other_event_ids
        data_type: map
      - name: http_info
        data_type:
          type: custom
          schema: http_schema
      - name: geo
        data_type: map
      - name: metrics
        data_type: map
      - name: others
        data_type: map
      - name: clicks
        data_type:
          type: list
          element:
            type: custom
            schema: aqfer_click_subevent
      - name: engagements
        data_type:
          type: list
          element:
            type: custom
            schema: aqfer_engagement_subevent
    partitions:
      - entity_type
      - entity_domain
      - event_date
      - event_hour
      - batch_id
  aqfer_entity_graph:
    columns:
      - key
      - value
      - name: event_timestamp
        data_type: long
      - name: confidence
        data_type: double
      - name: others
        data_type: map
    partitions:
      - key_type
      - value_type
      - key_domain
      - value_domain
      - provider
      - mapping_date
schema_mappings:
  ttd_impression_to_aqfer_impression:
    input_schema: ttd_impression
    output_schema: aqfer_impression
    if_missing: ""
    column_mappings:
      entity_id: TDID
      event_timestamp:
        type: expr
        expr: '${LogEntryTime}'
        transformations:
          - type: type_conversion
            output_data_type:
              type: date_part
              parse: "yyyy-MM-dd'T'HH:mm:ss"
      event_type:
        type: const
        value: "impr"
      event_id: ImpressionId
      parent_event_id: ImpressionId
      source:
        type: const
        value: "TTD"
      country_code: Country
      region_code: Region
      agency_id:
        type: const
        value: "NA"
      advertiser_id: AdvertiserId
      page_referer_url:
        type: inner
        column_mappings:
          query:
            type: map
            entries: { }
      campaign_id: CampaignId
      ad_group_id: AdGroupId
      creative_id: CreativeId
      other_marketing_program_levels:
        type: map
        entries:
          ad_format: AdFormat
      media_partner: PartnerId
      supply_vendor_publisher_id: SupplyVendorPublisherID
      site_id: Site
      other_media_group_levels:
        type: map
        entries: { }
      other_entity_ids:
        type: list
        elements: [ ]
      other_event_ids:
        type: map
        entries:
          impression_id: ImpressionId
      http_info:
        type: inner
        column_mappings:
          cookie:
            type: map
            entries: { }
          headers:
            type: map
            entries: { }
          user_agent_info:
            type: map
            entries:
              user_agent: UserAgent
              browser: Browser
              os: OS
              os_family: OSFamily
              device_id: DeviceID
              device_type: DeviceType
      geo:
        type: map
        entries:
          latitude: Latitude
          longitude: Longitude
          metro: Metro
          city: City
          zip_code: ZipCode
          ip_address: IPAddress
      metrics:
        type: map
        entries:
          media_cost: MediaCost
          fee_feature_cost: FeeFeatureCost
          data_usage_total_cost: DataUsageTotalCost
          ttd_cost_in_usd: TTDCostInUSD
          partner_cost_in_usd: PartnerCostInUSD
          advertiser_cost_in_usd: AdvertiserCostInUSD
      others:
        type: map
        entries:
          private_contract_id: PrivateContractID
          audience_id: AudienceID
          frequency: Frequency
          supply_vendor: SupplyVendor
          deal_id: DealID
          referrer_categories_list: ReferrerCategoriesList
          fold_position: FoldPosition
          user_hour_of_week: UserHourOfWeek
          recency: Recency
          language_code: LanguageCode
          processed_time: ProcessedTime
          device_make: DeviceMake
          device_model: DeviceModel
          rendering_context: RenderingContext
          carrier_id: CarrierID
          temparature_in_celsius_name: TemperatrueInCelsiusName
          temparature_bucket_start_in_celsius_name: TemperatureBucketStartInCelsiusName
          temparature_bucket_end_in_celsius_name: TemperatureBucketEndInCelsiusName
      clicks:
        type: list
        elements: [ ]
      engagements:
        type: list
        elements: [ ]
      entity_type:
        type: const
        value: "ck"
      entity_domain:
        type: const
        value: "TTD"
      event_date:
        type: expr
        expr: '${LogEntryTime}'
        transformations:
          - type: type_conversion
            output_data_type:
              type: date_part
              format: 'yyyyMMdd'
              parse: "yyyy-MM-dd'T'HH:mm:ss"
      event_hour:
        type: expr
        expr: '${LogEntryTime}'
        transformations:
          - type: type_conversion
            output_data_type:
              type: date_part
              format: 'HH'
              parse: "yyyy-MM-dd'T'HH:mm:ss"
      batch_id:
        type: const
        value: NA
  ttd_click_to_aqfer_click_subevent_ext:
    input_schema: ttd_click
    output_schema: aqfer_click_subevent_ext
    if_missing: ""
    column_mappings:
      entity_id: TDID
      event_timestamp:
        type: expr
        expr: '${LogEntryTime}'
        transformations:
          - type: type_conversion
            output_data_type:
              type: date_part
              parse: "yyyy-MM-dd'T'HH:mm:ss"
      event_type:
        type: const
        value: "clk"
      event_id: ClickId
      parent_event_id: DisplayImpressionId
      source:
        type: const
        value: TTD
      agency_id:
        type: const
        value: NA
      advertiser_id: AdvertiserId
      campaign_id: CampaignId
      other_marketing_program_levels:
        type: map
        entries: { }
      other_media_group_levels:
        type: map
        entries:
          distribution_network: DistributionNetwork
          impression_id: DisplayImpressionId
      has_click_conversion:
        type: const
        value: true
      other_entity_ids:
        type: list
        elements: [ ]
      other_event_ids:
        type: map
        entries: { }
      http_info:
        type: inner
        column_mappings:
          cookie:
            type: map
            entries: { }
          headers:
            type: map
            entries: { }
          user_agent_info:
            type: map
            entries:
              ip_address: IPAddress
              device_id: DeviceID
      page_referer_url:
        type: inner
        column_mappings:
          host: ReferrerURL
          query:
            type: map
            entries: { }
      geo:
        type: map
        entries: { }
      metrics:
        type: map
        entries: { }
      others:
        type: map
        entries:
          redirect_url: RedirectURL
          channel_id: ChannelId
          keyword: Keyword
          keyword_id: KeywordId
          match_type: MatchType
          raw_url: RawUrl
          processed_time: ProcessedTime
      entity_type:
        type: const
        value: "ck"
      entity_domain:
        type: const
        value: "TTD"
      event_date:
        type: expr
        expr: '${LogEntryTime}'
        transformations:
          - type: type_conversion
            output_data_type:
              type: date_part
              format: 'yyyyMMdd'
              parse: "yyyy-MM-dd'T'HH:mm:ss"
      event_hour:
        type: expr
        expr: '${LogEntryTime}'
        transformations:
          - type: type_conversion
            output_data_type:
              type: date_part
              format: 'HH'
              parse: "yyyy-MM-dd'T'HH:mm:ss"
      batch_id:
        type: const
        value: NA
  aqfer_impression_to_aqfer_entity_graph_cookie:
    input_schema: aqfer_impression
    output_schema: aqfer_entity_graph
    if_missing: ""
    column_mappings:
      key: entity_id
      value:
        type: expr
        expr: '${entity_id}'
        transformations:
          - type: hash
            algorithm: SHA256
      event_timestamp: $now
      confidence:
        type: const
        value: -1
      others:
        type: map
        entries: { }
      key_type:
        type: const
        value: ck
      value_type:
        type: const
        value: cookie
      key_domain:
        type: const
        value: TTD
      value_domain:
        type: const
        value: hashed_cookie
      provider:
        type: const
        value: TTD
      mapping_date:
        type: const
        value: 20220101
  aqfer_impression_to_aqfer_entity_graph_ip:
    input_schema: aqfer_impression
    output_schema: aqfer_entity_graph
    if_missing: ""
    column_mappings:
      key: entity_id
      value: geo[ip_address]
      event_timestamp: $now
      confidence:
        type: const
        value: -1
      others:
        type: map
        entries: { }
      key_type:
        type: const
        value: ck
      value_type:
        type: const
        value: ip
      key_domain:
        type: const
        value: TTD
      value_domain:
        type: const
        value: ip
      provider:
        type: const
        value: TTD
      mapping_date:
        type: const
        value: 20220101
```

### data_channels.yaml

```
~~cid~~:
  tmp:
    type: s3aq
    format: avro
    bucket: com.aqfer.inc.tmp
    base_path: /amdp-services/mapper/examples/example-2/work_area
    pattern: "*"
    credentials: default
  input_ttd_impressions:
    type: s3aq
    base_path: /amdp-services/mapper/examples/example-2/input
    bucket: com.aqfer.inc.tmp
    format: csv
    pattern: /date=*/hour=*/impressions*.tsv
    credentials: default
    options:
      delimiter: "\t"
  input_ttd_clicks:
    type: s3aq
    format: csv
    bucket: com.aqfer.inc.tmp
    base_path: /amdp-services/mapper/examples/example-2/input
    pattern: /date=*/hour=*/clicks*.tsv
    credentials: default
    options:
      delimiter: "\t"
  output_aqfer_impressions:
    type: s3aq
    format: avro
    base_path: /amdp-services/mapper/examples/example-2/output/impressions
    bucket: com.aqfer.inc.tmp
    credentials: default
  output_aqfer_click_subevents:
    type: s3aq
    format: avro
    base_path: /amdp-services/mapper/examples/example-2/output/clicks
    bucket: com.aqfer.inc.tmp
    credentials: default
  output_aqfer_entity_graph:
    type: s3aq
    format: avro
    base_path: /amdp-services/mapper/examples/example-2/output/aqfer_entity_graph
    bucket: com.aqfer.inc.tmp
    credentials: default
```

### jobconf.yaml

```
~~cid~~:
  mappings_config: "/etc/opt/aqfer/mappings.yaml"
  jobs:
    # When running in ~~cid~~ prod sandbox, change the job name from import_impressions to sandbox-mapper
    import_impressions:
      type: event_import
      partner: TTD
      publish_metrics: false
      use_dynamic_conversion: true
      use_dynamic_conversion_output: true
      event_schema:
        name: aqfer_impression
      input:
        - data_channel: input_ttd_impressions
          event_schema:
            name: ttd_impression
      output:
        - event_schema:
            name: aqfer_impression
          data_channels:
            - output_aqfer_impressions
        - event_schema:
            name: aqfer_entity_graph
          data_channels:
            - output_aqfer_entity_graph
    # When running in ~~cid~~ prod sandbox, change the job name from import_clicks to sandbox-mapper
    import_clicks:
      type: event_import
      partner: TTD
      publish_metrics: false
      use_dynamic_conversion: true
      event_schema:
        name: aqfer_click_subevent_ext
      input:
        - data_channel: input_ttd_clicks
          event_schema:
            name: ttd_click
      output:
        - event_schema:
            name: aqfer_click_subevent_ext
          data_channels:
            - output_aqfer_click_subevents
```
