import wikipedia

def scrape(name="Microsoft",length=1):
    result = wikipedia.summary(name, sentences=1)
    return result
    #click.echo(click.style(f"Result: {result}:", fg='yellow', bg='blue'))

