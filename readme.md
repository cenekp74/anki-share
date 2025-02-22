# anki-share

Normally, sharing decks can be quite frustrating - most people don't use anki and don't like the idea of installing it just to view a few flashcards. And of course there is ankiweb, but it requires an account and you cannot import local decks. As a result, it is almost impossible to share your amazing Anki cards with someone that doesn't use anki.

Anki-share takes care of this problem. You simply upload the Anki deck to https://anki-share.com/ and share the generated url with anyone. They will then be able to view the deck from any web browser - be it on a computer, tablet or mobile phone. They won't be able to use all the advance features Anki has to offer, but for a quick learning session, it's perfect!

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