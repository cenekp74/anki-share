from .process import process_deck
from celery import shared_task

@shared_task
def start_deck_processing(deck_id: str):
    process_deck(deck_id)
    return True