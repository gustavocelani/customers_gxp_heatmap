# Clipp Customers GXP Heatmap

## Dataset Parser

```
 ____        _                 _     ____
|  _ \  __ _| |_ __ _ ___  ___| |_  |  _ \ __ _ _ __ ___  ___ _ __
| | | |/ _` | __/ _` / __|/ _ \ __| | |_) / _` | '__/ __|/ _ \ '__|
| |_| | (_| | || (_| \__ \  __/ |_  |  __/ (_| | |  \__ \  __/ |
|____/ \__,_|\__\__,_|___/\___|\__| |_|   \__,_|_|  |___/\___|_|

Dataset path:  ./dataset/example_dataset.html
Output  path:  ./example_out/example_customers.txt

Parsing HTML Table    |████████████████████████████████| 654/654

Building JSON Dataset |████████████████████████████████| 11/11

Acquiring Geolocation |████████████████████████████████| 11/11

Parsed dataset saved successfully!
```

## Data Analysis

```
 ____        _             _                _           _
|  _ \  __ _| |_ __ _     / \   _ __   __ _| |_   _ ___(_)___
| | | |/ _` | __/ _` |   / _ \ | '_ \ / _` | | | | / __| / __|
| |_| | (_| | || (_| |  / ___ \| | | | (_| | | |_| \__ \ \__ \
|____/ \__,_|\__\__,_| /_/   \_\_| |_|\__,_|_|\__, |___/_|___/
                                              |___/

Customers path:  ./example_out/example_customers.txt

Attributes Usage Analysis |████████████████████████████████| 11/11

Attributes Percent Usage  |████████████████████████████████| 56/56
```

![Attributes Usage](example_out/example_attributes.png?raw=true "Attributes Usage")

## GXP Heatmap

```
  ______  ______    _   _            _
 / ___\ \/ /  _ \  | | | | ___  __ _| |_ _ __ ___   __ _ _ __
| |  _ \  /| |_) | | |_| |/ _ \/ _` | __| '_ ` _ \ / _` | '_ \ 
| |_| |/  \|  __/  |  _  |  __/ (_| | |_| | | | | | (_| | |_) |
 \____/_/\_\_|     |_| |_|\___|\__,_|\__|_| |_| |_|\__,_| .__/
                                                        |_|

Customers path:  ./example_out/example_customers.txt

Latitude/Longitude Normalization |████████████████████████████████| 11/11

Total Customers..............   11 [   100% ]
Not Found Locations..........    5 [ 45.45% ]
Out of GXP Locations.........    1 [  9.09% ]
                              ---------------
Total Locations Used.........    5 [ 45.45% ]
```

![GXP Heatmap](example_out/example_gxp_heatmap.png?raw=true "GXP Heatmap")


