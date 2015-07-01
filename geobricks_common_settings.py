import logging

settings_app = {

    "settings": {

        # base url used by nginx
        "base_url" : "demo/fenix/geo/",

        # Logging configurations
        "logging": {
            "level": logging.WARN,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Folders
        "folders": {
            "tmp": "/work/fenix_gis/dbms/layers/tmp/",
            "geoserver_datadir": "/work/fenix_gis/dbms/geoserver/demo/fenix/data/",
            "distribution": "/work/fenix_gis/dbms/geobricks/demo/fenix/distribution/",
            "distribution_sld": "/work/fenix_gis/dbms/geobricks/demo/fenix/distribution_sld/",
            "storage": "/www/storage/demo/fenix/layer/",
            "workspace_layer_separator": ":"
        },

        "db": {
            # Spatial Database
            "spatial": {
                # default_db will search in the dbs["database"] as default option
                "dbname": "fenix",
                "host": "EXLPRFAOSTAT1.ext.fao.org",
                "port": "5432",
                "username": "fenix",
                "password": "Qwaszx",
                "schema": "spatial",
                "tables": {
                    "country": {
                        "table":"gaul0_faostat3_3857",
                        "column": {
                            "faostat": "faost_code",
                            "gaul": "adm0_code",
                            "iso2":"iso2",
                            "iso3":"iso3",
                            "name":"adm0_name",
                            "geom": "geom"
                        }
                    }
                }
            },
            # Spatial Database
            "afo": {
                # default_db will search in the dbs["database"] as default option
                "dbname": "africafertilizer",
                "host": "EXLPRFAOSTAT1.ext.fao.org",
                "port": "5432",
                "username": "fenix",
                "password": "Qwaszx"
            }
        },

        # Metadata settings
        "metadata": {
            "url_create_metadata": "http://fenix.fao.org/d3s_/msd/resources/metadata",
            "url_get_metadata_uid": "http://fenix.fao.org/d3s/msd/resources/metadata/uid/<uid>",

            # delete metadata
            "url_delete_metadata": "http://fenix.fao.org/d3s/msd/resources/metadata/uid/<uid>",

            # get metadata
            "url_get_metadata": "http://fenix.fao.org/d3s/msd/resources/find",
            "url_get_metadata_full": "http://fenix.fao.org/d3s/msd/resources/metadata/uid/<uid>?full=true&dsd=true",

            # coding system
            "url_create_coding_system": "http://fenix.fao.org/d3s/msd/resources",
            "url_data_coding_system": "http://fenix.fao.org/d3s/msd/resources/data/uid/<uid>",

            # DSD
            "url_overwrite_dsd_rid": "http://fenix.fao.org/d3s/msd/resources/dsd"
        },

        # Email configurations
        "email": {
            "user": "geobrickspy@gmail.com",
            "password": "Geobricks2014"
        }
    }
}
