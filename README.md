# VizHash.py: visual hashes in Python

After [VizHash GD](http://sebsauvage.net/wiki/doku.php?id=php:vizhash_gd) and [VizHash.js](https://github.com/sametmax/VizHash.js), here is the Python (2.7 and 3.x) implementation: VizHash.py.

It converts a string to a hash image (almost unique) to give possibility to easily compare with other string hashes. It can be really useful to compare passwords or to identify people from their IP without displaying it.

This implementation results are quite similar to those of VizHash GD and VizHash.js but differ on a certain number of points (I'm working to reduce differences, any help is welcomed!).

VizHash.py is distributed under the [zlib/libpng](http://www.opensource.org/licenses/zlib-license.php) license.

Please note VizHash.py requires the [Pillow module](http://python-pillow.github.io/).

## Usage

First usage is with the command line:

```bash
$ python vizhash/vizhash.py --size=128x128 "your string" > img.png
```

You should see appearing a new image which is the hash visualisation of `your string`.

If module is installed in your default Python path, you can also call the module as following:

```bash
$ python -m vizhash.vizhash "your string" > img.png
```

Second usage is in your source file and it is quite easy:

```python
import vizhash.vizhash

img = vizhash.vizhash.draw('your string', size=(128, 128))
fp = open('img.png', 'w')
img.save(fp)
```

Another usage is to use it in your websites / web applications. For instance, with Django, simply add in your `views.py` file:

```python
import vizhash.vizhash

def vizhash(request, string, size=128):
    image = vizhash.vizhash.draw(string, (size, size))
    response = HttpResponse(content_type="image/png")
    image.save(response, 'PNG')

    return response
```

and in `urls.py`:

```python
urlpatterns = patterns(
    […]
    url(r'^vizhash/(?P<string>\w+)/((?P<size>\d+)/)?$', views.vizhash, name='vizhash'),
    […]
)
```

Note by this way you reveal your string in the URL and it may not what you want. Feel free to adapt these examples to your needs!

## What's next?

There are some points we can improve in VizHash.py:

- Make resulting images closer than those of other implementations of VizHash.
- Make images more beautiful.
- Add unit tests (because for now it is only a quick refactored and commented piece of code)
- Add it on PyPi
- Make it not depending on Pillow which is kinda overkill (but with good performances and very helpul functions)

Please use the [GitHub bugtracker](https://github.com/marienfressinaud/vizhash.py/issues) to signal bugs or ideas of improvement.

## Thanks

- [SebSauvage](http://sebsauvage.net/) for the first implementation of VizHash.
- [Sam & Max](http://sametmax.com/) for their JavaScript implementation and their really helpul Python articles.
