# anki-share

*description soon*

## logic
After uploading the file, it is handled by `upload` in `routs.py`. It generates a unique id for the deck and writes it into the site's db.
It starts a celery task (function `start_deck_processing` in `celery_tasks.py`). That uses function `process_deck` from `process.py`. This function unzips the anki file and opens the sqlite database inside (`collection.anki21`). It reads the cards (table `notes` column `flds` - only 2 fields are expected). 
It sends the cards to template `deck_body.html` and saves the generated html. *rest of logic description soon*