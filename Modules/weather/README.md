## Attribution

This project uses [Weather Icons by Erik Flowers](https://github.com/erikflowers/weather-icons).

- Font licensed under the SIL OFL 1.1[SIL OFL 1.1](http://scripts.sil.org/OFL)
- CSS and code licensed under the [MIT License](http://opensource.org/licenses/mit-license.html)


## Dependecies

-[OpenWeatherMap API Key](https://openweathermap.org/api)
-[Weather Icons by Erik Flowers](https://github.com/erikflowers/weather-icons)



## Weather Widget
This widget was made with only my personal needs in mind; I can't promise compatibility with your setup. To use the widget, clone the `/weather` directory to `~/.config/polybar/modules/`.

In `weather.py`, change the variables `key, lat, lng` to your OWM API Key, city latitude, and city longitude, respectively. Then add the following to `~/.config/polybar/config.ini`:


`
    [module/weather]
    type = custom/script
    exec = ~/.config/polybar/modules/weather/weather.py
    interval = 600`
