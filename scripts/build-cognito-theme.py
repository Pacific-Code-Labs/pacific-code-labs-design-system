"""Generate Cognito managed login settings from the shared semantic CSS tokens."""
import colorsys,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
css=(root/'styles.css').read_text()
def tokens(selector):
 block=re.search(re.escape(selector)+r'\s*\{(.*?)\}',css,re.S)[1]
 return dict(re.findall(r'--([\w-]+):\s*([^;]+);',block))
light=tokens(':root');dark={**light,**tokens('.dark')}
def rgba(t,key):
 value=t[key].strip()
 h,s,l=map(float,value.replace('%','').split())
 return ''.join(f'{round(v*255):02x}' for v in colorsys.hls_to_rgb(h/360,l/100,s/100))+'ff'
settings={'categories':{'global':{'colorSchemeMode':'DYNAMIC','spacingDensity':'REGULAR','pageHeader':{'enabled':False},'pageFooter':{'enabled':False}},'form':{'languageSelector':{'enabled':True},'displayGraphics':False,'location':{'horizontal':'CENTER','vertical':'CENTER'}}},'components':{'form':{'borderRadius':20,'logo':{'enabled':True,'location':'CENTER','position':'TOP','formInclusion':'IN'}},'pageBackground':{'image':{'enabled':True}},'pageText':{},'primaryButton':{},'secondaryButton':{}},'componentClasses':{'buttons':{'borderRadius':12},'input':{'borderRadius':12},'inputLabel':{},'inputDescription':{},'focusState':{},'link':{},'divider':{}}}
for mode,t in [('lightMode',light),('darkMode',dark)]:
 c=lambda key:rgba(t,key)
 comps=settings['components'];classes=settings['componentClasses']
 comps['form'][mode]={'backgroundColor':c('card'),'borderColor':c('border')}
 comps['pageBackground'][mode]={'color':c('background')}
 comps['pageText'][mode]={'bodyColor':c('foreground'),'headingColor':c('foreground'),'descriptionColor':c('muted-foreground')}
 comps['primaryButton'][mode]={state:{'backgroundColor':c('primary'),'textColor':c('primary-foreground')} for state in ['defaults','hover','active']}
 comps['secondaryButton'][mode]={state:{'backgroundColor':c('secondary'),'textColor':c('foreground'),'borderColor':c('border')} for state in ['defaults','hover','active']}
 classes['input'][mode]={'defaults':{'backgroundColor':c('background'),'borderColor':c('border')},'placeholderColor':c('muted-foreground')}
 classes['inputLabel'][mode]={'textColor':c('foreground')};classes['inputDescription'][mode]={'textColor':c('muted-foreground')};classes['focusState'][mode]={'borderColor':c('ring')}
 classes['link'][mode]={state:{'textColor':c('primary')} for state in ['defaults','hover']};classes['divider'][mode]={'borderColor':c('border')}
 bg='#'+c('background')[:6];blue='#'+c('primary')[:6]
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000"><defs><radialGradient id="glow"><stop stop-color="{blue}" stop-opacity=".12"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient><pattern id="grid" width="64" height="64" patternUnits="userSpaceOnUse"><path d="M64 0H0V64" fill="none" stroke="{blue}" stroke-opacity=".05"/></pattern></defs><rect width="1600" height="1000" fill="{bg}"/><ellipse cx="1250" cy="180" rx="900" ry="650" fill="url(#glow)"/><rect width="1600" height="1000" fill="url(#grid)"/></svg>'''
 (root/'assets'/('login-'+mode+'.svg')).write_text(svg)
(root/'cognito-theme.json').write_text(json.dumps(settings,indent=2)+'\n')
