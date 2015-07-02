import logging

settings_app = {

    "settings": {

        # base url used by nginx
        "base_url": "",

        # Logging configurations
        "logging": {
            "level": logging.WARN,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Folders
        "folders": {
            "tmp": "/tmp/",
            "geoserver_datadir": "/geoserver_data_dir/",
            "distribution": "/distribution/",
            "distribution_sld": "/distribution_sld/",
            "storage": "/storage/",
            "workspace_layer_separator": ":"
        }
    }
}
