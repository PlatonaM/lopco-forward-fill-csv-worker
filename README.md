#### Description

    {
        "name": "Forward Fill CSV",
        "image": "platonam/lopco-forward-fill-csv-worker:latest",
        "data_cache_path": "/data_cache",
        "description": "Forward fill values in a Comma-Separated Values files.",
        "configs": {
            "delimiter": null,
            "target_columns": null
        },
        "input": {
            "type": "single",
            "fields": [
                {
                    "name": "source_csv",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": {
            "type": "single",
            "fields": [
                {
                    "name": "output_file",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        }
    }
