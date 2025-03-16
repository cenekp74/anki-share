# anki-share

Normally, sharing decks can be quite frustrating - most people don't use anki and don't like the idea of installing it just to view a few flashcards. And of course there is ankiweb, but it requires an account and you cannot import local decks. As a result, it is almost impossible to share your amazing Anki cards with someone that doesn't use anki.

Anki-share takes care of this problem. You simply upload the Anki deck to https://anki-share.com/ and share the generated url with anyone. They will then be able to view the deck from any web browser - be it on a computer, tablet or mobile phone. They won't be able to use all the advance features Anki has to offer, but for a quick learning session, it's perfect!

For a more detailed description of this project please visit [https://potuznik.dev/](https://potuznik.dev/projects/anki-share)

## local installation
Data privacy may be a concern for many with service like this. If you plan on using it extensively, the best way is to run your own server. 

1. clone github repo
2. install python and the `virtualenv` module
3. activate virtualenv and run `pip install -r requirements.txt`
4. install a configure a [broker](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/) for celery task management
    - I recomment RabbitMQ for windows and Redis for linux
5. start celery service - `celery -A app.celery_app worker --loglevel INFO -P solo`
6. run `run_debug.py` or configure a production server

## logic
After uploading the file, it is handled by `upload` in `routs.py`. It generates a unique id for the deck and writes it into the site's db.

It then starts a celery task (function `start_deck_processing` in `celery_tasks.py`). That uses function `process_deck` from `process.py`. This function unzips the anki file and opens the sqlite database inside (`collection.anki21`). It reads the cards (table `notes` column `flds` - only 2 fields are expected). 
It sends the cards to template `deck_body.html` and saves the generated html. 

After that, the function reads `media` file inside anki folder. It moves all media files to `/media` and renames them accordingly inside the html. 

After upload, user gets redirected to `/deck/<deck_id>`. The `deck` function in `routs.py` checks if the deck exists in database. It then checks the processing status in `processing_status.txt`. If the processing is completed, it reads the `deck_body.html` file inside the deck folder and sends it to `deck.html` template, which is displayed to the user. If the processing is not completed, it shows the user either error of processing in progress message. 

### process_deck logic
The logic of `process_deck` function in `process.py`
1. unzip .apkg file
2. check if `collection.anki21b` exists
- if it does, that means the deck if from a newer version
- decks from newer versions are compressed uzing zstd and serialized using protocol buffers
3. if `collection.anki21b` exists, decompress it to `collection.anki21` using `decompress_pyzstd` function form `utils.py`
4. read notes from `collection.anki21` sqlite database
5. generate deck html using template `deck_body.html`
6. read `media` file into a dict
- if the deck is from new anki versions, the `media` file is serialized using protocol buffers. it has to be processed with `import_export_pb2.py`. the files in anki_proto directory have been generated using protoc (https://protobuf.dev/getting-started/pythontutorial/)
7. move all media files to media directory and replace the references in html
8. if the deck is from a new anki versions, the media files also have to be decompressed using `decompress_pyzstd`

## db structure
### deck
- id - 16 characters long hexadecimal id, randomly generated
- name - name of the deck, created from the uploaded filename
- processed - 0 or 1, represents if the deck has been successfully processed. this is NOT by the celery task for deck processing, but by the deck function in `routs.py` if the deck was successfully loaded
