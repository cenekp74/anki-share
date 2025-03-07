# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki/decks.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from app.anki_proto import generic_pb2 as anki_dot_generic__pb2
from app.anki_proto import collection_pb2 as anki_dot_collection__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61nki/decks.proto\x12\nanki.decks\x1a\x12\x61nki/generic.proto\x1a\x15\x61nki/collection.proto\"\x15\n\x06\x44\x65\x63kId\x12\x0b\n\x03\x64id\x18\x01 \x01(\x03\"\x17\n\x07\x44\x65\x63kIds\x12\x0c\n\x04\x64ids\x18\x01 \x03(\x03\"\x9d\x0b\n\x04\x44\x65\x63k\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nmtime_secs\x18\x03 \x01(\x03\x12\x0b\n\x03usn\x18\x04 \x01(\x05\x12\'\n\x06\x63ommon\x18\x05 \x01(\x0b\x32\x17.anki.decks.Deck.Common\x12)\n\x06normal\x18\x06 \x01(\x0b\x32\x17.anki.decks.Deck.NormalH\x00\x12-\n\x08\x66iltered\x18\x07 \x01(\x0b\x32\x19.anki.decks.Deck.FilteredH\x00\x1a\xd1\x01\n\x06\x43ommon\x12\x17\n\x0fstudy_collapsed\x18\x01 \x01(\x08\x12\x19\n\x11\x62rowser_collapsed\x18\x02 \x01(\x08\x12\x18\n\x10last_day_studied\x18\x03 \x01(\r\x12\x13\n\x0bnew_studied\x18\x04 \x01(\x05\x12\x16\n\x0ereview_studied\x18\x05 \x01(\x05\x12\x1c\n\x14milliseconds_studied\x18\x07 \x01(\x05\x12\x18\n\x10learning_studied\x18\x06 \x01(\x05\x12\x0e\n\x05other\x18\xff\x01 \x01(\x0cJ\x04\x08\x08\x10\x0e\x1a\xf4\x02\n\x06Normal\x12\x11\n\tconfig_id\x18\x01 \x01(\x03\x12\x12\n\nextend_new\x18\x02 \x01(\r\x12\x15\n\rextend_review\x18\x03 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1c\n\x14markdown_description\x18\x05 \x01(\x08\x12\x19\n\x0creview_limit\x18\x06 \x01(\rH\x00\x88\x01\x01\x12\x16\n\tnew_limit\x18\x07 \x01(\rH\x01\x88\x01\x01\x12<\n\x12review_limit_today\x18\x08 \x01(\x0b\x32 .anki.decks.Deck.Normal.DayLimit\x12\x39\n\x0fnew_limit_today\x18\t \x01(\x0b\x32 .anki.decks.Deck.Normal.DayLimit\x1a(\n\x08\x44\x61yLimit\x12\r\n\x05limit\x18\x01 \x01(\r\x12\r\n\x05today\x18\x02 \x01(\rB\x0f\n\r_review_limitB\x0c\n\n_new_limitJ\x04\x08\x0c\x10\x10\x1a\x90\x04\n\x08\x46iltered\x12\x12\n\nreschedule\x18\x01 \x01(\x08\x12:\n\x0csearch_terms\x18\x02 \x03(\x0b\x32$.anki.decks.Deck.Filtered.SearchTerm\x12\x0e\n\x06\x64\x65lays\x18\x03 \x03(\x02\x12\x15\n\rpreview_delay\x18\x04 \x01(\r\x12\x1a\n\x12preview_again_secs\x18\x07 \x01(\r\x12\x19\n\x11preview_hard_secs\x18\x05 \x01(\r\x12\x19\n\x11preview_good_secs\x18\x06 \x01(\r\x1a\xba\x02\n\nSearchTerm\x12\x0e\n\x06search\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\r\x12\x39\n\x05order\x18\x03 \x01(\x0e\x32*.anki.decks.Deck.Filtered.SearchTerm.Order\"\xd1\x01\n\x05Order\x12\x19\n\x15OLDEST_REVIEWED_FIRST\x10\x00\x12\n\n\x06RANDOM\x10\x01\x12\x17\n\x13INTERVALS_ASCENDING\x10\x02\x12\x18\n\x14INTERVALS_DESCENDING\x10\x03\x12\n\n\x06LAPSES\x10\x04\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x05\x12\x07\n\x03\x44UE\x10\x06\x12\x11\n\rREVERSE_ADDED\x10\x07\x12\x1c\n\x18RETRIEVABILITY_ASCENDING\x10\x08\x12\x1d\n\x19RETRIEVABILITY_DESCENDING\x10\t\x1aq\n\rKindContainer\x12)\n\x06normal\x18\x01 \x01(\x0b\x32\x17.anki.decks.Deck.NormalH\x00\x12-\n\x08\x66iltered\x18\x02 \x01(\x0b\x32\x19.anki.decks.Deck.FilteredH\x00\x42\x06\n\x04kindB\x06\n\x04kind\"L\n\x1c\x41\x64\x64OrUpdateDeckLegacyRequest\x12\x0c\n\x04\x64\x65\x63k\x18\x01 \x01(\x0c\x12\x1e\n\x16preserve_usn_and_mtime\x18\x02 \x01(\x08\"\x1e\n\x0f\x44\x65\x63kTreeRequest\x12\x0b\n\x03now\x18\x01 \x01(\x03\"\xf2\x02\n\x0c\x44\x65\x63kTreeNode\x12\x0f\n\x07\x64\x65\x63k_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\r\x12\x11\n\tcollapsed\x18\x05 \x01(\x08\x12\x14\n\x0creview_count\x18\x06 \x01(\r\x12\x13\n\x0blearn_count\x18\x07 \x01(\r\x12\x11\n\tnew_count\x18\x08 \x01(\r\x12\x19\n\x11intraday_learning\x18\t \x01(\r\x12\"\n\x1ainterday_learning_uncapped\x18\n \x01(\r\x12\x14\n\x0cnew_uncapped\x18\x0b \x01(\r\x12\x17\n\x0freview_uncapped\x18\x0c \x01(\r\x12\x15\n\rtotal_in_deck\x18\r \x01(\r\x12 \n\x18total_including_children\x18\x0e \x01(\r\x12\x10\n\x08\x66iltered\x18\x10 \x01(\x08\x12*\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x18.anki.decks.DeckTreeNode\"\x9b\x01\n\x17SetDeckCollapsedRequest\x12\x0f\n\x07\x64\x65\x63k_id\x18\x01 \x01(\x03\x12\x11\n\tcollapsed\x18\x02 \x01(\x08\x12\x38\n\x05scope\x18\x03 \x01(\x0e\x32).anki.decks.SetDeckCollapsedRequest.Scope\"\"\n\x05Scope\x12\x0c\n\x08REVIEWER\x10\x00\x12\x0b\n\x07\x42ROWSER\x10\x01\"K\n\x13GetDeckNamesRequest\x12\x1a\n\x12skip_empty_default\x18\x01 \x01(\x08\x12\x18\n\x10include_filtered\x18\x02 \x01(\x08\"4\n\tDeckNames\x12\'\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x16.anki.decks.DeckNameId\"&\n\nDeckNameId\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"<\n\x14ReparentDecksRequest\x12\x10\n\x08\x64\x65\x63k_ids\x18\x01 \x03(\x03\x12\x12\n\nnew_parent\x18\x02 \x01(\x03\"6\n\x11RenameDeckRequest\x12\x0f\n\x07\x64\x65\x63k_id\x18\x01 \x01(\x03\x12\x10\n\x08new_name\x18\x02 \x01(\t\"q\n\x15\x46ilteredDeckForUpdate\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12)\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x19.anki.decks.Deck.Filtered\x12\x13\n\x0b\x61llow_empty\x18\x04 \x01(\x08\x32\xfa\x0c\n\x0c\x44\x65\x63ksService\x12\x30\n\x07NewDeck\x12\x13.anki.generic.Empty\x1a\x10.anki.decks.Deck\x12=\n\x07\x41\x64\x64\x44\x65\x63k\x12\x10.anki.decks.Deck\x1a .anki.collection.OpChangesWithId\x12\x45\n\rAddDeckLegacy\x12\x12.anki.generic.Json\x1a .anki.collection.OpChangesWithId\x12U\n\x15\x41\x64\x64OrUpdateDeckLegacy\x12(.anki.decks.AddOrUpdateDeckLegacyRequest\x1a\x12.anki.decks.DeckId\x12\x41\n\x08\x44\x65\x63kTree\x12\x1b.anki.decks.DeckTreeRequest\x1a\x18.anki.decks.DeckTreeNode\x12\x39\n\x0e\x44\x65\x63kTreeLegacy\x12\x13.anki.generic.Empty\x1a\x12.anki.generic.Json\x12<\n\x11GetAllDecksLegacy\x12\x13.anki.generic.Empty\x1a\x12.anki.generic.Json\x12;\n\x0fGetDeckIdByName\x12\x14.anki.generic.String\x1a\x12.anki.decks.DeckId\x12/\n\x07GetDeck\x12\x12.anki.decks.DeckId\x1a\x10.anki.decks.Deck\x12:\n\nUpdateDeck\x12\x10.anki.decks.Deck\x1a\x1a.anki.collection.OpChanges\x12\x42\n\x10UpdateDeckLegacy\x12\x12.anki.generic.Json\x1a\x1a.anki.collection.OpChanges\x12S\n\x10SetDeckCollapsed\x12#.anki.decks.SetDeckCollapsedRequest\x1a\x1a.anki.collection.OpChanges\x12\x37\n\rGetDeckLegacy\x12\x12.anki.decks.DeckId\x1a\x12.anki.generic.Json\x12\x46\n\x0cGetDeckNames\x12\x1f.anki.decks.GetDeckNamesRequest\x1a\x15.anki.decks.DeckNames\x12\x41\n\x14GetDeckAndChildNames\x12\x12.anki.decks.DeckId\x1a\x15.anki.decks.DeckNames\x12\x37\n\rNewDeckLegacy\x12\x12.anki.generic.Bool\x1a\x12.anki.generic.Json\x12G\n\x0bRemoveDecks\x12\x13.anki.decks.DeckIds\x1a#.anki.collection.OpChangesWithCount\x12V\n\rReparentDecks\x12 .anki.decks.ReparentDecksRequest\x1a#.anki.collection.OpChangesWithCount\x12G\n\nRenameDeck\x12\x1d.anki.decks.RenameDeckRequest\x1a\x1a.anki.collection.OpChanges\x12P\n\x17GetOrCreateFilteredDeck\x12\x12.anki.decks.DeckId\x1a!.anki.decks.FilteredDeckForUpdate\x12^\n\x17\x41\x64\x64OrUpdateFilteredDeck\x12!.anki.decks.FilteredDeckForUpdate\x1a .anki.collection.OpChangesWithId\x12H\n\x17\x46ilteredDeckOrderLabels\x12\x13.anki.generic.Empty\x1a\x18.anki.generic.StringList\x12@\n\x0eSetCurrentDeck\x12\x12.anki.decks.DeckId\x1a\x1a.anki.collection.OpChanges\x12\x37\n\x0eGetCurrentDeck\x12\x13.anki.generic.Empty\x1a\x10.anki.decks.Deck2\x15\n\x13\x42\x61\x63kendDecksServiceB\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anki.decks_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'P\001'
  _globals['_DECKID']._serialized_start=75
  _globals['_DECKID']._serialized_end=96
  _globals['_DECKIDS']._serialized_start=98
  _globals['_DECKIDS']._serialized_end=121
  _globals['_DECK']._serialized_start=124
  _globals['_DECK']._serialized_end=1561
  _globals['_DECK_COMMON']._serialized_start=323
  _globals['_DECK_COMMON']._serialized_end=532
  _globals['_DECK_NORMAL']._serialized_start=535
  _globals['_DECK_NORMAL']._serialized_end=907
  _globals['_DECK_NORMAL_DAYLIMIT']._serialized_start=830
  _globals['_DECK_NORMAL_DAYLIMIT']._serialized_end=870
  _globals['_DECK_FILTERED']._serialized_start=910
  _globals['_DECK_FILTERED']._serialized_end=1438
  _globals['_DECK_FILTERED_SEARCHTERM']._serialized_start=1124
  _globals['_DECK_FILTERED_SEARCHTERM']._serialized_end=1438
  _globals['_DECK_FILTERED_SEARCHTERM_ORDER']._serialized_start=1229
  _globals['_DECK_FILTERED_SEARCHTERM_ORDER']._serialized_end=1438
  _globals['_DECK_KINDCONTAINER']._serialized_start=1440
  _globals['_DECK_KINDCONTAINER']._serialized_end=1553
  _globals['_ADDORUPDATEDECKLEGACYREQUEST']._serialized_start=1563
  _globals['_ADDORUPDATEDECKLEGACYREQUEST']._serialized_end=1639
  _globals['_DECKTREEREQUEST']._serialized_start=1641
  _globals['_DECKTREEREQUEST']._serialized_end=1671
  _globals['_DECKTREENODE']._serialized_start=1674
  _globals['_DECKTREENODE']._serialized_end=2044
  _globals['_SETDECKCOLLAPSEDREQUEST']._serialized_start=2047
  _globals['_SETDECKCOLLAPSEDREQUEST']._serialized_end=2202
  _globals['_SETDECKCOLLAPSEDREQUEST_SCOPE']._serialized_start=2168
  _globals['_SETDECKCOLLAPSEDREQUEST_SCOPE']._serialized_end=2202
  _globals['_GETDECKNAMESREQUEST']._serialized_start=2204
  _globals['_GETDECKNAMESREQUEST']._serialized_end=2279
  _globals['_DECKNAMES']._serialized_start=2281
  _globals['_DECKNAMES']._serialized_end=2333
  _globals['_DECKNAMEID']._serialized_start=2335
  _globals['_DECKNAMEID']._serialized_end=2373
  _globals['_REPARENTDECKSREQUEST']._serialized_start=2375
  _globals['_REPARENTDECKSREQUEST']._serialized_end=2435
  _globals['_RENAMEDECKREQUEST']._serialized_start=2437
  _globals['_RENAMEDECKREQUEST']._serialized_end=2491
  _globals['_FILTEREDDECKFORUPDATE']._serialized_start=2493
  _globals['_FILTEREDDECKFORUPDATE']._serialized_end=2606
  _globals['_DECKSSERVICE']._serialized_start=2609
  _globals['_DECKSSERVICE']._serialized_end=4267
  _globals['_BACKENDDECKSSERVICE']._serialized_start=4269
  _globals['_BACKENDDECKSSERVICE']._serialized_end=4290
# @@protoc_insertion_point(module_scope)
