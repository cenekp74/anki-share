# anki-share

*description soon*

## logic
After uploading the file, it is handled by `upload` in `routs.py`. It generates a unique id for the deck and writes it into the site's db.
It starts a celery task (function `start_deck_processing` in `celery_tasks.py`). That uses function `process_deck` from `process.py`. This function unzips the anki file and opens the sqlite database inside (`collection.anki21`). It reads the cards (table `notes` column `flds` - only 2 fields are expected). 
It sends the cards to template `deck_body.html` and saves the generated html. 
After upload, user gets redirected to `/deck/<deck_id>`. The `deck` function in `routs.py` checks if the deck exists in database. It then checks the processing status in `processing_status.txt`. If the processing is completed, it reads the `deck_body.html` file inside the deck folder and sends it to `deck.html` template, which is displayed to the user. If the processing is not completed, it shows the user either error of processing in progress message. 