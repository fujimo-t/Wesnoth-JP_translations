import os
import requests
from transifex.api import transifex_api

organization_name = 'wesnoth-jp'
project_name = 'wesnoth-118'
language_code = 'ja'

token = os.getenv('TX_TOKEN')
transifex_api.setup(auth=token)

language = transifex_api.Language.get(code=language_code)

# Download translations foreach resource
resources = transifex_api.Resource.filter(project=f'o:{organization_name}:p:{project_name}')
for resource in resources:
    print('Downloading translations for resource:', resource.slug)
    
    out_dir = f'{project_name}/{resource.slug}'
    os.makedirs(out_dir, exist_ok=True)

    url = transifex_api.ResourceTranslationsAsyncDownload.download(resource=resource, language=language)
    req = requests.get(url, stream=True)
    with open(f'{out_dir}/{language_code}.po', 'wb') as fd:
        for chunk in req.iter_content(chunk_size=10240):
            fd.write(chunk)
