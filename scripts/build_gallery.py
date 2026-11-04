from pathlib import Path
from PIL import Image,ImageOps
import json,io
root=Path(__file__).resolve().parents[1]
src=root/'photos-original';out=root/'images';out.mkdir(exist_ok=True)
result={}
for folder in sorted(p for p in src.iterdir() if p.is_dir()):
    entries=[]
    dest=out/folder.name;dest.mkdir(parents=True,exist_ok=True)
    valid=[]
    for original in sorted(folder.iterdir(),key=lambda p:p.name.lower()):
        if original.suffix.lower() not in {'.jpg','.jpeg','.png','.webp'}:continue
        try:
            with Image.open(original) as im:
                im=ImageOps.exif_transpose(im).convert('RGB')
                stem=original.stem
                # stable filename, avoid collisions across same stem with different extensions
                import hashlib
                key=hashlib.sha256(original.name.encode()).hexdigest()[:8]
                base=f'{stem}-{key}'
                paths={}
                for kind,width,quality in [('thumb',320,72),('display',1200,78),('large',2000,84)]:
                    resized=im.copy();resized.thumbnail((width,width*3),Image.Resampling.LANCZOS)
                    name=f'{base}-{kind}.webp';resized.save(dest/name,'WEBP',quality=quality,method=5)
                    paths[kind]=f'images/{folder.name}/{name}'
                    valid.append(name)
                entries.append({**paths,'alt':stem.replace('_',' ').replace('-',' ')})
        except Exception as ex:print(f'Skipped {original}: {ex}')
    for stale in dest.glob('*.webp'):
        if stale.name not in valid:stale.unlink()
    result[folder.name]=entries
(root/'gallery.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated galleries:',{k:len(v) for k,v in result.items()})
