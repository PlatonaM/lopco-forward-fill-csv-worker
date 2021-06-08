## lopco-forward-fill-csv-worker

Uses forward fill to populate gabs in CSV files.

### Configuration

`delimiter`: Delimiter used in the CSV file.

`target_columns`: Columns containing gabs.

### Inputs

Type: single

`source_csv`: CSV file to fill.

### Outputs

Type: single

`output_file`: Result CSV file.

### Description

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
