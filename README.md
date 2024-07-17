# ProPresenter-HomeAssistant
This integration allows Home Assistant to view information from ProPresenter.

To install, put the ProPresenter folder into the custom_components folder. If the custom_components folder doesn't exist, create it. Then include this in the configuration.yaml:

```
text:
  - platform: ProPresenter
    scan_interval: 0.2 # Number of seconds between each HTTP get request
```
