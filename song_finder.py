"""
# Song Finder

Sorts all your music into an easily accessible dictionary. 

NOTE: It will only read folder and file names, no actual parsing of
metadata occurs.

Example Output:

.. code-block:: bash
    $ song_finder.py
    Artists:
        Lindsey Stirling
    Albums for Lindsey Stirling:
        Artemis
    Songs in Artemis:
        01 - Underground
        02 - Artemis
        03 - Til the Light Goes Out
        04 - Between Twilight
        05 - Foreverglow
        06 - Love Goes On And On (feat. Amy Lee)
        07 - Masquerade
        08 - Sleepwalking
        09 - Darkside
        10 - The Upside
        11 - Guardian
        12 - Aurora
        13 - The Upside (feat. Elle King)
    Path for song 01 - Underground:
        /.../Artemis/01 - Underground.mp3

Raw Output:

.. code-block:: python
    {'Lindsey Stirling':
        {'Artemis':
            {'01 - Underground': PosixPath('/.../Artemis/01 - Underground.mp3'),
            '02 - Artemis': PosixPath('/.../Artemis/02 - Artemis.mp3'),
            '03 - Til the Light Goes Out': PosixPath('/.../Artemis/03 - Til the Light Goes Out.mp3'),
            '04 - Between Twilight': PosixPath('/.../Artemis/04 - Between Twilight.mp3'),
            '05 - Foreverglow': PosixPath('/.../Artemis/05 - Foreverglow.mp3'),
            '06 - Love Goes On And On (feat. Amy Lee)': PosixPath('/.../Artemis/06 - Love Goes On And On (feat. Amy Lee).mp3'),
            '07 - Masquerade': PosixPath('/.../Artemis/07 - Masquerade.mp3'),
            '08 - Sleepwalking': PosixPath('/.../Artemis/08 - Sleepwalking.mp3'),
            '09 - Darkside': PosixPath('/.../Artemis/09 - Darkside.mp3'),
            '10 - The Upside': PosixPath('/.../Artemis/10 - The Upside.mp3'),
            '11 - Guardian': PosixPath('/.../Artemis/11 - Guardian.mp3'),
            '12 - Aurora': PosixPath('/.../Artemis/12 - Aurora.mp3'),
            '13 - The Upside (feat. Elle King)': PosixPath('/.../Artemis/13 - The Upside (feat. Elle King).mp3')}
        }
    }
"""
from pathlib import Path

EXTENTIONS = {'flac', 'mp3', 'm4a', 'ogg', 'opus', 'wav'}


def subfolders(folder: Path):
    return [path.name for path in folder.glob('*') if path.is_dir()]


def songs_in(folder: Path):
    songs = sorted(
        song
        for ext in EXTENTIONS
        for song in folder.glob(f'*.{ext}')
    )
    return {song.stem: song for song in songs}


def song_finder(music_folder: Path):
    artists = {artist: {} for artist in subfolders(music_folder)}

    for artist in artists:
        for album in subfolders(music_folder / artist):
            artists[artist][album] = songs_in(music_folder / artist / album)

        if (singles := songs_in(music_folder / artist)):
            artists[artist]['Singles'] = singles

    if (songs := songs_in(music_folder)):
        artists['Unknown Artist'] = {}
        artists['Unknown Artist']['Unknown Album'] = songs

    return artists


if __name__ == '__main__':
    music = song_finder(Path.home() / 'Music')
    print('Artists:', *music, sep='\n    ')

    artist = list(music)[-1]
    print(f'Albums for {artist}:', *music[artist], sep='\n    ')

    album = list(music[artist])[0]
    print(f'Songs in {album}:', *music[artist][album], sep='\n    ')

    song = list(music[artist][album])[0]
    print(f'Path for song {song}:', music[artist][album][song], sep='\n    ')
