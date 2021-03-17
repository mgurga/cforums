# cforums
Extremely lightweight forum software built on django. Uses very little javascript to correct timezones and basic functionality. 
Only uses one [library](https://github.com/js-cookie/js-cookie) to save and manage cookies, cookies only save theme.

<img src="https://raw.githubusercontent.com/mgurga/cforums/master/docs/techscreenshot.png" width="900px">

![network stats](https://raw.githubusercontent.com/mgurga/cforums/master/docs/networkinspector.png)

## Features
- Completely Anonymous
- Image upload
- Dual Pane
- Theme support (optional)
- SQLite3 database
- Minimal javascript
- Easily customizable

## Themes
Themes are loaded in the form of CSS files located in ```static/themes``` at server startup. 
There is a file called ```template.css``` which outlines what ids and classes should be edited to create a theme.

Included Themes:
- [AMOLED Black](https://github.com/mgurga/cforums/blob/master/static/themes/AMOLED%20Black.css)
<img src="https://raw.githubusercontent.com/mgurga/cforums/master/docs/techamoled.png" href="" width="700px">

- [HACKERMAN](https://github.com/mgurga/cforums/blob/master/static/themes/HACKERMANS.css)
<img src="https://raw.githubusercontent.com/mgurga/cforums/master/docs/techhacker.png" width="700px">

## Start your own forum
```
git clone https://github.com/mgurga/cforums
cd cforums
pip3 install -r requirments.txt
./flushdb.sh
python3 manage.py runserver
```
Edit lines in ```cforums/settings.py``` as you see fit such as ```TITLE```, ```TOPICS```, and ```DEFAULTTHEME```.

```flushdb.sh``` deletes the database and resets to zero then creates a new database from scratch.
