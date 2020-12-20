from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

session = PromptSession()

text = session.prompt('> ', auto_suggest=AutoSuggestFromHistory())
print('You said: %s' % text)
