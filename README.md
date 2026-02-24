# WeeWX OgoXe uploader

This [WeeWX](https://weewx.com/) extension lets your weather station upload measurements to the OgoXe weather platform.

## Maintainer

This extension is maintained by **OgoXe** (@ogoxe).

It is inspired by the WundergroundLike WeeWX extension by **Sigi Meisenbichler** (@smeisens).
Originally created by Vince Skahan (@vinceskahan), derived from the WeeWX 
Weather Underground uploader by Tom Keffer.

Notes:
* Weather Underground 'rapidfire' is 'not' supported here, and is actually disabled in this code
* this extension requires python3

## Installing

### Install via the extension installer

* if you are running a pip install, activate your venv first
* use the weewx extension installer to install this extension
   * For weewx v5 users - see [weectl](https://www.weewx.com/docs/5.2/utilities/weectl-extension/) for detailed instructions
   * For weewx v4 users - see [wee_extension](https://www.weewx.com/docs/4.10/utilities.htm\#wee_extension_utility) for detailed instructions
* edit the ogoxeUploader stanza in weewx.conf to set your parameters
* restart weewx
* check your syslogs to make sure things are working

### Example installation

````
# weectl extension install https://github.com/ogoxe/weewx-ogoxe/archive/refs/heads/main.zip
# weectl extension list
Using configuration file /etc/weewx/weewx.conf
Extension Name    Version   Description
ogoxeUploader 1.0.1    Post to the OgoXe weather platform
# sudo systemctl restart weewx
````

### Configuration Options

| Option | Required | Default | Description |
|--------|----------|---------|-------------|
| enable | Yes | false | Enable/disable the uploader |
| station | Yes | - | Your station ID |
| password | Yes | - | Your station password |
| archive_post | No | true | Upload archive records |
| log_success | No | true | Log successful uploads |
| log_failure | No | true | Log failed uploads |

_Note: the server_url option of WeeWX's builtin Wunderground driver is preset and immutable in this extension._

## Requirements

- WeeWX 4.0+ or 5.0+
- Python 3.7+

### Uninstall
Again, use the extension installer. For weewx v5 `weectl extension uninstall ogoxeUploader`

## Support

- Issues: https://github.com/ogoxe/weewx-ogoxe/issues
- Reach out to us by email (dev@ogoxe.com) 

## Credits

- **Current Maintainer:** OgoXe developers team
- **Original Authors:** Sigi Meisenbichler, Vince Skahan
- **Upstream:** Based on WeeWX restx.py by Tom Keffer

## License

GPL-3.0 - See LICENSE.txt
