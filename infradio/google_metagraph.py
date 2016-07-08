
from .metagraph import MetaGraph


class GoogleMetagraph(MetaGraph):

    '''
    A metadata graph using the Google Music API.

    Loads songs from one station (default "I'm feeling lucky") and then
    creates related-song stations for each of the random songs chosen.
    '''

    def __init__(self, api, seed_station_id='IFL'):
        self.api = api
        self.seed_buffer_len = 10
        self.station_buffer_len = 10

        self.seed_station_id = seed_station_id
        self.buffered_seed_songs = []

    def next_seed_song(self, rng):

        if not self.buffered_seed_songs:

            self.buffered_seed_songs = \
                self.api.get_station_tracks(self.seed_station_id,
                                            num_tracks=self.seed_buffer_len)

            rng.shuffle(self.buffered_seed_songs)

        return self.buffered_seed_songs.pop()

    class Node:

        def __init__(self, station_seed_song,
                     station_id,
                     buffered_songs,
                     song_position):

            self.station_seed_song = station_seed_song
            self.station_id = station_id
            self.buffered_songs = buffered_songs
            self.song_position = song_position

            if self.song_position < len(self.buffered_songs) and \
               self.song_position >= 0:
                self.song = self.buffered_songs[self.song_position]
            else:
                self.song = None

    @staticmethod
    def song_id(song_json):
        return song_json.get('id') or \
            song_json.get('storeId') or \
            song_json.get('nid')

    def select_node(self, rng):

        station_seed_song = self.next_seed_song(rng)

        station_name = station_seed_song.get('artist') + " - " + \
            station_seed_song.get('album') + " - " + \
            station_seed_song.get('title')

        station_name = "".join([c if (c.isalnum() or c in " -") else '_'
                                for c in station_name])

        station_seed_song_id = GoogleMetagraph.song_id(station_seed_song)

        station_id = self.api.create_station(station_name,
                                             track_id=station_seed_song_id)

        return self.select_next_node(
            GoogleMetagraph.Node(station_seed_song, station_id, [], -1), rng)

    def select_next_node(self, node, rng):

        if node.song_position < len(node.buffered_songs) - 1:
            return GoogleMetagraph.Node(node.station_seed_song,
                                        node.station_id,
                                        node.buffered_songs,
                                        node.song_position + 1)

        last_buffered_song_ids = \
            [GoogleMetagraph.song_id(song) for song in node.buffered_songs]

        next_buffered_songs = \
            self.api.get_station_tracks(
                node.station_id,
                num_tracks=self.station_buffer_len,
                recently_played_ids=last_buffered_song_ids)

        return GoogleMetagraph.Node(node.station_seed_song,
                                    node.station_id,
                                    next_buffered_songs,
                                    0)
